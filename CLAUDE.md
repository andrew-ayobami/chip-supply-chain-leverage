# Project brief: chip-supply-chain leverage for AI safety

Andrew and Ayodele's project for the middle-powers hackathon on Mangrove, Track C (Diplomacy).
Hackathon date and submission deadline: **[Andrew to fill in]**

The full plan is in `research_plan.md`. It is the source of truth for the steps and tasks.

Andrew leads and checks every judgment call. Ayodele works with him on the scoring. Talk to both of them in plain, simple language, and explain any stats briefly.

## Your job for now

Do **Steps 1 and 2** of the plan, then stop and report back.

Andrew and Ayodele will do Steps 3 and 4 themselves. Do not start Step 3.

## What the judges reward, and what it means for you

The organisers describe the judging like this:

- **50%:** rigour and clarity, not polish. Work that states what it did not establish scores well.
- **40%:** could a reader outside the team follow what was done and why?
- **10%:** is the question worth asking, and cut to a size the work can answer?

In practice:

- Every number needs a year and a source.
- Every choice gets logged with a reason.
- Anything uncertain gets flagged, not smoothed over.

## Hard rules

1. **No spending.** Don't use paid data, services or API calls. If a step seems to need one, ask Andrew first.
2. **Pre-work is allowed.** The organisers confirmed this on 19 Oct 2026, so you can start Steps 1 and 2 now. You don't need a separate prior-work log, because the git history and `notes/decisions.md` already show when each piece was done.
3. **Log every choice** in `notes/decisions.md`, with the time and a one-line reason. Write each rule (threshold, category mapping, share definition) down *before* you look at the results it affects.
4. **Commit after every task** with a clear message. When a task is done, tick it in `research_plan.md` (change `- [ ]` to `- [x]`) in the same commit.
5. **Do not score anything.** Steps 3 and 4 rely on Andrew and Ayodele scoring separately, then checking how often they agree. If you fill in any score, that check means nothing. You can build the scoring sheets, but leave every score cell empty.
6. **Do not write report prose.** Code, data, tables, figures, short factual method notes in `notes/`, and checking their drafts are all fine.
7. **Keep raw downloads untouched** in `data/raw/`, and work on copies in `data/processed/`. Cite every dataset the way its publisher asks. Check the dataset's licence before committing raw files. If the licence is unclear, add `data/raw/` to `.gitignore`.

## Always ask Andrew before you

- use a second data source (for example, for HBM memory)
- finalise how ETO's categories map onto the plan's five supply chain steps
- change the 40% threshold, or any other rule, after seeing results
- add or drop a country by hand
- delete files
- move on to Step 3

## Step 1: Pick the countries

**Goal:** a country set that comes from a stated rule, not from our own picks.

### Data

- **Main source:** ETO's Advanced Semiconductor Supply Chain Dataset, which sits behind the [ETO Supply Chain Explorer](https://eto.tech/tool-docs/chipexplorer). Dataset docs are at https://eto.tech/dataset-docs/chipexplorer. It is open access.
- Download the latest release. Record the version and download date in `notes/decisions.md`, and keep the original file in `data/raw/`.
- Record the year of every figure. Some shares are recent and some are older, so never mix years without saying so.
- If the download is blocked from your environment, stop and ask Andrew to download it for you.

### Gaps to check first

ETO covers the supply chain for advanced *logic* chips. It probably has no market shares for **HBM memory**, and it may only cover packaging in general terms rather than **advanced packaging** (for example, CoWoS).

Check both. If a step is missing, propose one dated, citable source per missing step in `notes/decisions.md`, then wait for Andrew's OK before using it.

### How to run the screen

