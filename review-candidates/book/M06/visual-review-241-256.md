# Independent visual review — M06, printed pages 241–256

**53/53 records reviewed: 45 PASS, 8 RECROP_REQUIRED. Not ready for integration.**

- Assignment: printed pages **241–256**, PDF pages **121–129**.
- Manifest: `review-candidates/book/M06/images-241-256.json`.
- Authoritative sources: `sources/pages/page-241.png` through `sources/pages/page-256.png`, mapped using `sources/index.json`.
- Detailed per-record decisions, root-relative image paths, pages, reasons and safe proposals: `review-candidates/book/M06/visual-review-241-256.json`.
- Only the two review reports were written in the repository. Delivered images, manifest, text and integration state were not edited. No delegation, retouching, commit or push.

## Review method and integrity

Opened all 16 source PNGs and all 53 delivered crops. Inspected complete musical content and all four crop edges at native crop resolution; enlarged tight source-edge neighborhoods. Checked numbers/actual continuation labels, variants, attributions, realization titles, notes, figures, staff ends and lowest stems. Checked feasible original whitespace and excluded prose, page numbers, neighboring examples and recognizable foreign marks.

**Decoded RGB equality: 53/53 exact** against the manifest rectangles on their source PNGs. **Source-index mapping: 53/53 correct**, including PDF page numbers. These checks establish pixel provenance, not visual acceptance by themselves.

Rectangles below use original source-local pixels `[left, top, right, bottom]`, with exclusive right and bottom. Five proposed rectangles were rendered in temporary storage and visually tested; no proposal was applied. A null proposal means no safe complete clean-margin rectangle was established, not permission to paint or clip. Ordinary isolated scan speckle was distinguished from recognizable foreign characters/handwriting.

## Failures and tested proposals

| ID | Example / printed page | Decision | Safe proposed source rectangle | Finding |
| --- | --- | --- | --- | --- |
| M06-p243-slot-09 | 3.147 / 243 | RECROP_REQUIRED | None — source-limited | Partial marginal/handwritten stroke at bottom. Lowest intended figure and first faint foreign pixels both occupy source row2152. A trial bottom2153 still contains foreign pixels; bottom2152 removes figure pixels. Right-edge trimming would lose the complete staff. |
| M06-p246-slot-15 | 3.153 / 246 | RECROP_REQUIRED | `[562,118,1304,573]` | Only two pixels below `(DD)` although safe source whitespace exists. Tested proposal provides seven pixels below its dark extent without admitting prose. |
| M06-p246-slot-16 | 3.154 / 246 | RECROP_REQUIRED | None — source-limited | Bottom includes clipped top of 3.155's `d)`. Intended sharp-2 stack ends at row1393 inclusive; next label starts1394. No blank row for a clean lower margin. |
| M06-p246-slot-17 | 3.155 / 246 | RECROP_REQUIRED | None — source-limited | Top includes clipped figures from 3.154. Raising top to1394 removes those figures but leaves the actual `d)` label touching the boundary. No clean upper margin preserves the label. |
| M06-p247-slot-22 | ZADACI 5 / 247 | RECROP_REQUIRED | `[238,1373,1752,1695]` | Lowest sharp touches bottom boundary. Proposal retains it with ten pixels of source whitespace and excludes exercise6. |
| M06-p248-slot-26 | ZADACI 9 / 248 | RECROP_REQUIRED | `[194,306,1706,673]` | Small unrelated mark intersects top edge. Tested proposal removes it and preserves complete highest slurs and both systems. |
| M06-p250-slot-35 | 3.164 / 250 | RECROP_REQUIRED | `[171,1913,1691,2440]` | Lowest analysis natural touches bottom boundary. Proposal restores six pixels below it and excludes printed page250. |
| M06-p253-slot-43 | ZADACI 2 / 253 | RECROP_REQUIRED | `[218,1343,1738,1813]` | Tiny foreign prose-tail/mark at top boundary. Proposal removes it while retaining highest accidental, number, both systems and figures. |

The two page246 failures must not be accepted merely because the main notation is visible. Their source has no clean horizontal whitespace between the complete intended extents. Removing foreign ink by painting, synthesizing a border or clipping labels/figures is not an acceptable solution.

## Complete record ledger

Each range below enumerates only the explicitly listed reviewed records. Full individual image paths and reasons are in the companion JSON.

