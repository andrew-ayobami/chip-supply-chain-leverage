# Rule for settling scoring disagreements (DRAFT for Andrew and Ayodele to approve or change)

This rule applies to both kinds of sheet: past cases (Step 3) and today's chokepoints (Step 4).

## Before comparing

1. Each of you scores your own sheet (`scoring/*_andrew.csv` or `scoring/*_ayodele.csv`) **without looking at the other's**.
2. When **both** sheets are complete, commit them. The git history then shows the scores were made independently.
3. Run `python src/compare_scores.py cases` (or `chokepoints`). It reports how often you agreed and lists every disagreement. These agreement figures are what we publish, because they're computed on the **original** scores, before any settling.

## Settling each disagreement

| How far apart | What to do |
| --- | --- |
| Same level | Nothing. That score is final. |
| One level apart (low vs medium, or medium vs high) | Discuss and agree a final score. Write one line on why. |
| Two levels apart (low vs high) | **First**, each of you writes your evidence (one or two lines, with a source) without seeing the other's. **Then** discuss, agree a final score, and record why. |
| Still no agreement after discussion | Andrew, as lead, decides. The score is marked **disputed**, and Step 6 checks whether flipping it would change any verdict. |

## What to record

- **Always keep both original scores.** Never overwrite a personal sheet after comparing.
- Record the settled scores in `scoring/<cases|chokepoints>_final.csv`, one row per disagreement, with the columns `id, variable, andrew, ayodele, final, how_settled, reason`.
  - `how_settled` is one of `discussed`, `evidence_then_discussed`, or `lead_call_disputed`.
- Scores you already agreed on don't need a row. The final value is simply the shared score.
