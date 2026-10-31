# Leverage profile (Claude's DRAFT, rerun 31 Oct 2026; Andrew reviews)

**What this covers:**
- **All 35 chokepoint rows**, using Claude's draft scores (`notes/step4_draft_scores_{andrew,ayodele,shared}_rows.csv`).
- **All 5 past cases**, using Claude's drafts (`notes/step3_draft_scores_claude.csv`).

None of these scores is final yet. Andrew's review changes aren't in this run, so rerun it once he has decided.

**How "closest case" is measured:** the number of score steps between a row and a case, added up across the six variables (low to high counts as 2 steps). The case with the smallest total is the closest. Ties are counted for each case involved.

## Where the leverage is strongest

**Eight rows** score **high on time to replace**, meaning the US would need more than 5 years to build its own supply. That is the variable that separated the past cases:
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
- **Austria and Singapore:** Austria is neutral and Singapore is not a treaty ally, so their dependence on the US is medium. But both may hold supply that is in practice US-controlled: IMS (C02, if Intel-owned) and Kulicke & Soffa (C35). The headquarters-based screen probably overstates their leverage.
- **Across the board:** 32 of 35 rows score high on dependence on the US, and 34 of 35 score medium on state control. So most holders rely on the US for their security and can direct their firms only through export licensing.

## Which past case it most resembles

| Closest case (ties counted for each) | Rows |
| --- | --- |
| K5 Japan–Korea 2019 (backfired, draft) | 20 |
| K2 CIPEC (failed) | 14 |
| K4 China–Japan 2010 (backfired) | 9 |
| K3 Tin council (backfired) | 5 |
| K1 Oil embargo (partly worked) | 2 (C14, C26, both ties) |

- **Overall:** by score distance, today's chokepoints look most like the Japan–Korea and CIPEC cases. Those are cases where the leverage failed or backfired. None of the 35 rows is closest to the oil embargo alone.
- **The strongest rows are a mix no past case had.** EUV, ArF, Taiwan's fabs and Tokyo Electron's resist processing look like China–Japan 2010 and Japan–Korea 2019 on concentration and substitutability. But they score **high** on time to replace, like the oil embargo. So the five cases don't directly cover the strongest chokepoints, and the write-up should say so.
- **What this suggests (draft):** for most of today's chokepoints, a threat to cut supply resembles past cases that failed or backfired. That supports the working hypothesis that conditions attached to supply work better than threats. Only the handful of ASML, TSMC and Tokyo Electron rows have the long replacement time that held up in 1973, and even there the closest structural matches backfired.

## Caveats

- **These are draft scores by one scorer (Claude),** reviewed only by Andrew. There is no agreement figure.
- **The distances are partly driven by variables that barely vary today** (dependence and state control).
- **The past-case evidence is thin:** only 5 cases, 4 of them commodities.