1. **Map ETO's inputs onto the plan's five steps:** manufacturing equipment, materials, leading-edge fabrication, HBM memory, advanced packaging. Out of scope: chip design, design software (EDA) and raw minerals. Write the mapping as a table in `notes/decisions.md`, and show it to Andrew before running the screen.
2. **Screen individual inputs, not whole steps.** Screen EUV lithography tools or photoresists, not "equipment" or "materials" as a whole. A country can dominate one input without holding 40% of a whole step. Group the results under the five steps afterwards.
3. **Use ETO's country shares as given.** Check how ETO assigns shares to countries. It appears to use each firm's headquarters country, in which case TSMC's overseas fabs count as Taiwan. Log whatever you find as a known limit.
4. **Apply the threshold.** A country passes for an input if it holds 40% or more of world supply.
5. **Remove the US and China** from the set, since they're the parties the coalition would bargain with. Keep their rows in the data for context.
6. **Rerun at 25% and 60%,** and record who moves in or out.
7. **Treat Taiwan like any other country.** It stays in if it passes. Do no extra analysis of whether it could join a coalition openly.

### Outputs

- `data/processed/shares.csv`: one row per input and country, with columns `step, input, country, share, year, source, source_url`
- `results/screen_25.csv`, `results/screen_40.csv`, `results/screen_60.csv`: the inputs and countries that pass at each threshold
- `results/country_set.md`: the final set at 40%, plus a short table of who changes at 25% and 60%
- `results/chokepoint_rows.csv`: one row per country and input that passed at 40%, excluding the US and China, with share, year and source. This becomes the row list for Step 4.

**Sanity check:** the plan expects roughly the Netherlands, Japan, South Korea, Taiwan and Germany. If the result differs a lot, don't force it. Report what you found and why.

## Step 2: Set up the variables

**Goal:** get the six variables ready to score, and build the sheets Andrew and Ayodele will score in.

The variables and their questions are in `research_plan.md`, Step 2. The "target" is the side the leverage is aimed at. For today's chokepoints, that's the US.

The three "Agree..." tasks in Step 2 of the plan belong to Andrew and Ayodele. Tick them only when Andrew tells you they're done.

### Tasks

1. **Draft the anchors.** In `notes/variable_anchors.md`, write a one-line meaning of low, medium and high for each variable.
   - For each variable, say which end helps the supplier. For example, high concentration helps the supplier, while high dependence on the target hurts it.
   - Use numbers where they're natural (shares, years to replace) and plain descriptions elsewhere.
   - The anchors must work for both a 1970s commodity case and a 2026 chip input.
   - This is a draft. Andrew and Ayodele approve or change it.
2. **Draft a rule for settling disagreements,** also for their approval. A simple default:
   - One level apart: discuss and agree.
   - Low against high: each writes down their evidence, then they agree and record why.
   - Always keep both original scores.
3. **Build blank scoring sheets in `scoring/`,** one per person so neither sees the other's scores:
   - `cases_andrew.csv` and `cases_ayodele.csv`: one row per case in Step 3 of the plan
   - `chokepoints_andrew.csv` and `chokepoints_ayodele.csv`: one row per line of `results/chokepoint_rows.csv`
   - Both kinds of sheet get one column per variable, plus `evidence` and `sources` columns. Allowed scores are low, medium and high. Leave every score cell empty.
4. **Write `src/compare_scores.py`.** It reads both people's sheets and reports:
   - how often they agreed exactly
   - how often they were one level apart
   - Cohen's kappa, weighted because low/medium/high are ordered, with one plain sentence on what the number means
   - a list of every disagreement for them to settle

   Test it on made-up scores kept in `tests/` only. Never put test scores in `scoring/`.

## When you finish

Write `notes/handback_steps_1_2.md`. It should cover:

- what you did
- the final country set
- every choice you made, and why
- open questions
- anything in the data that looked off

Then stop.

## Repo layout

```
CLAUDE.md  research_plan.md  .gitignore
data/raw/          # original downloads, untouched
data/processed/    # cleaned tables
results/           # screen outputs, country set, chokepoint rows
scoring/           # blank sheets for Andrew and Ayodele
src/               # screen.py, compare_scores.py
tests/
notes/             # decisions.md, variable_anchors.md, handback_steps_1_2.md
```

**Setup:** Python 3.11+, pandas, scikit-learn (for kappa) and pytest. Run `git init` if the folder isn't already a repo.
