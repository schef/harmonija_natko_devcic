# M02 image-review hand-off

## Current checkpoint

The original batch below covers examples 2.1–2.71. A subsequent batch has added
examples 2.72–2.97 and ten exercises from printed page 45: **36 additional
approved images**, of which 31 are source-only and five are retouched.
There are now **111 approved embedded image parts** (82 source-only and
29 retouched). No saved image remains pending at this checkpoint.

### Subsequent batch: printed pages 38–46 / PDF pages 20–24

Prose on printed pages 38–44 and 46 was transcribed and visually verified by
text agents. Page 45 contains the separately cropped exercises. Continuation
of the paragraph from page 43 to page 44 was joined. Printed asterisk footnotes
for examples 2.83 and 2.87 were transcribed and linked to their captions.

Every example in each range below has the stated final decision.

| Examples / exercises | Printed page | Final image-review result |
| --- | ---: | --- |
| 2.72 | 38 | PASS, source-only |
| 2.73–2.75 | 39 | PASS, source-only |
| 2.76–2.79 | 40 | PASS, source-only |
| 2.80 | 41 | PASS, source-only |
| 2.81 | 41 | PASS, retouched derivative |
| 2.82 | 41 | PASS, source-only |
| 2.83 | 41 | PASS, retouched derivative |
| 2.84–2.86 | 42 | PASS, source-only |
| 2.87–2.89 | 43 | PASS, source-only |
| 2.90 | 44 | PASS, source-only |
| 2.91 | 44 | PASS, retouched derivative |
| 2.92 | 44 | PASS, source-only |
| 2.93 | 44 | PASS, retouched derivative |
| 2.94 | 44 | PASS, source-only |
| Exercises 1–10 (`zadatak-2-45-<number>.png`) | 45 | PASS, source-only |
| 2.95–2.96 | 46 | PASS, source-only |
| 2.97 | 46 | PASS, retouched derivative |

The five additional derivatives were independently checked against original
crops and scans, including every changed region and all four edges. Original
crops remain intact and pixel-identical to their recorded source rectangles.

- **2.81:** removed pencil fragments beneath the bass. Restored small erased
  portions of the printed example number from source pixels; re-review passed.
- **2.83:** removed the separately transcribed footnote sentence where it
  overlapped the lowest bass stem vertically. Preserved the score asterisk and
  full stem; restored slur-edge source pixels; re-review passed.
- **2.91:** removed a neighbouring 2.90 fragment while retaining both complete
  melodic/harmonic rhythm labels and note sequences; re-review passed.
- **2.93:** removed only a prose fragment in crop-local box `[112,0,121,2)`.
  All other pixels were restored from the scan after cleanup touched the label
  and barline. Re-review confirmed exactly 15 altered pixels, all inside the
  authorized prose-removal box, with complete notation and labels.
- **2.97:** removed pencil marks above variant b and below the notation.
  Independent review confirmed intact number, a–b, NE, all printed notation,
  and figured-bass 6; all four edges passed. The unchanged original rectangle
  `[457,1523,1292,1887]` remains recorded in the crop manifest.
- Source-only boundary corrections to **2.82, 2.86, and 2.87** were independently
  re-reviewed and passed. No printed notation was sacrificed to hide marks.

### Resume here

1. Continue on printed page **47 / PDF page 24**, starting with example 2.98.
   Page-46 prose already references 2.98 and 2.99; their source images and the
   continuation still need processing.
2. Complete M02 through printed page 63 and perform full-section prose/link/
   rendered-preview checks before marking the milestone complete.

No musical content was unreadable in this subsequent batch. All saved crops
are now approved in their documented source-only or retouched form. After the
stopping request, the user explicitly requested the final GIMP cleanup of 2.97;
it passed review and was integrated without proceeding to the next page.

## Original batch: examples 2.1–2.71

## Scope and status

- Assigned milestone: M02, printed pages 11–63, PDF pages 6–32.
- This image batch: printed pages 11–37, PDF pages 6–19.
- 71 numbered examples, represented by 75 image files, independently reviewed.
- 51 embedded images pass as unchanged source-only crops.
- 24 embedded images pass as explicitly authorized manually retouched derivatives.
- Image integration for this batch is complete. This does not certify prose or
  complete M02; printed pages 38–63 remain outside this batch.

