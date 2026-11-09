# Independent visual review — M03, printed pages 119–136

**67/67 reviewed: 29 PASS; 38 RECROP_REQUIRED. Not ready for integration.**

- Assigned source range: printed **119–136**, PDF **60–69**. The 67 records in `review-candidates/book/M03/images-119-136.json` themselves map to **PDF 60–68**, including printed page **136 on PDF page 68**. No record in this manifest is assigned to PDF page 69; record-level mappings below preserve the manifest.
- **67/67 exact decoded-pixel matches; 0 mismatches.** All sources/candidates are RGB. Every candidate's dimensions and raw decoded bytes equal the authoritative source PNG cropped to its manifest rectangle. This establishes provenance, not crop approval.
- Every complete image and authoritative source page was inspected, with **all four edges separately inspected in native-resolution strips**. Ambiguous marks and the page-130 overlap were enlarged. Original source whitespace, staff ends, lowest stems/figures, example numbers, variants, attributions, and realization titles were checked.
- **37 failures are source-limited**: embedded handwriting, coherent foreign source lines, or physically touching printed examples prevent a completely isolated rectangular crop. These are failures, not waivers or permission to retouch.
- **1 fully tested safe replacement rectangle:** `primjer-2-265`, **[209, 2010, 1738, 2381]**. Coordinates are source PNG pixels `[left, top, right, bottom]`, right/bottom exclusive. Top=2010 removes the preceding handwritten 3 fragment and retains genuine whitespace above the highest/rightmost bracket (first ink y=2014). **Top=2015 is unsafe and clips that bracket.** The replacement was tested only in temporary storage, not applied.
- Isolated disconnected scan flecks were distinguished from coherent writing. For example, the small cluster beneath 2.265's first bracket and tiny flecks in the passing 2.295/2.296 and realization images are not treated as letters. The dotted diagonal lines noted below are coherent foreign lines, not handwriting claims or isolated specks.
- Report files only were created. No production crops, manifests, chapter text, tracker, source pixels, commits, or approvals were changed. Temporary inspection/correction tests are under `/tmp/opencode/visual119136/`.

## Critical source limitation: page 130, exercises 5 and 6

Enlarged authoritative source pixels show exercise 5's lowest **x-like figure at the left** and **3 at the right** physically meeting exercise 6's long slur. Exercise 5's crop includes the foreign slur at its bottom. Exercise 6's crop cuts the top of its own slur and includes exercise-5 figure fragments. Raising/lowering a rectangular boundary cannot preserve the complete intended content while removing the adjacent content. **Both are RECROP_REQUIRED, source_limited=true; no safe proposed rectangle.** No retouching or reconstruction was performed or authorized.

## Page totals

| Printed page | PDF page | Reviewed | PASS | RECROP_REQUIRED |
| --- | --- | ---: | ---: | ---: |
| 119 | 60 | 2 | 0 | 2 |
| 120 | 60 | 4 | 0 | 4 |
| 121 | 61 | 4 | 0 | 4 |
| 122 | 61 | 2 | 0 | 2 |
| 123 | 62 | 3 | 2 | 1 |
| 124 | 62 | 3 | 1 | 2 |
| 125 | 63 | 2 | 1 | 1 |
| 126 | 63 | 3 | 0 | 3 |
| 127 | 64 | 3 | 1 | 2 |
| 128 | 64 | 3 | 0 | 3 |
| 129 | 65 | 3 | 0 | 3 |
| 130 | 65 | 10 | 8 | 2 |
| 131 | 66 | 2 | 1 | 1 |
| 132 | 66 | 4 | 2 | 2 |
| 133 | 67 | 4 | 2 | 2 |
| 134 | 67 | 5 | 1 | 4 |
| 135 | 68 | 9 | 9 | 0 |
| 136 | 68 | 1 | 1 | 0 |
| **Total** | **60–68 (manifest)** | **67** | **29** | **38** |

## Per-image decisions

Paths below are complete repository-root-relative image paths. The JSON companion carries the same 67 IDs, page mappings, decisions, detailed reasons, pixel-match results, `proposed_rect`, and boolean `source_limited`. In this table, **—** means `proposed_rect=null`: no fully safe replacement certified. PASS rows have source_limited=false and no proposed change.

