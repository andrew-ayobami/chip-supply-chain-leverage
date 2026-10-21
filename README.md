# Chip-supply-chain leverage for AI safety

Andrew and Ayodele's project for the Middle Powers hackathon (Track C, Diplomacy). The submission deadline is 1 November 2026.

The question: which AI-safety asks could the countries that hold chip-supply-chain chokepoints (other than the US and China) credibly attach to their leverage?

## Start here (Step 3)

1. [`notes/brief_for_ayodele_step3.md`](notes/brief_for_ayodele_step3.md): a short need-to-know brief for Step 3.
2. [`notes/variable_anchors.md`](notes/variable_anchors.md): what low, medium and high mean for each of the six variables.
3. [`notes/disagreement_rule.md`](notes/disagreement_rule.md): who scores what, and how disagreements are settled.

For the bigger picture:

- [`research_plan.md`](research_plan.md): the full plan and task list. This is the source of truth for the steps.
- [`results/country_set.md`](results/country_set.md): the Step 1 result, which countries pass the screen.
- [`notes/handback_steps_1_2.md`](notes/handback_steps_1_2.md): a summary of Steps 1 and 2, with open questions.
- [`notes/decisions.md`](notes/decisions.md): every choice made so far, with its time and reason.

## Rules for anyone working in this repo, including AI assistants

- **Never fill in, suggest or change any score in `scoring/`.** The scores must be Andrew's and Ayodele's own independent judgments. How often they agree is part of the result, and that check means nothing if anyone else, or any tool, helps with the scores.
- **Don't open the other person's scoring sheet** before both of you have finished. Score offline, and don't commit or push a sheet until both are done.
- **Every number needs a year and a source.** Log every choice in `notes/decisions.md`, with the time and a one-line reason.
- **Keep `data/raw/` untouched.** Work on copies in `data/processed/`.

## Repo map

```
research_plan.md   the plan
data/raw/          original downloads, untouched
data/processed/    cleaned tables (shares.csv, second-source figures)
results/           screen outputs, country set, chokepoint rows
scoring/           scoring sheets, one per person (cases_*.csv, chokepoints_*.csv)
src/               screen.py, make_scoring_sheets.py, compare_scores.py
tests/             tests, using made-up scores only
notes/             decisions log, anchors, disagreement rule, briefs
```

## Running the code

Python 3.11 or later, with pandas, scikit-learn and pytest.

```
python src/screen.py                     # rebuild the Step 1 screen and results
python src/compare_scores.py cases       # agreement report, once both case sheets are scored
python src/compare_scores.py chokepoints
python -m pytest tests
```

## Data and licences

- **Main data:** Emerging Technology Observatory, *Semiconductor Supply Chain Dataset* (September 2026 release), https://eto.tech/dataset-docs/chipexplorer. Licensed CC BY-NC 4.0.
- **Other sources:** CSET's 2021 report (CC BY-NC 4.0), TrendForce (HBM, 2025) and SIA/BCG (2024). Their files are listed in `notes/decisions.md`. Files with unclear licences are kept out of this repo.
