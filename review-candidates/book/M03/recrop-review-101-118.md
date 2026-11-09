# Independent recrop review: five corrected images

**Result: 5 PASS, 0 RECROP_REQUIRED, 0 unreviewed.**

Scope: only the five `pending_recrop_review` records in `review-candidates/book/M03/images-corrected-101-118.json`. Printed source pages 104, 106 and 117 correspond to PDF pages 53, 54 and 59. No other records were reassessed.

Each corrected image was opened at native resolution and compared with its source-page content/context. All four edges, complete notation, identifiers, variants, figures and applicable labels were inspected. All five images exactly match their declared source rectangles: RGB mode, dimensions and every decoded channel value. No added borders or retouching were detected. Isolated scan specks were distinguished from meaningful foreign marks.

## Decisions

| ID | Image | Printed page | Decision | source_limited | proposed_rect |
| --- | --- | --- | --- | --- | --- |
| `primjer-2-224` | `images/02-dijatonika-b/recrops/primjer-2-224.png` | 104 | PASS | false | null |
| `primjer-2-229` | `images/02-dijatonika-b/recrops/primjer-2-229.png` | 106 | PASS | false | null |
| `zadatak-2-117-1` | `images/02-dijatonika-b/recrops/zadatak-2-117-1.png` | 117 | PASS | false | null |
| `zadatak-2-117-3` | `images/02-dijatonika-b/recrops/zadatak-2-117-3.png` | 117 | PASS | false | null |
| `zadatak-2-117-5` | `images/02-dijatonika-b/recrops/zadatak-2-117-5.png` | 117 | PASS | false | null |

### `primjer-2-224`

All a–d labels, example number, clef, chords, accidentals, printed interval text/brackets and staff ends remain complete. The lower handwritten harmonic lettering is excluded. Genuine source margins remain on every edge. Dark-content clearances, left/top/right/bottom: **20/13/16/5 px**. Exact source rectangle: `[182,1400,1707,1595]`.

### `primjer-2-229`

The handwritten chord names above the staff are excluded. Number, clef, key signature, chords, accidentals, II7/IV7/VI7 labels and staff ends are intact. No prose or meaningful foreign edge marks remain. Genuine source clearances: **17/9/19/21 px**. Exact source rectangle: `[519,103,1268,298]`.

### `zadatak-2-117-1`

The unrelated horizontal stroke above the staff is excluded. Number 1, upper key-signature sharps, time signature, all notes, final barline and lowest stacked figures/accidentals remain complete. Genuine source clearances: **17/6/16/9 px**. Exact source rectangle: `[248,687,1763,873]`.

### `zadatak-2-117-3` — natural-separation qualification

Number 3, clef, signatures, slur, all notes and staff ends are complete. No fragment of exercise 2 remains.

**Correction to the earlier margin description:** there is no full-width blank top row. Native-source pixel inspection establishes that the preceding exercise's last figure pixels end at **y=1074**, and the intended slur's first pixels begin at **y=1075**, exactly the retained top row. No part of the slur exists above that boundary. An upward expansion would include the preceding figure; a downward cut would clip the slur. This therefore passes at the natural source separation under the no-feasible-margin exception. Do not expand by a fixed margin or add an artificial border.

Other dark-content clearances, left/right/bottom: **18/8/7 px**. Exact source rectangle: `[243,1075,1763,1213]`. `source_limited: false` indicates no unresolved failure; the natural top-margin constraint is documented, not concealed.

### `zadatak-2-117-5`

The lower-left diagonal foreign stroke is excluded. Number 5, clef, signatures, all slurs/ties, accidentals, notes, stems and final barline remain intact. Genuine source clearances: **5/3/16/15 px**. Remaining isolated specks are not meaningful foreign lettering. Exact source rectangle: `[261,1434,1763,1609]`.

## Handoff

- No remaining blocking image issues in these five corrected files; all five are ready for image integration.
- This does not change the remaining findings for other images in `review-candidates/book/M03/visual-review-101-118.json` and `.md` or approve the milestone globally.
- Created only `review-candidates/book/M03/recrop-review-101-118.json` and `review-candidates/book/M03/recrop-review-101-118.md`.
- No image, chapter, manifest or other metadata was edited; originals remain unchanged. No retouching, commit or push.
