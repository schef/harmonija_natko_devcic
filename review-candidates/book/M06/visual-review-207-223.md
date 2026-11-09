# Independent visual review — M06, printed pages 207–223

**52/52 records reviewed: 30 PASS; 22 RECROP_REQUIRED. Not ready for integration.**

## Scope and verification

- Input: `review-candidates/book/M06/images-207-223.json` (52 records).
- Assignment: printed pages **207–223**, PDF pages **104–112**, inclusive, 1-based.
- Authoritative pages: `sources/pages/page-207.png` through `sources/pages/page-223.png`; mapping checked against `sources/index.json`.
- Independently opened all 17 source pages and all 52 actual crop PNGs. Inspected each crop's four edges at native resolution, staff ends, numbers/variants/exercise IDs, attribution/realization/modulation titles, figures, lowest stems, surrounding whitespace and foreign marks. Enlarged crowded source regions and the 3.95 bass/bottom edge separately.
- **52/52 actual crops are pixel-identical** to their recorded `[left, top, right, bottom]` source rectangles, including dimensions. No generated margins, resampling or retouching detected.
- Independently rendered all nine PDF spreads at 300 dpi into temporary storage. **17/17 authoritative source PNGs are pixel-identical** to the indexed halves of those fresh renders. PDF side/page provenance is therefore confirmed, not inferred from the text comments.
- Manifest image names, IDs, printed pages and captions agree with source identities. The candidate text currently uses visual-slot comments rather than final Markdown image/alt-text blocks: final integrated alt text/link placement cannot yet be approved. This does not invalidate the reviewed image identities.
- This worker did not extract or modify any final image. No delegation, API/model subprocess, GUI, retouching, chapter/manifest/global edits, commit or push.

## Source/PDF mapping and separate text metadata issue

| Printed page(s) | PDF page | Side(s) |
| --- | ---: | --- |
| 207 | 104 | right |
| 208–209 | 105 | left / right |
| 210–211 | 106 | left / right |
| 212–213 | 107 | left / right |
| 214–215 | 108 | left / right |
| 216–217 | 109 | left / right |
| 218–219 | 110 | left / right |
| 220–221 | 111 | left / right |
| 222–223 | 112 | left / right |

The eight even-page `pdf-page` comments in `review-candidates/book/M06/text-207-223.md` are one too low: **208→105, 210→106, 212→107, 214→108, 216→109, 218→110, 220→111, 222→112**. Parent/integration worker must correct them. No text edits were made here. These are metadata errors, **not evidence of incorrectly sourced images**; all image records follow the verified source index.

## Per-image decisions

Each row covers all four edges and complete printed content. Detailed reasons and root-relative image paths are in `review-candidates/book/M06/visual-review-207-223.json`.

