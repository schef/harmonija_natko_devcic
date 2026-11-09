# M07 extraction hand-off — printed pages 257–276

## Outcome and scope

- Assigned printed pages: **257–276**, inclusive (20 pages).
- Assigned PDF pages: **129–139**, 1-based. Source PNGs are individual printed-page halves, not PDF-spread indices.
- **57 visual slots → 57 separate PNGs:** 40 numbered examples, 15 exercises, 2 realizations.
- Every assigned source PNG was opened visually before selecting its individual rectangles. Each example has four separately selected boundaries; no fixed-margin or automatic page-batch cropping was used.
- No cross-page example occurs in these 57 slots. Multi-system examples and their variants remain together within their own single source-page crop; no stitching or repeated/generated numbers were needed.
- Extraction only: no prose, chapter files, shared manifests, or global milestone trackers changed. No delegation, model subprocess, API, GUI, commit, or push used.

## Deliverables

- `images/03-kromatika-c/`: 57 new direct source-pixel PNG crops.
- `review-candidates/book/M07/images.json`: ordered one-to-one slot mapping, captions, local original-pixel rectangles, source PNG paths, PDF indices, and review notes.
- `review-candidates/book/M07/extract.py`: explicit per-visual boundaries and guarded extraction/reproduction code. Existing output files and manifests are deliberately refused rather than blindly overwritten. The documented `--refine-boundaries` operation validates the original manifest rectangles and exact prior source-pixel content before applying its three specific extractor corrections; it is not a general overwrite mode.
- `review-candidates/book/M07/extraction.md`: this hand-off.

There was no pre-existing assigned output directory or extraction file to preserve. The existing verified text and text-review JSON were read but not modified.

## Complete slot/source mapping

All entries below have image-review status **`pending_independent_review`**. This is an extractor hand-off, **not** independent review or self-approval.

| Manifest IDs | Printed page | PDF page | Visuals |
| --- | ---: | ---: | --- |
| M07-01–02 | 257 | 129 | 3.176, 3.177 |
| M07-03–05 | 258 | 130 | 3.178, 3.179, 3.180 |
| M07-06–07 | 259 | 130 | 3.181, 3.182 (including printed chordal reduction) |
| M07-08–10 | 260 | 131 | 3.183, 3.184, 3.185 |
| M07-11–13 | 261 | 131 | 3.186, 3.187, 3.188 |
| M07-14–15 | 262 | 132 | 3.189, 3.190 |
| M07-16–17 | 263 | 132 | 3.191, 3.192 |
| M07-18–21 | 264 | 133 | 3.193; chapter 3.8 tasks 1, 2, 3 |
| M07-22–28 | 265 | 133 | chapter 3.8 tasks 4, 5, 6, 7, 8, 9, 10 |
| M07-29 | 266 | 134 | Realizacija zadatka 6., including printed title |
| M07-30–31 | 267 | 134 | 3.194, 3.195 |
| M07-32–34 | 268 | 135 | 3.196, 3.197, 3.198 |
| M07-35–37 | 269 | 135 | 3.199, 3.200, 3.201 |
| M07-38–41 | 270 | 136 | 3.202, 3.203, 3.204, 3.205 |
| M07-42–46 | 271 | 136 | chapter 3.9 tasks 1, 2, 3, 4, 5 |
| M07-47 | 272 | 137 | Realizacija zadatka 3., including printed title |
| M07-48–49 | 273 | 137 | 3.206, 3.207 |
| M07-50–52 | 274 | 138 | 3.208, 3.209, 3.210 |
| M07-53–55 | 275 | 138 | 3.211, 3.212, 3.213 |
| M07-56–57 | 276 | 139 | 3.214, 3.215 |

## Extractor checks and source limitations

- All 57 source/output pairs were checked programmatically: output dimensions, image mode, and every pixel equal the recorded source rectangle exactly. There is no resampling, painting, cleaning, generated border, or altered notation.
- Full-resolution top, bottom, left, and right strips were visually inspected for every initial crop. Three refined crops were then opened again: chapter 3.8 tasks 1 and 2, and example 3.207.
- Page 264 has unusually close task separation. Task 1's last sharp ends at source y=1255; its revised bottom is y=1258. Task 2 begins at y=1260, excluding that preceding mark while retaining its highest notes. These small genuine source margins are intentional.
- Page 270 examples 3.202 and 3.203 have a very narrow horizontal separation. Their individually selected rectangles preserve both the first example's final barline and the next example's printed number. Wider generic padding would introduce neighbouring notation.
- Body-text explanatory footnotes are excluded from the image crops and remain in the verified text. Printed asterisk callouts, attribution lines, analytical figures, reductions, and realizations' titles are retained with the relevant notation.
- **18 examples have `cleanup_required: true`:** 3.176, 3.177, 3.178, 3.179, 3.190, 3.194, 3.195, 3.196, 3.201, 3.202, 3.203, 3.204, 3.205, 3.206, 3.207, 3.208, 3.214, 3.215. The scans contain handwritten analysis, circles, or source marks among/against the printed notation. These were not erased. The manifest gives the per-image issue. In particular, the dense handwritten analysis around 3.202–3.204 and 3.215 can extend toward neighbouring layout areas; these are source-cleanliness limitations, not permission to approve the images.
- No printed musical content was judged unreadable enough to omit. Handwritten source analysis can be faint or illegible and is not transcribed or treated as authoritative.

## Integration readiness

**Ready for independent visual review; not ready for final integration approval.** Every image remains pending. The independent reviewer must compare each crop and its caption/source reference against the original source page, explicitly adjudicate the 18 cleanup flags, and report pass or recrop required. The extraction worker has not approved any crop. The integrator must add image blocks/captions/MuseScore placeholders to the assigned text and update milestone status only after the required reviews pass.
