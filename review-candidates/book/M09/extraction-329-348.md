# M09 extraction hand-off: printed 329–348

## Scope and output

- Assigned printed pages **329–348**, 20 authoritative source PNGs individually opened visually, including every page 344–348.
- Assigned 1-based PDF indices **165–175**. Two-up mapping: `printed_page // 2 + 1`; manifest rectangles are local original source-PNG pixels, not PDF-spread coordinates. Rectangles use exclusive right/bottom edges.
- Visual-slot authorities: the >=329 portion of `review-candidates/book/M09/text-319-333.md` and all of `review-candidates/book/M09/text-334-348.md`. No file named `verifiedtext-319-333.md` was found; the existing verified candidate shard has the former name. Neither shard was edited.
- Created **66 separate source-pixel PNG crops** in `images/04-neakordicki-b/`: 39 numbered examples, 22 exercise parts, 5 realization parts.
- Created `review-candidates/book/M09/images-329-348.json`, `review-candidates/book/M09/extract-329-348.py`, and this hand-off file.
- The manifest supplies every requested field: `id`, `example`, `kind`, `printed_page`, `pdf_page`, `source_image`, `rect`, `image`, `review_status`, `review_note`, and `caption`. Paths are repository-root-relative.
- No old `extract.py` plan was imported or executed. No chapter, verified text, <=328 chapter image, shared manifest, or global tracker was changed. No delegation, model subprocess, API, GUI, commit, or push was used.

## Exact slot mapping and independent-review status

**Every image listed below is `pending_independent_review`. None is self-approved.** This status is recorded individually in the manifest. Extractor inspection does not substitute for a separate reviewer.

Filename conventions within `images/04-neakordicki-b/`:

- Numbered example 4.N: `primjer-4-N.png`.
- Exercise N on printed P: `zadatak-4-P-N.png`.
- Realization N on printed P: `zadatak-4-P-N-realizacija.png`.
- Cross-page parts use the explicit suffixes listed below; no stitching or synthetic number/title was added.

| Printed | PDF | Visual slots / images in shard order | Count | Result for each listed image |
| --- | --- | --- | ---: | --- |
| 329 | 165 | Zadaci 1, 2, 3, 4; zadatak 5 početak (`zadatak-4-329-5-a.png`) | 5 | pending independent review |
| 330 | 166 | Zadatak 5 nastavak (`zadatak-4-330-5-b.png`); Realizacija zadatka 3 | 2 | pending independent review |
| 331 | 166 | 4.104, 4.105, 4.106 | 3 | pending independent review |
| 332 | 167 | 4.107; zadaci 1, 2 | 3 | pending independent review |
| 333 | 167 | Zadaci 3, 4; Realizacija zadatka 3 | 3 | pending independent review |
| 334 | 168 | 4.108, 4.109, 4.110 a–c | 3 | pending independent review |
| 335 | 168 | 4.111 a–b, 4.112; zadatak 1 | 3 | pending independent review |
| 336 | 169 | Zadaci 2, 3; Realizacija zadatka 1 početak (`zadatak-4-336-1-realizacija-a.png`) | 3 | pending independent review |
| 337 | 169 | Realizacija zadatka 1 nastavak (`zadatak-4-337-1-realizacija-b.png`); 4.113 a–b | 2 | pending independent review |
| 338 | 170 | 4.114 a–b, 4.115, 4.116 a–b, 4.117 a–b | 4 | pending independent review |
| 339 | 170 | 4.118 a–b, 4.119, 4.120 a–b, 4.121 a–b, 4.122 a–b, 4.123 a–b | 6 | pending independent review |
| 340 | 171 | 4.124, 4.125, 4.126 a–e, 4.127 | 4 | pending independent review |
| 341 | 171 | 4.128, 4.129, 4.130 a–b, 4.131 | 4 | pending independent review |
| 342 | 172 | 4.132 a–b, 4.133, 4.134 a–b | 3 | pending independent review |
| 343 | 172 | 4.135 a–b, 4.136 a–c, 4.137 a–f (both systems) | 3 | pending independent review |
| 344 | 173 | 4.138 a–d; 4.139 a–e (both systems and itd.) | 2 | pending independent review |
| 345 | 173 | 4.140, 4.141, 4.142 a–b | 3 | pending independent review |
| 346 | 174 | Zadaci 1, 2, 3, 4, 5 | 5 | pending independent review |
| 347 | 174 | Zadaci 6, 7, 8, 9 | 4 | pending independent review |
| 348 | 175 | Realizacija zadatka 3 | 1 | pending independent review |
| **Total** | | **66 text slots → 66 images** | **66** | **all pending** |

