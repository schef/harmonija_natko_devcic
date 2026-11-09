# Extraction hand-off: printed pages 137–155

- Assignment: 19 printed pages, 137–155; PDF pages 69–78, read from `sources/index.json`.
- All 19 original source PNGs were opened visually. Individual four-edge bounds were checked with native-resolution edge strips; this is extractor quality control, not independent approval.
- Exactly 72 verified text slots map to 73 source-only PNG rectangles, covering examples 2.302–2.372 (71 distinct numbers). Example 2.305 occupies two cross-page slots (a–b on 139, c on 140), without stitching. Example 2.325 occupies one slot with two separate parts to exclude the running footer and retain its complete lowest stem.
- Every crop remains `pending_independent_review`; no pass/self-approval is asserted.
- Source pixels only: no retouching, border generation, padding, deskewing, stitching, or resampling of outputs. Rectangles are source-local `[left, top, right, bottom)` pixels.
- Created: `review-candidates/book/M04/extract-137-155.py`, `review-candidates/book/M04/images-137-155.json`, this report, and the 73 images listed below in `images/02-dijatonika-c/`.
- Preserved untouched: existing `crop-plan.json`, `crop.py`, verified text, chapter files, shared manifests, milestone tracker, and all other assigned ranges.
- Readiness: ready for independent visual review; NOT ready for final integration. Flagged layout/handwriting cases require reviewer disposition. No unreadable example was omitted. Continuation 2.305 c and the second part of 2.325 have no repeated source number; none was fabricated.

## Flagged source-layout / handwriting cases

- **primjer-2-317**, printed 144: cleanup_required: source layout interleaves next example C–E title with this example's lower analysis. Candidate retains complete 2.317 but includes adjacent title; no retouch.
- **primjer-2-318**, printed 144: cleanup_required: previous example 2.317 lower analysis overlaps vertical span of this example's title/clef. Candidate retains complete 2.318; adjacent analysis remains, no retouch.
- **primjer-2-321**, printed 145: cleanup_required: faint handwritten marks alongside the lower analysis cannot be excluded by a rectangular crop while retaining the complete example; source pixels preserved.
- **primjer-2-323**, printed 145: cleanup_required: analysis of 2.323 vertically interleaves title/clef of following example 2.324. No retouch.
- **primjer-2-324**, printed 145: cleanup_required: preceding 2.323 analysis and following 2.325 title interleave this crop's vertical span. No retouch.
- **primjer-2-325-score**, printed 145: cleanup_required: preceding 2.324 lower analysis interleaves this score's title. Lower analysis of 2.325 is separately cropped to avoid printed footer; no stitching/retouch. First analysis line retained with score so lowest bass stem is complete.
- **primjer-2-347**, printed 151: cleanup_required: lower analysis interleaves following example 2.348 title; source pixels preserved.
- **primjer-2-348**, printed 151: cleanup_required: preceding example 2.347 lower analysis interleaves title; source pixels preserved.

## Slot-by-slot mapping and pending review

All paths below are repository-root-relative, matching the JSON manifest. Each image group belongs to one original verified-text slot.

### Slot 01: primjer 2.302, tiskana str. 137

![Primjer 2.302 — tiskana str. 137.](images/02-dijatonika-c/primjer-2-302.png)

Primjer 2.302 — tiskana str. 137.

- Source: `sources/pages/page-137.png`, PDF page 69, local rectangle `[201, 1372, 1735, 1904]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 02: primjer 2.303, tiskana str. 137

![Primjer 2.303 — tiskana str. 137.](images/02-dijatonika-c/primjer-2-303.png)

Primjer 2.303 — tiskana str. 137.

- Source: `sources/pages/page-137.png`, PDF page 69, local rectangle `[201, 1906, 1734, 2411]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 03: primjer 2.304, tiskana str. 138

![Primjer 2.304 — tiskana str. 138.](images/02-dijatonika-c/primjer-2-304.png)

Primjer 2.304 — tiskana str. 138.

- Source: `sources/pages/page-138.png`, PDF page 70, local rectangle `[144, 1742, 1675, 2043]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 04: primjer 2.305, tiskana str. 139

![Primjer 2.305 — tiskana str. 139 (p139).](images/02-dijatonika-c/primjer-2-305-p139.png)

Primjer 2.305 — tiskana str. 139 (p139).

- Source: `sources/pages/page-139.png`, PDF page 70, local rectangle `[201, 1858, 1738, 2307]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 05: primjer 2.305, tiskana str. 140

