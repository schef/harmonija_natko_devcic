# M10 — integration hand-off

Assigned scope: **printed pages 349–378 (30 pages), PDF pages 175–190**. Work stops at printed page 378. Exactly one integration worker; no delegation, model subprocess, API, GUI, image modification, global-tracker edit, commit, or push.

## Outcome and holds

All five verified text shards and all 86 identity/page slots are integrated in [the chapter](../../../chapters/04-neakordicki-c.md). **80 independent_pass / five cleanup_required / one source_damage**. M10 is **not ready for final completion**: six visual slots remain unapproved. Integration is ready for parent inspection with those holds explicitly preserved, not for milestone completion or notation certification.

- **4.169, p. 362:** foreign footnote-character fragments at bottom; required bass beams share their vertical band. No safe full-content rectangular replacement verified.
- **4.178 opening, p. 366; continuation, p. 367:** handwritten circles around bass notes. Both remain separate provisional slots; marked notation is uncertified. No safe replacement verified without losing notation.
- **4.192, p. 378:** recrop restored the complete Beethoven Symphony 9 title but retains preceding prose fragments at top; lowest slur meets the next attribution's height band. No safe replacement verified.
- **4.193, p. 378:** foreign lower slurs of 4.192 above/touching the Ravel attribution. Printed open endpoints are not crop damage. Do not invent a final barline or a page-379 continuation. The earlier text-shard boundary comment tentatively mentioned checking a continuation; the later independent review resolves that uncertainty without altering the preserved transcription.
- **4.173, p. 363:** **SOURCE DAMAGE / NOTATION UNCERTAIN / UNAPPROVED**. Abrasion interrupts the right final barline; faint/damaged notes must not be inferred. Independent crop PASS is retained only as `crop_review_status`, never as notation approval. Linked, not embedded.

No unreadable prose is reported by the text reviewers. Their full text, headings, instructions, asterisk explanations, attributions, source markers and continuation comments are retained. For 4.151, the supplied verified paragraph joins printed `škol-/skih` across an inserted example and places the example after the complete paragraph; that documented arrangement is preserved. Other interrupted sentences and all paired visual continuations remain in shard order. No wording corrections beyond the verified inputs were made.

## Files created

1. [chapters/04-neakordicki-c.md](../../../chapters/04-neakordicki-c.md)
2. [images/04-neakordicki-c/REVIEW.md](../../../images/04-neakordicki-c/REVIEW.md)
3. [images-integrated.json](images-integrated.json) — 86 records, final statuses and original source provenance.
4. This report, [INTEGRATION.md](INTEGRATION.md).

Existing chapter content was absent at integration start. Other pre-existing repository changes are untouched. Raw manifests, source text shards, source pages, images and MILESTONES.md were not edited.

## Validation

- Exactly 86 one-to-one identity/page matches: shard counts **7 + 13 + 18 + 27 + 21**; order preserved.
- All 30 printed pages have verified text-review records; every page/PDF pair agrees with `sources/index.json` (including 350 → 176 and 378 → 190).
- Full-text round trip PASS for every shard: stripping only generated visual blocks restores each input byte-for-byte. Thus all headings, footnotes/explanations, composer/work text, source markers, continuation comments and the documented 4.151 paragraph arrangement survive unchanged.
- Every slot has a printed-page/PDF caption, original-page link and MuseScore placeholder. Exactly 80 image embeds and six ordinary crop links. No blocked slot is embedded.
- All 86 images match their original source rectangles pixel-for-pixel (RGB and dimensions); no borders, painting, reconstruction or generated pixels. SHA-256 and rectangle retained per record. This test is provenance only, not approval of notation.
- Local Markdown links checked relative to each containing Markdown file. Chapter links use `../images/...` and `../sources/...`; JSON keeps repository-relative provenance paths.
- Passed realization-title recrops retained for printed pages 359, 360 and 374; failed 4.192 title-restoration recrop retained only as a provisional link. No new recrops or image edits.
- The chapter ends at printed 378; no page 379 work or invented 4.193 continuation/barline.

## Input audit trail

- [text-349-350.md](text-349-350.md) and [text-349-350-review.json](text-349-350-review.json): 7 visual slots; text SHA-256 `6811f2c214d09bf725808dbcad67e94368059d98647f1acc23b5e7d809b303a1`.
- [text-351-354.md](text-351-354.md) and [text-351-354-review.json](text-351-354-review.json): 13 visual slots; text SHA-256 `5fd8f166670d9daa56046c8eb4d9cddaff0d268eb531524520be672e8d87aff4`.
- [text-355-358.md](text-355-358.md) and [text-355-358-review.json](text-355-358-review.json): 18 visual slots; text SHA-256 `c2a2a31e9d0d08f3da0a1763cd193b487f8db9f54ba18d0e3981c24d8b17ace9`.
- [text-359-368.md](text-359-368.md) and [text-359-368-review.json](text-359-368-review.json): 27 visual slots; text SHA-256 `978979bd4dceceb8f849ffc2aeb2c8999cb68eab695ba411bd1dfa2b4db76b99`.
- [text-369-378.md](text-369-378.md) and [text-369-378-review.json](text-369-378-review.json): 21 visual slots; text SHA-256 `bb3e2600e147584f9dbab2ed89ab4e96eb7644ee1f6a9f8ea22f357e04d82852`.

