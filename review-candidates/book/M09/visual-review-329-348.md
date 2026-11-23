# M09 independent visual review — printed pages 329–348

## Outcome

- **66/66 records reviewed; 0 unreviewed.**
- **59 PASS; 7 RECROP_REQUIRED.**
- **7 source-limited holds**, all among the failures; **0 PASS records with a separate source-limited hold**.
- **Not ready for integration:** the seven failures cannot be certified as complete, clean, single rectangular crops from the supplied source pages.
- No safe replacement rectangle is proposed. `proposed_rect` is deliberately absent from every JSON record: no untested or partially effective suggestion is presented as safe.

## Assignment and authoritative sources

Reviewed every record of `review-candidates/book/M09/images-329-348.json` against the corresponding authoritative `sources/pages/page-329.png` through `sources/pages/page-348.png`. Printed pages **329–348** correspond to **1-based PDF pages 165–175**. All record page/image mappings agree with `sources/index.json`.

| Printed pages | PDF page (1-based) |
| --- | --- |
| 329 | 165 |
| 330–331 | 166 |
| 332–333 | 167 |
| 334–335 | 168 |
| 336–337 | 169 |
| 338–339 | 170 |
| 340–341 | 171 |
| 342–343 | 172 |
| 344–345 | 173 |
| 346–347 | 174 |
| 348 | 175 |

The index identifies the page images as direct lossless halves of 300-dpi PDF spreads. This review used those authoritative page images, not embedded OCR or a newly inferred page sequence.

## Method and scope of certification

Every crop was visually compared with its full source-page context, including example/exercise identifiers, actual variant labels, realization titles, attributions, score asterisks/footnote markers, notation, figures, staff ends, lowest stems and feasible genuine whitespace. Native-size crop panels were made only in `/tmp/opencode/m09-review`; their gray labels/separators were review aids, not edits to deliverable images. Full-length source strips spanning both sides of **all four crop boundaries for all 66 records** were also inspected at native pixel resolution. The page-336 collision, 4.113 handwriting and both boundaries of 4.125 were additionally inspected at 2× enlargement.

Decoded-pixel comparison established **66/66 exact matches** between each delivered PNG and its manifest rectangle cut directly from its stated source image. This verifies provenance/no resampling or artificial border in these files; it does not by itself certify that a rectangle is well chosen. Boundary connected-component checks supplemented, but did not replace, visual inspection. Isolated scan flecks were not mistaken for notation, letters or handwriting.

`source_limited: true` denotes an unresolved limitation already present in the authoritative scan/layout, including embedded handwriting or an inseparable printed-content collision. It does **not** authorize painting, retouching, inventing notation or accepting the failed crop. No additional definite abrasion-only uncertainty was identified in the PASS set. Dense original figures are retained as printed; these images are not certified musical transcriptions.

## Failures and source holds

| Record | Printed / PDF page | Decision | Finding |
| --- | --- | --- | --- |
| `primjer-4-108` | 334 / 168 | RECROP_REQUIRED | Pencil circles surround notes in both scale systems. These are embedded handwriting, not printed notation or dust; a full rectangular crop cannot exclude them without losing notation. |
| `primjer-4-109` | 334 / 168 | RECROP_REQUIRED | Handwritten curves below/around notes in the first system. Outer crop edges are clean, but the interior violates the no-handwriting requirement. No complete clean rectangle certified. |
| `zadatak-4-336-2` | 336 / 169 | RECROP_REQUIRED | Bottom `y=892` clips the lowest sharp/4 figure. Enlarged source shows that figure meets the following exercise's opening slur. Extending the rectangle imports foreign slur ink; shrinking loses required figures. |
| `zadatak-4-336-3` | 336 / 169 | RECROP_REQUIRED | Top `y=894` clips its opening long slur and cannot be raised enough without importing exercise 2's lowest figures. The source collision affects both records, not merely their whitespace. |
| `primjer-4-113` | 337 / 169 | RECROP_REQUIRED | Handwritten underlining and a descending arrow above a), reaching the first printed asterisk; handwritten harmonic marks beneath the bass. Tightening only the bottom would leave the upper contamination. |
| `primjer-4-114` | 338 / 170 | RECROP_REQUIRED | Handwritten harmonic analysis below left/middle bass measures interleaves the vertical range of printed lower stars and reaches the staff area. A simple rectangular trim cannot preserve all printed content while eliminating it. |
| `primjer-4-125` | 340 / 171 | RECROP_REQUIRED | Top `y=555` loses the closing attribution parenthesis beginning at `y=553`. Bottom `y=988` truncates the last low bass note, whose ink continues through `y=988`, and already includes prose accent tips beginning at `y=987`, e.g. near `x=604`. These are foreign partial letters/diacritics, not dust. No single full-width rectangle can include the complete bass note while excluding the earlier-starting prose. |

Coordinates above are zero-based source-image coordinates; manifest rectangles use `[left, top, right, bottom]` with right/bottom exclusive. PDF indices are separately **1-based**. No alternative crop has been certified, and no candidate-image changes were made.

## Special contextual checks

- **Exercise 5, pages 329/330:** number 5 is printed on the first page only. Both continuation systems on 330 match the opening. Both records PASS; filename suffixes do not imply printed a)/b) labels.
- **Realization 1, pages 336/337:** the title `Realizacija zadatka 1.` belongs to the opening on 336. The two systems on 337 continue it and end with the final barline; no repeated title/number is printed or needed. Both realization crops PASS, independently of the exercise-2/3 collision higher on page 336.
- **4.124 on page 340:** the lowest staccato dot ends at source `y=552`; bottom `y=555` retains it with narrow genuine separation. The following attribution's upper ink is outside this crop. PASS; do not enlarge its bottom indiscriminately.
- **Footnotes:** score markers are retained in realization 3 on 333, 4.119, 4.131 and realization 3 on 348. Explanatory prose is outside their score-only crops. Printed analytical stars elsewhere, especially those below 4.112, 4.116, 4.120 and 4.122, were checked as score content, not trimmed as footnotes.
- **Actual labels:** 4.137 retains a)–f); 4.139 retains the actual printed a)–e) plus `itd.`. The surrounding prose's reference to f) is not a reason to invent another label.
- Open right staff ends in excerpt examples were compared with the scan and are not assumed to require an invented final barline. Attribution wording is preserved even where the source attribution and visible key signature disagree (4.119).

## Complete per-record results

The companion `review-candidates/book/M09/visual-review-329-348.json` contains one decision and specific reason for **every one of the 66 manifest records**, with the original image path and printed source page. Examples 4.104–4.142 span printed pages 331–345; exercises and realizations cover 329–333, 335–337 and 346–348. The JSON is the complete individual-image hand-off, including all PASS records, not just a list of exceptions.

## Files and integration hand-off

Created only these repository files:

- `review-candidates/book/M09/visual-review-329-348.json`
- `review-candidates/book/M09/visual-review-329-348.md`

No musical examples were extracted or recropped by this reviewer. No images, input manifest, chapter, global tracker or source files were edited; no retouching, delegation, model subprocess, API/GUI work, commit or push was performed. Review aids were temporary only. No human approval is asserted.

**Integration readiness: NO.** Resolve the seven explicit source/crop holds before calling this range visually complete. A rectangle that merely reduces handwriting or foreign ink, clips a figure/slur/note, or leaves a partial prose accent is not an acceptable correction. Unreviewed records: **0**.