| ID | Printed page | Decision | Principal finding |
| --- | ---: | --- | --- |
| primjer-3-79 | 207 | PASS | Number, a–c, low notes/figures and clean source margins complete. |
| primjer-3-80 | 207 | PASS | Number, a–d, low figures and staff ends complete. |
| primjer-3-81 | 208 | PASS | All a–h, both systems, NE/DA and lowest flats complete. |
| primjer-3-82 | 208 | PASS | All a–e, NE, brackets and figures complete. |
| primjer-3-83 | 208 | RECROP_REQUIRED | Printed footer 208 shares lowest-figure band; no safe rectangle. |
| primjer-3-84 | 209 | PASS | Both variants, modulation titles and analyses complete. |
| primjer-3-85 | 209 | PASS | a–d, both systems, titles, NE/DA and low naturals complete. |
| primjer-3-86 | 210 | PASS | a–c, both systems, titles and lowest analyses complete. |
| primjer-3-87 | 210 | PASS | Title, enclosed chords and complete lower analyses retained. |
| primjer-3-88 | 211 | PASS | Title and entire stepped analysis retained. |
| primjer-3-89 | 211 | PASS | Full Beethoven attribution, two systems and terminal reduction retained. |
| primjer-3-90 | 211 | PASS | Full Schumann attribution, notation and low analysis retained. |
| primjer-3-91 | 212 | PASS | Full Beethoven attribution, bass and low analysis complete. |
| primjer-3-92 | 212 | PASS | Full Chopin attribution, lowest bass notes and analysis complete. |
| zadatak-3-212-2 | 212 | PASS | ID2, all bass/figures and final barline retained. |
| zadatak-3-212-3 | 212 | PASS | ID3, ledger-line notes and lowest stacked 2 retained. |
| zadatak-3-212-4 | 212 | RECROP_REQUIRED | Partial exercise-5 high note at bottom; source bands overlap. |
| zadatak-3-212-5 | 212 | RECROP_REQUIRED | Previous figures at top and footer 212 at bottom; source bands overlap. |
| zadatak-3-213-6 | 213 | PASS | ID6 and lowest sharp-2 intact; narrow genuine bottom gap. |
| zadatak-3-213-7 | 213 | PASS | ID7, complete melody/slurs, lowest note and barline. |
| zadatak-3-213-8 | 213 | PASS | ID8, full slur/melody and final barline. |
| zadatak-3-213-9 | 213 | PASS | ID9, full slur/melody and final barline. |
| zadatak-3-213-10 | 213 | PASS | ID10, full slur/tie/melody and final barline. |
| zadatak-3-213-11 | 213 | PASS | ID11, dotted/flagged notes, slur and final barline. |
| zadatak-3-213-12 | 213 | PASS | ID12, all slurs/ties, low notes and final barline. |
| zadatak-3-213-13 | 213 | PASS | ID13, all slurs/ties, final dotted note and barline. |
| realizacija-3-213-zadatak-7 | 213 | PASS | Complete realization title, both systems and lowest stems. |
| primjer-3-93 | 214 | RECROP_REQUIRED | Pencil analysis embedded beside variant a. |
| primjer-3-94 | 214 | PASS | a–c, equality signs, accidentals and lowest 3 complete. |
| primjer-3-95 | 215 | RECROP_REQUIRED | Faint internal bass pencil arc and tiny foreign bottom-edge tip. |
| primjer-3-96 | 215 | RECROP_REQUIRED | Handwriting inside bass and adjacent to printed figures. |
| primjer-3-97 | 215 | PASS | a–d, DA/NE and all low notes/motion lines complete. |
| primjer-3-98 | 216 | RECROP_REQUIRED | Pencil circles around required a/c variant labels. |
| primjer-3-99 | 216 | RECROP_REQUIRED | Pencil words/circles/strokes embedded in notation and figures. |
| primjer-3-100 | 216 | RECROP_REQUIRED | Both a–f systems complete, but embedded pencil analysis remains. |
| primjer-3-101-a-c | 216 | RECROP_REQUIRED | Printed number and a–c complete; handwriting inside c. |
| primjer-3-101-d-f | 217 | RECROP_REQUIRED | d–f complete; handwriting inside d. Source has no repeated number. |
| primjer-3-102 | 217 | RECROP_REQUIRED | Embedded pencil analysis and partial exterior pencil marks. |
| primjer-3-103 | 217 | RECROP_REQUIRED | Pencil words/circles intersect notation/figures and boundaries. |
| primjer-3-104 | 218 | RECROP_REQUIRED | Pencil circle surrounds required first figured bass. |
| primjer-3-105 | 218 | PASS | All a–h, both systems, terminal itd. and low figures retained. |
| primjer-3-106 | 219 | RECROP_REQUIRED | Extensive pencil analysis interleaved with both systems. |
| primjer-3-107 | 220 | RECROP_REQUIRED | All a–i/three systems retained; embedded handwriting/top foreign strokes. |
| primjer-3-108 | 220 | RECROP_REQUIRED | Full Chopin attribution retained, but prior pencil analysis shares its band. |
| primjer-3-109 | 221 | RECROP_REQUIRED | Pencil names/arrows inside required label/staff/figure rectangle. |
| primjer-3-110 | 221 | RECROP_REQUIRED | Pencil circles and Roman numerals interleaved with print. |
| primjer-3-111 | 221 | RECROP_REQUIRED | Pencil analysis inside staves and at upper/lower boundaries. |
| primjer-3-112 | 222 | RECROP_REQUIRED | Pencil analysis/circle within and below grand staff. |
| primjer-3-113 | 222 | RECROP_REQUIRED | Embedded pencil figures plus following title fragment at bottom. |
| primjer-3-114 | 222 | PASS | Full C(c)–G(g) title, low stems and analyses; no preceding figures. |
| primjer-3-115 | 223 | PASS | Both a–e systems, titles and lowest analyses complete. |
| primjer-3-116 | 223 | PASS | Both variants/titles, low stems and full stacked analyses complete. |