![Primjer 2.305 — tiskana str. 140 (p140).](images/02-dijatonika-c/primjer-2-305-p140.png)

Primjer 2.305 — tiskana str. 140 (p140).

- Source: `sources/pages/page-140.png`, PDF page 71, local rectangle `[486, 112, 1374, 542]`.
- Image review: **pending_independent_review**. Continuation variant c); source does not repeat example number, retained without fabrication.

<!-- MuseScore: pending -->

### Slot 06: primjer 2.306, tiskana str. 140

![Primjer 2.306 — tiskana str. 140.](images/02-dijatonika-c/primjer-2-306.png)

Primjer 2.306 — tiskana str. 140.

- Source: `sources/pages/page-140.png`, PDF page 71, local rectangle `[426, 1343, 1417, 1795]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 07: primjer 2.307, tiskana str. 140

![Primjer 2.307 — tiskana str. 140.](images/02-dijatonika-c/primjer-2-307.png)

Primjer 2.307 — tiskana str. 140.

- Source: `sources/pages/page-140.png`, PDF page 71, local rectangle `[140, 1874, 1676, 2325]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 08: primjer 2.308, tiskana str. 141

![Primjer 2.308 — tiskana str. 141.](images/02-dijatonika-c/primjer-2-308.png)

Primjer 2.308 — tiskana str. 141.

- Source: `sources/pages/page-141.png`, PDF page 71, local rectangle `[487, 477, 1472, 905]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 09: primjer 2.309, tiskana str. 141

![Primjer 2.309 — tiskana str. 141.](images/02-dijatonika-c/primjer-2-309.png)

Primjer 2.309 — tiskana str. 141.

- Source: `sources/pages/page-141.png`, PDF page 71, local rectangle `[460, 1555, 1452, 1989]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 10: primjer 2.310, tiskana str. 141

![Primjer 2.310 — tiskana str. 141.](images/02-dijatonika-c/primjer-2-310.png)

Primjer 2.310 — tiskana str. 141.

- Source: `sources/pages/page-141.png`, PDF page 71, local rectangle `[356, 1998, 1582, 2417]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 11: primjer 2.311, tiskana str. 142

![Primjer 2.311 — tiskana str. 142.](images/02-dijatonika-c/primjer-2-311.png)

Primjer 2.311 — tiskana str. 142.

- Source: `sources/pages/page-142.png`, PDF page 72, local rectangle `[421, 115, 1405, 528]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 12: primjer 2.312, tiskana str. 142

![Primjer 2.312 — tiskana str. 142.](images/02-dijatonika-c/primjer-2-312.png)

Primjer 2.312 — tiskana str. 142.

- Source: `sources/pages/page-142.png`, PDF page 72, local rectangle `[420, 529, 1406, 949]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 13: primjer 2.313, tiskana str. 142

![Primjer 2.313 — tiskana str. 142.](images/02-dijatonika-c/primjer-2-313.png)

Primjer 2.313 — tiskana str. 142.

- Source: `sources/pages/page-142.png`, PDF page 72, local rectangle `[417, 1974, 1405, 2408]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 14: primjer 2.314, tiskana str. 143

![Primjer 2.314 — tiskana str. 143.](images/02-dijatonika-c/primjer-2-314.png)

Primjer 2.314 — tiskana str. 143.

- Source: `sources/pages/page-143.png`, PDF page 72, local rectangle `[438, 112, 1506, 525]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 15: primjer 2.315, tiskana str. 143

![Primjer 2.315 — tiskana str. 143.](images/02-dijatonika-c/primjer-2-315.png)

Primjer 2.315 — tiskana str. 143.

- Source: `sources/pages/page-143.png`, PDF page 72, local rectangle `[458, 1465, 1442, 1916]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 16: primjer 2.316, tiskana str. 143

![Primjer 2.316 — tiskana str. 143.](images/02-dijatonika-c/primjer-2-316.png)

Primjer 2.316 — tiskana str. 143.

