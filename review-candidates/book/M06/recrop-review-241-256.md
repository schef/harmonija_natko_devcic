# M06 recrop follow-up — five pending records only

**5/5 PASS; 0 RECROP_REQUIRED.**

Reviewed only the five `pending_recrop_review` records in `review-candidates/book/M06/images-corrected-241-256.json`. Assigned printed pages: **246, 247, 248, 250, 253**; corresponding PDF pages: **124, 124, 125, 126, 127**.

Each delivered recrop was opened at native resolution and checked for complete musical content and all four clean edges against authoritative source content reviewed in this session. Decoded RGB arrays match the stated source PNG rectangles **exactly in all five cases**. All five source/PDF mappings agree with `sources/index.json`. The original source margins are genuine; no painting, resampling or artificial border was detected.

| ID | Item | Root-relative reviewed image | Printed / PDF page | Decision | Findings |
| --- | --- | --- | --- | --- | --- |
| M06-p246-slot-15 | 3.153 | `images/03-kromatika-b/recrops/primjer-3-153.png` | 246 / 124 | PASS | Number, C–g, grand staff, continuation mark, lowest stems and complete `(DD)` retained. Seven-pixel lower dark-extent margin; following prose excluded. All four edges clean. |
| M06-p247-slot-22 | ZADACI 5 | `images/03-kromatika-b/recrops/zadatak-3-7-2-5.png` | 247 / 124 | PASS | Number5, both systems, signatures, notes, slurs and final barline intact. Complete lowest sharp with ten-pixel lower dark-extent margin; exercise6 excluded. All four edges clean. |
| M06-p248-slot-26 | ZADACI 9 | `images/03-kromatika-b/recrops/zadatak-3-7-2-9.png` | 248 / 125 | PASS | Number9, both systems, highest slurs, lowest stems, accidentals and ending tie/barline intact. Top foreign mark removed with genuine six-pixel upper dark-extent margin. All four edges clean. |
| M06-p250-slot-35 | 3.164 | `images/03-kromatika-b/recrops/primjer-3-164.png` | 250 / 126 | PASS | Number, complete Schubert attribution, full staves, notes, ledger lines, slurs and analysis intact. Lowest natural retained with six-pixel lower dark-extent margin; page250 excluded. All four edges clean. |
| M06-p253-slot-43 | ZADACI 2 | `images/03-kromatika-b/recrops/zadatak-3-7-3-2.png` | 253 / 127 | PASS | Number2, both systems, highest accidental, every figure and final barline retained. Top foreign mark removed with nine-pixel upper dark-extent margin; preceding prose and exercise3 excluded. All four edges clean. |

Margin measurements describe distances to pixels with grayscale value below160; visual review, rather than threshold measurements alone, established the decisions. Detailed rectangles, paths, per-record checks and reasons are in `review-candidates/book/M06/recrop-review-241-256.json`.

## Hand-off

- Created only `review-candidates/book/M06/recrop-review-241-256.json` and `review-candidates/book/M06/recrop-review-241-256.md`.
- No images extracted or modified; no manifest, chapter, tracker or prior review report edited. No delegation, model calls, GUI, commit or push.
- No unreadable or incomplete source material prevents acceptance of these five delivered recrops.
- **These five recrops are ready for integration.** This bounded follow-up does not approve or alter the other48 records. The previously reported source-limited cases **3.147, 3.154 and 3.155 remain outside this follow-up and unresolved**; overall milestone readiness is not established here.