| ID | Image | Printed / PDF page | Decision | Reason | proposed_rect | source_limited |
| --- | --- | --- | --- | --- | --- | --- |
| primjer-2-256 | images/02-dijatonika-b/primjer-2-256.png | 119 / 60 | RECROP_REQUIRED | All variants present; pencil arrows enter top/left, handwritten numerals at bottom and overlapping music. | — | true |
| primjer-2-257 | images/02-dijatonika-b/primjer-2-257.png | 119 / 60 | RECROP_REQUIRED | Complete music; handwritten harmonic letters/figures above/below and within bracket heights. | — | true |
| primjer-2-258 | images/02-dijatonika-b/primjer-2-258.png | 120 / 60 | RECROP_REQUIRED | Complete printed system; coherent handwritten letters/numerals in bracket and margin ranges. | — | true |
| primjer-2-259 | images/02-dijatonika-b/primjer-2-259.png | 120 / 60 | RECROP_REQUIRED | Lowest bass stems retained; handwritten analysis overlaps required rectangle and horizontal boundaries. | — | true |
| primjer-2-260 | images/02-dijatonika-b/primjer-2-260.png | 120 / 60 | RECROP_REQUIRED | Complete printed open excerpt; handwriting above/below overlaps printed bracket/stem range. | — | true |
| primjer-2-261 | images/02-dijatonika-b/primjer-2-261.png | 120 / 60 | RECROP_REQUIRED | Staff ends/ties intact; pencil lettering retained and fragmented at top. | — | true |
| primjer-2-262 | images/02-dijatonika-b/primjer-2-262.png | 121 / 61 | RECROP_REQUIRED | Slurs/notation intact; handwritten labels above and analysis beneath/at bottom. | — | true |
| primjer-2-263 | images/02-dijatonika-b/primjer-2-263.png | 121 / 61 | RECROP_REQUIRED | Complete music; surrounding prose's pencil arrows enter top/sides; internal analysis remains. | — | true |
| primjer-2-264 | images/02-dijatonika-b/primjer-2-264.png | 121 / 61 | RECROP_REQUIRED | Left-edge arrow fragment plus internal/bottom handwritten analysis. | — | true |
| primjer-2-265 | images/02-dijatonika-b/primjer-2-265.png | 121 / 61 | RECROP_REQUIRED | Prior example's handwritten 3 fragment at top. Tested top=2010 removes it and preserves all brackets/notation; internal disconnected flecks are not lettering. | [209, 2010, 1738, 2381] | false |
| primjer-2-266 | images/02-dijatonika-b/primjer-2-266.png | 122 / 61 | RECROP_REQUIRED | Bach attribution/all staves intact; handwritten star/check starts y=1235, overlapping lowest required beams' vertical range through y=1241. | — | true |
| primjer-2-267 | images/02-dijatonika-b/primjer-2-267.png | 122 / 61 | RECROP_REQUIRED | Mozart attribution/two systems intact; enlarged inspection confirms internal pencil analysis between systems. | — | true |
| primjer-2-268 | images/02-dijatonika-b/primjer-2-268.png | 123 / 62 | PASS | Beethoven attribution, number, brackets/slurs/ties, staves and lowest stems complete; four clean margins. | — | false |
| primjer-2-269 | images/02-dijatonika-b/primjer-2-269.png | 123 / 62 | RECROP_REQUIRED | Complete Chopin excerpt; coherent dotted diagonal foreign source line enters left and exits bottom, not isolated specks. | — | true |
| primjer-2-270 | images/02-dijatonika-b/primjer-2-270.png | 123 / 62 | PASS | Wagner attribution, number, all slurs/accidentals/staff ends and low stems complete; clean margins. | — | false |
| primjer-2-271 | images/02-dijatonika-b/primjer-2-271.png | 124 / 62 | RECROP_REQUIRED | Variants/figures complete; pencil arrows begin inside notation and lead to handwritten labels. | — | true |
| primjer-2-272 | images/02-dijatonika-b/primjer-2-272.png | 124 / 62 | PASS | Number, accidental, both staves/barlines, connections and 6, 9/7 figures intact; clean edges. | — | false |
| primjer-2-273 | images/02-dijatonika-b/primjer-2-273.png | 124 / 62 | RECROP_REQUIRED | Both variants/lowest figures intact; long pencil arrows and chord labels overlap staves. | — | true |
| primjer-2-274 | images/02-dijatonika-b/primjer-2-274.png | 125 / 63 | PASS | a/b/c, both NE markings, number, stems and all staff ends intact; no surrounding prose/arrows. | — | false |
| primjer-2-275 | images/02-dijatonika-b/primjer-2-275.png | 125 / 63 | RECROP_REQUIRED | All variants/lowest figures retained; coherent handwritten arithmetic between staff and printed figures. | — | true |
| primjer-2-276 | images/02-dijatonika-b/primjer-2-276.png | 126 / 63 | RECROP_REQUIRED | All a–e/figures present; added letters, cross, numerals and pencil curves internal/at edges. | — | true |
| primjer-2-277 | images/02-dijatonika-b/primjer-2-277.png | 126 / 63 | RECROP_REQUIRED | Both systems/a–e/lowest figures intact; pencil curve near a) and dotted foreign line exiting bottom-right. | — | true |
| primjer-2-278 | images/02-dijatonika-b/primjer-2-278.png | 126 / 63 | RECROP_REQUIRED | All systems/variants/lowest figures present; next prose's dotted-j fragment at bottom and coherent diagonal source line at top-right. | — | true |
| primjer-2-279 | images/02-dijatonika-b/primjer-2-279.png | 127 / 64 | PASS | a–d, all staves/ends and lowest stacked figures complete; four clean genuine margins. | — | false |
| primjer-2-280 | images/02-dijatonika-b/primjer-2-280.png | 127 / 64 | RECROP_REQUIRED | Complete variants/NE/figures; handwritten chord names, circles and foreign diagonal line within music rectangle. | — | true |
| primjer-2-281 | images/02-dijatonika-b/primjer-2-281.png | 127 / 64 | RECROP_REQUIRED | Beethoven attribution/notation/printed analysis intact; handwritten letters/numbers/arrows share high-note/attribution heights. | — | true |
| primjer-2-282 | images/02-dijatonika-b/primjer-2-282.png | 128 / 64 | RECROP_REQUIRED | Haydn attribution/printed figures intact; chord lettering, curved pencil arrow and analysis inside bounding rectangle. | — | true |
| primjer-2-283 | images/02-dijatonika-b/primjer-2-283.png | 128 / 64 | RECROP_REQUIRED | Mozart attribution/printed figures intact; handwritten letters below attribution and numerals below staff. | — | true |
| primjer-2-284 | images/02-dijatonika-b/primjer-2-284.png | 128 / 64 | RECROP_REQUIRED | Both Grieg attributions/variants/continuation intact; internal handwritten analysis/circles/arrows and bottom check fragment. | — | true |
| primjer-2-285 | images/02-dijatonika-b/primjer-2-285.png | 129 / 65 | RECROP_REQUIRED | Both variants/notes/ties complete; coherent handwritten letters/figures and connector inside music rectangle. | — | true |
| primjer-2-286 | images/02-dijatonika-b/primjer-2-286.png | 129 / 65 | RECROP_REQUIRED | a–d and lowest figures intact; internal handwriting/arrows and following example's pencil fragments at bottom. | — | true |
| primjer-2-287 | images/02-dijatonika-b/primjer-2-287.png | 129 / 65 | RECROP_REQUIRED | a–d intact; top-cut handwriting, circled 2–3, internal arrows and analysis below bass. | — | true |
| zadatak-2-130-1 | images/02-dijatonika-b/zadatak-2-130-1.png | 130 / 65 | PASS | Number/signatures/tie/staff ends and all chromatic figures including lowest 3 intact; clean edges. | — | false |
| zadatak-2-130-2 | images/02-dijatonika-b/zadatak-2-130-2.png | 130 / 65 | PASS | Number/signatures/elevated rest/tie and lowest 5 complete; tight genuine top margin is clean. | — | false |
| zadatak-2-130-3 | images/02-dijatonika-b/zadatak-2-130-3.png | 130 / 65 | PASS | Number/high notes/staff ends, all lowest figures/accidentals/lines intact; four clean margins. | — | false |
| zadatak-2-130-4 | images/02-dijatonika-b/zadatak-2-130-4.png | 130 / 65 | PASS | Number/signatures/staff/notes, all figures including lowest 2/line complete; no exercise-5 fragments. | — | false |
| zadatak-2-130-5 | images/02-dijatonika-b/zadatak-2-130-5.png | 130 / 65 | RECROP_REQUIRED | Foreign exercise-6 slur at bottom physically meets exercise-5 lowest x-like figure/3; no safe rectangle. | — | true |
| zadatak-2-130-6 | images/02-dijatonika-b/zadatak-2-130-6.png | 130 / 65 | RECROP_REQUIRED | Own long slur cut at top; exercise-5 figure fragments retained. Touching printed figures/slur prevent separation. | — | true |
| zadatak-2-130-7 | images/02-dijatonika-b/zadatak-2-130-7.png | 130 / 65 | PASS | Number/opening ledger note/full slur/all stems and staff ends intact; clean margins. | — | false |
| zadatak-2-130-8 | images/02-dijatonika-b/zadatak-2-130-8.png | 130 / 65 | PASS | Number/time/both slurs/ledger note/lowest stems/staff ends intact; clean edges. | — | false |
| zadatak-2-130-9 | images/02-dijatonika-b/zadatak-2-130-9.png | 130 / 65 | PASS | Number/both systems/full slurs/high and low notes/staff ends complete; clean outer/inter-system space. | — | false |
| zadatak-2-130-10 | images/02-dijatonika-b/zadatak-2-130-10.png | 130 / 65 | PASS | Two-digit number/signatures/full slur/accidentals/beams/staff ends intact; page number excluded. | — | false |
| realizacija-2-131-6 | images/02-dijatonika-b/realizacija-2-131-6.png | 131 / 66 | PASS | Full realization title, both staves/slur/ledger notes/lowest bass stems/barline complete; clean margins. | — | false |
| primjer-2-288 | images/02-dijatonika-b/primjer-2-288.png | 131 / 66 | RECROP_REQUIRED | All a–d/notation/figures complete; handwriting above, between staves and beneath figures remains. | — | true |
| primjer-2-289 | images/02-dijatonika-b/primjer-2-289.png | 132 / 66 | PASS | a–c/staves/ties/low stems/figures and 9/7-to-8 sign intact; four clean margins. | — | false |
| primjer-2-290 | images/02-dijatonika-b/primjer-2-290.png | 132 / 66 | PASS | a/b, v.7 bracket, both staves and all lowest figures/lines complete; four clean margins. | — | false |
| primjer-2-291 | images/02-dijatonika-b/primjer-2-291.png | 132 / 66 | RECROP_REQUIRED | Seven printed chord columns/labels complete; handwritten Dm9/F9-like labels share highest-note vertical range. | — | true |
| primjer-2-292 | images/02-dijatonika-b/primjer-2-292.png | 132 / 66 | RECROP_REQUIRED | Both variants/brackets/ties/lowest figures retained; faint coherent handwritten numerals/letters below, foreign marks above. | — | true |
| primjer-2-293 | images/02-dijatonika-b/primjer-2-293.png | 133 / 67 | RECROP_REQUIRED | a–c/lowest figures complete; handwritten C/F9/G7 and internal/bottom analysis remain. | — | true |
| primjer-2-294 | images/02-dijatonika-b/primjer-2-294.png | 133 / 67 | RECROP_REQUIRED | a–c/lowest figures complete; chord lettering and pencil circles around internal notes/accidentals. | — | true |
| primjer-2-295 | images/02-dijatonika-b/primjer-2-295.png | 133 / 67 | PASS | Number/key/all chords/accidentals/ledger lines/Roman numerals/staff ends intact; adjacent 2.296 excluded. | — | false |
| primjer-2-296 | images/02-dijatonika-b/primjer-2-296.png | 133 / 67 | PASS | Number/both staves/ties/ledger notes/accidentals/full 9/7/5 and 10/lines intact; clean edges. | — | false |
| primjer-2-297 | images/02-dijatonika-b/primjer-2-297.png | 134 / 67 | RECROP_REQUIRED | Complete printed chords/labels; enlarged source shows coherent pencil circle around final VII figure, overlapping label heights. | — | true |
| primjer-2-298 | images/02-dijatonika-b/primjer-2-298.png | 134 / 67 | RECROP_REQUIRED | Staves/figures complete; pencil arrows from prose enter top and overlap bass notes; internal analysis remains. | — | true |
| primjer-2-299 | images/02-dijatonika-b/primjer-2-299.png | 134 / 67 | RECROP_REQUIRED | Staves/ties/figures complete; internal upper-staff pencil arrow and handwritten analysis below. | — | true |
| primjer-2-300 | images/02-dijatonika-b/primjer-2-300.png | 134 / 67 | PASS | Number/all chords/ledger lines/staff ends and both c: and (Es:) rows intact; clean margins. | — | false |
| primjer-2-301 | images/02-dijatonika-b/primjer-2-301.png | 134 / 67 | RECROP_REQUIRED | Printed sequence/figures complete; added pencil figures above brackets, analysis between staves, edge remnants below. | — | true |
| zadatak-2-135-1 | images/02-dijatonika-b/zadatak-2-135-1.png | 135 / 68 | PASS | Number/clef/time/notes/staff ends/all figures including lowest 3/line intact; clean margins. | — | false |
| zadatak-2-135-2 | images/02-dijatonika-b/zadatak-2-135-2.png | 135 / 68 | PASS | Number/key/time/high ledger note/staff ends/all figures and lowest naturals intact; clean edges. | — | false |
| zadatak-2-135-3 | images/02-dijatonika-b/zadatak-2-135-3.png | 135 / 68 | PASS | Number/signatures/beams/rests/staff ends/all accidentals/lowest figures/lines intact; clean edges. | — | false |
| zadatak-2-135-4 | images/02-dijatonika-b/zadatak-2-135-4.png | 135 / 68 | PASS | Number/two systems/signatures/high/low notes/staff ends/all figures complete; clean outer/inter-system space. | — | false |
| zadatak-2-135-5 | images/02-dijatonika-b/zadatak-2-135-5.png | 135 / 68 | PASS | Number/signatures/both complete slurs/high and low dotted notes/staff ends intact; clean margins. | — | false |
| zadatak-2-135-6 | images/02-dijatonika-b/zadatak-2-135-6.png | 135 / 68 | PASS | Number/signatures/full slur/internal ties/low stems/final high dotted note/staff ends intact; clean margins. | — | false |
| zadatak-2-135-7 | images/02-dijatonika-b/zadatak-2-135-7.png | 135 / 68 | PASS | Number/signatures/slur/accidentals/lowest beamed stems/staff ends complete; clean edges. | — | false |
| zadatak-2-135-8 | images/02-dijatonika-b/zadatak-2-135-8.png | 135 / 68 | PASS | Number/signatures/both full slurs/all notes/low stems/staff ends intact; clean edges. | — | false |
| zadatak-2-135-9 | images/02-dijatonika-b/zadatak-2-135-9.png | 135 / 68 | PASS | Number/signatures/full slur/ties/lowest beams/final ledger note/staff ends intact; upper fleck not lettering. | — | false |
| realizacija-2-136-9 | images/02-dijatonika-b/realizacija-2-136-9.png | 136 / 68 | PASS | Full title/both staves/brackets/slur/ties/footnote marker/lowest final bass beams complete; footnote prose/page number excluded. | — | false |

## Hand-off

1. **Assigned pages:** printed 119–136; PDF 60–69. Manifest records cover PDF 60–68, with printed page 136 mapped to PDF 68, not 69.
2. **Files created:** `review-candidates/book/M03/visual-review-119-136.json` and `review-candidates/book/M03/visual-review-119-136.md` only.
3. **Examples reviewed, not extracted or changed:** all 67 manifest records, individually listed above with printed/PDF pages and image paths. No images were extracted by this reviewer.
4. **Image-review results:** 29 PASS, 38 RECROP_REQUIRED; 37 source-limited failures; one source-tested safe proposal, unapplied.
5. **Ambiguous/incomplete material:** page-130 exercises 5/6 cannot be cleanly isolated because their printed content touches. Embedded pencil writing and coherent foreign lines on other failing scans cannot be removed by a complete rectangular crop. No missing notation was reconstructed. Small disconnected scan flecks are not asserted to be lettering. This review does not approve prose transcription, external caption/alt-text integration, or retouching.
6. **Integration readiness:** **not ready**. Apply the one safe recrop through the assigned extraction/integration workflow and obtain independent re-review; resolve source-limited failures without treating this report as human approval or authorization to alter source ink.