- Source: `sources/pages/page-143.png`, PDF page 72, local rectangle `[318, 1917, 1551, 2402]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 17: primjer 2.317, tiskana str. 144

![Primjer 2.317 — tiskana str. 144.](images/02-dijatonika-c/primjer-2-317.png)

Primjer 2.317 — tiskana str. 144.

- Source: `sources/pages/page-144.png`, PDF page 73, local rectangle `[426, 856, 1417, 1280]`.
- Image review: **pending_independent_review**. cleanup_required: source layout interleaves next example C–E title with this example's lower analysis. Candidate retains complete 2.317 but includes adjacent title; no retouch.

<!-- MuseScore: pending -->

### Slot 18: primjer 2.318, tiskana str. 144

![Primjer 2.318 — tiskana str. 144.](images/02-dijatonika-c/primjer-2-318.png)

Primjer 2.318 — tiskana str. 144.

- Source: `sources/pages/page-144.png`, PDF page 73, local rectangle `[425, 1239, 1415, 1637]`.
- Image review: **pending_independent_review**. cleanup_required: previous example 2.317 lower analysis overlaps vertical span of this example's title/clef. Candidate retains complete 2.318; adjacent analysis remains, no retouch.

<!-- MuseScore: pending -->

### Slot 19: primjer 2.319, tiskana str. 144

![Primjer 2.319 — tiskana str. 144.](images/02-dijatonika-c/primjer-2-319.png)

Primjer 2.319 — tiskana str. 144.

- Source: `sources/pages/page-144.png`, PDF page 73, local rectangle `[423, 1638, 1415, 2046]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 20: primjer 2.320, tiskana str. 144

![Primjer 2.320 — tiskana str. 144.](images/02-dijatonika-c/primjer-2-320.png)

Primjer 2.320 — tiskana str. 144.

- Source: `sources/pages/page-144.png`, PDF page 73, local rectangle `[417, 2047, 1412, 2463]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 21: primjer 2.321, tiskana str. 145

![Primjer 2.321 — tiskana str. 145.](images/02-dijatonika-c/primjer-2-321.png)

Primjer 2.321 — tiskana str. 145.

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[507, 103, 1495, 512]`.
- Image review: **pending_independent_review**. cleanup_required: faint handwritten marks alongside the lower analysis cannot be excluded by a rectangular crop while retaining the complete example; source pixels preserved.

<!-- MuseScore: pending -->

### Slot 22: primjer 2.322, tiskana str. 145

![Primjer 2.322 — tiskana str. 145.](images/02-dijatonika-c/primjer-2-322.png)

Primjer 2.322 — tiskana str. 145.

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[503, 513, 1490, 929]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 23: primjer 2.323, tiskana str. 145

![Primjer 2.323 — tiskana str. 145.](images/02-dijatonika-c/primjer-2-323.png)

Primjer 2.323 — tiskana str. 145.

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[455, 1237, 1503, 1668]`.
- Image review: **pending_independent_review**. cleanup_required: analysis of 2.323 vertically interleaves title/clef of following example 2.324. No retouch.

<!-- MuseScore: pending -->

### Slot 24: primjer 2.324, tiskana str. 145

![Primjer 2.324 — tiskana str. 145.](images/02-dijatonika-c/primjer-2-324.png)

Primjer 2.324 — tiskana str. 145.

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[403, 1622, 1568, 2047]`.
- Image review: **pending_independent_review**. cleanup_required: preceding 2.323 analysis and following 2.325 title interleave this crop's vertical span. No retouch.

<!-- MuseScore: pending -->

### Slot 25: primjer 2.325, tiskana str. 145

![Primjer 2.325 — tiskana str. 145 (score).](images/02-dijatonika-c/primjer-2-325-score.png)

Primjer 2.325 — tiskana str. 145 (score).

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[460, 1991, 1503, 2395]`.
- Image review: **pending_independent_review**. cleanup_required: preceding 2.324 lower analysis interleaves this score's title. Lower analysis of 2.325 is separately cropped to avoid printed footer; no stitching/retouch. First analysis line retained with score so lowest bass stem is complete.

![Primjer 2.325 — tiskana str. 145 (analysis).](images/02-dijatonika-c/primjer-2-325-analysis.png)

Primjer 2.325 — tiskana str. 145 (analysis).

- Source: `sources/pages/page-145.png`, PDF page 73, local rectangle `[792, 2395, 1087, 2491]`.
- Image review: **pending_independent_review**. Remaining lower analysis; first analysis line is in -score. No repeated number in this source part; pair with -score. Separate rectangle excludes running footer.

<!-- MuseScore: pending -->

### Slot 26: primjer 2.326, tiskana str. 146

![Primjer 2.326 — tiskana str. 146.](images/02-dijatonika-c/primjer-2-326.png)

Primjer 2.326 — tiskana str. 146.

- Source: `sources/pages/page-146.png`, PDF page 74, local rectangle `[392, 104, 1443, 588]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 27: primjer 2.327, tiskana str. 146

