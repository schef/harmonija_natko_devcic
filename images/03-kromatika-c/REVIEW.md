# M07 — provisional image integration review

**Scope:** printed pages 257–276, 1-based PDF pages 129–139. **Not complete:** 40 independent passes; 17 source-limited failures (`cleanup_required`). No crop was newly approved by the integration worker.

- [Integrated chapter](../../chapters/03-kromatika-c.md)
- [Final 57-record manifest](../../review-candidates/book/M07/images-integrated.json)
- [Complete identity/page slot map and validation](../../review-candidates/book/M07/INTEGRATION.md)
- [Initial independent review](../../review-candidates/book/M07/visual-review.json): 36 PASS, 21 RECROP_REQUIRED, including 17 source-limited failures.
- [Independent recrop review](../../review-candidates/book/M07/recrop-review.json): all four replacement crops PASS.
- [Authoritative source index](../../sources/index.json)

The chapter embeds only the 40 approved crops. The other 17 entries are explicitly marked **PROVISIONAL — cleanup_required**, with ordinary links to unapproved source crops and reasons, rather than image embeds. Each of the 57 slots has its own caption, printed page, authoritative 1-based PDF page and MuseScore TODO. All images remain unchanged, direct source-pixel rectangles; the integration worker verified all 57 decoded RGB crops against the recorded source rectangles. Exact pixels do not imply checklist approval.

## Approved crops — 40 independent passes

The complete per-image identity and page map is in the integration report and final manifest linked above. Initial PASS applies to M07-05, M07-07–14, M07-16–26, M07-28–29, M07-32–36, M07-42–43, M07-46–47 and M07-51–55 (36 records). All required printed variants, staff ends, figures, attributions and feasible original white margins are covered by that independent review.

The following four corrected crops supersede their failed originals. Only these replacement paths are embedded:

| ID | Identity | Printed / PDF page | Approved replacement | Restored content |
| --- | --- | --- | --- | --- |
| M07-06 | 3.181 | 259 / 130 | [Crop](recrops/primjer-3-181.png) | Complete lowest (D) annotation and genuine lower margin. |
| M07-27 | §3.8, exercise 9 | 265 / 133 | [Crop](recrops/zadatak-3-8-9.png) | Complete lower-system treble-clef curl and lower margin. |
| M07-44 | §3.9, exercise 3 | 271 / 136 | [Crop](recrops/zadatak-3-9-3.png) | Complete treble-clef bottom curl and lower margin. |
| M07-45 | §3.9, exercise 4 | 271 / 136 | [Crop](recrops/zadatak-3-9-4.png) | Complete lower-system treble-clef curl and lower margin. |

## Blocked source crops — 17 cleanup_required

Every row below is **RECROP_REQUIRED / source-limited, not approved**. These links are retained solely for traceability. Internal handwriting shares the required notation/label envelope; edge trimming alone cannot produce a compliant crop. A cleaner authoritative scan or an explicit policy decision is needed; this integration does not authorize retouching or relaxing the review checklist.

| ID | Identity | Printed / PDF page | Unapproved crop | Independent-review reason (summary) |
| --- | --- | --- | --- | --- |
| M07-01 | 3.176 | 257 / 129 | [Source crop](primjer-3-176.png) | Handwritten V below c and strokes beside its label occupy the required content envelope. |
| M07-02 | 3.177 | 257 / 129 | [Source crop](primjer-3-177.png) | Harmonic writing above a/b, below systems and inside notation cannot be excluded while retaining a–h. |
| M07-03 | 3.178 | 258 / 130 | [Source crop](primjer-3-178.png) | Handwriting between Chopin attribution and upper slur lies inside the required rectangle. |
| M07-04 | 3.179 | 258 / 130 | [Source crop](primjer-3-179.png) | Harmonic handwriting intersperses printed a–d labels, including the upper boundary. |
| M07-15 | 3.190 | 262 / 132 | [Source crop](primjer-3-190.png) | Writing above a shares the printed labels' height; all a–f, NE and itd. must remain. |
| M07-30 | 3.194 | 267 / 134 | [Source crop](primjer-3-194.png) | Writing above variants and circles touching low figures; upper edge intersects handwriting. |
| M07-31 | 3.195 | 267 / 134 | [Source crop](primjer-3-195.png) | Pencil lettering/line crosses clef and notation; additional writing above c. |
| M07-37 | 3.201 | 269 / 135 | [Source crop](primjer-3-201.png) | Harmonic labels above, between and below staves; internal analysis remains after edge trimming. |
| M07-38 | 3.202 | 270 / 136 | [Source crop](primjer-3-202.png) | Pencil labels/strokes between staves and under notation remain within the envelope. |
| M07-39 | 3.203 | 270 / 136 | [Source crop](primjer-3-203.png) | Handwriting within/below notation and bottom-left mark from the region above 3.204. |
| M07-40 | 3.204 | 270 / 136 | [Source crop](primjer-3-204.png) | Handwriting beside title/between voices and partial neighbouring analysis at upper edge. |
| M07-41 | 3.205 | 270 / 136 | [Source crop](primjer-3-205.png) | Pencil labels above scale and beneath its staff lie inside the grand-staff envelope. |
| M07-48 | 3.206 | 273 / 137 | [Source crop](primjer-3-206.png) | Analysis/lines overlap slurs and notes, cross/below staves and extend right. |
| M07-49 | 3.207 | 273 / 137 | [Source crop](primjer-3-207.png) | Label above right chord shares the clef-top height; lowering top would clip the clef. |
| M07-50 | 3.208 | 274 / 138 | [Source crop](primjer-3-208.png) | Harmonic writing between three staves and among lower figures cannot be removed by cropping. |
| M07-56 | 3.214 | 276 / 139 | [Source crop](primjer-3-214.png) | Writing beside/above a–c labels occupies their required height envelope. |
| M07-57 | 3.215 | 276 / 139 | [Source crop](primjer-3-215.png) | Extensive labels/circles overlap lower notation; foreign partial marks at right/bottom. Retain all a/b/c and printed umjesto:. |

Full original English review reasons are preserved in the final manifest. No source prose is reported unreadable by the verified text review. The blocker is image cleanliness, not missing transcription. No human approval or milestone completion is claimed.
