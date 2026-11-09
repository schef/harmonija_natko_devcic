# Independent visual review — M03, printed pages 82–100

## Outcome

- **80/80 reviewed; 0 unreviewed.**
- **32 PASS; 48 RECROP_REQUIRED.**
- All **48 rejected crops are source-limited** under the strict clean-crop checklist: 46 contain source handwriting within the required printed-content envelope; two have an unavoidable rectangular-layout conflict (page 91, exercises 4 and 5).
- **80/80 exact decoded-pixel matches:** each image has the dimensions and RGB pixel values of its authoritative source PNG cropped with the manifest rectangle. No generated border or other pixel substitution was detected.
- **No safe replacement rectangles proposed.** None was established that removes all foreign content without losing required printed content. Consequently there are no proposed rectangles awaiting a temporary-crop test.
- **Not ready for integration under the mandatory image checklist.** A source-limited rejection is not approval to erase handwriting, clip notation or accept the current crop.

Assignment: printed **82–100**, PDF **42–51**; manifest `review-candidates/book/M03/images-082-100.json`. Sources: `sources/pages/page-082.png` through `sources/pages/page-100.png`.

## Inspection and evidence

Reviewed every authoritative page against its assigned crops, including printed numbers, variant letters, exercise and realization titles, composer/work attributions, clefs, key/time signatures, lowest stems, final barlines and complete harmonic/figured-bass analysis. Every crop's **top, bottom, left and right edges** was inspected in native-resolution 40-pixel strips; side strips were rotated without resampling. Separate complete side strips were inspected for the three tall crops whose first sheet did not fit both sides. Additional individual crop views and enlarged source details resolved ambiguous handwriting and the page-91 overlap. Temporary inspection material was confined to `/tmp/opencode/m03-review/`.

Pillow decoded-pixel comparison checked every crop against `source.crop(rect)`; all 80 matched exactly. Sparse irregular scan specks were not misclassified as pencil lettering. Coherent handwritten numerals, Roman numerals, letters, arrows and circles were treated as foreign source marks, even where faint. Printed `NE`, `DA`, accidentals, brackets and figures were retained as intended content, not confused with handwriting.

Image paths, manifest identities/captions and printed source pages were compared with the sources. Actual chapter Markdown alt text and placement were not part of this assigned image review and are not certified here. The JSON companion records every full image path, decision, reason, `proposed_rect` and `source_limited` flag.

## Critical source conflicts and split examples

### Page 91: exercises 4 and 5

Enlarged source inspection and foreground-component coordinates confirm that exercise 4's lowest figured-bass continuation extends through **y=2247**, while exercise 5's highest ledger-note group begins at **y=2244**. These are source coordinates, with crop rectangles interpreted as `[left, top, right, bottom)`.

- Exercise 4's bottom at 2256 admits the upper part of exercise 5's note.
- Exercise 5's top at 2245 admits the lower parts of exercise 4's figures and also begins below the highest exercise-5 ink.
- Moving a horizontal edge cannot separate the two vertical ranges. Moving a side edge far enough to discard the conflict would lose required staff or analysis content. **Both are RECROP_REQUIRED, source_limited=true; no safe rectangular correction.**

### Pages 97–98: example 2.213

- Page 97 contains the printed number and variants **a)–m)** over two systems.
- Page 98 continues with **n), o), p), r), s), t)**. The missing alphabetic q is as printed, not a missing crop component. No example number is reprinted on this continuation.
- Both portions retain their complete printed notation and lowest figures, including the stars on page 97 and t)'s signatures on page 98. Both are rejected for embedded source handwriting, **not** because either portion should independently contain the whole cross-page example or an invented repeated number.

### Page 98: example 2.214

- Part a retains **2.214**, **a)**, **J. S. Bach: Koral br.7**, signatures, fermatas and complete 6/5.
- Part b retains **b)**, its separate **J. S. Bach: Koral br.71** attribution, signatures, lowest bass stem/fermata and figured bass. Its number is supplied by part a in the source layout; no repeated number should be fabricated.
- Both parts contain handwriting within their required printed bounds and are rejected as source-limited. Keep their association explicit during integration.

## All 80 decisions

All rows have `proposed_rect: null`. “Limited” means `source_limited: true`; it is a blocker, not an approval exception. Detailed reasons and full image paths are in `review-candidates/book/M03/visual-review-082-100.json`.