![Primjer 2.327 — tiskana str. 146.](images/02-dijatonika-c/primjer-2-327.png)

Primjer 2.327 — tiskana str. 146.

- Source: `sources/pages/page-146.png`, PDF page 74, local rectangle `[281, 891, 1552, 1294]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 28: primjer 2.328, tiskana str. 146

![Primjer 2.328 — tiskana str. 146.](images/02-dijatonika-c/primjer-2-328.png)

Primjer 2.328 — tiskana str. 146.

- Source: `sources/pages/page-146.png`, PDF page 74, local rectangle `[275, 1324, 1590, 2164]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 29: primjer 2.329, tiskana str. 147

![Primjer 2.329 — tiskana str. 147.](images/02-dijatonika-c/primjer-2-329.png)

Primjer 2.329 — tiskana str. 147.

- Source: `sources/pages/page-147.png`, PDF page 74, local rectangle `[213, 973, 1743, 1429]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 30: primjer 2.330, tiskana str. 147

![Primjer 2.330 — tiskana str. 147.](images/02-dijatonika-c/primjer-2-330.png)

Primjer 2.330 — tiskana str. 147.

- Source: `sources/pages/page-147.png`, PDF page 74, local rectangle `[213, 1984, 913, 2398]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 31: primjer 2.331, tiskana str. 147

![Primjer 2.331 — tiskana str. 147.](images/02-dijatonika-c/primjer-2-331.png)

Primjer 2.331 — tiskana str. 147.

- Source: `sources/pages/page-147.png`, PDF page 74, local rectangle `[940, 1985, 1746, 2397]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 32: primjer 2.332, tiskana str. 148

![Primjer 2.332 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-332.png)

Primjer 2.332 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[174, 257, 926, 647]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 33: primjer 2.333, tiskana str. 148

![Primjer 2.333 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-333.png)

Primjer 2.333 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[953, 259, 1707, 648]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 34: primjer 2.334, tiskana str. 148

![Primjer 2.334 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-334.png)

Primjer 2.334 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[390, 651, 1493, 1046]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 35: primjer 2.335, tiskana str. 148

![Primjer 2.335 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-335.png)

Primjer 2.335 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[168, 1048, 927, 1442]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 36: primjer 2.336, tiskana str. 148

![Primjer 2.336 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-336.png)

Primjer 2.336 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[944, 1048, 1700, 1460]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 37: primjer 2.337, tiskana str. 148

![Primjer 2.337 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-337.png)

Primjer 2.337 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[303, 1495, 1530, 1903]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 38: primjer 2.338, tiskana str. 148

![Primjer 2.338 — tiskana str. 148.](images/02-dijatonika-c/primjer-2-338.png)

Primjer 2.338 — tiskana str. 148.

- Source: `sources/pages/page-148.png`, PDF page 75, local rectangle `[365, 1973, 1476, 2384]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 39: primjer 2.339, tiskana str. 149

![Primjer 2.339 — tiskana str. 149.](images/02-dijatonika-c/primjer-2-339.png)

Primjer 2.339 — tiskana str. 149.

- Source: `sources/pages/page-149.png`, PDF page 75, local rectangle `[468, 475, 1515, 926]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 40: primjer 2.340, tiskana str. 149

![Primjer 2.340 — tiskana str. 149.](images/02-dijatonika-c/primjer-2-340.png)

Primjer 2.340 — tiskana str. 149.

- Source: `sources/pages/page-149.png`, PDF page 75, local rectangle `[377, 994, 1599, 1439]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 41: primjer 2.341, tiskana str. 149

![Primjer 2.341 — tiskana str. 149.](images/02-dijatonika-c/primjer-2-341.png)

Primjer 2.341 — tiskana str. 149.

- Source: `sources/pages/page-149.png`, PDF page 75, local rectangle `[409, 1923, 1519, 2362]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 42: primjer 2.342, tiskana str. 150

![Primjer 2.342 — tiskana str. 150.](images/02-dijatonika-c/primjer-2-342.png)

Primjer 2.342 — tiskana str. 150.

- Source: `sources/pages/page-150.png`, PDF page 76, local rectangle `[393, 152, 1502, 613]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 43: primjer 2.343, tiskana str. 150

![Primjer 2.343 — tiskana str. 150.](images/02-dijatonika-c/primjer-2-343.png)

