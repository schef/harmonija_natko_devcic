# M03 extraction hand-off: printed 64–81 / PDF 33–41

- Extraction only; all 18 source PNGs visually inspected. No chapter text or global manifests changed.
- Extractor inspected native-resolution strips of all four edges of all 68 output crops, in addition to the source-page inspection. This is extraction QA only, not the mandatory independent review.
- 68 source-only crops match the 68 visual slots in `review-candidates/book/M03/text-064-081.md`, in source order. No count discrepancy.
- The old 62 definitions become 68: split the combined page-68 progression into two (+1), and add example 2.167 plus four page-81 exercises (+5).
- Retained identifying titles in the realizations on pages 74 and 75. Cross-page examples remain separate page-specific parts; exercises 13 (p.73), 2 and 4 (p.81), and realization 13 retain both systems in one crop.
- `rect` is `[left, top, right, bottom]` in the original source PNG pixels, with right/bottom exclusive. No resizing, painting, generated borders, or other retouching was applied to output crops.
- Prior `extract.py` and any prior manifests are unchanged. Identical existing pixels are reused; differing prior images are snapshotted inside `images/02-dijatonika-b/snapshots-064-081/` before replacement.
- Every crop is **pending_independent_review**; this extractor has not approved any image. Parent must inspect all four edges against the source and give pass/recrop decisions.
- Source handwriting frequently overlaps labels, notes, and analysis, or obstructs clean whitespace. `cleanup_required` notes identify these original-pixel limitations; they are not passes. No printed music was deliberately omitted to hide handwriting.
- Continuation crops 2.140.c, 2.143.c, 2.151.e–g, and 2.154.f–g have their example number only on the preceding source page; no number has been synthesized.
- No unreadable printed example was omitted. Handwritten additions are not authoritative notation; independent review may require a cleaner source for affected images.
- Ready for independent image review, **not ready for final integration approval**.

## Files

- `review-candidates/book/M03/images-064-081.json`
- `review-candidates/book/M03/extraction-064-081.md`
- `review-candidates/book/M03/extract-064-081.py`
- The 68 PNG paths listed below in `images/02-dijatonika-b/`.

## Per-image hand-off

