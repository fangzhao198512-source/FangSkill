# Editable packaging and review for industrial ads

Use this reference only when a campaign needs a timeline that can be revised after delivery, an editable caption track, or a higher-finish sample/hero ad. It supplements FangSkill's batch workflow; it does not replace the source-range ledger or authorize paid generation.

## Keep the editable layers separate

- Keep real factory footage as the product-proof layer. Do not replace a real identifiable machine with generated imagery.
- Keep hook text, benefit copy, CTA, and captions as editable text layers rather than baking them into generated pixels.
- When narration exists, make captions an editable track with real sentence timing. Derive timing from the TTS provider, sentence-level audio files, silence analysis, or an existing subtitle file; do not invent word-level timing from a long voice track.
- Use restrained motion for industrial B2B copy. Fixed text with a short fade is usually preferable to repeated bouncing, wobbling, or word-by-word motion unless the user explicitly requests that treatment.

## Default English typography for industrial ads

Use a verified local face rather than assuming a web font is installed. On the current Windows editing environment, use this hierarchy unless the user provides brand fonts:

| Text role | Preferred face | Fallback | Use |
| --- | --- | --- | --- |
| Hook / product title | Bahnschrift SemiBold Condensed | Arial Black | Short all-caps product claim; compact industrial appearance |
| Benefit / CTA title | Franklin Gothic Medium | Segoe UI Semibold | Two-line buyer benefit or project prompt |
| Phone / WhatsApp / support copy | Segoe UI Semibold | Arial | Clear contact text and smaller explanatory lines |
| Chinese bilingual label, when needed | Noto Sans SC Black | Segoe UI | Preserve Chinese legibility; do not fake a Latin condensed look |

Keep the typography role stable within one ad. Main English title is normally white; use the brand yellow only for a short eyebrow or contact accent with a dark backing panel. Do not use Impact by default: reserve it for a deliberately bold, short hook after checking it against the machine footage.

## Opening and vertical layout gate

Before exporting, inspect frame 0 and the first second at the intended 9:16 crop.

- If the hook sells finished machinery, the machine must be recognisable on frame 0, not introduced several seconds later.
- Put essential hook/product/CTA text inside the verified safe area. For 1080x1920 short-form layouts, avoid the top 168 px and do not place essential text below 1330 px unless the target placement has been checked.
- Use a readable contrast treatment behind small yellow/accent text; brand color alone is not proof of readability.
- At the CTA, show the contact method long enough to read and verify the final visible frame has no accidental black tail or cut-off contact detail.

## Revision-safe workflow

For an editable project, record the project identity, current revision/version, source asset paths, source time ranges, narration file, caption track, and output path in the campaign manifest. After a material change:

1. Re-read the active project/version before writing; do not apply an old patch to an unknown GUI change.
2. Save one named revision with a short summary of what changed.
3. Export to a new versioned filename; do not overwrite a file already delivered for a prior revision.
4. Recheck the changed interval and its adjacent cuts, then rerun applicable technical checks.

## Three independent release checks

Record each as `passed`, `failed`, or `not_run`.

1. **Technical:** file exists, dimensions/fps/duration, H.264 video, AAC audio when required, and full FFmpeg decode.
2. **Visual and claim:** opening product identity, actual shot-to-copy/narration fit, no repeated visible moment, subtitle fit, safe-area placement, readable CTA, and final-frame check.
3. **Audio perception:** actual exported mix is listened to at opening, a dense narration segment, and CTA. Check pronunciation, intelligibility, clipping, silence, and whether BGM masks the voice. If listening was unavailable, state `not_run`; an audio stream or waveform is not listening evidence.

## When to use this path

Prefer it for a first sample, a flagship ad, or an ad likely to receive several copy/CTA/subtitle revisions. For a ten-video production batch, use it selectively for the stronger variants; FangSkill's ffmpeg/JianYing path remains the efficient default for the rest.