Primjer 2.343 — tiskana str. 150.

- Source: `sources/pages/page-150.png`, PDF page 76, local rectangle `[189, 1164, 974, 1584]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 44: primjer 2.344, tiskana str. 150

![Primjer 2.344 — tiskana str. 150.](images/02-dijatonika-c/primjer-2-344.png)

Primjer 2.344 — tiskana str. 150.

- Source: `sources/pages/page-150.png`, PDF page 76, local rectangle `[990, 1162, 1715, 1590]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 45: primjer 2.345, tiskana str. 150

![Primjer 2.345 — tiskana str. 150.](images/02-dijatonika-c/primjer-2-345.png)

Primjer 2.345 — tiskana str. 150.

- Source: `sources/pages/page-150.png`, PDF page 76, local rectangle `[367, 1604, 1476, 2031]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 46: primjer 2.346, tiskana str. 150

![Primjer 2.346 — tiskana str. 150.](images/02-dijatonika-c/primjer-2-346.png)

Primjer 2.346 — tiskana str. 150.

- Source: `sources/pages/page-150.png`, PDF page 76, local rectangle `[406, 2035, 1396, 2436]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 47: primjer 2.347, tiskana str. 151

![Primjer 2.347 — tiskana str. 151.](images/02-dijatonika-c/primjer-2-347.png)

Primjer 2.347 — tiskana str. 151.

- Source: `sources/pages/page-151.png`, PDF page 76, local rectangle `[502, 136, 1493, 522]`.
- Image review: **pending_independent_review**. cleanup_required: lower analysis interleaves following example 2.348 title; source pixels preserved.

<!-- MuseScore: pending -->

### Slot 48: primjer 2.348, tiskana str. 151

![Primjer 2.348 — tiskana str. 151.](images/02-dijatonika-c/primjer-2-348.png)

Primjer 2.348 — tiskana str. 151.

- Source: `sources/pages/page-151.png`, PDF page 76, local rectangle `[449, 500, 1558, 883]`.
- Image review: **pending_independent_review**. cleanup_required: preceding example 2.347 lower analysis interleaves title; source pixels preserved.

<!-- MuseScore: pending -->

### Slot 49: primjer 2.349, tiskana str. 151

![Primjer 2.349 — tiskana str. 151.](images/02-dijatonika-c/primjer-2-349.png)

Primjer 2.349 — tiskana str. 151.

- Source: `sources/pages/page-151.png`, PDF page 76, local rectangle `[495, 883, 1484, 1275]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 50: primjer 2.350, tiskana str. 151

![Primjer 2.350 — tiskana str. 151.](images/02-dijatonika-c/primjer-2-350.png)

Primjer 2.350 — tiskana str. 151.

- Source: `sources/pages/page-151.png`, PDF page 76, local rectangle `[444, 1286, 1550, 1683]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 51: primjer 2.351, tiskana str. 151

![Primjer 2.351 — tiskana str. 151.](images/02-dijatonika-c/primjer-2-351.png)

Primjer 2.351 — tiskana str. 151.

- Source: `sources/pages/page-151.png`, PDF page 76, local rectangle `[444, 2042, 1493, 2489]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 52: primjer 2.352, tiskana str. 152

![Primjer 2.352 — tiskana str. 152.](images/02-dijatonika-c/primjer-2-352.png)

Primjer 2.352 — tiskana str. 152.

- Source: `sources/pages/page-152.png`, PDF page 77, local rectangle `[213, 114, 1555, 577]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 53: primjer 2.353, tiskana str. 152

![Primjer 2.353 — tiskana str. 152.](images/02-dijatonika-c/primjer-2-353.png)

Primjer 2.353 — tiskana str. 152.

- Source: `sources/pages/page-152.png`, PDF page 77, local rectangle `[291, 827, 1458, 1259]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 54: primjer 2.354, tiskana str. 152

![Primjer 2.354 — tiskana str. 152.](images/02-dijatonika-c/primjer-2-354.png)

Primjer 2.354 — tiskana str. 152.

- Source: `sources/pages/page-152.png`, PDF page 77, local rectangle `[239, 1275, 1523, 1720]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 55: primjer 2.355, tiskana str. 153

![Primjer 2.355 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-355.png)

Primjer 2.355 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[191, 103, 907, 511]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 56: primjer 2.356, tiskana str. 153

![Primjer 2.356 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-356.png)

