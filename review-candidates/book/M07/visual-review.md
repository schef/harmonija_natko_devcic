# M07 — independent visual review

**Outcome: not ready for integration.** All **57/57** records reviewed: **36 PASS**, **21 RECROP_REQUIRED**, including **17 source-limited** handwriting failures. **Unreviewed: none.** Source-limited is a subset of RECROP_REQUIRED, not an additional decision.

## Assignment and verification

- Scope: printed pages **257–276**, PDF pages **129–139 (1-based)** only.
- Read `images.json`, verified `text-257-276.md`, `text-257-276-review.json`, and `sources/index.json`.
- Opened every authoritative `sources/pages/page-257.png` through `page-276.png`, and every one of the 57 individual crops. Examined all four crop edges at native crop resolution, including clef curls, lowest stems/figures, staff ends, variant labels, attributions and realization titles. Enlarged the ambiguous marks in 3.196 separately.
- Independent decoded-pixel comparison: **57/57** crops equal their recorded source rectangle, with no resampling, retouching or artificial border detected. Source image and 1-based PDF mappings: **57/57** agree with source index.
- Manifest filenames, example/exercise identities, captions and printed-page references agree with source. Text candidate still uses visual comments rather than final image embeds: final alt text, image blocks, captions and MuseScore placeholders must be checked during integration.
- Multi-system examples retain their printed number on the first system only, with later variant labels preserved. No repeated numbers need to be invented.

## Per-image decisions

Full image paths and detailed reasons are recorded for every ID in `visual-review.json`; IDs below are those of `images.json`.

| ID | Example / exercise | Printed page | Decision | Finding |
| --- | --- | ---: | --- | --- |
| M07-01 | 3.176 | 257 | RECROP_REQUIRED | Handwritten V below c and strokes beside its label; source-limited. |
| M07-02 | 3.177 | 257 | RECROP_REQUIRED | Handwritten harmonic analysis above/below and within content envelope; source-limited. |
| M07-03 | 3.178 | 258 | RECROP_REQUIRED | Handwriting between Chopin attribution and slur; source-limited. |
| M07-04 | 3.179 | 258 | RECROP_REQUIRED | Handwritten labels interspersed with a–d; source-limited. |
| M07-05 | 3.180 | 258 | PASS | Complete a–g, three systems, figures and continuation marks; clean edges. |
| M07-06 | 3.181 | 259 | RECROP_REQUIRED | Lowest (D) clipped; tested replacement below. |
| M07-07 | 3.182 | 259 | PASS | Full Liszt excerpt, Akordička redukcija, links and figures. |
| M07-08 | 3.183 | 260 | PASS | Attribution, staves, slurs and lowest figures complete. |
| M07-09 | 3.184 | 260 | PASS | Attribution, asterisks, low beams and figures complete. |
| M07-10 | 3.185 | 260 | PASS | a/b, modulation titles and low figures complete. |
| M07-11 | 3.186 | 261 | PASS | Both variants, alternative chords and lowest parentheses complete. |
| M07-12 | 3.187 | 261 | PASS | a–c, modulation titles and figures complete. |
| M07-13 | 3.188 | 261 | PASS | Both a/b systems and brackets complete. |
| M07-14 | 3.189 | 262 | PASS | a/b and all lower accidentals complete. |
| M07-15 | 3.190 | 262 | RECROP_REQUIRED | Handwritten labels at same heights as mandatory printed labels; source-limited. |
| M07-16 | 3.191 | 263 | PASS | Two systems, a–d and continuing c complete. |
| M07-17 | 3.192 | 263 | PASS | All a/b/c parts, brackets, v.2, triplet and flags complete. |
| M07-18 | 3.193 | 264 | PASS | Number, low sharp, scale and final barline complete. |
| M07-19 | 3.8 exercise 1 | 264 | PASS | Two systems and all figures complete; tight genuine separation. |
| M07-20 | 3.8 exercise 2 | 264 | PASS | Three systems and all figures complete; preceding figures excluded. |
| M07-21 | 3.8 exercise 3 | 264 | PASS | Two complete systems, number and final barline. |
| M07-22 | 3.8 exercise 4 | 265 | PASS | Two complete systems and low stems. |
| M07-23 | 3.8 exercise 5 | 265 | PASS | Two systems, low tie, fermata and final barline. |
| M07-24 | 3.8 exercise 6 | 265 | PASS | Full clef, slurs, beams and final barline. |
| M07-25 | 3.8 exercise 7 | 265 | PASS | Full clef including curl; narrow genuine bottom whitespace. |
| M07-26 | 3.8 exercise 8 | 265 | PASS | Slurs, low ledger notes and final barline complete. |
| M07-27 | 3.8 exercise 9 | 265 | RECROP_REQUIRED | Lower clef curl clipped; tested replacement below. |
| M07-28 | 3.8 exercise 10 | 265 | PASS | Number 10, both systems, slurs and low notes complete. |
| M07-29 | Realizacija zadatka 6. | 266 | PASS | Full title, both grand-staff systems and lowest stems. |
| M07-30 | 3.194 | 267 | RECROP_REQUIRED | Writing interleaved with a–d and circles touching figures; source-limited. |
| M07-31 | 3.195 | 267 | RECROP_REQUIRED | Pencil line/lettering crosses notation; source-limited. |
| M07-32 | 3.196 | 268 | PASS | Complete excerpt/attribution; enlarged tiny marks are isolated specks/dashes, not meaningful lettering. |
| M07-33 | 3.197 | 268 | PASS | a–d and lowest stems/ties complete. |
| M07-34 | 3.198 | 268 | PASS | a–d, low stems and all staff ends complete. |
| M07-35 | 3.199 | 269 | PASS | a–d and both staves complete. |
| M07-36 | 3.200 | 269 | PASS | Both systems, all a–g, low ties/stems complete. |
| M07-37 | 3.201 | 269 | RECROP_REQUIRED | Handwritten harmonic labels above/between/below staves; source-limited. |
| M07-38 | 3.202 | 270 | RECROP_REQUIRED | Pencil analysis within required notation envelope; source-limited. |
| M07-39 | 3.203 | 270 | RECROP_REQUIRED | Internal handwriting and surrounding analysis; source-limited. |
| M07-40 | 3.204 | 270 | RECROP_REQUIRED | Internal writing and upper foreign partial marks; source-limited. |
| M07-41 | 3.205 | 270 | RECROP_REQUIRED | Handwriting above/below upper scale inside required envelope; source-limited. |
| M07-42 | 3.9 exercise 1 | 271 | PASS | Both systems, number and lowest figures complete. |
| M07-43 | 3.9 exercise 2 | 271 | PASS | All three systems and lowest figures complete; tight clean lower gap. |
| M07-44 | 3.9 exercise 3 | 271 | RECROP_REQUIRED | Clef curl clipped; tested replacement below. |
| M07-45 | 3.9 exercise 4 | 271 | RECROP_REQUIRED | Lower-system clef curl clipped; tested replacement below. |
| M07-46 | 3.9 exercise 5 | 271 | PASS | Both systems, complete clefs/slurs and final barline. |
| M07-47 | Realizacija zadatka 3. | 272 | PASS | Full title, both grand-staff systems and lowest notes. |
| M07-48 | 3.206 | 273 | RECROP_REQUIRED | Handwritten analysis overlaps slurs/notation; source-limited. |
| M07-49 | 3.207 | 273 | RECROP_REQUIRED | Handwritten upper label shares height envelope with clef; source-limited. |
| M07-50 | 3.208 | 274 | RECROP_REQUIRED | Handwriting between staves and among lower figures; source-limited. |
| M07-51 | 3.209 | 274 | PASS | High staccato notes, low beams and complete harmonic lines retained. |
| M07-52 | 3.210 | 274 | PASS | a–d, full lower figures; page number excluded. |
| M07-53 | 3.211 | 275 | PASS | Full Strauss attribution, ties and lowest figures. |
| M07-54 | 3.212 | 275 | PASS | a–d and lowest flats complete. |
| M07-55 | 3.213 | 275 | PASS | Full Grieg attribution, three staves, lowest ledger notes and slur. |
| M07-56 | 3.214 | 276 | RECROP_REQUIRED | Handwriting beside a–c within printed-label envelope; source-limited. |
| M07-57 | 3.215 | 276 | RECROP_REQUIRED | Internal handwritten circles/labels and foreign edge marks; source-limited. |

