---
name: fangskill
description: Create batch industrial B2B social ad videos from local factory/product footage with multilingual copy, voiceover, captions, BGM, dynamic hooks, non-repeating edits, and final QC. Use when the user asks to make Facebook/Meta/TikTok/Reels vertical ads, export manufacturer promo videos, product sales videos, energy-saving motor ads, or batches of localized industrial marketing videos from local素材/materials.
---

# FangSkill

## Overview

Use FangSkill to turn local factory footage into conversion-oriented industrial ad videos. Keep the core ad logic stable while varying language, hooks, footage, pacing, subtitles, voiceover, BGM, and CTA across each output.

Default to local/free tooling first: Python scripts, ffmpeg/ffprobe, local assets, JianYing automation when useful, and optional HyperFrames/general-video packaging for motion graphics. Do not depend on paid cloud plugins unless the user explicitly asks and confirms availability.

## Workflow

1. Clarify the campaign only when needed: product, buyer, target language/market, quantity, length, aspect ratio, and primary selling point. If the user is continuing an existing campaign, infer these from the current folder/script history.
2. Inspect local素材 before editing. Prefer real product, factory, assembly, testing, packaging, delivery, and aerial clips. Exclude source videos with burned-in subtitles or irrelevant consumer-style footage.
3. Build each ad around this structure: 0-3s hook, product proof, buyer pain point, benefit, trust signal, inquiry CTA.
4. Localize the script. The language is a parameter, not a fixed rule. Use the target market's language for hook, captions, voiceover, and CTA.
5. Compose the edit with varied footage order, different crops, changed hook copy, different CTA phrasing, and distinct pacing so batch outputs are not simple duplicates. Before selecting source segments, check the asset usage ledger and avoid reusing the same source time ranges.
6. Add voiceover and real downloaded BGM. Use existing online/free music tracks by default; do not synthesize fake music unless the user explicitly asks for synthetic audio. For batches, use a different commercial/corporate-style music track for each video unless the user explicitly approves reuse. Keep BGM audible but below narration; duck music if narration is present.
7. Render vertical-first deliverables unless the user asks otherwise. For Facebook/Reels/TikTok default to 1080x1920, 20-35 seconds, h.264 mp4, AAC audio.
8. Run QC before delivery: count files, dimensions, duration, audio stream, subtitle fit, opening clarity, ending CTA, and sample frame review.

## Tool Selection

- Use `video-processor` / ffmpeg for the batch render, transcoding, trimming, subtitles, BGM mix, and QC.
- Use `jianying-editor` when the user specifically wants JianYing/CutCap-style projects, templates, timeline editing, or a workflow based on an existing JianYing batch script.
- Use `speech` or the local TTS path already configured in the project for multilingual voiceover.
- Use `media-use` or browser/download tools for local/free BGM and SFX resolution when the project does not already include usable music. Prefer downloaded tracks from free/royalty-free libraries over generated tones.
- Use `hyperframes` or `general-video` only for extra motion packaging: title cards, dynamic benefit cards, animated CTA, and visual hooks. Then composite those assets into the final ffmpeg/JianYing batch.

## Multilingual Defaults

Support any language the user requests. Common defaults:

- Turkish: industrial buyers, energy-saving motors, inquiry CTA.
- English: export buyers, distributors, OEM/ODM, factory-direct supply.
- Arabic: Gulf/North Africa buyers, trust and supply capacity.
- Spanish: LATAM distributors and factory procurement.
- Russian: machinery buyers and wholesale procurement.

When translating, do not produce literal Chinese-style copy. Write short ad lines that fit on a phone screen. Use 1-2 line captions and keep long words from being clipped.

## Industrial Ad Logic

Use buyer-driven claims, not vague slogans:

- Cost: save electricity, lower operating cost, reduce downtime.
- Product: power, efficiency, durability, stable performance, suitable model selection.
- Factory proof: assembly, winding, testing, stock, packaging, shipment, factory aerial.
- Procurement: bulk orders, project supply, distributor cooperation, fast quotation.
- CTA: send voltage/power/quantity/application; ask for quote; contact Botao/Fang brand as applicable.

Do not start with a generic factory scene without context. The first 3 seconds must make the product and benefit obvious.

## Product Profiles

Before writing copy, identify the product profile and adapt the proof shots and benefits:

- Motors and electrical equipment: efficiency, power match, stable operation, energy cost, testing.
- Machinery and production equipment: output, labor saving, precision, uptime, installation, factory trial run.
- Spare parts and components: material, fit, durability, inventory, packaging, repeat orders.
- Construction/industrial materials: specification, load, corrosion resistance, project supply, bulk shipment.
- Agricultural or utility equipment: application scenario, ease of use, durability, maintenance, seasonal supply.

When the product changes, rewrite hooks, captions, narration, and CTA around that product's buyer pain. Do not reuse motor-specific terms unless the product is actually a motor.

## Batch Variation Rules

For every batch, create a manifest or script-level list that records each ad's hook, main message, CTA, source clips, and exact source time ranges. Across a 10-video batch:

- Use different hook text in every video.
- Use different first shot categories where possible.
- Rotate product detail, factory proof, testing, packaging, and aerial footage.
- Change crop/zoom direction, segment duration, transition timing, subtitle wording, and CTA line.
- Track source usage as `source file + start second + end second`. Do not reuse an already-recorded source range in later batches unless the user explicitly approves reuse.
- Use non-repeating BGM across the batch; do not rotate only a few tracks through many videos.
- Avoid using the same visible Chinese burned-in subtitle source.
- Do not promise platform-detection evasion. Focus on genuinely distinct creative, claims, and footage.

## Resources

- Read `references/ad-video-workflow.md` when planning or revising the creative structure for a campaign.
- Read `references/asset-usage-ledger.md` before selecting source clips for a batch or when the user complains that footage repeats.
- Read `references/music-sourcing.md` before adding BGM or SFX to a deliverable.
- Read `references/multilingual-copy.md` when generating localized hooks, captions, narration, or CTAs.
- Run `scripts/asset_usage_ledger.py` to check or append source time ranges used by a batch.
- Run `scripts/qc_video_batch.py` after rendering a batch to verify deliverables and extract sample frames.

## Delivery

Place finished videos in a clearly named local folder, open the folder for the user, and report the absolute path. Mention only the checks that were actually performed.
