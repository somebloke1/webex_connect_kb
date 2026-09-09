#!/usr/bin/env python3
"""Captions-first YouTube/local transcription; evidence is never replaced by a guess."""
from __future__ import annotations

import argparse
import hashlib
import html
import importlib.metadata
import json
import math
import os
from pathlib import Path
import re
import signal
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse


class TranscriptionError(Exception):
    pass


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def video_id(source):
    """Accept known YouTube URL shapes, never arbitrary downloader URLs."""
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", source):
        return source
    parsed = urlparse(source)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"}:
        raise TranscriptionError("Expected an existing local file or a YouTube URL/video ID.")
    if host in {"youtu.be", "www.youtu.be"}:
        candidate = parsed.path.strip("/").split("/")[0]
    elif host in {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "www.youtube-nocookie.com"}:
        parts = parsed.path.strip("/").split("/")
        candidate = parse_qs(parsed.query).get("v", [""])[0]
        if len(parts) == 2 and parts[0] in {"embed", "shorts", "live"}:
            candidate = parts[1]
    else:
        candidate = ""
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
        raise TranscriptionError("Not a supported single-video YouTube URL; playlists are not accepted.")
    return candidate


def clean_text(value):
    # Strip known caption markup, preserving technical comparisons/placeholders.
    markup = r"<(?:/?(?:b|i|u|c|v|lang|ruby|rt)(?:[ .][^>]*)?|(?:\d{2}:)?\d{2}:\d{2}\.\d{3})>"
    return re.sub(r"\s+", " ", html.unescape(re.sub(markup, "", str(value), flags=re.I))).strip()


def normalize_segments(raw):
    """Validate time bounds and collapse only identical adjacent overlapping captions."""
    result = []
    for item in raw:
        start = float(item["start"])
        end = float(item.get("end", start + float(item.get("duration", 0))))
        text = clean_text(item.get("text", ""))
        if not math.isfinite(start) or not math.isfinite(end) or start < 0 or end < start:
            raise TranscriptionError("Transcript has invalid, negative, or reversed timestamps.")
        if not text:
            continue
        if result and start < result[-1]["start"]:
            raise TranscriptionError("Transcript segments are out of chronological order.")
        if result and text == result[-1]["text"] and start <= result[-1]["end"] + 0.05:
            result[-1]["end"] = max(result[-1]["end"], end)
            continue
        result.append({"start": round(start, 3), "end": round(end, 3), "text": text})
    if not result:
        raise TranscriptionError("No nonempty transcript segments were returned.")
    return result


def timestamp(seconds, srt=False):
    total_ms = int(round(seconds * 1000))
    hours, remainder = divmod(total_ms, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02}{',' if srt else '.'}{millis:03}"


def parse_timestamp(value):
    hours, minutes, seconds = value.replace(",", ".").split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def load_subtitles(path):
    import webvtt
    suffix = Path(path).suffix.lower()
    if suffix in {".json", ".json3"}:
        data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
        if isinstance(data, dict) and "events" in data:
            raw = [{"start": e.get("tStartMs", 0) / 1000,
                    "duration": e.get("dDurationMs", 0) / 1000,
                    "text": "".join(s.get("utf8", "") for s in e.get("segs", []))}
                   for e in data["events"]]
        else:
            raw = data.get("segments", []) if isinstance(data, dict) else data
        if not isinstance(raw, list):
            raise TranscriptionError("JSON must contain a segment list or YouTube JSON3 events.")
        return normalize_segments(raw)
    captions = webvtt.from_srt(str(path)) if suffix == ".srt" else webvtt.read(str(path))
    # webvtt-py's *_in_seconds properties truncate milliseconds.
    return normalize_segments([{"start": parse_timestamp(c.start), "end": parse_timestamp(c.end),
                                "text": c.raw_text} for c in captions])