| ID | Decision | Limited | Finding |
| --- | --- | --- | --- |
| p082:zadatak 5 | PASS | No | Number and both complete systems; four clean edges. |
| p082:zadatak 6 | PASS | No | Full signatures, low natural and final barline. |
| p082:zadatak 7 | PASS | No | Number, sharps, slurs and final barline intact. |
| p082:Realizacija zadatka 4. | PASS | No | Full title, both systems and lowest stems. |
| p083:2.168 | PASS | No | Brackets and lower 7s complete; no prose. |
| p083:2.169 | PASS | No | Full notation/figures; isolated marks are specks. |
| p083:2.170 | RECROP_REQUIRED | Yes | Pencil around NE and below a), overlapping required content. |
| p083:2.171 | RECROP_REQUIRED | Yes | Pencil above variants and between staves. |
| p084:2.172 | RECROP_REQUIRED | Yes | Pencil below a) overlaps lowest-stem height. |
| p084:2.173 | RECROP_REQUIRED | Yes | Pencil above/alongside variant labels. |
| p084:2.174 | RECROP_REQUIRED | Yes | Internal and inter-system pencil analysis. |
| p085:2.175 | RECROP_REQUIRED | Yes | Pencil diagonal connects notation to handwriting. |
| p085:2.176 | RECROP_REQUIRED | Yes | Internal pencil circles and analysis. |
| p085:2.177 | RECROP_REQUIRED | Yes | Pencil text conflicts with staff-end/lowest-3 bounds. |
| p085:2.178 | RECROP_REQUIRED | Yes | Pencil words, circles and analysis within full bounds. |
| p086:2.179 | RECROP_REQUIRED | Yes | Pencil circle crosses barline/bracket area. |
| p086:2.180 | PASS | No | Full chord, bracket, lower 2 and barline. |
| p086:2.181 | PASS | No | All four variants and complete lower figures. |
| p086:2.182 | RECROP_REQUIRED | Yes | Pencil starts before lowest printed 3s end. |
| p087:2.183 | RECROP_REQUIRED | Yes | Pencil above c) and between b)'s staves. |
| p087:2.184 | RECROP_REQUIRED | Yes | Pencil words and inter-system/internal marks. |
| p087:2.185 | RECROP_REQUIRED | Yes | Internal pencil; printed star and figures retained. |
| p088:2.186 | RECROP_REQUIRED | Yes | Pencil words, circled notes and analysis. |
| p088:2.187 | PASS | No | Complete small example; four clean edges. |
| p088:2.188 | RECROP_REQUIRED | Yes | Pencil brackets/numerals within e) and elsewhere. |
| p088:2.189 | RECROP_REQUIRED | Yes | Pencil circle around NE and internal analysis. |
| p089:2.190 | RECROP_REQUIRED | Yes | Pencil between staves and around/below analysis. |
| p089:2.191 | RECROP_REQUIRED | Yes | Pencil 7, circled chord and lower analysis. |
| p089:2.192 | RECROP_REQUIRED | Yes | Pencil circle overlaps printed NE label height. |
| p089:2.193 | RECROP_REQUIRED | Yes | Pencil diagonal/circle through printed area. |
| p090:2.194 | RECROP_REQUIRED | Yes | Pencil analysis conflicts with printed B: analysis. |
| p090:2.195 | RECROP_REQUIRED | Yes | Pencil D–T, circles and Roman numerals. |
| p090:2.196 | RECROP_REQUIRED | Yes | Pencil arrow enters printed arrow/note area. |
| p091:2.197 | RECROP_REQUIRED | Yes | Bach attribution complete; internal/lower pencil. |
| p091:2.198 | RECROP_REQUIRED | Yes | Attribution and lowest bass intact; pencil overlaps low range. |
| p091:2.199 | RECROP_REQUIRED | Yes | Schumann attribution complete; overlapping pencil analysis. |
| p091:zadatak 1 | PASS | No | All three figured-bass levels retained. |
| p091:zadatak 2 | PASS | No | Full figures including lowest natural. |
| p091:zadatak 3 | PASS | No | Full signatures, figures and continuations. |
| p091:zadatak 4 | RECROP_REQUIRED | Yes | Source vertical overlap with exercise 5. |
| p091:zadatak 5 | RECROP_REQUIRED | Yes | Source vertical overlap; present top cuts highest ink. |
| p092:zadatak 6 | PASS | No | Highest/lowest ledger notes complete; isolated specks only. |
| p092:zadatak 7 | PASS | No | Low final dotted note and all signatures intact. |
| p092:zadatak 8 | PASS | No | Full accidentals, signature and fermata. |
| p092:zadatak 9 | PASS | No | Both slurs and final note/barline intact. |
| p092:zadatak 10 | PASS | No | Full number, flats, slurs and melody. |
| p092:zadatak 11 | PASS | No | Nested/long slurs intact; isolated speck only. |
| p092:zadatak 12 | PASS | No | Full melody, sharp and slurs. |
| p092:zadatak 13 | PASS | No | Both systems and continuation intact. |
| p092:zadatak 14 | PASS | No | Full flats and highest ledger notes. |
| p092:zadatak 15 | PASS | No | Full slur and barline; tiny scan speck only. |
| p092:zadatak 16 | PASS | No | All sharps, rhythms and low notes retained. |
| p093:Realizacija zadatka 13. | PASS | No | Full title and both complete grand-staff systems. |
| p093:2.200 | PASS | No | All seven chords and I7–VII7 analysis. |
| p093:2.201 | RECROP_REQUIRED | Yes | Internal pencil and lower Roman numerals. |
| p094:2.202 | RECROP_REQUIRED | Yes | Pencil overlaps labels/low-stem height. |
| p094:2.203 | RECROP_REQUIRED | Yes | Pencil circle around DA and internal marks. |
| p094:2.204 | RECROP_REQUIRED | Yes | Pencil word, arrow and circled bass. |
| p094:2.205 | RECROP_REQUIRED | Yes | Internal circles/numerals and upper arrow. |
| p095:2.206 | RECROP_REQUIRED | Yes | Coherent handwritten 7 inside b)'s grand staff. |
| p095:2.207 | RECROP_REQUIRED | Yes | Pencil starts before rightmost low accidental ends. |
| p095:2.208 | RECROP_REQUIRED | Yes | Pencil words, figures and internal strokes. |
| p096:2.209 | RECROP_REQUIRED | Yes | Pencil diagonals/figures within staves. |
| p096:2.210 | RECROP_REQUIRED | Yes | Embedded circles, DA, analysis and brackets. |
| p097:2.211 | RECROP_REQUIRED | Yes | Pencil arrows touch upper notation. |
| p097:2.212 | RECROP_REQUIRED | Yes | Pencil labels and circle overlap printed bounds. |
| p097:2.213.a—m | RECROP_REQUIRED | Yes | Complete first portion; internal/inter-system handwriting. |
| p098:2.213.n—t (nastavak) | RECROP_REQUIRED | Yes | Complete continuation; pencil overlaps figure-height range. |
| p098:2.214.a | RECROP_REQUIRED | Yes | Number, title, fermatas intact; upper/lower pencil. |
| p098:2.214.b | RECROP_REQUIRED | Yes | Separate title and low stems intact; internal pencil arrows. |
| p099:2.215 | RECROP_REQUIRED | Yes | All a)–h) retained; internal pencil circles/analysis. |
| p099:2.216 | RECROP_REQUIRED | Yes | Dense harmonic handwriting within full content envelope. |
| p100:2.217 | RECROP_REQUIRED | Yes | Internal pencil circles and lower Roman numerals. |
| p100:2.218 | PASS | No | Complete signatures, brackets, stems and stacked figures. |
| p100:2.219 | PASS | No | Complete ties, ledger notes and analysis. |
| p100:2.220 | PASS | No | Complete bass continuation and 2/7 figures. |
| p100:2.221 | PASS | No | All a)–d), lowest figures and barline intact. |
| p100:zadatak 1 | PASS | No | Full figures/signatures; heading excluded. |
| p100:zadatak 2 | PASS | No | High notes and three-level analysis retained. |
| p100:zadatak 3 | PASS | No | Low melody and three-level analysis retained; page excluded. |

## Hand-off

1. **Assigned pages:** printed 82–100 / PDF 42–51; all 80 manifest entries reviewed.
2. **Files created:** `review-candidates/book/M03/visual-review-082-100.json` and `review-candidates/book/M03/visual-review-082-100.md` only. No image, manifest, chapter or milestone/global file was changed.
3. **Examples extracted:** none by this reviewer. Existing examples 2.168–2.221, exercises and two realizations were reviewed on their manifest printed pages, explicitly enumerated above.
4. **Review results:** 32 PASS / 48 RECROP_REQUIRED; every entry has a decision and full reason in JSON; zero unreviewed.
5. **Source limitations:** 46 images have coherent source handwriting inseparable by a complete rectangular crop; page-91 exercises 4/5 have overlapping vertical extents. Faint handwritten words need not be transcribed to establish that they are foreign marks. No printed content was silently reconstructed, erased or clipped. Cross-page/split numbering limitations are documented, not treated as missing invented content.
6. **Integration readiness:** blocked by the 48 image rejections. Obtain an appropriately clean authoritative source or resolve the source limitation explicitly under the parent workflow; do not interpret this review as a waiver. No human approval, self-approval, commit or push is claimed.