Every PASS includes all four clean edges, intact required notation/labels, feasible genuine source-white margins, and no meaningful foreign lettering, prose, page numbers or handwriting. Tiny isolated scan specks are not confused with meaningful labels. In exercises 3.8/1–2 and 3.9/2–3 the tight natural separations constrain white margins; do not apply a fixed padding expansion.

## Fully source-tested replacement rectangles

Coordinates are `[left, top, right, bottom]`, with right/bottom exclusive, in the recorded authoritative PNG. Each proposal was saved as an unmodified source crop under `/tmp/opencode/M07-review/` and opened; all four replacement edges were checked. Proposals are recommendations only: no repository images were changed.

| ID | Authoritative source | Replacement rectangle | Tested temporary crop |
| --- | --- | --- | --- |
| M07-06 | `sources/pages/page-259.png` | `[237, 373, 1773, 1296]` | `/tmp/opencode/M07-review/proposed-06.png` |
| M07-27 | `sources/pages/page-265.png` | `[210, 1421, 1732, 1770]` | `/tmp/opencode/M07-review/proposed-27.png` |
| M07-44 | `sources/pages/page-271.png` | `[199, 1443, 1719, 1597]` | `/tmp/opencode/M07-review/proposed-44.png` |
| M07-45 | `sources/pages/page-271.png` | `[196, 1620, 1719, 1980]` | `/tmp/opencode/M07-review/proposed-45.png` |

These restore complete lowest printed content with genuine white margins and do not import adjacent exercise/prose ink. No replacement rectangle is proposed for the 17 source-limited records: handwriting is interleaved with mandatory printed content, not simply removable outer whitespace. **Do not retouch, paint out handwriting, fabricate borders or clip required notation to force a pass.** A cleaner authoritative scan or explicit source-policy decision is needed. Newly applied crops still require the integration/re-review checks.

## Hand-off

1. Assigned/reviewed: printed **257–276**, PDF **129–139**; all 20 pages opened.
2. Only repository files created: `review-candidates/book/M07/visual-review.json` and `review-candidates/book/M07/visual-review.md`.
3. No musical examples extracted by this reviewer. Reviewed examples **3.176–3.215**, chapter 3.8 exercises **1–10** and realization **6**, chapter 3.9 exercises **1–5** and realization **3**, with printed pages listed above.
4. Image results: **36 PASS / 21 RECROP_REQUIRED**, **17 source-limited**, **0 unreviewed**.
5. Main source limitation is meaningful handwritten analysis over/among printed music. No additional unreadable printed material identified that justifies inventing notation. The disputed tiny marks in 3.196 were enlarged and classified as isolated specks, not legible analysis.
6. **Not ready for integration:** apply the four tested clipping corrections and obtain their re-review; resolve the 17 source-limited failures; then validate final Markdown image/alt/caption/source-page/MuseScore blocks. No images, raw manifest, chapter, global tracker, commits or pushes were changed/performed.
