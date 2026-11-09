# M05 — independent applied-recrops review

**2/2 PASS; 0 RECROP_REQUIRED; 0 unreviewed.** Both reviewed recrops are ready for image integration individually. This is not approval of the whole milestone.

## Scope and method

Reviewed **only the two `pending_recrop_review` records** selected from `review-candidates/book/M05/images-corrected.json`:

- Example 3.2: printed **175**, PDF **88**.
- Example 3.33: printed **188**, PDF **95**.

One independent reviewer reopened both full source PNGs and both complete applied recrop files, compared all printed content, and inspected **all four edges at native resolution**. Approval is based on the applied files, not merely on the earlier proposed bounds. No delegation, model calls or GUI used.

Both files are **exact decoded RGB pixel matches** to their declared source rectangles, including mode and dimensions. Genuine source whitespace is retained; no retouch, resampling or artificial border was detected. Coordinates below are `[left, top, right, bottom]`, with exclusive right/bottom.

## Decisions

### `primjer-3-2` — PASS

- **Image:** `images/03-kromatika-a/recrops/primjer-3-2.png`
- **Source:** `sources/pages/page-175.png`
- **Printed / PDF:** 175 / 88
- **Rectangle:** `[215, 1958, 848, 2298]`
- **Dimensions:** 633 × 340, RGB
- **Exact source-pixel equality:** PASS

Complete number **3.2**, variants **a/b**, both clefs, brace, both staves, all notes/accidentals and both printed connecting lines are retained.

| Edge | Independent finding |
| --- | --- |
| Top | Complete a/b labels, upper clef and highest note; genuine blank margin; no foreign character fragment. |
| Bottom | Complete lower clef, lowest notes, staff and barlines; real blank margin beneath. |
| Left | Number, brace and clefs complete; marginal foreign fragments excluded; genuine margin remains. |
| Right | Both staff ends and final barlines intact; real source whitespace beyond. |

No surrounding prose, adjacent example, printed page number or handwriting is retained. ID, source-page reference and manifest caption agree with the source. **No further recrop proposed; not source-limited.**

### `primjer-3-33` — PASS

- **Image:** `images/03-kromatika-a/recrops/primjer-3-33.png`
- **Source:** `sources/pages/page-188.png`
- **Printed / PDF:** 188 / 95
- **Rectangle:** `[157, 1459, 1678, 1802]`
- **Dimensions:** 1521 × 343, RGB
- **Exact source-pixel equality:** PASS

Complete number **3.33**, **all three brackets**, highest upward stems, lowest bass down-stems, both clefs, all notes/accidentals, both staves and final barlines are retained. No printed variant label or composer attribution belongs to this example in the source.

| Edge | Independent finding |
| --- | --- |
| Top | Highest bracket and all other brackets/stems complete; genuine blank margin; pencil chord names and residual fragments excluded. |
| Bottom | Lowest bass stems and lower staff ends intact; real blank margin beneath. |
| Left | Number, brace and clefs complete with genuine source whitespace; no neighbouring content. |
| Right | Both staff ends and final barlines complete, followed by real whitespace. |

No prose, adjacent example, printed page number or handwriting remains. ID, source-page reference and manifest caption agree with the source. **No further recrop proposed; not source-limited.**

## Hand-off

1. **Assigned pages:** printed 175 / PDF 88 and printed 188 / PDF 95; two pending recrop records only.
2. **Files created:** only `review-candidates/book/M05/recrop-review.json` and `review-candidates/book/M05/recrop-review.md`.
3. **Examples extracted or changed by reviewer:** none. The parent-applied recrops of 3.2 and 3.33 were reviewed without modifying them.
4. **Results:** 3.2 **PASS**; 3.33 **PASS**. **0 unreviewed.**
5. **Ambiguous/unreadable/incomplete material:** none identified in these two recrops. Isolated scan grain is not interpreted as a foreign character.
6. **Integration readiness:** these **two images are ready individually**. Previously reported source-limited conflicts elsewhere remain outside this follow-up; no other record or milestone status is reclassified here.

No images, manifest, other metadata, chapters or global files edited. No retouching, commit or push.
