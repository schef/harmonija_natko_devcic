# M10 extraction / coverage hand-off

- Assigned/opened: printed349–378, all30 source PNGs; PDF175–190 (1-based, checked against `sources/index.json`). No page outside this range opened.
- Exact coverage: **86/86** positional slots =7+13+18+27+21 across the five verified Markdown shards and review JSONs. No new/missing slot or multipart-count difference.
- Read all five text shards and all five review JSONs; verified text was not edited.
- Deliverables: `review-candidates/book/M10/images-complete.json`, this report, `review-candidates/book/M10/reconcile.py`, and the four separate PNG replacements listed below.
- Original `images.json` (86 records) and all86 original PNGs preserved byte-for-byte; SHA-256 compared before/after. All86 final candidates equal the exact source rectangle pixel-for-pixel.
- Crop edges were examined individually, using source pages and native-resolution 40-pixel edge strips (temporary diagnostic sheets only, not score deliverables). No batch margin expansion, painting, synthetic border, resampling, joining or notation reconstruction.
- **All86 candidates remain pending_independent_review.** Extractor observations are not independent image-review results or approvals. A separate reviewer must inspect every candidate against its source.

## Separate recrops (original files retained)

- `images/04-neakordicki-c/zadatak-4-359-9-realizacija-coverage-recrop.png`: Restore the complete printed Realizacija zadatka 9. title; keep all three systems and lowest figures. Original `images/04-neakordicki-c/zadatak-4-359-9-realizacija.png`, local rect `[199, 238, 1745, 1731]`; replacement local rect `[199, 116, 1745, 1731]`.
- `images/04-neakordicki-c/zadatak-4-360-12-realizacija-coverage-recrop.png`: Restore the complete printed Realizacija zadatka 12. title; keep all four systems and lowest stem. Original `images/04-neakordicki-c/zadatak-4-360-12-realizacija.png`, local rect `[154, 251, 1703, 2062]`; replacement local rect `[154, 127, 1703, 2062]`.
- `images/04-neakordicki-c/zadatak-4-374-1-realizacija-a-coverage-recrop.png`: Restore the complete printed Realizacija zadatka 1. title; keep the opening system, tied bass and source margin. Original `images/04-neakordicki-c/zadatak-4-374-1-realizacija-a.png`, local rect `[165, 1953, 1719, 2354]`; replacement local rect `[165, 1880, 1719, 2354]`.
- `images/04-neakordicki-c/primjer-4-192-coverage-recrop.png`: Restore the very top of the Beethoven attribution, clipped by the old top edge. The preceding prose descenders overlap its vertical range: cleanup_required/layout_conflict, no masking or retouch. Original `images/04-neakordicki-c/primjer-4-192.png`, local rect `[158, 1300, 1686, 1948]`; replacement local rect `[158, 1293, 1686, 1948]`.

## Integration blockers / source limitations

- 4.169 (362): lowest bass beam overlaps the explanatory footnote vertical range. Preserve the full beam; current source-only candidate contains partial related-footnote ink. cleanup_required/layout_conflict; not a pass.
- 4.173 (363): abrasion interrupts the right final barline in the source itself. source_damage; no repair or concealed clipping.
- 4.178 parts on366/367: handwritten bass-note circles are source ink. cleanup_required/handwriting; no erasure.
- 4.192 (378): old top clipped the Beethoven attribution; replacement restores it but retains unavoidable preceding-prose descenders. Bottom slurs and next Ravel attribution share the same vertical range, leaving a constrained bottom margin. cleanup_required/layout_conflict; reviewer must not approve merely because notes are present.
- 4.193 (378): complete Ravel attribution retained with unavoidable preceding-example slur fragments at top. cleanup_required/layout_conflict. Lowest bass notes retained and page number excluded.
- 4.193 is an open-ended printed excerpt, NOT an incomplete extraction requiring an invented final barline. Parent reports379 starts5.REKAPITULACIJA and Zadaci1/2, with no4.193 continuation. This worker stopped at378; no379 crop/continuation added. Supersedes the earlier text-review suggestion to investigate a possible continuation; verified text remains untouched.
- Multipart identities: 4.152351/352; exercise8356/357; exercise11357/358; exercise2364/365; 4.178366/367; 4.182368/369; exercise2371/372; exercise5373/374; realization1374/375. Keep separate images and actual printed number/title only where present, never repeat or synthesize labels.
- Explanatory footnotes are already separately transcribed in the verified shards. Their score markers remain in crops. Realization titles are restored in the new PNGs; Allegro, ma non troppo and Andantino grazioso remain in the original complete score crops.
- No unreadable prose discovered in this extraction task; no musical symbol repaired, inferred or replaced. The abrasion/handwriting/layout conflicts above require explicit reviewer/integrator disposition.
- **Ready for independent review, not final integration or milestone completion.** No chapter Markdown, global tracker, raw manifest, commit or push changed.

