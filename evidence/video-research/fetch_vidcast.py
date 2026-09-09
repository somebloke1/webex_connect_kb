#!/usr/bin/env python3
"""Fetch publicly shared Vidcast captions; no login, cookies, or access bypass.

Endpoint shapes were read from the public Vidcast player on 2026-09-08.
This is an ingestion adapter, not a supported Cisco API contract.
Normalize its source.en.vtt with scripts/transcribe.py to use the shared workflow.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.request
from urllib.parse import urlparse

UUID = re.compile(r"[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}")


def timestamp(ms):
    ms = int(ms)
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    seconds, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{ms:03}"


def fetch_json(url):
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Public app.vidcast.io/share/UUID URL or UUID")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    source = args.source.strip()
    if source.startswith("https://"):
        parsed = urlparse(source)
        if parsed.netloc != "app.vidcast.io" or not parsed.path.startswith("/share/"):
            parser.error("Expected an official public app.vidcast.io/share/UUID URL")
        source = parsed.path.rstrip("/").split("/")[-1]
    if not UUID.fullmatch(source):
        parser.error("Invalid Vidcast share UUID")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    names = ["source.en.vtt", "transcript.raw.json", "provenance.json", "failure.json"]
    if any((args.output_dir / name).exists() for name in names):
        parser.error("Output already exists; choose a new directory to preserve evidence")
    metadata_url = f"https://api.vidcast.io/v2/videos/shared/{source}"
    transcript_url = f"https://api.vidcast.io/v3/transcripts/{source}"
    provenance = {
        "source_url": f"https://app.vidcast.io/share/{source}",
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "metadata_url": metadata_url,
        "transcript_url": transcript_url,
        "method": "public-vendor-transcript",
        "authenticated": False,
        "human_reviewed": False,
    }
    try:
        metadata = fetch_json(metadata_url)
        data = fetch_json(transcript_url)
        transcript = data.get("transcript") or {}
        segments = transcript.get("transcripts") or []
        if data.get("transcript_status") != "ready" or not segments:
            raise ValueError("Vendor transcript not ready or empty")
        language = transcript.get("language")
        if language != "en":
            raise ValueError(f"Expected English transcript; vendor returned {language!r}")
        lines = ["WEBVTT", ""]
        previous_start = -1
        for segment in segments:
            start = int(segment["start_time_ms"])
            end = int(segment["end_time_ms"])
            raw_text = segment["transcript"]
            if not isinstance(raw_text, str):
                raise ValueError("Vendor caption text must be a string")
            text = raw_text.strip()
            if start < previous_start or start < 0 or end <= start or not text:
                raise ValueError("Invalid/unsorted/empty vendor caption segment")
            previous_start = start
            lines.extend([f"{timestamp(start)} --> {timestamp(end)}", text, ""])
        vtt = "\n".join(lines) + "\n"
        (args.output_dir / "source.en.vtt").write_text(vtt, encoding="utf-8")
        (args.output_dir / "transcript.raw.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        provenance.update({"status": "success", "title": metadata.get("name"),
                           "publisher": metadata.get("user_name"), "duration_ms": metadata.get("duration"),
                           "language": language, "segment_count": len(segments),
                           "vtt_sha256": hashlib.sha256(vtt.encode()).hexdigest(),
                           "quality_note": "Vendor caption generation/editing method is not independently verified"})
    except (urllib.error.URLError, OSError, ValueError, KeyError, TypeError) as error:
        provenance.update({"status": "failed", "error_type": type(error).__name__, "error": str(error)})
        (args.output_dir / "failure.json").write_text(json.dumps(provenance, indent=2), encoding="utf-8")
        raise SystemExit(f"Caption fetch failed: {type(error).__name__}; see failure.json")
    (args.output_dir / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": "success", "output_dir": str(args.output_dir), "segment_count": len(segments)}))


if __name__ == "__main__":
    main()
