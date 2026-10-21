# Handback: Steps 1 and 2

21 October 2026. Every decision, with its time and reason, is in `notes/decisions.md`. This note sums them up.

## What I did

**Step 1: picking the countries**

- **Downloaded ETO's dataset.** This is the September 2026 release, pinned to an exact GitHub commit, with checksums recorded. It is CC BY-NC licensed, so the raw files are committed.
- **Checked for gaps.** ETO has no HBM data and no share for leading-edge fabs or advanced-packaging capacity. Most materials list countries but give no share numbers.
- **Drafted the mapping of all 126 ETO inputs** onto the five steps (`notes/eto_step_mapping.csv`), plus the screening rules. Andrew approved both before the screen ran.
- **Added the second sources Andrew approved:**
  - HBM: TrendForce, 2025.
  - Leading-edge fabs: SIA/BCG, 2022 data.
  - The CSET 2021 report was approved for materials but turned out to have no country shares for them (see open questions).
- **Ran the screen** (`src/screen.py`) at 40%, 25% and 60%. It writes `data/processed/shares.csv`, `results/screen_*.csv`, `results/country_set.md`, `results/chokepoint_rows.csv` and `results/could_not_screen.csv`.

**Step 2: setting up the variables**

- Drafted the anchors: `notes/variable_anchors.md`.
- Drafted the disagreement rule: `notes/disagreement_rule.md`.
- Built the four blank scoring sheets in `scoring/`, using `src/make_scoring_sheets.py`. It won't overwrite a sheet that already has scores.
- Wrote `src/compare_scores.py`, with 10 tests on made-up sheets in `tests/fixtures/`. All tests pass.
- I **did not** score anything, did not tick the three "Agree…" tasks, and did not start Step 3.

## The country set (40% threshold, US and China removed)

| Country | Inputs passed | What gets it in (largest shares) |
| --- | --- | --- |
| Japan | 22 | Crystal machining tools (99.7%), resist processing tools (95.2%), dicing tools (95%), wafer and photomask handlers, test tools. Also wafers (56%) and photomasks (53%), but those are 2019 figures. Equipment figures are 2025. |
| Netherlands | 6 | ASML: EUV lithography (100%), ArF immersion (99.3%), ArF dry (94.4%) and KrF lithography (66%), plus overlay metrology (47.9%). ASM International: atomic layer deposition (54.5%). All 2025. |
| Singapore | 4 | Kulicke & Soffa and ASM Pacific: bonders and integrated assembly tools (2025). |
| Austria | 3 | EV Group: wafer bonding (47.9%) and imprint lithography (90.8%). IMS Nanofabrication: e-beam mask writers (46.6%). All 2025. |
| Germany | 3 | SUSS MicroTec: mask aligners (82.2%). Also two tiny markets: crystal-growing furnaces (2022) and manual wire bonders. |
| South Korea | 2 | HBM memory (81%, a 2025 projection from TrendForce) and burn-in test tools (61.4%, 2025). |
| Sweden | 1 | Mycronic: laser mask writers (70.7%, 2025). |
| Taiwan | 1 | Leading-edge (<10nm) logic capacity (69%, **2022, by fab location**, from SIA/BCG). |

- **Same countries at 25% and 60%.** Only the number of inputs each country holds changes. For example, Japan holds 27 at 25% and 12 at 60%. The full table is in `results/country_set.md`.
- **Against the expected set** (Netherlands, Japan, South Korea, Taiwan, Germany), all five are in, plus **Austria, Singapore and Sweden**.
  - Why: ETO's 2025 equipment data splits tools into narrow niches, and small specialist firms dominate some of them.
  - I haven't forced the result. Whether these three belong in a coalition story is your call.
- **42 chokepoint rows:**
  - 38 equipment, 2 materials, 1 HBM and 1 leading-edge fabrication.
  - 7 of the 42 are flagged as small markets (under $100m). No country is in the set *only* because of small markets.
- **US and China, for context:** the US passes on 27 inputs and China on 1 (miscellaneous dry etch tools, 61.1%).

## Choices I made, and why (details in `notes/decisions.md`)

