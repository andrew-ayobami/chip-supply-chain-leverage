# Who scores what, and how disagreements are settled

**Planned but not used:** time ran out, so each case and chokepoint row ended up with one final scorer and no agreement figure (see the README).

This applies to both kinds of sheet: past cases (Step 3) and today's chokepoints (Step 4).

## Who scores what (Andrew's decision, 21 Oct 2026)

- **Past cases (5):** you split the **reading**, but not the scoring.
  - Andrew researches 3 cases and Ayodele researches 2. Each of you gathers 2–3 sources for your own cases and writes the 3-line summary.
  - Then you **both score all 5 cases**, separately, using the summaries plus your own reading. Every case is marked `assigned_to = both`.
- **Chokepoints (35 rows):** the `assigned_to` column on the sheet says who scores each row.
  - **`both`:** 10 rows that you both score. These give the agreement figure. They were drawn at random, with one row per country plus 2 more, using a fixed seed so the draw can be repeated (`src/make_scoring_sheets.py`).
  - **`andrew` or `ayodele`:** the other 25 rows, which only that person scores. They alternate down the list, so Andrew has 13 and Ayodele 12. Leave the other person's rows blank.
- **Cross-check:** once the agreement figure has been worked out, each of you reads the other's single-scored rows (and summaries) and flags anything that looks wrong. Flagged items are settled by the rule below.
- **Known limit:** the case scores share the same summaries, so they aren't fully independent. The agreement figure shows whether you read the **same facts** the same way.

## Before comparing

1. **Each of you scores your own sheet** (`scoring/*_andrew.csv` or `scoring/*_ayodele.csv`) **without looking at the other's**.
2. **Score offline.** Download your sheet and fill it in with Excel, Google Sheets or any editor. **Don't commit or push it until both of you are done.** GitHub's web editor saves straight to the shared repo, so the other person could see your scores early.
3. **When both sheets are complete, commit them together.** The git history then shows the scores were made independently.
4. **Run `python src/compare_scores.py cases`** (or `chokepoints`). It compares the rows you both scored, reports how often you agreed, and lists every disagreement. These agreement figures are what we publish, because they're computed on the **original** scores, before any settling.

## Settling each disagreement

| How far apart | What to do |
| --- | --- |
| Same level | Nothing. That score is final. |
| One level apart (low vs medium, or medium vs high) | Discuss and agree a final score. Write one line on why. |
| Two levels apart (low vs high) | **First**, each of you writes your evidence (one or two lines, with a source) without seeing the other's. **Then** discuss, agree a final score, and record why. |
| Still no agreement after discussion | Andrew, as lead, decides. The score is marked **disputed**, and Step 6 checks whether flipping it would change any verdict. |

## What to record

- **Always keep both original scores.** Never overwrite a personal sheet after comparing.
- **Record each settled score** in `scoring/<cases|chokepoints>_final.csv`, one row per disagreement or flagged item. Use the columns `id, variable, andrew, ayodele, final, how_settled, reason`.
  - `how_settled` is one of `discussed`, `evidence_then_discussed`, `lead_call_disputed` or `cross_check_changed`.
- **Scores you already agreed on don't need a row.** The final value is simply the shared score.
