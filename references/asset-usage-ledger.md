# FangSkill Asset Usage Ledger

## Purpose

Keep a persistent record of source footage ranges used in finished ads. This prevents later batches from reusing the same visible shots just because the file names differ or the crop/zoom changed.

## Default Ledger

Use a CSV ledger near the campaign or product folder. Recommended names:

- `_asset_usage_ledger.csv` beside the rendered batch.
- `D:/视频资料/<brand or product>/_asset_usage_ledger.csv` for a long-running product library.

Each row should contain:

- `batch`: campaign or batch folder name.
- `output_video`: final video filename.
- `source_file`: absolute source footage path when practical.
- `start`: source start time in seconds.
- `end`: source end time in seconds.
- `role`: hook, product-proof, factory-proof, testing, packaging, aerial, CTA, or other.
- `note`: optional reason or product context.

## Reuse Rule

Before planning a batch, check the ledger. Do not reuse source ranges that overlap existing rows by default. Treat near-overlaps as repeats too:

- Use at least a 1.0 second buffer before and after an existing used range.
- A different crop, zoom, speed, or transition does not make the same source seconds new.
- Reuse only when the user approves it, and record the approval in `note`.

## Planning Workflow

1. Build a candidate clip plan with source files and intended start/end seconds.
2. Check the candidate plan against the ledger.
3. Replace overlapping candidates with unused ranges from the same file or another file.
4. Render the batch.
5. Append the final used source ranges to the ledger.

If existing scripts do not expose start/end seconds, update them to store segment choices explicitly instead of relying on `trim=0:duration` everywhere. For source clips that are always started at 0, record `start=0` and `end=<segment duration>`.

## Helper Script

Use `scripts/asset_usage_ledger.py`:

- `check`: compare a proposed CSV plan with a ledger and report overlaps.
- `append`: append a confirmed plan to the ledger after rendering.

The proposed plan should use the same columns as the ledger. `batch`, `output_video`, `source_file`, `start`, and `end` are required.
