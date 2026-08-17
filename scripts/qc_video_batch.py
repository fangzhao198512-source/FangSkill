#!/usr/bin/env python3
"""QC a folder of rendered ad videos with ffprobe and optional frame extraction."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from pathlib import Path


def run_json(cmd: list[str]) -> dict:
    result = subprocess.run(cmd, check=True, capture_output=True, text=True, encoding="utf-8")
    return json.loads(result.stdout)


def probe(path: Path) -> dict:
    data = run_json(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    audio = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), {})
    return {
        "file": path.name,
        "width": video.get("width"),
        "height": video.get("height"),
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
        "video_codec": video.get("codec_name"),
        "audio_codec": audio.get("codec_name", ""),
        "has_audio": bool(audio),
        "size_bytes": path.stat().st_size,
    }


def extract_frame(video: Path, out_dir: Path, timestamp: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{video.stem}_{timestamp.replace('.', '_')}.jpg"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-ss",
            timestamp,
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(out),
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--pattern", default="*.mp4")
    parser.add_argument("--frames", action="store_true", help="extract opening and CTA sample frames")
    parser.add_argument("--timestamps", default="1.2,20.2")
    args = parser.parse_args()

    videos = sorted(args.folder.glob(args.pattern))
    rows = [probe(video) for video in videos]

    report = args.folder / "_qc_report.csv"
    with report.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file", "width", "height", "duration", "video_codec", "audio_codec", "has_audio", "size_bytes"],
        )
        writer.writeheader()
        writer.writerows(rows)

    if args.frames:
        frame_dir = args.folder / "_qc_frames"
        sample = videos[:2] + videos[-2:] if len(videos) > 4 else videos
        seen: set[Path] = set()
        for video in sample:
            if video in seen:
                continue
            seen.add(video)
            for timestamp in [t.strip() for t in args.timestamps.split(",") if t.strip()]:
                extract_frame(video, frame_dir, timestamp)

    print(f"videos={len(videos)} report={report}")
    for row in rows:
        print(
            f"{row['file']} | {row['width']}x{row['height']} | "
            f"{row['duration']:.2f}s | audio={row['audio_codec'] or 'none'}"
        )


if __name__ == "__main__":
    main()
