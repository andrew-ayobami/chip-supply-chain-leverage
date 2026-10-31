# Decision log

Times are local (UTC+1). Each entry says what was decided and why.
Status tags: **FINAL**, **DRAFT: needs Andrew's OK**, **OPEN QUESTION**.

---

## 2026-10-21 07:04 · Main dataset and version · FINAL

- **Dataset:** Emerging Technology Observatory (ETO), *Advanced Semiconductor Supply Chain Dataset*, **September 2026 release** (ETO changelog dated 15 Sep 2026).
- **Where from:** the `data/` folder of the GitHub repo `georgetown-cset/eto-chip-explorer` (the old `eto-supply-chain` URL now points there). It is pinned to commit `9a4e1b128c836cb3bdf065a06a3fc03397e00ff0` (13 Oct 2026), the latest commit that touched `data/`. That commit only changed `sequence.csv` (how resist-processing tools link to other inputs). The share data is the September 2026 release.
- **Downloaded:** 2026-10-21 06:04 UTC, into `data/raw/eto_supply_chain_2026-09/`. Files are kept untouched.
- **SHA-256 checksums**, so anyone can check the files are unchanged:
  - `inputs.csv` 0c0a3418a80a6e7edea5c63c98c4829d6d6b613cd648c30905fe22f70dbbd17b
  - `providers.csv` c529479afe7d35afa750729bf6dd45227a375568c02b8cf401aad239360a13e4
  - `provision.csv` d94267801a73745e40bfaee8a30341adb37a168a8a0f28bf5d03f78e05f6c16f
  - `sequence.csv` bffa57c370bc6b027dea318cda5f65b023eb08eb690e3e7dfaad6a9d61449174
  - `stages.csv` 87717f108a0fdc874d7a0a261d35c3450d46ce8042eba53e957b9a03a24786ce
- **Citation, in the form ETO asks for:** Emerging Technology Observatory, *Semiconductor Supply Chain Dataset* (September 2026 release), https://eto.tech/dataset-docs/chipexplorer
- **Why this source:** the plan names it, it is free, and its documentation states each figure's year and source.

## 2026-10-21 07:05 · Licence, and whether to commit the raw files · FINAL