Primjer 2.356 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[921, 111, 1723, 524]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 57: primjer 2.357, tiskana str. 153

![Primjer 2.357 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-357.png)

Primjer 2.357 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[190, 524, 939, 929]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 58: primjer 2.358, tiskana str. 153

![Primjer 2.358 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-358.png)

Primjer 2.358 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[954, 526, 1724, 926]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 59: primjer 2.359, tiskana str. 153

![Primjer 2.359 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-359.png)

Primjer 2.359 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[189, 936, 996, 1341]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 60: primjer 2.360, tiskana str. 153

![Primjer 2.360 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-360.png)

Primjer 2.360 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[1009, 929, 1724, 1339]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 61: primjer 2.361, tiskana str. 153

![Primjer 2.361 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-361.png)

Primjer 2.361 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[189, 1341, 1046, 1764]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 62: primjer 2.362, tiskana str. 153

![Primjer 2.362 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-362.png)

Primjer 2.362 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[1049, 1344, 1724, 1750]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 63: primjer 2.363, tiskana str. 153

![Primjer 2.363 — tiskana str. 153.](images/02-dijatonika-c/primjer-2-363.png)

Primjer 2.363 — tiskana str. 153.

- Source: `sources/pages/page-153.png`, PDF page 77, local rectangle `[380, 1764, 1489, 2168]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 64: primjer 2.364, tiskana str. 154

![Primjer 2.364 — tiskana str. 154.](images/02-dijatonika-c/primjer-2-364.png)

Primjer 2.364 — tiskana str. 154.

- Source: `sources/pages/page-154.png`, PDF page 78, local rectangle `[429, 466, 1532, 905]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 65: primjer 2.365, tiskana str. 154

![Primjer 2.365 — tiskana str. 154.](images/02-dijatonika-c/primjer-2-365.png)

Primjer 2.365 — tiskana str. 154.

- Source: `sources/pages/page-154.png`, PDF page 78, local rectangle `[428, 914, 1531, 1342]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 66: primjer 2.366, tiskana str. 154

![Primjer 2.366 — tiskana str. 154.](images/02-dijatonika-c/primjer-2-366.png)

Primjer 2.366 — tiskana str. 154.

- Source: `sources/pages/page-154.png`, PDF page 78, local rectangle `[424, 1347, 1530, 1768]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 67: primjer 2.367, tiskana str. 154

![Primjer 2.367 — tiskana str. 154.](images/02-dijatonika-c/primjer-2-367.png)

Primjer 2.367 — tiskana str. 154.

- Source: `sources/pages/page-154.png`, PDF page 78, local rectangle `[417, 1775, 1527, 2216]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 68: primjer 2.368, tiskana str. 155

![Primjer 2.368 — tiskana str. 155.](images/02-dijatonika-c/primjer-2-368.png)

Primjer 2.368 — tiskana str. 155.

- Source: `sources/pages/page-155.png`, PDF page 78, local rectangle `[258, 641, 1791, 1113]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 69: primjer 2.369, tiskana str. 155

![Primjer 2.369 — tiskana str. 155.](images/02-dijatonika-c/primjer-2-369.png)

Primjer 2.369 — tiskana str. 155.

- Source: `sources/pages/page-155.png`, PDF page 78, local rectangle `[257, 1224, 1090, 1666]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 70: primjer 2.370, tiskana str. 155

![Primjer 2.370 — tiskana str. 155.](images/02-dijatonika-c/primjer-2-370.png)

Primjer 2.370 — tiskana str. 155.

- Source: `sources/pages/page-155.png`, PDF page 78, local rectangle `[1098, 1201, 1791, 1675]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 71: primjer 2.371, tiskana str. 155

![Primjer 2.371 — tiskana str. 155.](images/02-dijatonika-c/primjer-2-371.png)

Primjer 2.371 — tiskana str. 155.

- Source: `sources/pages/page-155.png`, PDF page 78, local rectangle `[252, 1989, 1090, 2429]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->

### Slot 72: primjer 2.372, tiskana str. 155

![Primjer 2.372 — tiskana str. 155.](images/02-dijatonika-c/primjer-2-372.png)

Primjer 2.372 — tiskana str. 155.

- Source: `sources/pages/page-155.png`, PDF page 78, local rectangle `[1098, 1967, 1787, 2420]`.
- Image review: **pending_independent_review**. Source-only candidate; independent four-edge/source review required.

<!-- MuseScore: pending -->
