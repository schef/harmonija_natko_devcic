# M08 — bounded independent recrop review

**Result: 1 reviewed, 1 PASS, 0 RECROP_REQUIRED, 0 unreviewed within the assigned scope.**

Inventory: `review-candidates/book/M08/images-corrected.json`, confirmed to contain **105 records** and exactly one `pending_recrop_review` entry. Only that pending entry was re-reviewed.

| Field | Reviewed value |
| --- | --- |
| Record | `4.z307-3` |
| Current image | `images/04-neakordicki-a/recrops/zadatak-4-307-3.png` |
| Authoritative source | `sources/pages/page-307.png` |
| Printed source page | 307 |
| PDF source index | **154, 1-based** |
| Source rectangle `[left, top, right, bottom]` | `[232, 355, 1742, 1071]` |
| Decoded crop dimensions | 1510 × 716 pixels |
| Decision | **PASS** |
| Source-limited | No |

## Independent checks

Re-opened the authoritative full source page and the current image in its separate `recrops` directory. Compared every decoded RGB pixel with the specified source rectangle: dimensions and pixels match exactly. The current image is also pixel-identical to the previously tested proposal, permitting reuse and fresh inspection of its native-resolution four-edge strips; vertical strips are rotated, not rescaled.

- **Printed identity:** complete exercise number **3** retained. Caption `Zadatak 3. Tiskana str. 307.` agrees with the source and the section 4.1.7 exercise-3 slot.
- **Full content:** all **four staff rows** retained, with complete clefs/signatures, accidentals, notes, stems, slurs, ledger notes and final double barline.
- **Top edge:** clean genuine source whitespace; no preceding exercise-2 figures or notation intrude.
- **Bottom edge:** lowest final ledger note and all downward stems retained with genuine source whitespace; no exercise-4 slur or other neighbouring ink.
- **Left edge:** all four staff starts and the complete number 3 retained. The margin is narrow but genuinely blank and feasible. The former unrelated diagonal stroke at approximately source x224–230, y692–694 is fully outside the new x232 boundary, not partially retained or painted out.
- **Right edge:** complete staff ends and final barline retained, with clean original whitespace.
- **Excluded material:** no surrounding prose, printed page number, scan-border line, handwriting or partial neighbouring example.
- **Source fidelity:** exact decoded source pixels; no generated margin, artificial border or retouching.
- **Page indexing:** printed page 307 corresponds to **PDF page 154 using 1-based indexing**, consistent with this inventory's spread mapping.

## Bounded handoff

The applied recrop **passes** and is ready for integration as this one image. The older original image is not approved by this decision. No new extraction or candidate-image edit was performed during this review.

Only `review-candidates/book/M08/recrop-review.json` and `review-candidates/book/M08/recrop-review.md` were created. No manifests, images, chapter files, trackers or earlier review reports were changed; no commit or push was made.

Other 104 inventory records were outside this bounded re-review. In particular, the intentional **source_damage** holds for `4.z290-9-realizacija-cont` and `4.31` remain unchanged and are **not** converted to unqualified passes. This one-image approval makes no assertion that all of M08 is ready for completion. No unreadable or incomplete source material was identified within this reviewed crop.
