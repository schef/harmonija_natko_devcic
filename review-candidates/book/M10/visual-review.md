# M10 independent visual review

## Outcome

- **86/86 records reviewed; 0 unreviewed.**
- **81 PASS; 5 RECROP_REQUIRED.** PASS assesses the crop, not permission to publish damaged notation.
- **3 source-limited records:** 4.173 (crop PASS, source-damage hold) and both 4.178 parts (RECROP_REQUIRED, handwriting over notation).
- **Not ready for complete integration/approval.** Five failed crops and the 4.173 notation-certification hold remain unresolved.

Assigned scope: printed pages **349–378**, **1-based PDF pages 175–190**, all records in `review-candidates/book/M10/images-complete.json`. The JSON report provides a decision and reason for every record in manifest order, including the four current `coverage-recrop` candidates. No original candidate was substituted for a current recrop.

## Verification and method

Each source page and each individual candidate was opened for visual comparison. Number/exercise identity, actual variants, composer/work attribution or realization title, complete systems, staff ends, accidentals, figures, outer slurs/ties, lowest stems and four outer edges were inspected at native resolution. Disputed touching-height neighbourhoods and handwriting were additionally rendered to enlarged temporary views under `/tmp/opencode`. Genuine scan whitespace was distinguished from artificial borders; isolated source specks were not treated as letters or notation. No border, retouch or replacement image was produced.

Decoded RGB pixel comparisons: **86/86 images equal their declared source-image rectangles exactly**. Independently rendered PDF pages175–190 at300dpi with `pdftoppm`; split each spread at its midpoint. **30/30 authoritative `sources/pages/page-349.png` through `page-378.png` equal those rendered halves pixel-for-pixel.** Thus source mapping is independently checked, not inferred only from manifest arithmetic. Printed page n maps to 1-based PDF page floor(n/2)+1. Raw embedded-image extraction differs from rendered PNGs because PDF overlays/rendering are present; the authoritative check used complete PDF rendering.

Multipart identities were checked in paired context. Printed numbers and titles need not repeat in continuation images where absent in the source. Actual a–c/d–g labels of4.152 are preserved. Exercise8(356/357), exercise11(357/358), exercise2(364/365), 4.178(366/367), 4.182(368/369), exercise2(371/372), exercise5(373/374), and realization1(374/375) were assessed with their opening/continuation partners. Filename suffixes a/b are image-part identifiers, not claims that the print has those variant letters.

Manifest image paths, printed-page references, slot identities and candidate captions agree on identity/page. Text shards currently expose visual-slot comments rather than final embedded image/alt/caption blocks; final assembled Markdown link/alt/caption verification remains an integration task. No assertion is made that those not-yet-assembled blocks already pass.

## Failures and holds

| Record | Printed / PDF | Decision | Finding |
| --- | --- | --- | --- |
| 4.169 | 362 /182 | RECROP_REQUIRED | Partial explanatory-footnote letters on bottom edge. Lowest bass beams overlap their vertical band; no tested safe single rectangle can retain all score content and exclude prose. |
| 4.178 opening | 366 /184 | RECROP_REQUIRED; source-limited | Handwritten circles surround bass notes within the score. Full title and opening number are present, and outer edges are clean, but internal handwriting violates the checklist. |
| 4.178 continuation | 367 /184 | RECROP_REQUIRED; source-limited | Handwritten circles occur in both continuation systems. Cropping cannot remove them without removing notation. Number/title legitimately occur only in opening part. |
| 4.192 current recrop | 378 /190 | RECROP_REQUIRED | Beethoven attribution restored, but partial preceding prose remains at top; lowest bass slur reaches the lower crop boundary adjacent to Ravel attribution. |
| 4.193 | 378 /190 | RECROP_REQUIRED | Previous example's bass slurs remain at top and touch the attribution-height band. Preserve full Ravel attribution; do not clip title to hide foreign slurs. |
| 4.173 | 363 /182 | PASS crop; source-limited | Source abrasion interrupts right final barline. Source notation, including damaged/faint material, is **uncertified**; no restoration or inferred notes approved. Parent must retain `source_damage` hold. |

No `proposed_rect` is supplied: no safe full-content replacement was verified for a failed record. An omitted proposal must not be interpreted as approval of retouching or clipping. These layout/handwriting conflicts require an integration decision outside this review's write scope; merely moving an edge to make foreign ink less visible is not acceptable.

4.193 has printed open right staff endpoints on378. Those endpoints are not a missing final barline. This review does not require a continuation on379 and does not authorize inventing a barline. Parent-supplied379 context says the next page begins Chapter5 with exercises1/2;379 was not modified or included among the30 reviewed source pages.

## Current extractor recrops

- `images/04-neakordicki-c/zadatak-4-359-9-realizacija-coverage-recrop.png`: **PASS**, complete title, all three systems and lowest figures.
- `images/04-neakordicki-c/zadatak-4-360-12-realizacija-coverage-recrop.png`: **PASS**, complete title, all four systems and lowest final stem.
- `images/04-neakordicki-c/zadatak-4-374-1-realizacija-a-coverage-recrop.png`: **PASS**, complete title and opening realization system, paired with375.
- `images/04-neakordicki-c/primjer-4-192-coverage-recrop.png`: **RECROP_REQUIRED**, restored title does not resolve top foreign prose and bottom touching-height conflict.

## Hand-off

Only `review-candidates/book/M10/visual-review.json` and `review-candidates/book/M10/visual-review.md` were created by this review. No image, manifest, chapter, tracker or source was edited; no commit/push, delegation, model/API call, GUI action or human approval occurred. Temporary PDF renders, decoded extractions and enlarged inspection views were confined to `/tmp/opencode`.

The full per-example/exercise source-page and review-result inventory is `visual-review.json` alongside this report. Existing examples were reviewed, not extracted anew. All86 received a decision;81 crop passes may be carried forward subject to the explicit4.173 source-damage hold and final assembled Markdown checks. The milestone as a whole remains **blocked**, not approved.
