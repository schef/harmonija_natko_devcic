# Extraction hand-off: printed pages 82–100

## Scope and outcome

- Assignment: printed **82–100**, PDF **42–51**; all **19 source PNGs opened visually**.
- **80/80 visual slots covered**, in the exact identity and order of `review-candidates/book/M03/text-082-100.md`.
- Outputs: **80 new PNGs** in `images/02-dijatonika-b`, `review-candidates/book/M03/images-082-100.json`, `review-candidates/book/M03/extract-082-100.py`, and this report.
- No transcription, chapter, global manifest, tracker, earlier-page crop, or unrelated file edited. No delegation, model/API calls, GUI, commit, or push.
- Existing assigned image directory was inspected before extraction: it ended at example 2.167 and exercises on page 81; no prior assigned-range images were overwritten. Four of this worker's initial page-91 exercise crops were backed up in temporary staging before edge corrections.

## Crop provenance

Each output is one rectangular crop of its original `sources/pages/page-NNN.png`, with no resampling, compositing, stitching, retouching, artificial border, or generated pixels. Multiple systems belonging to one slot remain together in their original page layout. Realization titles are retained. Rectangles were selected separately for each visual after viewing every source page; they are not a fixed-margin batch rule.

The script's working coordinates use the page viewer's 2000-pixel-high reference frame. The manifest's `rect` is the resulting integer **original-pixel** `[left, top, right, bottom)` rectangle. Each manifest record includes the exact local slot text as `example`, a page-qualified `id`, kind, printed/PDF page, source image, output image, caption, review status and note.

## Coverage and review status

**Every individual image is `pending_independent_review`. No image has been approved by this extractor.** The manifest is the per-image hand-off; the following page inventory accounts for all 80 records.

| Printed page | PDF page | Visual slots extracted | Count | Image-review result |
|---|---|---|---:|---|
| 82 | 42 | Exercises 5, 6, 7; realization of exercise 4 | 4 | All pending independent review |
| 83 | 42 | 2.168–2.171 | 4 | All pending independent review |
| 84 | 43 | 2.172–2.174 | 3 | All pending independent review |
| 85 | 43 | 2.175–2.178 | 4 | All pending independent review |
| 86 | 44 | 2.179–2.182 | 4 | All pending independent review |
| 87 | 44 | 2.183–2.185 | 3 | All pending independent review |
| 88 | 45 | 2.186–2.189 | 4 | All pending independent review |
| 89 | 45 | 2.190–2.193 | 4 | All pending independent review |
| 90 | 46 | 2.194–2.196 | 3 | All pending independent review |
| 91 | 46 | 2.197–2.199; exercises 1–5 | 8 | All pending; exercises 4/5 have source-layout conflicts |
| 92 | 47 | Exercises 6–16 | 11 | All pending independent review |
| 93 | 47 | Realization of exercise 13; 2.200, 2.201 | 3 | All pending independent review |
| 94 | 48 | 2.202–2.205 | 4 | All pending independent review |
| 95 | 48 | 2.206–2.208 | 3 | All pending independent review |
| 96 | 49 | 2.209, 2.210 | 2 | All pending independent review |
| 97 | 49 | 2.211, 2.212, 2.213.a—m | 3 | All pending independent review |
| 98 | 50 | 2.213.n—t continuation; 2.214.a; 2.214.b | 3 | All pending independent review |
| 99 | 50 | 2.215, 2.216 | 2 | All pending independent review |
| 100 | 51 | 2.217–2.221; exercises 1–3 | 8 | All pending independent review |
| **Total** | | | **80** | **No self-approval** |

## Source limitations and review priorities

- **49 records are flagged `cleanup_required`** in `review_note`: 47 examples with pencil marks/scan interference and the two page-91 exercises with overlapping layout. This flag is not a review pass and does not authorize retouching.
- Pencil handwriting intersects or lies inside the bounding rectangle of many printed staves, figures and labels. Source pixels have been preserved. Some pencil strokes consequently reach crop edges; clean removal cannot be achieved by a rectangle without sacrificing printed content. Reviewers must inspect these conflicts rather than mistake them for cleaned publication-ready images.
- **Page 91, exercises 4 and 5:** the lowest printed figured-bass line of exercise 4 and highest ledger note of exercise 5 overlap vertically. Retaining all intended notation necessarily retains neighbouring fragments in these rectangular crops. Both records explicitly flag this conflict; these are not clean crop approvals.
- **Page 91, example 2.199:** pencil analysis from 2.198 adjoins the Schumann attribution. The source-layout conflict is noted; attribution retained.
- **Example 2.213:** `primjer-2-213-p97.png` retains a–m and the printed number; `primjer-2-213-p98.png` retains the separately scanned continuation. The continuation prints n, o, p, r, s, t; no missing q or repeated example number has been fabricated. No cross-page stitching.
- **Example 2.214:** separate `primjer-2-214-a.png` and `primjer-2-214-b.png` match the two requested slots and retain both Bach attributions. Only part a prints the shared example number; part b prints its own variant label.
- **Example 2.210:** all printed a–h variants retained, even though the nearby prose refers to a–g.
- Printed prose footnotes below examples 2.185, 2.210 and 2.213 are excluded from score crops and remain the text agent's responsibility; in-score footnote symbols are retained.
- No otherwise unreadable or missing source page was encountered. Pencil interference remains a source-quality limitation, not reconstructed notation.

## Validation and integration readiness

The reproducible script refuses to overwrite a differing existing PNG. The hand-off validation checks slot identities/order, page counts, unique output paths, source bounds, file existence, status values, and exact decoded pixel equality with every manifest source rectangle.

**Ready for independent image review, not ready for final integration approval.** An independent reviewer must inspect all four edges at full resolution for every image and provide pass/recrop-required decisions. The page-91 layout conflicts and source handwriting require explicit disposition. No completion status has been changed.