## Recrop feasibility and temporary testing

All **22 failures are source-limited under the required single, unretouched rectangular-crop rule**. `RECROP_REQUIRED` means the current image does not pass; it does not imply that an ordinary recrop is possible. No `proposed_rect` is published because none was independently demonstrated to remove all foreign content while retaining all required notation and genuine feasible whitespace.

- **3.83:** bottom-left footer shares the vertical band of the lowest right-hand figure and the horizontal band of the required left-hand example number. Cutting the bottom or shifting a side cannot solve both constraints.
- **Page 212, exercises 4/5:** enlarged native source region confirms exercise 4's lowest figure extends through source y2223 and exercise 5's high note begins at y2220. Exercise 4 necessarily includes a piece of that note if kept whole; exercise 5 necessarily includes pieces of prior figures if kept whole. Its footer also overlaps its bottom-figure band. These are real spatial overlaps, not a reason to clip notation.
- **3.95:** independently tested temporary source rectangles `[388,715,919,1025]` and `[388,715,919,1030]`. The former clips bass-stem ends. The latter removes the tiny lower foreign stroke and retains stems, but the faint handwritten arc remains inside the bass staff. Both are rejected; neither is a safe proposal. The internal arc is distinct from the source's printed notes and from ordinary isolated scan speckles.
- **Page 220 / 3.108:** do not remove the upper contamination by clipping the Chopin attribution. Pencil analysis from 3.107 occupies the same vertical band as the required title. Footnote asterisks are retained in the score; explanatory prose footnotes properly remain outside the score crop.
- **Page 222 / 3.113:** the final printed figure of variant c shares a vertical band with the next title at another x-position. Also contains embedded handwritten figures. Do not cut the low figure just to conceal the title fragment.
- **Page 222 / 3.114:** independently passes: full title is present and the narrower right edge safely excludes preceding c's figures without losing any of 3.114.
- Other failures contain handwriting enclosed by required labels, notes, staves or figures. Cosmetic edge trimming cannot make them pass. A different clean source or a separately authorized extraction strategy is needed; no retouching or alternative strategy was performed or approved here.

Temporary renders, enlarged source inspection and rejected trials were confined to `/tmp/opencode/m06-review/`. They are review aids, not replacement score assets.

## Handoff

1. **Assigned pages:** printed 207–223 / PDF104–112; all 52 records covered.
2. **Files created:** only `review-candidates/book/M06/visual-review-207-223.json` and `review-candidates/book/M06/visual-review-207-223.md` in the repository.
3. **Examples reviewed:** 3.79–3.116 (3.101 split a–c/d–f), exercises 2–13 and realization of exercise 7, with individual source pages above. No new examples extracted by this worker.
4. **Results:** 30 PASS, 22 RECROP_REQUIRED; zero unreviewed; zero safe proposed rectangles; 22 source-limited records. Every record is an exact source-pixel match.
5. **Source limitations:** footer/layout collisions and original pencil additions as detailed above. No wholly unreadable printed musical example was found; pencil overprinting makes affected notation unsuitable for a clean-score claim. No missing printed continuation number was invented.
6. **Integration readiness:** **NO** for the whole assignment. Passing images may be handed off individually; failed images must not be marked approved. Parent must also fix the eight text PDF comments and verify final image/alt/caption blocks. No human approval was requested or presumed.
