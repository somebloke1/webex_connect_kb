"""Offline behavior tests; network and real ASR checks are recorded separately."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "transcribe.py"
spec = importlib.util.spec_from_file_location("transcribe", SCRIPT)
transcribe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transcribe)


@pytest.mark.parametrize("source", [
    "I041FVBzU_s", "https://youtu.be/I041FVBzU_s?t=12",
    "https://www.youtube.com/watch?v=I041FVBzU_s&list=example",
    "https://www.youtube.com/embed/I041FVBzU_s", "https://www.youtube.com/shorts/I041FVBzU_s",
])
def test_youtube_identity(source):
    assert transcribe.video_id(source) == "I041FVBzU_s"


@pytest.mark.parametrize("source", [
    "https://evil.test/watch?v=I041FVBzU_s", "https://youtube.com.evil.test/watch?v=I041FVBzU_s",
    "https://www.youtube.com/playlist?list=example", "/nonexistent/audio.wav", "not-video",
])
def test_rejects_other_sources(source):
    with pytest.raises(transcribe.TranscriptionError):
        transcribe.video_id(source)


def test_manual_language_preference_and_no_implicit_translation():
    code, generated, track = transcribe.select_caption_track(
        {"en-GB": ["manual"]}, {"en": ["auto"]}, ["en", "en-GB"])
    assert (code, generated, track) == ("en-GB", False, ["manual"])
    with pytest.raises(transcribe.TranscriptionError):
        transcribe.select_caption_track({"fr": ["manual"]}, {}, ["en"])


def test_subtitle_import_roundtrip_and_metadata(tmp_path):
    fixture = tmp_path / "source.vtt"
    fixture.write_text("WEBVTT\n\n00:00:00.125 --> 00:00:02.750\nValidate <b>input</b> &amp; route.\n\n"
                       "00:00:03.000 --> 00:00:04.999\nHandle the error.\n")
    output = tmp_path / "result"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture), "--output-dir", str(output)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    data = json.loads((output / "transcript.json").read_text())
    assert data["segments"][0] == {"start": .125, "end": 2.75, "text": "Validate input & route."}
    assert transcribe.load_subtitles(output / "transcript.srt") == data["segments"]
    metadata = json.loads((output / "metadata.json").read_text())
    assert metadata["input_sha256"] == transcribe.sha256(fixture)
    assert metadata["method"] == "local-subtitle-import"
    assert metadata["human_reviewed"] is False
    for name, checksum in metadata["artifact_sha256"].items():
        assert transcribe.sha256(output / name) == checksum
    again = subprocess.run([sys.executable, str(SCRIPT), str(fixture), "--output-dir", str(output)],
                           capture_output=True, text=True)
    assert again.returncode == 2
    assert "already exist" in again.stderr


def test_json3_and_rolling_caption_deduplication(tmp_path):
    path = tmp_path / "captions.json3"
    path.write_text(json.dumps({"events": [
        {"tStartMs": 0, "dDurationMs": 2000, "segs": [{"utf8": "Test "}, {"utf8": "flow"}]},
        {"tStartMs": 1500, "dDurationMs": 1000, "segs": [{"utf8": "Test flow"}]},
        {"tStartMs": 3000, "dDurationMs": 1000, "segs": [{"utf8": "Test flow"}]},
    ]}))
    assert transcribe.load_subtitles(path) == [
        {"start": 0, "end": 2.5, "text": "Test flow"},
        {"start": 3, "end": 4, "text": "Test flow"},
    ]


@pytest.mark.parametrize("raw", [[], [{"start": -1, "end": 1, "text": "bad"}],
                                   [{"start": 2, "end": 1, "text": "bad"}],
                                   [{"start": 0, "end": float("nan"), "text": "bad"}]])
def test_rejects_invalid_transcripts(raw):
    with pytest.raises(transcribe.TranscriptionError):
        transcribe.normalize_segments(raw)


def test_timeout_records_failed_attempt(monkeypatch, tmp_path):
    class TimeoutProcess:
        pid = 12345
        def communicate(self, timeout=None):
            if timeout is not None:
                raise subprocess.TimeoutExpired("worker", 1)
            return "", ""
        def kill(self):
            pass
    killed = []
    monkeypatch.setattr(subprocess, "Popen", lambda *a, **kw: TimeoutProcess())
    monkeypatch.setattr(transcribe.os, "killpg", lambda pid, sig: killed.append(pid))
    attempts = []
    with pytest.raises(transcribe.TranscriptionError, match="exceeded"):
        transcribe.run_worker("captions-api", {"work_dir": str(tmp_path)}, 1, attempts)
    assert len(attempts) == 1
    assert attempts[0]["status"] == "failed"
    if transcribe.os.name == "posix":
        assert killed == [12345]


def test_timestamp_carries_milliseconds():
    assert transcribe.timestamp(59.9996, srt=True) == "00:01:00,000"


def test_cleanup_preserves_technical_text():
    assert transcribe.clean_text("<v Speaker><b>Use</b> x < 5 and y > 3; <TOKEN></v>") == "Use x < 5 and y > 3; <TOKEN>"


def test_blocked_error_does_not_keep_signed_urls():
    message = transcribe.error_summary(Exception("HTTP 403 https://youtube.com/api?token=secret"))
    assert "blocked" in message
    assert "secret" not in message


def test_failure_emits_no_transcript(tmp_path):
    output = tmp_path / "failed"
    assert transcribe.main(["https://example.com/invalid", "--output-dir", str(output)]) == 1
    assert (output / "failure.json").is_file()
    assert not (output / "transcript.json").exists()


@pytest.mark.parametrize("fault", ["write", "commit", "rollback"])
def test_overwrite_preserves_previous_artifacts_on_io_error(tmp_path, monkeypatch, fault):
    fixture = tmp_path / "source.srt"
    fixture.write_text("1\n00:00:00,125 --> 00:00:01,750\nOriginal transcript.\n")
    output = tmp_path / "result"
    args = [str(fixture), "--output-dir", str(output)]
    assert transcribe.main(args) == 0
    (output / "review.txt").write_text("Preserve this independent source review.")
    before = {p.name: p.read_bytes() for p in output.iterdir()}
    fixture.write_text("1\n00:00:00,125 --> 00:00:01,750\nReplacement transcript.\n")
    if fault == "write":
        def broken_write(staged, data, metadata):
            (staged / "transcript.json").write_text("incomplete new output")
            raise OSError("simulated output write failure")
        monkeypatch.setattr(transcribe, "write_artifacts", broken_write)
    else:
        real_replace = transcribe.os.replace
        def broken_replace(source, destination):
            if Path(source).name == "new" or (fault == "rollback" and Path(source).name == "previous"):
                raise OSError("simulated rename failure")
            return real_replace(source, destination)
        monkeypatch.setattr(transcribe.os, "replace", broken_replace)
    assert transcribe.main(args + ["--overwrite"]) == 1
    failure = json.loads((output / "failure.json").read_text())
    preserved = output
    if fault == "rollback":
        backups = list(tmp_path.glob(".result.publish-*/previous"))
        assert len(backups) == 1
        preserved = backups[0]
        assert str(preserved) in failure["error"]
    for name, content in before.items():
        assert (preserved / name).read_bytes() == content
    if fault != "rollback":
        assert not list(tmp_path.glob(".result.publish-*"))


def test_successful_overwrite_keeps_companion_files(tmp_path):
    fixture = tmp_path / "source.srt"
    fixture.write_text("1\n00:00:00,000 --> 00:00:01,000\nOriginal.\n")
    output = tmp_path / "result"
    args = [str(fixture), "--output-dir", str(output)]
    assert transcribe.main(args) == 0
    (output / "review.txt").write_text("Independent review")
    (output / "failure.json").write_text('{"status":"old failure"}')
    fixture.write_text("1\n00:00:00,000 --> 00:00:01,000\nReplacement.\n")
    assert transcribe.main(args + ["--overwrite"]) == 0
    assert json.loads((output / "transcript.json").read_text())["segments"][0]["text"] == "Replacement."
    assert (output / "review.txt").read_text() == "Independent review"
    assert not (output / "failure.json").exists()
    assert not list(tmp_path.glob(".result.publish-*"))


def test_interrupted_commit_restores_originals(tmp_path, monkeypatch):
    output = tmp_path / "result"
    output.mkdir()
    (output / "review.txt").write_text("Original evidence")
    real_replace = transcribe.os.replace
    def interrupted(source, destination):
        if Path(source).name == "new":
            raise KeyboardInterrupt()
        return real_replace(source, destination)
    monkeypatch.setattr(transcribe.os, "replace", interrupted)
    with pytest.raises(KeyboardInterrupt):
        transcribe.publish_artifacts(output,
            {"segments": [{"start": 0, "end": 1, "text": "new"}], "method": "fixture"},
            {"source": "fixture", "created_at": "fixture"})
    assert (output / "review.txt").read_text() == "Original evidence"
    assert not (output / "transcript.json").exists()