| ID | Example / item | Printed page | PDF page | Decision |
| --- | --- | ---: | ---: | --- |
| M06-p241-slot-01 | 3.140 | 241 | 121 | PASS |
| M06-p241-slot-02 | 3.141 | 241 | 121 | PASS |
| M06-p241-slot-03 | 3.142 | 241 | 121 | PASS |
| M06-p242-slot-04 | 3.143 | 242 | 122 | PASS |
| M06-p242-slot-05 | 3.144 a–b | 242 | 122 | PASS |
| M06-p243-slot-06 | 3.144 c | 243 | 122 | PASS |
| M06-p243-slot-07 | 3.145 | 243 | 122 | PASS |
| M06-p243-slot-08 | 3.146 | 243 | 122 | PASS |
| M06-p243-slot-09 | 3.147 | 243 | 122 | RECROP_REQUIRED |
| M06-p244-slot-10 | 3.148 | 244 | 123 | PASS |
| M06-p244-slot-11 | 3.149 | 244 | 123 | PASS |
| M06-p245-slot-12 | 3.150 | 245 | 123 | PASS |
| M06-p245-slot-13 | 3.151 | 245 | 123 | PASS |
| M06-p245-slot-14 | 3.152 | 245 | 123 | PASS |
| M06-p246-slot-15 | 3.153 | 246 | 124 | RECROP_REQUIRED |
| M06-p246-slot-16 | 3.154 | 246 | 124 | RECROP_REQUIRED |
| M06-p246-slot-17 | 3.155 | 246 | 124 | RECROP_REQUIRED |
| M06-p246-slot-18 | 3.156 | 246 | 124 | PASS |
| M06-p247-slot-19 | ZADACI 2 | 247 | 124 | PASS |
| M06-p247-slot-20 | ZADACI 3 | 247 | 124 | PASS |
| M06-p247-slot-21 | ZADACI 4 | 247 | 124 | PASS |
| M06-p247-slot-22 | ZADACI 5 | 247 | 124 | RECROP_REQUIRED |
| M06-p247-slot-23 | ZADACI 6 | 247 | 124 | PASS |
| M06-p247-slot-24 | ZADACI 7 | 247 | 124 | PASS |
| M06-p248-slot-25 | ZADACI 8 | 248 | 125 | PASS |
| M06-p248-slot-26 | ZADACI 9 | 248 | 125 | RECROP_REQUIRED |
| M06-p248-slot-27 | Realizacija zadatka 7. | 248 | 125 | PASS |
| M06-p249-slot-28 | 3.157 | 249 | 125 | PASS |
| M06-p249-slot-29 | 3.158 | 249 | 125 | PASS |
| M06-p249-slot-30 | 3.159 | 249 | 125 | PASS |
| M06-p250-slot-31 | 3.160 | 250 | 126 | PASS |
| M06-p250-slot-32 | 3.161 | 250 | 126 | PASS |
| M06-p250-slot-33 | 3.162 | 250 | 126 | PASS |
| M06-p250-slot-34 | 3.163 | 250 | 126 | PASS |
| M06-p250-slot-35 | 3.164 | 250 | 126 | RECROP_REQUIRED |
| M06-p251-slot-36 | 3.165 | 251 | 126 | PASS |
| M06-p251-slot-37 | 3.166 | 251 | 126 | PASS |
| M06-p251-slot-38 | 3.167 | 251 | 126 | PASS |
| M06-p251-slot-39 | 3.168 | 251 | 126 | PASS |
| M06-p252-slot-40 | 3.169 | 252 | 127 | PASS |
| M06-p252-slot-41 | 3.170 a–c | 252 | 127 | PASS |
| M06-p253-slot-42 | 3.170 d | 253 | 127 | PASS |
| M06-p253-slot-43 | ZADACI 2 | 253 | 127 | RECROP_REQUIRED |
| M06-p253-slot-44 | ZADACI 3 | 253 | 127 | PASS |
| M06-p253-slot-45 | ZADACI 4 | 253 | 127 | PASS |
| M06-p253-slot-46 | ZADACI 5 | 253 | 127 | PASS |
| M06-p254-slot-47 | ZADACI 6 | 254 | 128 | PASS |
| M06-p254-slot-48 | Realizacija zadatka 5. | 254 | 128 | PASS |
| M06-p255-slot-49 | 3.171 | 255 | 128 | PASS |
| M06-p255-slot-50 | 3.172 | 255 | 128 | PASS |
| M06-p255-slot-51 | 3.173 | 255 | 128 | PASS |
| M06-p255-slot-52 | 3.174 | 255 | 128 | PASS |
| M06-p256-slot-53 | 3.175 | 256 | 129 | PASS |

## Special cases and hand-off

- **Multipart numbering:** 3.144 c and 3.170 d correctly carry only their actual printed continuation labels. Their example number appears on the first part only. Neither needs a fabricated repeated number.
- **Tight but clean natural separations:** 3.168 stops immediately above page251, preserving the entire lowest figure; 3.173/3.174 share a very narrow blank horizontal separation. Their tiny feasible margins were checked against the source, not expanded into foreign material. The bottom of 3.174 preserves the complete lowest slur and excludes the prose footnote.
- All assigned musical records were inspected; no musical content was newly extracted or altered by this reviewer. Source labels and page assignments agree with the manifest. This is an image review, not an independent prose transcription or assembled-book alt-text audit.
- No unreadable notation prevented these decisions. Three records are **source-limited for a clean complete rectangular extraction**, as detailed above. Five further records have safe source-tested proposals and need implementation followed by independent re-review.
- **Integration blocked:** eight current images fail. Do not treat tested proposals as already corrected delivered files, and do not approve source-limited images on the basis of pixel provenance alone.