- The repo's `LICENSE.md` puts the data under **Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**. A copy is saved next to the data. ETO's dataset page also points to its general terms of use (https://eto.tech/tou).
- This project is non-commercial research, and we cite ETO, so we are allowed to share the files. The licence is clear, so the raw files **are committed**, and `data/raw/` is not gitignored.

## 2026-10-21 07:06 · How ETO assigns shares to countries · FINAL (a known limit)

- ETO's docs say a firm's share counts for the country where its **ultimate parent company has its headquarters**, not where it makes things. For example, TSMC's fabs in Arizona or Japan count as Taiwan.
- **Exception:** the stage-level figures for *Fabrication* and *Assembly, testing and packaging* (ETO `stages`, 2022, from SIA) measure **capacity by site location**. They are on a different basis from everything else, which is one reason they are not screened (see the screening rules below).
- Companies with 1% or less of every input were not given a country, so countries with many small suppliers may be under-counted.
- ETO rounds any share between 0% and 1% up to 1%, so an input's shares can add up to more than 100%. This doesn't matter at thresholds of 25% and above.

## 2026-10-21 07:07 · Gap check: what ETO does and does not cover · FINAL (the facts)

What I checked: every ETO input, whether it has rows at country level, whether those rows hold a number, and the year. At this point the only share values I had seen were three firm rows (ACM Research) in a file preview.

| Plan step | What ETO has | Usable for the screen? |
| --- | --- | --- |
| Manufacturing equipment | 66 narrow tool inputs with country shares. Almost all are **2025** (TechInsights data published 3 Jul 2026). Crystal-growing furnaces are 2022. Linear and discrete testing tools are 2021. | **Yes** |
| Materials | 13 narrow inputs. All **2019** (from CSET's 2021 report). Only **Wafers** (5 countries) and **Photomasks** (3 of 5 countries) have numbers. Photoresists, gases, wet chemicals, CMP materials, deposition materials and all packaging materials list countries and firms **with no share numbers**. | **Partly.** Most materials can't be screened from ETO. |
| Leading-edge fabrication | Only a stage-level share of **all** fab capacity (logic, memory and other), **by site location**, for **2022**. The text says advanced logic (<10nm) was "located solely in Taiwan and South Korea" in 2022, but gives no number. | **No** (wrong measure) |
| HBM memory | None. ETO's technical notes say "anything relating specifically to memory chips" was left out. It has memory *chip design* (out of scope) and memory *test tools* (equipment). | **No** |
| Advanced packaging | Eleven narrow **tool** inputs for advanced packaging, 2025. There is no share of advanced-packaging *services or capacity* (e.g. CoWoS). The stage-level ATP figure covers all packaging, by site, for 2022. | **Tools only** |
| (Out of scope) Raw minerals | Not in ETO at all. | n/a |

## 2026-10-21 07:10 · Proposed second sources, one per gap · DRAFT: needs Andrew's OK

I have **not** used any of these. Each is free to read. Note: I saw each source's headline numbers while searching for it, before writing the rules below.

| Gap | Proposed source | Year and basis | Flags |
| --- | --- | --- | --- |
| HBM memory | TrendForce News, "NVIDIA Reportedly Drives 27% of SK hynix Revenue in 1H25…", 18 Aug 2025, https://www.trendforce.com/news/2025/08/18/news-nvidia-reportedly-drives-27-of-sk-hynix-revenue-in-1h25-cementing-ai-chip-partnership | 2025, firm shares. Grouping by HQ: SK hynix and Samsung are South Korea, Micron is US. | A **projection** made mid-2025, not an actual. Other trackers differ (Counterpoint put SK hynix at 57% in Q3 2025), but every source I saw puts the two Korean firms well above 60% combined. |
| Leading-edge fabrication | SIA and BCG, *Emerging Resilience in the Semiconductor Supply Chain*, May 2024, https://www.bcg.com/publications/2024/emerging-resilience-in-semiconductor-supply-chain | 2022 baseline. Share of <10nm logic capacity **by location**. | Different basis from ETO (location, not HQ). For 2022 this changes little, because TSMC and Samsung made almost all advanced logic in Taiwan and Korea. The country figures I saw came from press coverage, so **they must be checked against the PDF**. |
| Advanced packaging | DIGITIMES Research, "Global capacity of CoWoS packaging" (2024), https://digitimes.com/news/a20240829RS400.html | Forecast for end-2025 monthly CoWoS and CoWoS-like capacity: TSMC >65k wafers, ASE/SPIL + Amkor 17k combined. | A **forecast**, and the full report is **paywalled** (the free summary gives those two numbers). A share would have to be **derived** by us from two figures, and it leaves out Intel and Samsung. This is the weakest of the three. If we can't find a better free source, we could keep the step qualitative and say so. |
| Materials (most have no numbers) | CSET, *The Semiconductor Supply Chain: Assessing National Competitiveness* (Jan 2021), https://cset.georgetown.edu/publication/the-semiconductor-supply-chain/ | 2019, the same underlying source as ETO's materials rows. | ETO's notes say it left these blank because the report splits them into sub-types. Using the sub-type shares would be our own step on top of ETO. **OPEN QUESTION:** fill these in from the report, or leave materials partly unscreened and say so? |

## 2026-10-21 07:10 · Draft mapping of ETO inputs onto the five plan steps · DRAFT: needs Andrew's OK

The full table, covering all 126 ETO inputs, is in `notes/eto_step_mapping.csv`. The script reads that file, so it is the working copy. A summary follows the rules below.

Judgment calls in the draft:

1. **Advanced-packaging tools go under *manufacturing equipment*** (subgroup "advanced-packaging tools"), not under *advanced packaging*. Reason: the leverage there sits with the toolmakers. The *advanced packaging* step means who can do CoWoS-class packaging, which needs the second source above. **Alternative:** put these tools under advanced packaging, so the step has some ETO data.
2. **Assembly and test tools count as manufacturing equipment** (back-end tools), including memory test tools.
3. **Four "non-IC" or discrete-device tool inputs are out of scope**: Other deposition tools (non-IC), Die attaching tools for non-IC, Auto ball bonders for non-IC, and Linear and discrete testing tools. Reason: they aren't used to make advanced logic chips or HBM.
4. **Core IP is out of scope** along with EDA, as part of chip design.
5. **Packaging materials** (substrates, lead frames and so on) go under *materials*. In practice almost none of them have numbers (see the gap check).
6. **Broad categories are not screened.** Examples are "Lithography tools", "Deposition tools" and "Etch and clean tools", which are sums of narrower inputs. Only the narrowest inputs are screened. This follows the brief ("screen EUV tools, not equipment as a whole") and avoids counting the same chokepoint twice.

## 2026-10-21 07:10 · Screening rules (set before seeing any results) · DRAFT: needs Andrew's OK with the mapping

1. **What counts as a share:** ETO's own **country-level** rows (`provider_type == country` in `provision.csv`), used as given. I do not add up firm shares myself.
2. **What gets screened:** inputs marked `screened = yes` in `notes/eto_step_mapping.csv`. These are the narrowest in-scope inputs.
3. **Pass rule:** a country passes for an input if its share is **≥ 40%** (40% exactly counts as a pass). The robustness runs use ≥ 25% and ≥ 60%, with nothing else changed.
4. **Not countries:** "Various countries" (ETO's catch-all for the rest of the world) and "Europe" can never pass. Their rows stay in `shares.csv` for context.
5. **Missing numbers:** if ETO lists a country for an input but gives no number, that input is **not screened**. It is listed in a "could not screen" table with the reason. I do not fill in or guess numbers.
6. **US and China:** kept in `shares.csv` and in the `screen_*.csv` files (marked `bargaining_party = yes`), but left out of the country set and `chokepoint_rows.csv`.
7. **Taiwan:** treated like any other country.
8. **Years:** every row keeps ETO's year. Equipment is mostly 2025 and materials are 2019. Results tables show the year next to each share, and years are never mixed silently.
9. **Very small markets (OPEN QUESTION):** some screened inputs are tiny, for example Ion milling tools ($0.4 million) and Manual wire bonders ($5 million). Holding 100% of a tiny market is not much leverage. My draft rule: **keep them, but flag any input with a global market under $100 million** in the results, so we can see whether any country is in the set *only* because of tiny markets. Andrew to decide whether to keep them flagged or drop them.
10. **Second-source steps** (HBM, leading-edge fab, advanced packaging): once Andrew approves a source, its rows go into `shares.csv` with their own source, year and basis, and face the same thresholds.

### Mapping summary

| Plan step | Subgroup | ETO inputs (year) | Screened? |
| --- | --- | --- | --- |
| manufacturing equipment | front-end fab tools | Crystal growing furnaces (2022), Crystal machining tools (2025), Wafer handlers (2025), Photomask handlers (2025), Ion implanters (2025), Imprint lithography (2025), EUV lithography tools (2025), ArF dry (DUV) lithography tools (2025), ArF immersion (DUV) lithography tools (2025), KrF (DUV) lithography tools (2025), i-line lithography tools (2025), Mask exposure systems - e-beam (2025), Mask exposure systems - laser beam (2025), Direct write systems (2025), Resist processing tools (2025), Plasma CVD tools (2025), Low-pressure CVD tools (2025), High-temperature CVD tools (2025), Atomic layer deposition tools (2025), Physical vapor deposition tools (2025), Rapid thermal processing tools (2025), Tube-based diffusion and deposition tools (2025), Electrochemical plating tools (2025), Plasma modification tools (2025), Wet etching and cleaning tools (2025), Conductor etching tools (2025), Insulator etching tools (2025), Misc. dry etch tools (2025), Ion milling tools (2025), Dry stripping tools (2025), Dry clean tools (2025), Photomask inspection and repair tools (2025), Process monitoring tools (2025), Film, stack, and shape metrology tools (2025), Critical dimensions metrology tools (2025), Defect inspection tools (2025), Overlay metrology tools (2025), E-beam metrology tools (2025), Defect review stations (2025), CMP tools (2025), Mask aligners (2025) | yes |
| manufacturing equipment | advanced-packaging tools | Wafer bonding and aligning tools (2025), Inspection tools (adv. pkg.) (2025), Dry etching tools (adv. pkg.) (2025), CVD tools (adv. pkg.) (2025), PVD tools (adv. pkg.) (2025), Spin-on deposition tools (adv. pkg.) (2025), ECP tools (adv. pkg.) (2025), Resist processing tools (adv. pkg.) (2025), CMP tools (adv. pkg.) (2025), Single wafer spin & spray systems (adv. pkg.) (2025), Direct write systems (adv. pkg.) (2025) | yes |
| manufacturing equipment | aggregate | Lithography tools (2025), Maskless lithography tools (no year), Deposition tools (2025), Etch and clean tools (2025), Chemical vapor deposition tools (2025), Dry etching and cleaning tools (2025), Dry etch tools (2025), Wafer and photomask handlers (2025), Process control tools (2025), Wafer inspection tools (2019), Bonding tools (2025), Die attaching tools (2025), Wire bonding tools (2025), Fabrication tools (for advanced packaging) (2025), Assembly tools (no year), Test tools (2025), Lithography tools (adv. pkg.) (2025), Deposition tools (adv. pkg.) (2025), Etch and clean tools (adv. pkg.) (2025) | no |
| manufacturing equipment | assembly and test tools | Assembly inspection tools (2025), Dicing tools (2025), Die attaching tools for IC (2025), Manual wire bonders (2025), Auto ball bonders for IC (2025), Automatic wedge bonders (2025), Wafer level stud bonders (2025), Other interconnect tools (2025), Packaging tools (2025), Integrated assembly tools (2025), Memory test tools (2025), SoC test tools (2025), Burn-in test tools (2025), Handlers and probers (2025) | yes |
| materials | fab materials | Wafer (2019), Photoresists (2019), Photomasks (2019), Deposition materials (2019), CMP materials (2019), Electronic gases (2019), Wet chemicals (2019) | yes |
| materials | packaging materials | Lead frames (2019), Bond wires (2019), Ceramic packages (2019), Substrates (2019), Encapsulation resins (2019), Die attach materials (2019) | yes |
| materials | aggregate | Packaging materials (2019) | no |
| out of scope | chip design | Chip design (2022), Logic chip design (2022), Advanced CPUs (2019), Discrete GPUs (2019), FPGAs (2019), AI ASICs (2019), Memory chip design (2022), DAO chip design (2022) | no |
| out of scope | EDA and core IP | EDA and Core IP (2019), Electronic design automation software (2019), Core intellectual property (2019) | no |
| out of scope | non-IC tools | Other deposition tools (non-IC) (2025), Die attaching tools for non-IC (2025), Auto ball bonders for non-IC (2025), Linear and discrete testing tools (2021) | no |
| leading-edge fabrication | (none in ETO) | Proposed second source, see above | pending |
| HBM memory | (none in ETO) | Proposed second source, see above | pending |
| advanced packaging | (none in ETO) | Proposed second source, see above | pending |

---

## 2026-10-21 07:15 · Andrew's decisions on the drafts above · FINAL

Andrew answered in chat:

1. **Advanced-packaging tools count as manufacturing equipment** (the draft). So the *advanced packaging* step means advanced-packaging capacity only (CoWoS-class).
2. **Second sources approved:** HBM from TrendForce (2025), leading-edge fabrication from SIA/BCG (2024 report, 2022 data), and the materials ETO leaves blank from the CSET 2021 report (2019 data).
3. **The DIGITIMES source for advanced packaging is not approved.** The advanced packaging step stays **qualitative**: there is no share and no screen, and this is stated as a limit. (From what we know, TSMC, a Taiwan firm, holds most CoWoS-class capacity, but we have no free, dated, citable share for it.)
4. **Tiny markets are kept but flagged:** inputs with a world market under $100 million stay in the screen and are flagged in the results.
5. **The rest of the mapping is approved as drafted.** `notes/eto_step_mapping.csv` is now final. The status of its rows is FINAL.

## 2026-10-21 07:15 · Rules for the second sources (set before extracting their numbers) · FINAL

I saw the HBM and fab headline numbers while searching for the sources (logged above). I have not opened the CSET materials tables yet.

1. **HBM memory** (one input, "HBM memory"): TrendForce's firm shares are added up by **headquarters country**. SK hynix and Samsung are South Korea, Micron is the US. Year 2025, labelled a projection. Basis: HQ, the same as ETO.
2. **Leading-edge fabrication** (one input, "Leading-edge logic fabrication (<10nm capacity)"): the country shares are used as SIA/BCG report them. Year 2022. Basis: **site location**, which differs from ETO and is flagged on every row. If the PDF figures differ from the press coverage, the PDF wins.
3. **Materials from CSET 2021:** only for materials where ETO has no numbers. I use the report's own country-level figures, as given, at the narrowest level the report gives. If it splits a material into sub-types (for example ArF and EUV photoresists), each sub-type is screened as its own input, which matches rule 2 of the screening rules. I don't build country shares from firm shares. Year 2019, with the source given as the report and the page or table. If the report gives no country figure for a material, it stays in the "could not screen" table.
4. Second-source rows go through the same thresholds and the same US/China and Taiwan rules as ETO rows.
5. **Raw copies:** each source's original file goes in its own folder under `data/raw/`. For any file whose licence doesn't clearly allow sharing, that folder is gitignored and the citation and URL are logged here instead.

## 2026-10-21 07:20 · CSET 2021 report cannot fill the materials gap · FINAL (a fact, with an open question)

- The approved CSET report gives **no country shares** for the materials ETO leaves blank. Its Table 1 (p. 8) says it "excludes fab materials besides wafers … and packaging materials" **"because of lack of data"**. Its materials table (Table 18, pp. 55–56) lists key firms and China's share only.
- Following rule 3 of the second-source rules, these 11 inputs stay **unscreened** and are listed in `results/could_not_screen.csv`: photoresists, electronic gases, wet chemicals, CMP materials, deposition materials, substrates, lead frames, bond wires, ceramic packages, encapsulation resins and die attach materials.
- This matters. ETO's own text says "Japanese firms are the leading producers" of photoresists, so Japan's materials hold is **under-counted** in the screen. Japan passes anyway on other inputs.
- **OPEN QUESTION for Andrew:** approve a further source for photoresists (and perhaps gases), or leave materials partly unscreened and state it as a limit?
- Housekeeping: I first downloaded the wrong CSET file (a one-page issue brief, `...Issue-Brief.pdf`). I deleted it before committing and replaced it with the full 98-page report (`...Issue-Brief-1.pdf`, SHA-256 319d942ba53468a6d5af97c9e46f6134fda2bf03958237e966bdc8c9cc8098ff). Flagging it because the brief says to ask before deleting files. It was my own uncommitted mistake, and the wrong file was never used.

## 2026-10-21 07:25 · How the second-source figures were taken · FINAL

- **HBM:** TrendForce's 2025 projection, quoted in the article: SK hynix 52.3%, Samsung 28.7%, Micron 19%. By HQ, that gives **South Korea 81.0%** and **United States 19.0%**. The firm rows are in `data/processed/second_source_figures.csv`.
- **Leading-edge fabrication:** SIA/BCG (May 2024), Exhibit 6, p. 14, row "Logic: <10 nm", 2022. **Taiwan 69%, South Korea 31%, United States 0%**, by fab location. The chart's text labels can't be read reliably from the PDF text, so I matched them by position and then checked them against an image of the page. China, Japan, Europe and Other carry no label in that row, and I have not entered them.
- **Licences and raw copies:**
  - CSET report: "© 2021 … licensed under a Creative Commons Attribution-Non Commercial 4.0 International License". It is **committed** in `data/raw/cset_2021_semiconductor_supply_chain/`.
  - SIA/BCG PDF: I found no licence statement, so it is **gitignored** (`data/raw/sia_bcg_2024_emerging_resilience/`). SHA-256 27040f69e8e036c927a193a8477e7d975a2ae35fb7e7cf37f759553fc14ff9cf. URL: https://www.semiconductors.org/wp-content/uploads/2024/05/Report_Emerging-Resilience-in-the-Semiconductor-Supply-Chain.pdf
  - TrendForce article: a copyrighted web page, saved as HTML on 2026-10-21 and **gitignored** (`data/raw/trendforce_2025-08-18_hbm/`). SHA-256 2956a09d0282f88b7d4fb6364183b692791e78b99d3ca9de6dc28d2db80a1d2e.

## 2026-10-21 07:27 · Results reporting: input counts per threshold · FINAL (how results are shown, not a rule change)

- The **country** set is the same at 25%, 40% and 60%. To show what does change, `results/country_set.md` also gives each country's **number of inputs** passed at each threshold, and which inputs join or drop out. No screening rule was changed.

## 2026-10-21 07:31 · Step 2 set-up choices · FINAL unless Andrew changes them

- **Anchors** (`notes/variable_anchors.md`) and the **disagreement rule** (`notes/disagreement_rule.md`) are **drafts** for Andrew and Ayodele to approve. The concentration cut-offs (25% and 60%) match the screen's robustness thresholds, so "medium" covers the band where the screen result itself would change.
- **Targets on the cases sheet** (for example, "Copper-importing countries" for CIPEC) are my draft wording, based on the plan's case table. **Confirm them before scoring**, because every score depends on who the target is.
- **Chokepoint sheet:** one row per line of `results/chokepoint_rows.csv` (42 rows), with share, year and target (United States) shown for reference. All six score cells, `evidence` and `sources` are empty.
- **Kappa uses linear weights.** Being one level apart gets half credit, and low against high gets none. Linear rather than quadratic weights, because with only three levels quadratic weights give 75% credit for a one-level gap, which would flatter our agreement.
- **The plain-language reading of kappa** uses the Landis and Koch (1977) bands: slight, fair, moderate, substantial, almost perfect. These are conventions, not tests.
- **Blank cells:** a cell left blank by either person is not compared, and the report shows how many were skipped, so gaps are visible rather than silently dropped.
- **Agreement is always computed on the original personal sheets.** Settled scores go in a separate `scoring/*_final.csv` (see the disagreement rule).
- **Tests use made-up sheets** in `tests/fixtures/` only, marked as invented. `scoring/` holds no scores.

## 2026-10-21 08:15 · Small-market rows dropped from Step 4 scoring · FINAL (Andrew, before any scoring)

- **Decision:** Andrew decided in chat to drop the 7 chokepoint rows whose input has a world market **under $100 million** from the Step 4 row list. This brings `results/chokepoint_rows.csv` and both `scoring/chokepoints_*.csv` sheets from 42 rows to **35**.
- **Why:** the tiny markets give little real leverage, and 42 rows meant 252 judgments per person in about 1.5 hours. Andrew saw the 7 rows listed before deciding.
- **Timing:** this was decided **after** the screen results were seen, but **before any scoring**. It changes the Step 4 row list only. The screen rules and the country set are unchanged. All 8 countries still pass at 40%, the small-market passes still count, and every country keeps at least one row to score. The 2 rows with no market size in their source (HBM and leading-edge fabrication) are clearly large markets and are kept.
- **Dropped rows**, kept in `results/chokepoint_rows_dropped_small_markets.csv`:
  - C01 Austria, imprint lithography
  - C04 Germany, crystal-growing furnaces
  - C05 Germany, manual wire bonders
  - C10 Japan, direct write systems
  - C36 Singapore, automatic wedge bonders
  - C37 Singapore, integrated assembly tools
  - C38 Singapore, wafer level stud bonders
- **Row IDs:** IDs were assigned before the drop, so the kept rows keep their original IDs, and gaps in the numbering mark the dropped rows.
- **Effect on rows to score:** Germany and Singapore now have one row each (mask aligners; auto ball bonders for IC). Austria has 2 and Japan 21.

## 2026-10-21 15:29 · Cohesion made countable; scoring split; sharing · FINAL (Andrew's decisions in chat)

- **Cohesion is redefined as a count, not a judgment.** Andrew wanted to drop cohesion as too subjective. I argued for keeping it: it is the variable closest to the hypothesis ("threats split the coalition"), and two cases (CIPEC and the tin council) are there because the group failed to hold. Andrew chose the middle option.
  - **New question:** "How many separate actors must hold the line to keep the supplier's share?" 1 actor = high, 2–3 = medium, 4 or more = low.
  - **Who the actors are:** member countries for a group, and firms for a single country.
  - **How to count:** count from the largest down until the actors together hold at least 80% of the supplier's share. Use shares at the start of the episode.
  - **Why counting fewer actors as high cohesion is reasonable:** the standard cartel finding is that groups with fewer members hold together better. The 80% cut-off leaves out fringe players that are too small to undercut the rest.
  - **Draft status:** the anchors are still a draft for approval.
- **Circularity guard added to the anchors:** past cases are scored as they stood at the **start** of the episode, never from how it ended, because the outcome is what the scores are meant to explain.
- **Scoring split.** Andrew first proposed splitting the cases (3 for him and 2 for Ayodele, with Andrew cross-checking). I pointed out that this removes the agreement figure, which is the plan's main defence against subjectivity. Andrew chose instead:
  - **Past cases:** the reading and summaries are split (3 and 2), but **both score all 5**. Known limit: the scores share the same summaries, so the agreement figure measures whether the same facts are read the same way.
  - **Chokepoints:** a shared set of **10 rows** that both score, chosen at random, one per country plus 2 more, with seed 20261021 in `src/make_scoring_sheets.py`. The other **25 rows alternate**, giving Andrew 13 and Ayodele 12. Who scores each row is in an `assigned_to` column on the sheets. `compare_scores.py` compares only the shared rows and reports how many rows were scored by one person.
  - **Cross-check:** each of them reads over the other's single-scored rows and summaries after the agreement figure is worked out, and flagged items are settled by the disagreement rule.
  - **The random draw left the HBM row (C39, South Korea) single-scored.** Swapping it into the shared set by hand would be a manual change and would need logging.
- **Plan text updated to match:** the cohesion question in Step 2, and the "each of you separately" tasks in Steps 3 and 4. No tasks were ticked.
- **Blind scoring with a shared repo:** score offline and don't commit or push a sheet until both are done, because GitHub's web editor commits at once. This is written into `notes/disagreement_rule.md`.
- **Sharing:** Andrew chose a **private GitHub repo** with Ayodele as a collaborator.
  - `winget` was blocked from this sandboxed shell. Instead, GitHub CLI **v2.102.0** (released 30 Sep 2026) was downloaded from the official `cli/cli` releases page, checked against GitHub's published SHA-256 checksum, and unpacked to `C:\Users\Hp\tools\gh-2.102.0`. Nothing was installed system-wide and PATH was not changed.
  - I chose v2.102.0 rather than v2.102.1, which was released only a day earlier, as a supply-chain precaution.

## 2026-10-31 05:28 · Scoring process changed because of time · FINAL (Andrew's decision in chat)

- **Why:** the submission deadline turned out to be **08:00 on 1 November 2026**, not end of day, and there is no longer time for independent double-scoring.
- **New process for past cases:** Andrew covers K1–K4 and Ayodele covers K5 (Japan–Korea).
  - Claude drafts the summaries, scores and outcomes for K1–K4 (`notes/step3_case_drafts.md`, `notes/step3_draft_scores_claude.csv`).
  - Andrew reviews them, changes any score he thinks is wrong, and is the **final judge**. He then fills in `scoring/cases_andrew.csv` himself.
  - Claude also drafted the outcomes, rules of thumb and non-separating variables (`notes/step3_patterns_draft.md`).
- **This overrides** hard rule 5 in CLAUDE.md ("do not score anything") and the double-scoring set-up in `notes/disagreement_rule.md`. On Andrew's explicit instruction, no disagreements will be settled, and the methodology will say so.
- **Limits to state:**
  - Each case has a single final scorer, so there is **no inter-rater agreement figure**.
  - K1–K4 scores started as AI drafts.
  - The drafter knew the outcomes, so there is a risk the scores were fitted to them.
- **Outcome categories:** CIPEC (K2) doesn't fit "worked / partly worked / backfired" because it simply had no effect. It is drafted as "failed", and Andrew decides whether to keep that category.

## 2026-10-31 05:42 · Claude drafts Andrew's 13 chokepoint rows · FINAL process (scores are drafts)

- At Andrew's request, Claude drafted scores for the 13 rows with `assigned_to = andrew`, in `notes/step4_draft_scores_andrew_rows.md` and `.csv`. Andrew reviews them and has the final say. `scoring/` is untouched.
- **Concentration and cohesion are mechanical.** Concentration comes from the ETO share. Cohesion is the number of firms needed to reach 80% of the country's share, from ETO firm rows (from TrendForce for HBM). For wafers, ETO has no firm shares, so the count of 2 firms (Shin-Etsu, SUMCO) is from general knowledge and flagged.
- **The other four variables are judgments,** each with a one-line reason in the draft.

## 2026-10-31 13:23 · Claude drafts K5 and Ayodele's 12 chokepoint rows · FINAL process (scores are drafts)

- At Andrew's request (Ayodele ran short of time), Claude drafted K5 (Japan–Korea) in `notes/step3_case_drafts.md`, and Ayodele's 12 rows in `notes/step4_draft_scores_ayodele_rows.md` and `.csv`, for Andrew to compare with Ayodele's partial scores. Andrew has the final say.
- **Time to replace now has a written rule** (in that file): low if a US or US-controlled maker already covers most of the need; medium if there's a minority US maker, or a mature technology a new entrant could manage in 2–5 years; high if there's no US maker and it's a lithography-class frontier system. Earlier drafts used the same reasoning without writing it down. Under the rule, C14 would move from high to medium if IMS is Intel-controlled.
- **Housekeeping:** a failed command briefly emptied `notes/step3_case_drafts.md`. It was restored from the last commit before any edit. The working tree had been clean, so nothing was lost.

## 2026-10-31 13:25 · Claude drafts the 10 shared chokepoint rows · FINAL process (scores are drafts)

- At Andrew's request, Claude drafted the 10 `assigned_to = both` rows in `notes/step4_draft_scores_shared_rows.md` and `.csv`, using the same method and the same written time-to-replace rule. All 35 rows now have Claude drafts. Andrew has the final say on all of them.
- **New flag:** C02 (IMS, possibly Intel-owned) and C35 (Kulicke & Soffa, US-incorporated) may in practice be US-controlled supply, so the HQ-based screen may overstate Austria's and Singapore's leverage.

## 2026-10-31 18:56 · Final scores recorded; drafts cleaned up · FINAL (Andrew's decisions in chat)

- **Final scores** are in `scoring/cases_final.csv` (5 cases) and `scoring/chokepoints_final.csv` (35 rows), each with evidence, sources and a `scored_by` column. Andrew's spreadsheet froze, so Claude wrote these sheets at his request. The blank per-person sheets were left untouched.
- **Andrew accepted Claude's drafts with one change:** tin council (K3) time to replace goes from **low to medium**. The stockpile was inventory, not new supply, and buyers never had to build their own. All 35 chokepoint rows are as drafted.
- **Outcome categories:** "failed" is used for CIPEC (K2) as a fourth category. K4 and K5 are recorded as backfired, with the alternative reading for K5 noted in the case file.
- **K4 dependence evidence** now rests on sourced figures (Japan imported about 23,300 t from China in 2010, against about 35,000 t of Chinese exports in January–November 2010), which gives a rough share of more than half.
- **Profile** comparison is now reproducible with `src/profile.py` (writes `results/profile_distances.csv`).
- **"Draft" and review-status lines removed** from the case, chokepoint, anchors and profile notes at Andrew's request. This log keeps the full history of who drafted and who decided.
