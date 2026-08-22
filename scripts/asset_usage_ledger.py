#!/usr/bin/env python3
"""Check and append source footage usage ranges for FangSkill video batches."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

REQUIRED = ["batch", "output_video", "source_file", "start", "end"]
FIELDS = REQUIRED + ["role", "note"]


def norm_source(value: str) -> str:
    try:
        return str(Path(value).resolve()).lower()
    except Exception:
        return value.strip().lower()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        missing = [field for field in REQUIRED if field not in row]
        if missing:
            raise SystemExit(f"{path} missing required columns: {', '.join(missing)}")
    return rows


def parse_time(row: dict[str, str], field: str) -> float:
    try:
        return float(row[field])
    except Exception as exc:
        label = row.get("output_video") or row.get("source_file") or row
        raise SystemExit(f"Invalid {field} in {label}: {row.get(field)!r}") from exc


def overlaps(a: dict[str, str], b: dict[str, str], buffer: float) -> bool:
    if norm_source(a["source_file"]) != norm_source(b["source_file"]):
        return False
    a_start = parse_time(a, "start") - buffer
    a_end = parse_time(a, "end") + buffer
    b_start = parse_time(b, "start")
    b_end = parse_time(b, "end")
    return max(a_start, b_start) < min(a_end, b_end)


def check(ledger: Path, plan: Path, buffer: float) -> int:
    existing = read_rows(ledger)
    proposed = read_rows(plan)
    conflicts: list[tuple[dict[str, str], dict[str, str]]] = []
    for candidate in proposed:
        for used in existing:
            if overlaps(used, candidate, buffer):
                conflicts.append((candidate, used))

    if not conflicts:
        print(f"OK: no overlaps found ({len(proposed)} proposed ranges, buffer={buffer}s)")
        return 0

    print(f"CONFLICTS: {len(conflicts)} overlapping source ranges found")
    for candidate, used in conflicts:
        print(
            "candidate "
            f"{candidate.get('output_video')} {candidate.get('source_file')} "
            f"{candidate.get('start')}-{candidate.get('end')} overlaps used "
            f"{used.get('batch')}/{used.get('output_video')} "
            f"{used.get('start')}-{used.get('end')}"
        )
    return 2


def append(ledger: Path, plan: Path) -> int:
    rows = read_rows(plan)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    exists = ledger.exists() and ledger.stat().st_size > 0
    with ledger.open("a", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDS})
    print(f"APPENDED: {len(rows)} rows -> {ledger}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    check_parser = sub.add_parser("check", help="check proposed source ranges against a ledger")
    check_parser.add_argument("--ledger", type=Path, required=True)
    check_parser.add_argument("--plan", type=Path, required=True)
    check_parser.add_argument("--buffer", type=float, default=1.0)

    append_parser = sub.add_parser("append", help="append confirmed source ranges to a ledger")
    append_parser.add_argument("--ledger", type=Path, required=True)
    append_parser.add_argument("--plan", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "check":
        raise SystemExit(check(args.ledger, args.plan, args.buffer))
    if args.command == "append":
        raise SystemExit(append(args.ledger, args.plan))


if __name__ == "__main__":
    main()