- [images-complete.json](images-complete.json) supplies identities, current source rectangles and passed extractor recrops.
- [visual-review.json](visual-review.json) supplies every independent crop decision and hold reason.
- [Image review ledger](../../../images/04-neakordicki-c/REVIEW.md) records the independent reason for each slot.

## Complete 86-slot map

| # | Identity / slot | Printed | PDF | Final status | Crop decision | Source crop |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `primjer-4-143` — 4.143 | 349 | 175 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-143.png) |
| 2 | `primjer-4-144` — 4.144 | 349 | 175 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-144.png) |
| 3 | `primjer-4-145` — 4.145 | 349 | 175 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-145.png) |
| 4 | `primjer-4-146` — 4.146 | 350 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-146.png) |
| 5 | `primjer-4-147` — 4.147 | 350 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-147.png) |
| 6 | `primjer-4-148` — 4.148 | 350 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-148.png) |
| 7 | `primjer-4-149` — 4.149 | 350 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-149.png) |
| 8 | `primjer-4-150` — 4.150 | 351 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-150.png) |
| 9 | `primjer-4-151` — 4.151 | 351 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-151.png) |
| 10 | `primjer-4-152-a` — 4.152 a–c | 351 | 176 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-152-a.png) |
| 11 | `primjer-4-152-b` — 4.152 d–g (nastavak) | 352 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-152-b.png) |
| 12 | `primjer-4-153` — 4.153 | 352 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-153.png) |
| 13 | `primjer-4-154` — 4.154 | 352 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-154.png) |
| 14 | `primjer-4-155` — 4.155 | 352 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-155.png) |
| 15 | `primjer-4-156` — 4.156 | 352 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-156.png) |
| 16 | `primjer-4-157` — 4.157 | 353 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-157.png) |
| 17 | `primjer-4-158` — 4.158 | 353 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-158.png) |
| 18 | `primjer-4-159` — 4.159 | 353 | 177 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-159.png) |
| 19 | `primjer-4-160` — 4.160 | 354 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-160.png) |
| 20 | `primjer-4-161` — 4.161 | 354 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-161.png) |
| 21 | `primjer-4-162` — 4.162 | 355 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-162.png) |
| 22 | `primjer-4-163` — 4.163 | 355 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-163.png) |
| 23 | `zadatak-4-355-1` — zadatak 1 | 355 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-355-1.png) |
| 24 | `zadatak-4-355-2` — zadatak 2 | 355 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-355-2.png) |
| 25 | `zadatak-4-355-3` — zadatak 3 | 355 | 178 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-355-3.png) |
| 26 | `zadatak-4-356-4` — zadatak 4 | 356 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-356-4.png) |
| 27 | `zadatak-4-356-5` — zadatak 5 | 356 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-356-5.png) |
| 28 | `zadatak-4-356-6` — zadatak 6 | 356 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-356-6.png) |
| 29 | `zadatak-4-356-7` — zadatak 7 | 356 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-356-7.png) |
| 30 | `zadatak-4-356-8-a` — zadatak 8 (početak) | 356 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-356-8-a.png) |
| 31 | `zadatak-4-357-8-b` — zadatak 8 (nastavak) | 357 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-357-8-b.png) |
| 32 | `zadatak-4-357-9` — zadatak 9 | 357 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-357-9.png) |
| 33 | `zadatak-4-357-10` — zadatak 10 | 357 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-357-10.png) |
| 34 | `zadatak-4-357-11-a` — zadatak 11 (početak) | 357 | 179 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-357-11-a.png) |
| 35 | `zadatak-4-358-11-b` — zadatak 11 (nastavak) | 358 | 180 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-358-11-b.png) |
| 36 | `zadatak-4-358-12` — zadatak 12 | 358 | 180 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-358-12.png) |
| 37 | `zadatak-4-358-13` — zadatak 13 | 358 | 180 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-358-13.png) |
| 38 | `zadatak-4-358-14` — zadatak 14 | 358 | 180 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-358-14.png) |
| 39 | `zadatak-4-359-9-realizacija` — realizacija zadatka 9 | 359 | 180 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-359-9-realizacija-coverage-recrop.png) |
| 40 | `zadatak-4-360-12-realizacija` — realizacija zadatka 12 | 360 | 181 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-360-12-realizacija-coverage-recrop.png) |
| 41 | `primjer-4-164` — 4.164 | 361 | 181 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-164.png) |
| 42 | `primjer-4-165` — 4.165 | 361 | 181 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-165.png) |
| 43 | `primjer-4-166` — 4.166 | 361 | 181 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-166.png) |
| 44 | `primjer-4-167` — 4.167 | 362 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-167.png) |
| 45 | `primjer-4-168` — 4.168 | 362 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-168.png) |
| 46 | `primjer-4-169` — 4.169 | 362 | 182 | cleanup_required; approved=false | RECROP_REQUIRED | [PNG](../../../images/04-neakordicki-c/primjer-4-169.png) |
| 47 | `primjer-4-170` — 4.170 | 362 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-170.png) |
| 48 | `primjer-4-171` — 4.171 | 363 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-171.png) |
| 49 | `primjer-4-172` — 4.172 | 363 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-172.png) |
| 50 | `primjer-4-173` — 4.173 | 363 | 182 | source_damage; approved=false | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-173.png) |
| 51 | `primjer-4-174` — 4.174 | 363 | 182 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-174.png) |
| 52 | `primjer-4-175` — 4.175 | 364 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-175.png) |
| 53 | `primjer-4-176` — 4.176 | 364 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-176.png) |
| 54 | `primjer-4-177` — 4.177 | 364 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-177.png) |
| 55 | `zadatak-4-364-1` — zadatak 1 | 364 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-364-1.png) |
| 56 | `zadatak-4-364-2-a` — zadatak 2 (početak) | 364 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-364-2-a.png) |
| 57 | `zadatak-4-365-2-b` — zadatak 2 (nastavak) | 365 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-365-2-b.png) |
| 58 | `zadatak-4-365-3` — zadatak 3 | 365 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-365-3.png) |
| 59 | `zadatak-4-365-4` — zadatak 4 | 365 | 183 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-365-4.png) |
| 60 | `primjer-4-178-a` — 4.178 (početak) | 366 | 184 | cleanup_required; approved=false | RECROP_REQUIRED | [PNG](../../../images/04-neakordicki-c/primjer-4-178-a.png) |
| 61 | `primjer-4-178-b` — 4.178 (nastavak) | 367 | 184 | cleanup_required; approved=false | RECROP_REQUIRED | [PNG](../../../images/04-neakordicki-c/primjer-4-178-b.png) |
| 62 | `primjer-4-179` — 4.179 | 367 | 184 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-179.png) |
| 63 | `primjer-4-180` — 4.180 | 367 | 184 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-180.png) |
| 64 | `primjer-4-181` — 4.181 | 368 | 185 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-181.png) |
| 65 | `primjer-4-182-a` — 4.182 | 368 | 185 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-182-a.png) |
| 66 | `primjer-4-182-b` — 4.182 (nastavak) | 369 | 185 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-182-b.png) |
| 67 | `primjer-4-183` — 4.183 | 369 | 185 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-183.png) |
| 68 | `primjer-4-184` — 4.184 | 369 | 185 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-184.png) |
| 69 | `primjer-4-185` — 4.185 | 370 | 186 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-185.png) |
| 70 | `primjer-4-186` — 4.186 | 370 | 186 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-186.png) |
| 71 | `primjer-4-187` — 4.187 | 370 | 186 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-187.png) |
| 72 | `zadatak-4-371-1` — zadatak 1 | 371 | 186 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-371-1.png) |
| 73 | `zadatak-4-371-2-a` — zadatak 2 (početak) | 371 | 186 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-371-2-a.png) |
| 74 | `zadatak-4-372-2-b` — zadatak 2 (nastavak) | 372 | 187 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-372-2-b.png) |
| 75 | `zadatak-4-372-3` — zadatak 3 | 372 | 187 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-372-3.png) |
| 76 | `zadatak-4-373-4` — zadatak 4 | 373 | 187 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-373-4.png) |
| 77 | `zadatak-4-373-5-a` — zadatak 5 (početak) | 373 | 187 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-373-5-a.png) |
| 78 | `zadatak-4-374-5-b` — zadatak 5 (nastavak) | 374 | 188 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-374-5-b.png) |
| 79 | `zadatak-4-374-1-realizacija-a` — realizacija zadatka 1 (početak) | 374 | 188 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-374-1-realizacija-a-coverage-recrop.png) |
| 80 | `zadatak-4-375-1-realizacija-b` — realizacija zadatka 1 (nastavak) | 375 | 188 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/zadatak-4-375-1-realizacija-b.png) |
| 81 | `primjer-4-188` — 4.188 | 376 | 189 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-188.png) |
| 82 | `primjer-4-189` — 4.189 | 377 | 189 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-189.png) |
| 83 | `primjer-4-190` — 4.190 | 377 | 189 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-190.png) |
| 84 | `primjer-4-191` — 4.191 | 378 | 190 | independent_pass; approved=true | PASS | [PNG](../../../images/04-neakordicki-c/primjer-4-191.png) |
| 85 | `primjer-4-192` — 4.192 | 378 | 190 | cleanup_required; approved=false | RECROP_REQUIRED | [PNG](../../../images/04-neakordicki-c/primjer-4-192-coverage-recrop.png) |
| 86 | `primjer-4-193` — 4.193 | 378 | 190 | cleanup_required; approved=false | RECROP_REQUIRED | [PNG](../../../images/04-neakordicki-c/primjer-4-193.png) |