## Per-slot coverage and image-review state

| Slot | Printed / PDF | Candidate | Image-review result | Extractor observation |
|---|---|---|---|---|
| 4.143 | 349 / 175 | `images/04-neakordicki-c/primjer-4-143.png` | pending independent review | Variants a/b/c, stars and bass figures 4–3 and 7–6. |
| 4.144 | 349 / 175 | `images/04-neakordicki-c/primjer-4-144.png` | pending independent review | Variants a/b and all lower stems. |
| 4.145 | 349 / 175 | `images/04-neakordicki-c/primjer-4-145.png` | pending independent review | Variants a/b, connecting lines and figures 4–3 / 7–6; page number excluded. |
| 4.146 | 350 / 176 | `images/04-neakordicki-c/primjer-4-146.png` | pending independent review | Variants a/b and both NE labels. |
| 4.147 | 350 / 176 | `images/04-neakordicki-c/primjer-4-147.png` | pending independent review | Variants a/b; right edge stops before the neighbouring 4.148 number. |
| 4.148 | 350 / 176 | `images/04-neakordicki-c/primjer-4-148.png` | pending independent review | Variants a/b including raised accidentals; left edge excludes 4.147. |
| 4.149 | 350 / 176 | `images/04-neakordicki-c/primjer-4-149.png` | pending independent review | Variants a/b/c, DA/DA/NE, brackets and bottom *) marker; explanation separately transcribed. |
| 4.150 | 351 / 176 | `images/04-neakordicki-c/primjer-4-150.png` | pending independent review | Variants a/b and both complete stacked figured-bass groups, including parentheses. |
| 4.151 | 351 / 176 | `images/04-neakordicki-c/primjer-4-151.png` | pending independent review | Star above the beamed soprano and complete final barline. |
| 4.152 a–c | 351 / 176 | `images/04-neakordicki-c/primjer-4-152-a.png` | pending independent review | First part a–c on351; continuation d–g on352, including *) marker. Printed number only on351; explanation separately transcribed. |
| 4.152 d–g (nastavak) | 352 / 177 | `images/04-neakordicki-c/primjer-4-152-b.png` | pending independent review | First part a–c on351; continuation d–g on352, including *) marker. Printed number only on351; explanation separately transcribed. |
| 4.153 | 352 / 177 | `images/04-neakordicki-c/primjer-4-153.png` | pending independent review | All five variants a–e, including cross-staff diagonal in d. |
| 4.154 | 352 / 177 | `images/04-neakordicki-c/primjer-4-154.png` | pending independent review | All three variants a–c, accidentals and connecting lines. |
| 4.155 | 352 / 177 | `images/04-neakordicki-c/primjer-4-155.png` | pending independent review | Complete two-line Beethoven concerto attribution, fermata/star, tuplets and lower slur. |
| 4.156 | 352 / 177 | `images/04-neakordicki-c/primjer-4-156.png` | pending independent review | Complete Chopin op.59 no.1 attribution, long upper/lower slurs, lowest beam and staccato dots; open right endpoint is printed. |
| 4.157 | 353 / 177 | `images/04-neakordicki-c/primjer-4-157.png` | pending independent review | Chopin op.7 no.1 attribution and *) marker; separate prose footnote excluded. |
| 4.158 | 353 / 177 | `images/04-neakordicki-c/primjer-4-158.png` | pending independent review | Schumann op.21 no.6 attribution, both excerpts and i dalje: label, single/double-star markers and bottom slur; prose explanations excluded. |
| 4.159 | 353 / 177 | `images/04-neakordicki-c/primjer-4-159.png` | pending independent review | Chopin op.50 no.1 attribution, *) marker and complete low stems/slurs; explanation excluded. |
| 4.160 | 354 / 178 | `images/04-neakordicki-c/primjer-4-160.png` | pending independent review | Variant a spans both left-hand systems; b/c occupy lower right. All belong to this single numbered slot. |
| 4.161 | 354 / 178 | `images/04-neakordicki-c/primjer-4-161.png` | pending independent review | All overlapping upper/lower slurs and final low bass stem; attribution is in the surrounding verified prose, not printed as a separate score title. |
| 4.162 | 355 / 178 | `images/04-neakordicki-c/primjer-4-162.png` | pending independent review | Both fermatas, accidentals, bottom bass stem and complete final barline; Janacek attribution is in preceding prose on354. |
| 4.163 | 355 / 178 | `images/04-neakordicki-c/primjer-4-163.png` | pending independent review | All three stars, bass appoggiatura and final barline. |
| zadatak 1 | 355 / 178 | `images/04-neakordicki-c/zadatak-4-355-1.png` | pending independent review | One complete soprano row. |
| zadatak 2 | 355 / 178 | `images/04-neakordicki-c/zadatak-4-355-2.png` | pending independent review | One complete soprano row. |
| zadatak 3 | 355 / 178 | `images/04-neakordicki-c/zadatak-4-355-3.png` | pending independent review | One complete soprano row, including low accidentals. |
| zadatak 4 | 356 / 179 | `images/04-neakordicki-c/zadatak-4-356-4.png` | pending independent review | Three bass rows with every stacked figure and final barline. |
| zadatak 5 | 356 / 179 | `images/04-neakordicki-c/zadatak-4-356-5.png` | pending independent review | Three bass rows with all star markers and final barline. |
| zadatak 6 | 356 / 179 | `images/04-neakordicki-c/zadatak-4-356-6.png` | pending independent review | One soprano row including lowest slur. |
| zadatak 7 | 356 / 179 | `images/04-neakordicki-c/zadatak-4-356-7.png` | pending independent review | One soprano row including lowest note. |
| zadatak 8 (početak) | 356 / 179 | `images/04-neakordicki-c/zadatak-4-356-8-a.png` | pending independent review | First soprano row of8; printed number here, continuation on357. |
| zadatak 8 (nastavak) | 357 / 179 | `images/04-neakordicki-c/zadatak-4-357-8-b.png` | pending independent review | Continuation of8, one soprano row; no repeated number; final barline. |
| zadatak 9 | 357 / 179 | `images/04-neakordicki-c/zadatak-4-357-9.png` | pending independent review | Four bass rows with all figures, accidentals and parentheses. |
| zadatak 10 | 357 / 179 | `images/04-neakordicki-c/zadatak-4-357-10.png` | pending independent review | Three bass rows with all stacked figures and parentheses. |
| zadatak 11 (početak) | 357 / 179 | `images/04-neakordicki-c/zadatak-4-357-11-a.png` | pending independent review | Opening bass row of11 with all figures; number here, continuation on358. |
| zadatak 11 (nastavak) | 358 / 180 | `images/04-neakordicki-c/zadatak-4-358-11-b.png` | pending independent review | Two bass rows finishing11, all stacked figures and final barline; no repeated number. |
| zadatak 12 | 358 / 180 | `images/04-neakordicki-c/zadatak-4-358-12.png` | pending independent review | Three soprano rows with all accidentals and long slurs. |
| zadatak 13 | 358 / 180 | `images/04-neakordicki-c/zadatak-4-358-13.png` | pending independent review | Two soprano rows, very low note, fermata and final barline. |
| zadatak 14 | 358 / 180 | `images/04-neakordicki-c/zadatak-4-358-14.png` | pending independent review | Two soprano rows with all accidentals, lower notes and final barline. |
| realizacija zadatka 9 | 359 / 180 | `images/04-neakordicki-c/zadatak-4-359-9-realizacija-coverage-recrop.png` | pending independent review | Realization of9; complete printed title and three grand-staff systems, including lowest figures. |
| realizacija zadatka 12 | 360 / 181 | `images/04-neakordicki-c/zadatak-4-360-12-realizacija-coverage-recrop.png` | pending independent review | Realization of12; complete printed title and four grand-staff systems, including lowest bass stem. |
| 4.164 | 361 / 181 | `images/04-neakordicki-c/primjer-4-164.png` | pending independent review | All variants a–d, stars and very lowest bass beam in c. |
| 4.165 | 361 / 181 | `images/04-neakordicki-c/primjer-4-165.png` | pending independent review | Complete Beethoven G-major op.49 no.2 attribution, both stars, low bass beams and printed open right endpoints. |
| 4.166 | 361 / 181 | `images/04-neakordicki-c/primjer-4-166.png` | pending independent review | Both stars and lower stems; no separate work attribution printed. |
| 4.167 | 362 / 182 | `images/04-neakordicki-c/primjer-4-167.png` | pending independent review | Complete Beethoven A-major op.2 no.2 attribution, *) marker, lowest bass beams/dots; explanation separately transcribed. |
| 4.168 | 362 / 182 | `images/04-neakordicki-c/primjer-4-168.png` | pending independent review | Star above soprano, lower flag and final barline. |
| 4.169 | 362 / 182 | `images/04-neakordicki-c/primjer-4-169.png` | pending independent review | Complete Beethoven c-minor op.111 attribution, all three *) markers and lowest bass beams. Related explanatory footnote touches the lowest-beam height: unavoidable partial footnote ink retained; cleanup_required/layout_conflict, no retouch. |
| 4.170 | 362 / 182 | `images/04-neakordicki-c/primjer-4-170.png` | pending independent review | Variants a/b, stars, all accidentals and lowest bass stem. |
| 4.171 | 363 / 182 | `images/04-neakordicki-c/primjer-4-171.png` | pending independent review | Complete Chopin Prelude op.28 no.2 attribution, star, arpeggiation, bottom fermata and very low bass note; narrow right margin is constrained by adjacent 4.172. |
| 4.172 | 363 / 182 | `images/04-neakordicki-c/primjer-4-172.png` | pending independent review | Complete Chopin Mazurka op.24 no.2 attribution, star and bass stems; left edge is the natural separation from 4.171. |
| 4.173 | 363 / 182 | `images/04-neakordicki-c/primjer-4-173.png` | pending independent review | Complete Schumann Carnaval op.9 attribution, stars, high ledger notes and lowest bass note. Source abrasion interrupts the right final barline; source_damage retained, not repaired. |
| 4.174 | 363 / 182 | `images/04-neakordicki-c/primjer-4-174.png` | pending independent review | Complete Chopin Prelude op.28 no.12 attribution, highest slur and lowest bass notes/staccato dots. |
| 4.175 | 364 / 183 | `images/04-neakordicki-c/primjer-4-175.png` | pending independent review | Complete Chopin Mazurka op.24 no.4 attribution, both single-star and double-star markers, lower staccato dot; explanations separately transcribed. |
| 4.176 | 364 / 183 | `images/04-neakordicki-c/primjer-4-176.png` | pending independent review | Complete J.S.Bach Koral br.8 attribution, fermatas above and below; narrow right separation from 4.177. |
| 4.177 | 364 / 183 | `images/04-neakordicki-c/primjer-4-177.png` | pending independent review | Separate unattributed numbered example; all accidentals and final barline. |
| zadatak 1 | 364 / 183 | `images/04-neakordicki-c/zadatak-4-364-1.png` | pending independent review | Two bass rows, printed1 and final barline. |
| zadatak 2 (početak) | 364 / 183 | `images/04-neakordicki-c/zadatak-4-364-2-a.png` | pending independent review | First bass row of2; printed number here, continuation on365. |
| zadatak 2 (nastavak) | 365 / 183 | `images/04-neakordicki-c/zadatak-4-365-2-b.png` | pending independent review | Final bass row of2; no repeated number. |
| zadatak 3 | 365 / 183 | `images/04-neakordicki-c/zadatak-4-365-3.png` | pending independent review | Two soprano rows and all slurs. |
| zadatak 4 | 365 / 183 | `images/04-neakordicki-c/zadatak-4-365-4.png` | pending independent review | Two soprano rows, lower slur and final barline. |
| 4.178 (početak) | 366 / 184 | `images/04-neakordicki-c/primjer-4-178-a.png` | pending independent review | First system and Chopin op.28 no.8 attribution on366; next two systems on367. Number only on366. Handwritten circles around bass notes preserved: cleanup_required/handwriting, no erasure. |
| 4.178 (nastavak) | 367 / 184 | `images/04-neakordicki-c/primjer-4-178-b.png` | pending independent review | First system and Chopin op.28 no.8 attribution on366; next two systems on367. Number only on366. Handwritten circles around bass notes preserved: cleanup_required/handwriting, no erasure. |
| 4.179 | 367 / 184 | `images/04-neakordicki-c/primjer-4-179.png` | pending independent review | Complete Bach b-minor Prelude / Wohltemperiertes Klavier I dio attribution and printed open right endpoints. |
| 4.180 | 367 / 184 | `images/04-neakordicki-c/primjer-4-180.png` | pending independent review | Complete Chopin Mazurka op.67 no.3 attribution, ornament, low bass stems and final barline; following prose excluded. |
| 4.181 | 368 / 185 | `images/04-neakordicki-c/primjer-4-181.png` | pending independent review | Complete Grieg Lirski komadi X,60 attribution and both grand-staff systems including low ledger notes. |
| 4.182 | 368 / 185 | `images/04-neakordicki-c/primjer-4-182-a.png` | pending independent review | Chopin Balada op.38 title and first system on368; one continuation system on369. Number/title occur only on368. Preserve long lower slurs and printed open endpoints. |
| 4.182 (nastavak) | 369 / 185 | `images/04-neakordicki-c/primjer-4-182-b.png` | pending independent review | Chopin Balada op.38 title and first system on368; one continuation system on369. Number/title occur only on368. Preserve long lower slurs and printed open endpoints. |
| 4.183 | 369 / 185 | `images/04-neakordicki-c/primjer-4-183.png` | pending independent review | Complete Chopin Mazurka op.17 no.4 attribution, ornaments, lower flags and final barline. |
| 4.184 | 369 / 185 | `images/04-neakordicki-c/primjer-4-184.png` | pending independent review | Complete Beethoven Sonata op.111 attribution, lowest left bass note, lowest right beam/slur and printed open endpoints; printer signature excluded. |
| 4.185 | 370 / 186 | `images/04-neakordicki-c/primjer-4-185.png` | pending independent review | Complete Schumann Albumblatter op.124,13 attribution and *) marker, lowest slur; explanation separately transcribed. |
| 4.186 | 370 / 186 | `images/04-neakordicki-c/primjer-4-186.png` | pending independent review | Complete R.Strauss Don Quichotte attribution and both three-staff systems, including lowest bass note and slurs. |
| 4.187 | 370 / 186 | `images/04-neakordicki-c/primjer-4-187.png` | pending independent review | Complete Schumann Papillons op.2 attribution and very lowest bass ledger notes. |
| zadatak 1 | 371 / 186 | `images/04-neakordicki-c/zadatak-4-371-1.png` | pending independent review | Three complete grand-staff systems, printed1 and lowest ties. |
| zadatak 2 (početak) | 371 / 186 | `images/04-neakordicki-c/zadatak-4-371-2-a.png` | pending independent review | Complete Allegro, ma non troppo instruction; two opening grand-staff systems of2. Number only here, continuation on372. |
| zadatak 2 (nastavak) | 372 / 187 | `images/04-neakordicki-c/zadatak-4-372-2-b.png` | pending independent review | Two grand-staff systems finishing2, no repeated number; lowest ties and final barline. |
| zadatak 3 | 372 / 187 | `images/04-neakordicki-c/zadatak-4-372-3.png` | pending independent review | Three grand-staff systems of3; number, lowest ties and final barline. |
| zadatak 4 | 373 / 187 | `images/04-neakordicki-c/zadatak-4-373-4.png` | pending independent review | Complete Andantino grazioso instruction and four grand-staff systems of4, lowest bass ties and final barline. |
| zadatak 5 (početak) | 373 / 187 | `images/04-neakordicki-c/zadatak-4-373-5-a.png` | pending independent review | Opening grand-staff system of5; printed number here, continuation on374. |
| zadatak 5 (nastavak) | 374 / 188 | `images/04-neakordicki-c/zadatak-4-374-5-b.png` | pending independent review | Four grand-staff systems finishing5; no repeated number, lowest ties and final barline. |
| realizacija zadatka 1 (početak) | 374 / 188 | `images/04-neakordicki-c/zadatak-4-374-1-realizacija-a-coverage-recrop.png` | pending independent review | Realization of1; complete printed title and first grand-staff system, continuation on375. |
| realizacija zadatka 1 (nastavak) | 375 / 188 | `images/04-neakordicki-c/zadatak-4-375-1-realizacija-b.png` | pending independent review | Three grand-staff systems finishing realization1; no repeated title/number, lowest ties and final barline. |
| 4.188 | 376 / 189 | `images/04-neakordicki-c/primjer-4-188.png` | pending independent review | Complete Beethoven f-minor op.57 attribution, dashed arrows, very low bass notes and lower/right slurs. |
| 4.189 | 377 / 189 | `images/04-neakordicki-c/primjer-4-189.png` | pending independent review | Complete Beethoven D-major op.10 no.3 attribution and both systems including lowest beam/accidental; printed open endpoints retained. |
| 4.190 | 377 / 189 | `images/04-neakordicki-c/primjer-4-190.png` | pending independent review | Complete Beethoven A-major op.2 no.2 attribution and both systems, star, low arpeggiations and bass stems; no separate explanation printed here. |
| 4.191 | 378 / 190 | `images/04-neakordicki-c/primjer-4-191.png` | pending independent review | Complete Beethoven Es-major op.81a attribution, both clef changes, lowest bass ledger note and bottom slur; following prose excluded. |
| 4.192 | 378 / 190 | `images/04-neakordicki-c/primjer-4-192-coverage-recrop.png` | pending independent review | Complete Beethoven Symphony9 attribution, trill, three staves, lowest bass ledger notes and long lower slurs. Prose descenders overlap attribution height; following Ravel attribution touches lowest-slur height. cleanup_required/layout_conflict; no clean rectangular separation at both edges, no clipping to conceal conflict. |
| 4.193 | 378 / 190 | `images/04-neakordicki-c/primjer-4-193.png` | pending independent review | Complete Ravel Rapsodie espagnole attribution, printed number, highest slurs and lowest bass ledger notes. Top includes unavoidable preceding 4.192 slur fragments: cleanup_required/layout_conflict. Open right endpoints are the actual end of this excerpt, not a lost final barline. Parent has checked379: chapter5 begins there, with no4.193 continuation;379 was not opened by this worker. |