| Source identity | Printed / PDF page | Image | Review / limitation |
| --- | --- | --- | --- |
| 2.134 | 64 / 33 | `images/02-dijatonika-b/primjer-2-134.png` | pending_independent_review — Source-only crop; independent visual review required. |
| 2.135 | 65 / 33 | `images/02-dijatonika-b/primjer-2-135.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwriting above/among variants a–d; retained original pixels. |
| 2.136 | 65 / 33 | `images/02-dijatonika-b/primjer-2-136.png` | pending_independent_review — Source-only crop; independent visual review required. |
| 2.137 | 65 / 33 | `images/02-dijatonika-b/primjer-2-137.png` | pending_independent_review — Source-only crop; independent visual review required. |
| 2.138 | 66 / 34 | `images/02-dijatonika-b/primjer-2-138.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil marks among lower figures. |
| 2.139 | 66 / 34 | `images/02-dijatonika-b/primjer-2-139.png` | pending_independent_review — Source-only crop; independent visual review required. |
| 2.140.a–b | 66 / 34 | `images/02-dijatonika-b/primjer-2-140-p66.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page example, variants a–b. Cleanup required: pencil marks among lower figures. |
| 2.140.c | 67 / 34 | `images/02-dijatonika-b/primjer-2-140-p67.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page continuation c; number printed on preceding page. Pencil analysis below bass overlaps crop. |
| 2.141 | 67 / 34 | `images/02-dijatonika-b/primjer-2-141.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil circle around NE and analysis among lower figures. |
| 2.142 | 67 / 34 | `images/02-dijatonika-b/primjer-2-142.png` | pending_independent_review — cleanup_required: faint source handwriting above the staff; no pixel alteration. |
| 2.143.a–b | 67 / 34 | `images/02-dijatonika-b/primjer-2-143-p67.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page example a–b; pencil annotations overlap original example. |
| 2.143.c | 68 / 35 | `images/02-dijatonika-b/primjer-2-143-p68.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page continuation c; number printed on preceding page. Pencil marks below staff. |
| 2.144 | 68 / 35 | `images/02-dijatonika-b/primjer-2-144.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil harmonic annotations among figures. |
| ZADACI: progresija I—II₆—V—I s kadencirajućim kvartsekstakordom | 68 / 35 | `images/02-dijatonika-b/zadatak-2-68-progresija-1.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI: progresija I—II₆—V—VI—II₆—V—I s kadencirajućim kvartsekstakordom | 68 / 35 | `images/02-dijatonika-b/zadatak-2-68-progresija-2.png` | pending_independent_review — Source-only crop; independent visual review required. |
| 2.145 | 69 / 35 | `images/02-dijatonika-b/primjer-2-145.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten analysis between labels/staves. |
| 2.146 | 69 / 35 | `images/02-dijatonika-b/primjer-2-146.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil wavy line beside printed NE. |
| 2.147 | 69 / 35 | `images/02-dijatonika-b/primjer-2-147.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil analysis under figures. |
| 2.148 | 70 / 36 | `images/02-dijatonika-b/primjer-2-148.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: faint pencil annotations among figured bass. |
| 2.149 | 71 / 36 | `images/02-dijatonika-b/primjer-2-149.png` | pending_independent_review — cleanup_required: original faint handwritten analysis near the lower edge; printed notation intact. |
| 2.150 | 71 / 36 | `images/02-dijatonika-b/primjer-2-150.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil check mark beside b and marks among notes. |
| 2.151.a–d | 71 / 36 | `images/02-dijatonika-b/primjer-2-151-p71.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page a–d. Pencil analysis below figures. |
| 2.151.e–g | 72 / 37 | `images/02-dijatonika-b/primjer-2-151-p72.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page e–g; number on preceding page. Pencil analysis below figures. |
| 2.152 | 72 / 37 | `images/02-dijatonika-b/primjer-2-152.png` | pending_independent_review — cleanup_required: original faint handwritten analysis near the lower edge; printed notation intact. |
| ZADACI 1 | 72 / 37 | `images/02-dijatonika-b/zadatak-2-72-1.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 2 | 72 / 37 | `images/02-dijatonika-b/zadatak-2-72-2.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 3 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-3.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 4 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-4.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 5 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-5.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 6 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-6.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 7 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-7.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 8 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-8.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 9 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-9.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 10 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-10.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 11 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-11.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 12 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-12.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 13 | 73 / 37 | `images/02-dijatonika-b/zadatak-2-73-13.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 14 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-14.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 15 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-15.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 16 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-16.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 17 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-17.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 18 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-18.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 19 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-19.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 20 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-20.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 21 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-21.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 22 | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-22.png` | pending_independent_review — Source-only crop; independent visual review required. |
| Realizacija zadatka 8. | 74 / 38 | `images/02-dijatonika-b/zadatak-2-74-8-realizacija.png` | pending_independent_review — Identifying title retained above the complete realization. |
| Realizacija zadatka 13. | 75 / 38 | `images/02-dijatonika-b/zadatak-2-75-13-realizacija.png` | pending_independent_review — Identifying title and both systems retained. |
| 2.153 | 76 / 39 | `images/02-dijatonika-b/primjer-2-153.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten chord names above notes and analysis below. |
| 2.154.a–e | 76 / 39 | `images/02-dijatonika-b/primjer-2-154-p76.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page a–e. Cleanup required: handwriting around labels and circled analysis. |
| 2.154.f–g | 77 / 39 | `images/02-dijatonika-b/primjer-2-154-p77.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cross-page f–g, number on preceding page. Handwriting near labels. |
| 2.155 | 77 / 39 | `images/02-dijatonika-b/primjer-2-155.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten chord labels above printed variants. |
| 2.156 | 77 / 39 | `images/02-dijatonika-b/primjer-2-156.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwriting beside labels. |
| 2.157 | 78 / 40 | `images/02-dijatonika-b/primjer-2-157.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwriting intersects notes and bass, not removable by rectangle. |
| 2.158 | 78 / 40 | `images/02-dijatonika-b/primjer-2-158.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil harmonic annotations around notation. |
| 2.159 | 78 / 40 | `images/02-dijatonika-b/primjer-2-159.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil arrow near b. |
| 2.160 | 78 / 40 | `images/02-dijatonika-b/primjer-2-160.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil writing above soprano. |
| 2.161 | 79 / 40 | `images/02-dijatonika-b/primjer-2-161.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten analysis between staves. |
| 2.162 | 79 / 40 | `images/02-dijatonika-b/primjer-2-162.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten chord names near variants. |
| 2.163 | 80 / 41 | `images/02-dijatonika-b/primjer-2-163.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwriting near labels and harmonic analysis. |
| 2.164 | 80 / 41 | `images/02-dijatonika-b/primjer-2-164.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwritten chord names over bracket and analysis below. |
| 2.165 | 80 / 41 | `images/02-dijatonika-b/primjer-2-165.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: pencil circles on bass notes. |
| 2.166 | 80 / 41 | `images/02-dijatonika-b/primjer-2-166.png` | pending_independent_review — cleanup_required: original source handwriting/layout retained without retouching. Cleanup required: handwriting between attribution and staff. |
| 2.167 | 81 / 41 | `images/02-dijatonika-b/primjer-2-167.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 1 | 81 / 41 | `images/02-dijatonika-b/zadatak-2-81-1.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 2 | 81 / 41 | `images/02-dijatonika-b/zadatak-2-81-2.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 3 | 81 / 41 | `images/02-dijatonika-b/zadatak-2-81-3.png` | pending_independent_review — Source-only crop; independent visual review required. |
| ZADACI 4 | 81 / 41 | `images/02-dijatonika-b/zadatak-2-81-4.png` | pending_independent_review — Source-only crop; independent visual review required. |