1. **Only the narrowest ETO inputs are screened**, not categories such as "Lithography tools". This follows the brief, and it avoids counting the same chokepoint twice.
2. **ETO's country-level shares are used as given.** I never add up firm shares myself. The one exception is HBM, where the approved rule was to add up TrendForce's firm shares by HQ country.
3. **Inputs with no share numbers are listed as "could not screen"**, not guessed.
4. **"Various countries" and "Europe" can't pass**, since they aren't countries.
5. **Four non-IC and discrete-device tool inputs are out of scope**, and core IP is out along with EDA. Andrew approved this.
6. **Advanced-packaging tools count as equipment.** Andrew chose this. The advanced packaging step itself stays **qualitative**, because no approved source exists.
7. **Small markets are kept but flagged.** Andrew chose this.
8. **Raw files with unclear licences are gitignored:** the SIA/BCG PDF and the TrendForce web page. Their URLs and checksums are logged.
9. **Kappa uses linear weights** (half credit for being one level apart). Quadratic weights would flatter agreement when there are only three levels.
10. **The anchors' concentration cut-offs (25% and 60%) match the screen's thresholds.**

## Open questions for Andrew (and Ayodele)

1. **Materials are mostly unscreened.**
   - Neither ETO nor the CSET report gives country shares for photoresists, gases, wet chemicals, CMP and deposition materials, or any packaging material. That is 11 inputs in total.
   - Japan's hold here (ETO: "Japanese firms are the leading producers" of photoresists) is therefore missing from the rows.
   - Do you want a further source for photoresists, or should we state this as a limit?
2. **42 rows is a lot to score in about 1.5 hours.** Each of you would make 252 judgments. Options:
   - score all 42
   - drop the 7 small-market rows
   - score at country-and-step level instead

   This should be decided **before** anyone scores. Changing it afterwards would be a rule change made after seeing results.
3. **Taiwan is in the set only because of the second source.**
   - Using ETO alone, Taiwan passes on nothing, because ETO's fab figure covers all nodes and is measured by site.
   - The Taiwan row is 2022 data, by fab location, while most other rows are 2025, by HQ.
4. **HBM is a projection.** TrendForce made it in mid-2025 for the full year. Other trackers differ, but all put the two Korean firms well above 60% combined.
5. **Approve or change the drafts:**
   - the anchors
   - the disagreement rule
   - the "target" wording on the cases sheet (e.g. CIPEC's target as "copper-importing countries")

   After that, you can tick the three "Agree…" tasks.
6. **Germany's strengths are only partly captured.** Zeiss's optics for ASML are not a separate ETO input. Wafers are 2019 data, and Germany holds only 14% of them.

## Things in the data that looked off

- **IMS Nanofabrication counts as Austria.**
  - ETO's rule is to use the ultimate parent's HQ, and as far as I know Intel still holds a majority stake (public reports from 2023). Worth checking.
  - Austria would still pass via EV Group either way.
- **Kulicke & Soffa counts as Singapore.** Its HQ is in Singapore, but it is incorporated in the US.
  - If it were counted as the US, Singapore's remaining passes would all be small markets.
  - I've used ETO as given, which is the rule.
- **Crystal-growing furnaces:** Germany has 100%, but that rests on one firm. It is 2022 data and a $44m market. ETO lists a Chinese firm with no share.
- **China's only pass is "Misc. dry etch tools" (61.1%, 2025).** It's a catch-all category ($420m), so be careful reading meaning into it.
- **ETO's stage-level shares for fabs and packaging are by site location**, unlike everything else. I did not screen them.
- **Years are mixed.** Equipment and HBM are 2025, the fab figure is 2022, and wafers and photomasks are 2019. Every row shows its year.
- **ETO's GitHub repo was renamed** (`eto-supply-chain` became `eto-chip-explorer`). The pinned commit (13 Oct) is later than the 15 Sep release, but it only changed one link in `sequence.csv`, with no share data.

## Housekeeping

- **I deleted one file without asking:** my own wrong download of a one-page CSET brief. It was never committed or used, and the brief says to ask before deleting, so I'm flagging it.
- **`notes/variable_anchors.md` landed in the Step 1 commit** by accident. Its content is unaffected.

## How to rerun

```
python src/screen.py                  # rebuild shares, screens, country set, chokepoint rows
python src/make_scoring_sheets.py     # rebuild blank sheets (skips any sheet with scores)
python src/compare_scores.py cases    # agreement report, once both case sheets are scored
python -m pytest tests                # tests on made-up scores
```
