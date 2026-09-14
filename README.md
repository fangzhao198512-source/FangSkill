# FangSkill

FangSkill is a Codex skill for creating batch industrial B2B social ad videos from local factory or product footage.

It is designed for export manufacturers and industrial sales teams that need localized vertical ads for platforms such as Facebook, Instagram Reels, TikTok, and similar short-video placements.

## What It Helps With

- Conversion-oriented industrial ad structure: hook, product proof, pain point, benefit, trust signal, CTA.
- Multilingual copy guidance for localized captions, narration, and calls to action.
- Source-footage usage tracking so later batches avoid reusing the same time ranges.
- BGM sourcing rules for real royalty-free commercial music instead of placeholder tones.
- QC workflow for checking video count, dimensions, duration, audio, captions, and sample frames.

## Skill Layout

```text
fangskill/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- ad-video-workflow.md
|   |-- asset-usage-ledger.md
|   |-- multilingual-copy.md
|   `-- music-sourcing.md
`-- scripts/
    |-- asset_usage_ledger.py
    `-- qc_video_batch.py
```

## Installation

Copy or clone this repository into your Codex skills folder:

```bash
git clone https://github.com/fangzhao198512-source/FangSkill.git ~/.codex/skills/fangskill
```

On Windows, the skills folder is commonly:

```powershell
git clone https://github.com/fangzhao198512-source/FangSkill.git "$env:USERPROFILE\.codex\skills\fangskill"
```

Then restart Codex or reload skills if your environment supports it.

## Requirements

The skill itself is instruction-first. Its helper scripts expect:

- Python 3.10+
- `ffmpeg` and `ffprobe` available on `PATH` for video QC workflows

The skill does not include media assets, music files, customer footage, API keys, or campaign data.

## Helper Scripts

Check a proposed source-footage usage plan against a persistent ledger:

```bash
python scripts/asset_usage_ledger.py check --ledger path/to/_asset_usage_ledger.csv --plan path/to/_asset_usage_plan.csv --buffer 1.0
```

Append a confirmed plan after rendering:

```bash
python scripts/asset_usage_ledger.py append --ledger path/to/_asset_usage_ledger.csv --plan path/to/_asset_usage_plan.csv
```

QC a rendered folder:

```bash
python scripts/qc_video_batch.py path/to/output-folder --frames --timestamps 1.2,20.2
```

## License

MIT License. See [LICENSE](LICENSE).