There is no count discrepancy. Exercise 5 and realization 1 each already occupy two shard slots. The printed exercise number appears only on 329; the realization title appears only on 336. Continuations retain only their actual printed content.

## Source caveats and required reviewer attention

- **4.113 / 337 — cleanup/source_damage/layout_overlap:** faint pencil pointer above the first asterisk meets handwriting below the preceding prose. Upper crop was revised after native-pixel inspection to preserve the pointer rather than cut it. Some pencil underlining remains near the upper edge, explicitly flagged; printed prose is excluded. Pencil harmonic analysis below the notation is also retained. Independent reviewer must assess this source-layout exception, not silently call it a clean-margin pass.
- **4.108–4.109 / 334 and 4.114 / 338 — cleanup:** original pencil circles/analysis remain; no pixels were painted, repaired, or erased.
- **Exercise 2/3 boundary / 336 — source_layout:** the lowest parenthesized figures of exercise 2 lie exceptionally close to the opening slur of exercise 3. Separate edges follow the actual narrow source gap; both printed contents remain. Review both images together against source.
- **4.125 / 340 — source_layout:** the lowest bass ledger note lies immediately above the next prose line. Lower edge uses the narrow natural source separation. The full ledger note is retained; do not enlarge downward indiscriminately.
- **4.116 / 338 and 4.140 / 345:** tight lower source separation; all low asterisks (4.116), beams and slurs (4.140) retained.
- **4.134 / 342:** crop is shifted right of the page-number region to retain complete lowest figured-bass annotations without the printed page number.
- **4.106–4.107, 4.114–4.115, 4.124–4.126, 4.132–4.133, 4.136, 4.139, 4.142:** open staff ends are in the source; no final barlines or continuation material were invented.
- **4.139 / 344:** prose refers to d–f, but the score prints only a–e and itd. The complete two-system score is retained; no f was fabricated.
- Printed composer/work attributions are retained for 4.106, 4.107, 4.115, 4.119, 4.124, 4.125, 4.127, 4.129, 4.131, and 4.142. Printed C-dur/c-mol, CAMBIATA, Allegretto, realization titles, variant labels, asterisks, brackets, and low figures are not replaced by captions.
- Footnote markers in the realization on 333, 4.119 on 339, 4.128 and 4.131 on 341, and the realization on 348 remain in their score images. Their explanatory prose is already separately transcribed in the assigned shards and was not duplicated as score-image body text.
- No unreadable notation was reconstructed or guessed. Original abrasion, faint printing and handwriting are retained; source limitations remain available for independent review.

## Checks and readiness

- Inspected each authoritative page and selected each visual's four edges separately; no fixed batch expansion was applied.
- Inspected all four edges of all 66 initial crops using native-resolution, unresized 32-pixel diagnostic edge strips (left/right strips rotated only for inspection). Additional native-resolution source detail and revised upper-edge checks were used for 4.113. Diagnostic sheets live only in `/tmp/opencode/m09-329-348-edges/`, not in deliverable chapter images.
- Programmatic verification: 66 assigned shard visual slots, matching per-page/order manifest counts, 66 unique existing output paths, correct 1-based PDF indices, and decoded pixel equality of every image with its manifest source rectangle. Extractor re-run also succeeded with its guard against overwriting differing existing images.
- Final images are original source-pixel rectangles only: no resizing, generated borders, padding, stitching, retouching, or generated content.
- **Ready for independent visual review: yes. Ready for final integration/completion: no.** All 66 require a separate reviewer's pass/recrop-required decision; the 4.113 handwriting overlap requires explicit disposition. Integration should insert manifest images/captions and MuseScore placeholders at the corresponding shard slots only after that review.
