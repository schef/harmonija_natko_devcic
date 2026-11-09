# M02 independent visual review: printed pages 47–63

## Outcome

**69/69 existing images reviewed: 39 PASS, 30 RECROP_REQUIRED.** Of the failures, **20 are source-limited** by meaningful pencil analysis within the required score bounds; **10 have source-tested replacement rectangles**. No images remain unreviewed. **Not ready for integration approval.** This report does not mark M02 complete or human-approved.

## Assignment and evidence

- Printed pages **47–63**, PDF pages **24–32**, using each record's individual PDF-page mapping (the PDF contains paired printed pages).
- Authoritative images opened: `sources/pages/page-047.png` through `sources/pages/page-063.png`, inclusive.
- Inputs: `review-candidates/book/M02/images.json`, `review-candidates/book/M02/text-047-063.md`, and `review-candidates/book/M02/text-047-063-review.json`.
- Compared every existing crop against its authoritative source page. Viewed all crops in unscaled inspection panels, checking top, bottom, left and right boundaries, number/variant identity, staves, notes, figures, connections and source whitespace. Enlarged uncertain clef boundaries and pencil/scan-remnant cases separately.
- Independently compared decoded RGB pixels of every image with its recorded source rectangle: **69/69 exact matches**, including dimensions. No generated border or altered pixels were detected. Exact pixel matching does not excuse clipping or foreign ink.
- Proposed rectangles are source coordinates `[left, top, right, bottom]`, with exclusive right/bottom, matching the input convention. Every proposed rectangle was rendered from the authoritative PNG and visually inspected on all four sides. These are proposals only; existing crops were not modified and remain failed pending recrop and re-review.
- Temporary inspection views were created only under `/tmp/opencode/m02-review`. No delegation, model subprocess, GUI, commit or push was used.

## Decisions by source page

The JSON contains an explicit image path, printed page, decision, reason, proposed rectangle or null, and source-limited flag for every image.

| Printed page | Reviewed images | PASS | RECROP_REQUIRED | Source-limited |
| --- | --- | ---: | ---: | ---: |
| 47 | 2.98–2.99; exercises 1–6 | 6 | 2 | 1 |
| 48 | 2.100–2.102 | 0 | 3 | 3 |
| 49 | 2.103–2.105 | 1 | 2 | 2 |
| 50 | 2.106–2.108 | 0 | 3 | 3 |
| 51 | 2.109–2.111 a | 1 | 2 | 1 |
| 52 | 2.111 b–d; 2.112–2.113 | 1 | 2 | 2 |
| 53 | 2.114–2.115 | 1 | 1 | 1 |
| 54 | 2.116–2.118 first system | 0 | 3 | 2 |
| 55 | 2.118 continuation; 2.119–2.121 | 2 | 2 | 1 |
| 56 | 2.122–2.123 | 2 | 0 | 0 |
| 57 | 2.124–2.125 | 0 | 2 | 2 |
| 58 | 2.126–2.128 | 2 | 1 | 1 |
| 59 | 2.129 | 0 | 1 | 1 |
| 60 | 2.130–2.133; exercises 1–3 | 7 | 0 | 0 |
| 61 | exercises 4–15 | 12 | 0 | 0 |
| 62 | exercises 16–23; realization of exercise 12 | 4 | 5 | 0 |
| 63 | realization of exercise 13, both systems | 0 | 1 | 0 |
| **Total** | **69** | **39** | **30** | **20** |

## Source-tested rectangular corrections