def versions():
    found = {"python": sys.version.split()[0]}
    for package in ("youtube-transcript-api", "yt-dlp", "webvtt-py", "faster-whisper", "ctranslate2"):
        try:
            found[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            pass
    return found


def select_caption_track(manual, automatic, languages):
    """Manual first across requested languages; exact or regional language match."""
    for tracks, generated in ((manual, False), (automatic, True)):
        for language in languages:
            matches = [language] + sorted(k for k in tracks if k.startswith(language + "-"))
            for code in matches:
                if code in tracks and tracks[code]:
                    return code, generated, tracks[code]
    raise TranscriptionError(f"No original captions for requested languages: {', '.join(languages)}")


def captions_api(config):
    import requests
    from youtube_transcript_api import YouTubeTranscriptApi

    class TimedSession(requests.Session):
        def request(self, *args, **kwargs):
            kwargs.setdefault("timeout", 15)
            return super().request(*args, **kwargs)

    with TimedSession() as session:
        tracks = list(YouTubeTranscriptApi(http_client=session).list(config["video_id"]))
        manual = {t.language_code: t for t in tracks if not t.is_generated}
        automatic = {t.language_code: t for t in tracks if t.is_generated}
        code, generated, track = select_caption_track(manual, automatic, config["languages"])
        fetched = track.fetch()
        return {"segments": normalize_segments(fetched.to_raw_data()),
                "method": "youtube-transcript-api", "language": code,
                "caption_kind": "automatic" if generated else "manual",
                "translated": False}


def ytdlp_options():
    return {"quiet": True, "no_warnings": False, "noplaylist": True,
            "retries": 0, "fragment_retries": 0, "extractor_retries": 0,
            "socket_timeout": 15, "skip_download": True,
            "ignore_no_formats_error": True,
            "extractor_args": {"youtube": {"skip": ["translated_subs"]}}}


def captions_ytdlp(config):
    from yt_dlp import YoutubeDL
    # Different implementation after a failed transcript API call, with no repeated requests loop.
    with YoutubeDL(ytdlp_options()) as ydl:
        info = ydl.extract_info(config["url"], download=False)
        code, generated, tracks = select_caption_track(info.get("subtitles", {}),
                                                       info.get("automatic_captions", {}),
                                                       config["languages"])
        track = next((t for ext in ("json3", "vtt", "srt") for t in tracks if t.get("ext") == ext), None)
        if not track:
            raise TranscriptionError("Captions exist but no JSON3/VTT/SRT track was available.")
        with ydl.urlopen(track["url"]) as response:
            body = response.read(20 * 1024 * 1024 + 1)
        if len(body) > 20 * 1024 * 1024:
            raise TranscriptionError("Subtitle file exceeds 20 MiB safety bound.")
        local = Path(config["work_dir"]) / ("captions." + track["ext"])
        local.write_bytes(body)
        return {"segments": load_subtitles(local), "method": "yt-dlp-captions",
                "language": code, "caption_kind": "automatic" if generated else "manual",
                "translated": False, "title": info.get("title"), "uploader": info.get("uploader"),
                "upload_date": info.get("upload_date"), "duration": info.get("duration"),
                "input_sha256": sha256(local)}


def download_audio(config):
    from yt_dlp import YoutubeDL
    options = ytdlp_options()
    options.update({"format": "bestaudio/best", "skip_download": False,
                    "ignore_no_formats_error": False,
                    "outtmpl": str(Path(config["work_dir"]) / "audio.%(ext)s"),
                    "max_filesize": 512 * 1024 * 1024,
                    "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "wav"}]})
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(config["url"], download=False)
        if info.get("is_live"):
            raise TranscriptionError("Live streams are not supported; use a finished recording.")
        duration = info.get("duration")
        if duration is None or duration > config["max_video_minutes"] * 60:
            raise TranscriptionError("Video duration is unknown or exceeds --max-video-minutes.")
        ydl.process_info(info)
        path = Path(config["work_dir"]) / "audio.wav"
        if not path.is_file():
            raise TranscriptionError("Audio was not downloaded; check ffmpeg and the download limits.")
        return {"path": str(path), "title": info.get("title"), "uploader": info.get("uploader"),
                "upload_date": info.get("upload_date"), "duration": duration, "input_sha256": sha256(path)}


def asr(config):
    try:
        from faster_whisper import WhisperModel
    except ImportError as error:
        raise TranscriptionError("ASR not installed. Run scripts/setup_venv.sh --with-asr") from error
    model = WhisperModel(config["model"], device=config["device"], compute_type=config["compute_type"],
                         cpu_threads=config["threads"], download_root=config.get("model_cache"),
                         local_files_only=config.get("offline", False))
    segments, info = model.transcribe(config["path"], language=config["languages"][0].split("-")[0],
                                      beam_size=5, vad_filter=True,
                                      initial_prompt=config.get("initial_prompt"))
    raw = [{"start": s.start, "end": s.end, "text": s.text} for s in segments]
    return {"segments": normalize_segments(raw), "method": "faster-whisper",
            "language": info.language, "language_probability": info.language_probability,
            "caption_kind": "local-asr", "model": config["model"],
            "device": config["device"], "compute_type": config["compute_type"],
            "duration": info.duration, "input_sha256": sha256(config["path"]),
            "asr_settings": {"beam_size": 5, "vad_filter": True,
                             "initial_prompt": config.get("initial_prompt")}}


WORKERS = {"captions-api": captions_api, "captions-ytdlp": captions_ytdlp,
           "download-audio": download_audio, "asr": asr}


def run_worker(operation, config, timeout, attempts):
    started = time.monotonic()
    config_path = Path(config["work_dir"]) / (operation + "-config.json")
    result_path = Path(config["work_dir"]) / (operation + "-result.json")
    config_path.write_text(json.dumps(config), encoding="utf-8")
    attempt = {"operation": operation, "started_at": utc_now(), "timeout_seconds": timeout}
    try:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--_worker", operation,
                                    str(config_path), str(result_path)], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, start_new_session=True)
        try:
            process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            # Kill the worker's process group, including a running ffmpeg child.
            if os.name == "posix":
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            else:
                process.kill()
            process.communicate()
            raise
        result = json.loads(result_path.read_text()) if result_path.is_file() else {}
        if process.returncode or "error" in result:
            # Avoid serializing signed media URLs or any potential request credential details.
            error = result.get("error", "Worker failed without a structured result")
            raise TranscriptionError(f"{operation}: {error}")
        attempt["status"] = "success"
        return result
    except subprocess.TimeoutExpired as error:
        attempt.update(status="failed", error=f"{operation} exceeded {timeout} seconds")
        raise TranscriptionError(attempt["error"]) from error
    except Exception as error:
        attempt.update(status="failed", error=str(error))
        raise
    finally:
        attempt["elapsed_seconds"] = round(time.monotonic() - started, 3)
        attempts.append(attempt)


def error_summary(error):
    """Keep useful failure classes, without retaining raw URLs containing tokens/cookies."""
    name = type(error).__name__
    message = str(error)
    low = message.lower()
    if any(s in low for s in ("confirm you're not a bot", "ipblocked", "requestblocked", "blocking requests", "429", "403", "forbidden")) or name in {"IpBlocked", "RequestBlocked"}:
        return (f"{name}: YouTube blocked this unauthenticated retrieval (bot/IP/403/429). "
                "Stop repeated requests. Supply legitimately obtained local subtitles/media, "
                "or retry later from your normal permitted connection. No cookies or proxy credentials were copied.")
    message = re.sub(r"https?://\S+", "[URL omitted]", message)
    return f"{name}: {message[:1400]}"


def write_artifacts(output, data, metadata):
    output.mkdir(parents=True, exist_ok=True)
    segments = normalize_segments(data["segments"])
    metadata.update({k: v for k, v in data.items() if k != "segments"})
    metadata["segment_count"] = len(segments)
    metadata["transcript_end_seconds"] = segments[-1]["end"]
    payload = {"schema_version": 1, "segments": segments}
    (output / "transcript.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    srt = "\n\n".join(f"{i}\n{timestamp(s['start'], True)} --> {timestamp(s['end'], True)}\n{s['text']}"
                       for i, s in enumerate(segments, 1)) + "\n"
    (output / "transcript.srt").write_text(srt, encoding="utf-8")
    title = metadata.get("title") or "Transcript"
    lines = [f"# {title}", "", f"Source: {metadata['source']}",
             f"Method: {metadata['method']}; language: {metadata.get('language') or 'unspecified'}; kind: {metadata.get('caption_kind')}",
             f"Retrieved/processed: {metadata['created_at']}", "",
             "Unedited machine/caption evidence. Verify exact UI fields, API names and numbers against the official text documentation.", ""]
    for segment in segments:
        label = timestamp(segment["start"])
        if metadata.get("video_id"):
            label = f"[{label}](https://www.youtube.com/watch?v={metadata['video_id']}&t={int(segment['start'])}s)"
        lines.append(f"- {label} — {segment['text']}")
    (output / "transcript.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    metadata["artifact_sha256"] = {name: sha256(output / name) for name in ("transcript.json", "transcript.srt", "transcript.md")}
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def publish_artifacts(output, data, metadata):
    """Stage a complete bundle, then replace it; preserve originals on any caught error."""
    output.parent.mkdir(parents=True, exist_ok=True)
    transaction = Path(tempfile.mkdtemp(prefix=f".{output.name}.publish-", dir=output.parent))
    staged = transaction / "new"
    backup = transaction / "previous"
    retain_backup = False
    try:
        if output.exists():
            # Preserve companion source/review files as well as the managed artifacts.
            shutil.copytree(output, staged, symlinks=True)
        else:
            staged.mkdir()
        for name in ("transcript.json", "transcript.md", "transcript.srt", "metadata.json", "failure.json"):
            (staged / name).unlink(missing_ok=True)
        write_artifacts(staged, data, metadata)
        if output.exists():
            # Set this before moving originals so an interrupt cannot delete the backup.
            retain_backup = True
            os.replace(output, backup)
        try:
            os.replace(staged, output)
        except BaseException as commit_error:
            if backup.exists():
                try:
                    os.replace(backup, output)
                    retain_backup = False
                except BaseException as rollback_error:
                    # Never clean up the only surviving originals if restoration itself fails.
                    retain_backup = True
                    raise TranscriptionError(
                        f"Output commit failed and rollback could not restore the destination. "
                        f"Original directory is preserved at {backup}. "
                        f"Commit: {error_summary(commit_error)}; rollback: {error_summary(rollback_error)}"
                    ) from commit_error
            raise
        retain_backup = False
    finally:
        if not retain_backup or not backup.exists():
            shutil.rmtree(transaction, ignore_errors=True)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", help="YouTube URL/ID or local subtitles/media file")
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--languages", default="en", help="Comma-separated language preference; manual captions preferred")
    p.add_argument("--title", help="Explicit human-supplied source title")
    p.add_argument("--source-url", help="Provenance URL for a legitimately obtained local file")
    p.add_argument("--allow-asr", action="store_true", help="Allow local ASR and, for YouTube, audio download if captions fail")
    p.add_argument("--asr-only", action="store_true", help="Skip previously failed captions and directly use permitted audio + local ASR; requires --allow-asr")
    p.add_argument("--model", default="small", help="faster-whisper model name or local path")
    p.add_argument("--device", choices=("cpu", "cuda", "auto"), default="cpu")
    p.add_argument("--compute-type", default="int8")
    p.add_argument("--threads", type=int, default=4)
    p.add_argument("--model-cache", help="Model cache directory; no media is sent to a speech service")
    p.add_argument("--offline", action="store_true", help="Load ASR models from existing local cache only")
    p.add_argument("--initial-prompt", help="Optional ASR vocabulary hint; recorded in provenance")
    p.add_argument("--timeout", type=int, default=120, help="Maximum seconds per network retrieval route")
    p.add_argument("--asr-timeout", type=int, default=3600, help="Maximum seconds for model loading and local ASR")
    p.add_argument("--max-video-minutes", type=float, default=180)
    p.add_argument("--overwrite", action="store_true", help="Replace previous transcript artifacts in this output directory")
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    output = args.output_dir.resolve()
    reserved = ["transcript.json", "transcript.md", "transcript.srt", "metadata.json", "failure.json"]
    if any((output / name).exists() for name in reserved) and not args.overwrite:
        parser().error("Output artifacts already exist. Choose another directory or explicitly use --overwrite.")
    if args.timeout < 1 or args.asr_timeout < 1 or args.threads < 1 or args.max_video_minutes <= 0:
        parser().error("Timeouts, thread count, and maximum duration must be positive.")
    if args.asr_only and not args.allow_asr:
        parser().error("--asr-only requires --allow-asr.")
    languages = [s.strip() for s in args.languages.split(",") if s.strip()]
    if not languages:
        parser().error("At least one language is required.")
    attempts = []
    metadata = {"schema_version": 1, "source": args.source_url or args.source,
                "created_at": utc_now(), "requested_languages": languages,
                "title": args.title, "uploader": None, "versions": versions(),
                "attempts": attempts, "human_reviewed": False}
    try:
        source_path = Path(args.source).expanduser()
        with tempfile.TemporaryDirectory(prefix="webex-transcribe-") as work:
            config = vars(args).copy()
            config.update(work_dir=work, output_dir=str(output), languages=languages)
            data = None
            if source_path.is_file():
                config["path"] = str(source_path.resolve())
                metadata.update(input_path=str(source_path.resolve()), input_sha256=sha256(source_path))
                if args.source_url:
                    try:
                        metadata["video_id"] = video_id(args.source_url)
                    except TranscriptionError:
                        pass
                if source_path.suffix.lower() in {".srt", ".vtt", ".json", ".json3"}:
                    data = {"segments": load_subtitles(source_path), "method": "local-subtitle-import",
                            "language": languages[0], "caption_kind": "local-unverified"}
                elif args.allow_asr:
                    data = run_worker("asr", config, args.asr_timeout, attempts)
                else:
                    raise TranscriptionError("Local media requires --allow-asr. Local subtitle imports do not.")
            else:
                identifier = video_id(args.source)
                config.update(video_id=identifier, url=f"https://www.youtube.com/watch?v={identifier}")
                metadata.update(video_id=identifier, source=config["url"])
                for operation in (() if args.asr_only else ("captions-api", "captions-ytdlp")):
                    try:
                        data = run_worker(operation, config, args.timeout, attempts)
                        break
                    except TranscriptionError:
                        continue
                if data is None and args.allow_asr:
                    downloaded = run_worker("download-audio", config, args.timeout, attempts)
                    config["path"] = downloaded.pop("path")
                    data = run_worker("asr", config, args.asr_timeout, attempts)
                    data.update(downloaded)
                if data is None:
                    raise TranscriptionError("Both caption retrieval routes failed. Read failure.json. "
                                             "Use local subtitles/media; --allow-asr may work if only captions are unavailable.")
            if args.title:
                data["title"] = args.title
                metadata["title_provenance"] = "user-supplied"
            publish_artifacts(output, data, metadata)
        print(json.dumps({"status": "success", "output_dir": str(output), "method": metadata["method"],
                          "segment_count": metadata["segment_count"]}))
        return 0
    except Exception as error:
        output.mkdir(parents=True, exist_ok=True)
        metadata.update(status="failed", error=error_summary(error))
        (output / "failure.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(metadata["error"], file=sys.stderr)
        print(f"Failure evidence: {output / 'failure.json'}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--_worker":
        _, _, operation, config_path, result_path = sys.argv
        try:
            result = WORKERS[operation](json.loads(Path(config_path).read_text()))
        except Exception as error:
            result = {"error": error_summary(error)}
        Path(result_path).write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
        sys.exit(1 if "error" in result else 0)
    sys.exit(main())