## Provenance and cleanup exception

Original crops are `images/02-dijatonika-a/primjer-2-<number>.png`, with
separately named continuation parts. Their authoritative source images and
rectangles are recorded in `tools/crop-locations.json`.

The user explicitly authorized removing handwriting in GIMP. Approved cleaned
copies are kept separately under `images/02-dijatonika-a/retouched/` and embedded
instead of their handwriting-contaminated originals. These are **retouched
derivatives**, not unaltered source-only crops, and do not claim strict compliance
with the default source-only extraction rule. Original source scans and crops
are retained. Working files remain under
`review-candidates/manual-cleanup/02-dijatonika-a/`.

Each derivative was independently compared against its original crop and source.
Review covered every changed region, all four edges at native resolution and
enlargement, complete printed notation and labels, and removal of handwriting.
No image generation, artificial borders, or score reconstruction was used.

## Final decisions by example

Every example in each listed range has the stated final result.
**S** = PASS as source-only crop; **R** = PASS as retouched derivative.

| Examples | Printed page | Final result |
| --- | ---: | --- |
| 2.1–2.2 | 11 | S |
| 2.3–2.4 | 12 | S |
| 2.5–2.6 | 13 | S |
| 2.7–2.9 | 14 | S |
| 2.10–2.11 | 15 | S |
| 2.12–2.15 | 16 | S |
| 2.16–2.19 | 17 | S |
| 2.20–2.22 | 18 | S |
| 2.23 | 19 | S |
| 2.24 | 19 | R |
| 2.25–2.26 | 20 | S |
| 2.27–2.28 | 21 | S |
| 2.29–2.32 | 22 | R |
| 2.33–2.34 | 23 | R |
| 2.35 | 23 | S |
| 2.36–2.37 | 23 | R |
| 2.38 | 24 | R |
| 2.39 | 24 | S |
| 2.40 | 25 | S |
| 2.41–2.42 | 25 | R |
| 2.43–2.45 | 26 | R |
| 2.46 | 27 | R |
| 2.47–2.49 | 27 | S |
| 2.50 | 27 | R |
| 2.51–2.52 | 28 | R |
| 2.53–2.54 | 29 | R |
| 2.55–2.56 | 30 | R |
| 2.57–2.60 | 32 | S |
| 2.61 | 33 | S |
| 2.62 | 33 | R |
| 2.63–2.64 | 33 | S |
| 2.65 | 34 | S |
| 2.66a–c (`primjer-2-66.png`) | 34 | S |
| 2.66d–e (`primjer-2-66-d-e.png`) | 35 | S |
| 2.67a–b (`primjer-2-67-a-b.png`) | 35 | S |
| 2.67c (`primjer-2-67-c.png`) | 35 | S |
| 2.67d (`primjer-2-67-d.png`) | 36 | S |
| 2.68 | 36 | S |
| 2.69a (`primjer-2-69.png`) | 36 | S |
| 2.69b (`primjer-2-69-b.png`) | 37 | S |
| 2.70–2.71 | 37 | S |

## Corrections resolved

- Restored omitted variants 2.24d–f and 2.42b with complete source-only recrops.
- Corrected 2.57 and 2.58, which initially contained 2.59 and 2.60 respectively.
- Separated 2.67a–b from c; removed the nonexistent b-continuation placeholder.
- Recovered the lowest bass stem in 2.51 without clipping notation to hide pencil.
- Trimmed foreign edge marks from 2.23, 2.39, and 2.40 and re-reviewed them.
- Re-reviewed every handwriting cleanup, including subsequent tiny edge repairs.
- Restored accidentally erased printed pixels in 2.41 and 2.44 directly from the
  authoritative source scans; both restored derivatives passed independent review.
- The 2.41 reference crop was accidentally edited during manual restoration. Its
  edited state is preserved as `primjer-2-41-edited-reference-backup.png` in the
  working directory. The original crop was rebuilt from its source rectangle and
  independently verified pixel-identical to the scan.
- Corrected the 2.68 caption to include Beethoven and J. S. Bach, and the 2.69
  caption to include Bach and Debussy on printed pages 36–37.

No unresolved unreadable or incomplete musical content was reported in these
approved images. MuseScore transcription remains pending. Full-section prose
verification and local rendered-preview review are not certified by this report.
