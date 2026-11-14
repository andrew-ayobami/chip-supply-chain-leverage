# Leverage profile: today's chokepoints against the past cases

Built from the final scores for all 35 chokepoint rows (`scoring/chokepoints_final.csv`) and the 8 past cases with known outcomes (`scoring/cases_final.csv`; K9 is left out because its outcome is too early to judge). Run `python src/profile.py` to reproduce it. Per-row distances are in `results/profile_distances.csv`.

**How "closest case" is measured:** the number of score steps between a row and a case, added up across the six variables (low to high counts as 2 steps). The case with the smallest total is the closest. Ties are counted for each case involved.

## Where the leverage is strongest

**Eight rows** score **high on time to replace**, meaning the US would need more than 5 years to build its own supply or a route around the holder. In the past cases, that is what separated the cuts that partly worked from the ones that backfired:
- **Netherlands (ASML):** EUV (C32), ArF immersion (C30), ArF dry (C29) and KrF (C33) lithography
- **Taiwan:** leading-edge fabrication (C42)
- **Japan:** front-end resist processing (C19, Tokyo Electron), i-line lithography (C26, Canon) and e-beam mask writers (C14)

Five of these (C19, C29, C30, C32, C42) are also **single-firm holds with low substitutability**. They are the strongest rows in the set.

## Where it is weakest

- **Rows where a US or US-controlled maker already covers most of the need:**
  - overlay metrology (C34, where KLA holds 51.5%)
  - Singapore's ball bonders (C35, Kulicke & Soffa is US-incorporated)
  - photomasks (C27, which leading-edge fabs mostly make themselves)

  These three are the only rows with low time to replace.
- **Lower-end and mature tools with several alternatives**, such as dry stripping, packaging tools, wet cleaning, handlers and probers, and wafers. They have medium share, medium substitutability and medium time to replace.
- **Austria and Singapore:** Austria is neutral and Singapore is not a treaty ally, so their dependence on the US is medium. But both may hold supply that is in practice US-controlled: IMS (C02, reportedly Intel-owned) and Kulicke & Soffa (C35). The headquarters-based screen probably overstates their leverage.
- **Across the board:** 32 of 35 rows score high on dependence on the US, and 34 of 35 score medium on state control. So most holders rely on the US for their security and can direct their firms only through export licensing.

## Which past case it most resembles

| Closest case (ties counted for each) | Form | Outcome | Rows |
| --- | --- | --- | --- |
| K7 EU data flows 2020–23 | condition | worked | 15 |
| K2 CIPEC | price management | failed | 12 |
| K6 Nuclear safeguards, from 1974 | condition | worked | 6 |
| K5 Japan–Korea 2019 | cut | backfired | 5 |
| K3 Tin council | price management | backfired | 2 |
| K1 Oil embargo | cut | partly worked | 2 |
| K4 China–Japan 2010 | cut | backfired | 1 |

- **Counting each row once:** 16 rows are closest only to cases that worked or partly worked, 13 only to cases that failed or backfired, and 6 are tied between the two.
- **The strongest rows now have a close match.** EUV, ArF immersion, ArF dry, Tokyo Electron's resist processing and Taiwan's leading-edge fabs are all closest to nuclear safeguards (K6): highly concentrated, hard to substitute, slow to replace, and held by countries that rely on the buyer. KrF lithography is closest to EU data flows (K7).
- **This changed when the condition cases were added.** With only the original five cases (all cuts and price schemes), most rows were closest to cases that backfired, and the strongest rows matched no case well. That result reflected the case set, not the chokepoints.

## How to read this

- **The distance measure compares the structure of the leverage, not how it is used.** It doesn't know whether a row would be used as a cut or a condition.
- **Read together with the rules of thumb, the picture is consistent:**
  - Used as a **condition**, the strongest chokepoints look like the nuclear safeguards case, which worked. Most of the rest look like the EU data case, which also worked.
  - Used as a **cut**, rule 2 applies: cuts only held where replacement took more than five years, which is true of 8 of the 35 rows. A threat from the other 27 would look like the cuts that backfired.
- **This supports the working hypothesis more directly than before:** the same chokepoints look strong as conditions and weak as threats.

## Caveats

- **One scorer per case and row, so there is no agreement figure.** Claude drafted the scores; Andrew reviewed the first five cases and the 35 rows. K6–K9 await his review.
- **The distances are partly driven by variables that barely vary today** (dependence and state control).
- **Two condition cases is a thin base.** Both are about verification and legal safeguards rather than chips.