| Image ID | Proposed rectangle | Correction |
| --- | --- | --- |
| `zadatak-2-47-6` | `[202, 2247, 1712, 2427]` | Restore extreme bottom of treble-clef curl and lower whitespace; exclude page number. |
| `primjer-2-111` | `[191, 2017, 1708, 2394]` | Remove faint pencil-only band below printed 6s; retain all part-a notation. |
| `primjer-2-116` | `[193, 1077, 978, 1456]` | Remove handwritten T/stroke below figures; retain printed 6s. |
| `primjer-2-121` | `[219, 2000, 1745, 2392]` | Remove preceding prose descender. Prose ink ends at source y=1997; variant d begins at y=2004. Only a narrow natural separation exists. |
| `zadatak-2-62-16` | `[146, 132, 1667, 303]` | Restore clipped clef bottom and margin. |
| `zadatak-2-62-17` | `[146, 341, 1667, 501]` | Restore clipped clef bottom and margin. |
| `zadatak-2-62-20` | `[143, 923, 1663, 1094]` | Add feasible source whitespace below nearly edge-touching complete clef. |
| `zadatak-2-62-22` | `[137, 1331, 1664, 1504]` | Restore clipped clef bottom and margin. |
| `zadatak-2-62-12-realizacija` | `[115, 1885, 1660, 2396]` | Include identifying printed label and number, preserving complete score and lower connections. |
| `zadatak-2-63-13-realizacija` | `[168, 125, 1715, 1094]` | Include identifying printed label and number, retaining both systems and excluding marginal ink. |

## Source limitations and identity notes

- Source-limited failures: `primjer-2-98`, `primjer-2-100`, `primjer-2-101`, `primjer-2-102`, `primjer-2-103`, `primjer-2-104`, `primjer-2-106`, `primjer-2-107`, `primjer-2-108`, `primjer-2-109`, `primjer-2-111-nastavak`, `primjer-2-113`, `primjer-2-114`, `primjer-2-117`, `primjer-2-118`, `primjer-2-119`, `primjer-2-124`, `primjer-2-125`, `primjer-2-128`, `primjer-2-129`.
- These contain meaningful pencil characters/circles within or vertically overlapping the required printed score area. A clean rectangular solution has not been established. `RECROP_REQUIRED` flags the failed checklist, **not** a claim that recropping will solve an intrinsically marked source. Seek a cleaner authoritative scan or an explicit source-limitation disposition. Do not erase, paint, synthesize or reconstruct notation.
- Isolated scan specks were not treated as foreign text. In particular, enlarged inspection of 2.127 did not establish a meaningful handwritten label warranting failure; the isolated lower-left blemish in 2.123 likewise does not establish a foreign character.
- No wrong source-page or example/exercise-number assignment was found. The page-52 2.111 continuation legitimately has b–d but no repeated example number; the page-55 2.118 continuation likewise has no repeated number. Keep explicit continuation captions when integrating.
- The realization identities are correct, but both crops omit their printed identifying labels/numbers. The proposed rectangles retain those example-specific labels, not unrelated body headings. Their manifest captions also omit the space in `zadatka12` / `zadatka13`; use the source wording `Realizacija zadatka 12.` / `Realizacija zadatka 13.` in final captions.
- The text shard has visual slots rather than final image embeds, alt text, source captions and MuseScore placeholders. This review verifies crop/manifest/slot identity, **not nonexistent final Markdown image blocks**. Integration must still check those final blocks and links. Printed footnotes for 2.103, 2.108 and 2.111 are separately represented in the text shard; their prose is not stray material to retain in score-only crops.
- No composer/work attribution was found omitted from these assigned examples. No printed musical material was identified as unreadable; the faint handwritten analysis is not transcribed or interpreted as authoritative notation.

## Hand-off

Only `review-candidates/book/M02/visual-review.json` and `review-candidates/book/M02/visual-review.md` were created. **No examples were extracted or changed by this reviewer**; all 69 pre-existing source-only crops received independent decisions. No crop, manifest, chapter, text shard or global tracker was edited.

Apply the ten proposed recrops through the extraction/integration role, then obtain independent re-review. Resolve the twenty source-limited failures without unauthorized pixel alteration. Complete final caption/alt/link checks before integration approval. **Not ready for integration; not milestone-complete; not human-approved.**
