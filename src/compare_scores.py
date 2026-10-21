"""Compare Andrew's and Ayodele's independent scores and list every disagreement.

Usage (from the repo root):
    python src/compare_scores.py cases
    python src/compare_scores.py chokepoints --write   # also saves results/agreement_<kind>.md
                                                       # and results/disagreements_<kind>.csv
"""
from pathlib import Path
import argparse
import math
import warnings

import pandas as pd
from sklearn.metrics import cohen_kappa_score

ROOT = Path(__file__).resolve().parent.parent
VARIABLES = ["concentration", "substitutability", "time_to_replace",
             "cohesion", "dependence_on_target", "state_control"]
LEVELS = {"low": 0, "medium": 1, "high": 2}
NAMES = {0: "low", 1: "medium", 2: "high"}
SHEETS = {  # kind -> (id column, label columns shown in the disagreement list)
    "cases": ("case_id", ["case"]),
    "chokepoints": ("row_id", ["country", "input"]),
}
PEOPLE = ("andrew", "ayodele")


def load_sheet(path, id_col):
    """Read one person's sheet. Scores must be low/medium/high or blank (not scored yet)."""
    df = pd.read_csv(path, dtype=str).fillna("")
    missing = [c for c in [id_col] + VARIABLES if c not in df.columns]
    if missing:
        raise ValueError(f"{path.name}: missing columns {missing}")
    if df[id_col].duplicated().any():
        raise ValueError(f"{path.name}: duplicate ids {sorted(df[id_col][df[id_col].duplicated()])}")
    for var in VARIABLES:
        df[var] = df[var].str.strip().str.lower()
        bad = df[~df[var].isin(list(LEVELS) + [""])]
        for _, row in bad.iterrows():
            raise ValueError(f"{path.name}: {row[id_col]} / {var} = {row[var]!r}; "
                             f"allowed: low, medium, high or blank")
    return df.set_index(id_col)


def shared_ids(sheet):
    """Rows both people are meant to score: assigned_to == 'both', or every row if there is no such column."""
    if "assigned_to" not in sheet.columns:
        return list(sheet.index)
    return list(sheet.index[sheet["assigned_to"].str.strip().str.lower() == "both"])


def pair_scores(a, b, labels):
    """Long table of (id, variable) pairs on shared rows scored by both people, as 0/1/2."""
    if set(a.index) != set(b.index):
        raise ValueError(f"the two sheets have different rows: only in first {sorted(set(a.index) - set(b.index))}, "
                         f"only in second {sorted(set(b.index) - set(a.index))}")
    if set(shared_ids(a)) != set(shared_ids(b)):
        raise ValueError("the two sheets disagree on which rows are assigned_to 'both'")
    rows, unscored = [], 0
    for i in shared_ids(a):
        for var in VARIABLES:
            x, y = a.at[i, var], b.at[i, var]
            if not x or not y:
                unscored += 1
                continue
            rows.append({"id": i, **{c: a.at[i, c] for c in labels if c in a.columns},
                         "variable": var, PEOPLE[0]: LEVELS[x], PEOPLE[1]: LEVELS[y]})
    cols = ["id"] + [c for c in labels if c in a.columns] + ["variable", *PEOPLE]
    return pd.DataFrame(rows, columns=cols), unscored


def weighted_kappa(x, y):
    """Cohen's kappa with linear weights (one level apart = half credit). NaN if undefined."""
    if len(x) == 0:
        return float("nan")
    with warnings.catch_warnings():  # 0/0 when both people used one single level throughout
        warnings.simplefilter("ignore")
        k = cohen_kappa_score(x, y, labels=[0, 1, 2], weights="linear")
    return float(k)


def agreement_stats(pairs):
    gap = (pairs[PEOPLE[0]] - pairs[PEOPLE[1]]).abs()
    n = len(pairs)
    return {
        "n": n,
        "exact": int((gap == 0).sum()),
        "one_apart": int((gap == 1).sum()),
        "two_apart": int((gap == 2).sum()),
        "kappa": weighted_kappa(pairs[PEOPLE[0]], pairs[PEOPLE[1]]),
    }


def kappa_sentence(k):
    if math.isnan(k):
        return ("Kappa can't be worked out here (no scores yet, or both of you used the same single "
                "level for everything, so there is nothing to compare against chance).")
    bands = [(0.20, "slight"), (0.40, "fair"), (0.60, "moderate"), (0.80, "substantial"),
             (math.inf, "almost perfect")]
    word = next(w for cut, w in bands if k <= cut) if k > 0 else "no better than chance"
    return (f"Weighted kappa = {k:.2f}. Kappa measures how much more you agreed than two people "
            f"picking levels at random would, with half credit for being one level apart: "
            f"1 is perfect agreement, 0 is no better than chance. "
            f"By the usual rule of thumb (Landis and Koch, 1977), {k:.2f} counts as \"{word}\" agreement.")


def disagreements(pairs):
    d = pairs[pairs[PEOPLE[0]] != pairs[PEOPLE[1]]].copy()
    d["levels_apart"] = (d[PEOPLE[0]] - d[PEOPLE[1]]).abs()
    for p in PEOPLE:
        d[p] = d[p].map(NAMES)
    return d.sort_values(["levels_apart", "id", "variable"], ascending=[False, True, True])


def pct(part, whole):
    return f"{100 * part / whole:.0f}%" if whole else "n/a"


def report(kind, scoring_dir):
    id_col, labels = SHEETS[kind]
    a = load_sheet(Path(scoring_dir) / f"{kind}_{PEOPLE[0]}.csv", id_col)
    b = load_sheet(Path(scoring_dir) / f"{kind}_{PEOPLE[1]}.csv", id_col)
    pairs, unscored = pair_scores(a, b, labels)
    s = agreement_stats(pairs)
    dis = disagreements(pairs)

    single = len(a) - len(shared_ids(a))
    lines = [f"# Scoring agreement: {kind}", "",
             f"- Scores compared: {s['n']} (row and variable pairs scored by both of you)",
             f"- Rows scored by only one of you by design (assigned_to is not 'both'), not compared: {single}",
             f"- Shared-row scores not compared because at least one of you left them blank: {unscored}",
             f"- **Exact agreement:** {s['exact']} of {s['n']} ({pct(s['exact'], s['n'])})",
             f"- **One level apart:** {s['one_apart']} ({pct(s['one_apart'], s['n'])})",
             f"- **Two levels apart (low vs high):** {s['two_apart']} ({pct(s['two_apart'], s['n'])})",
             f"- {kappa_sentence(s['kappa'])}", ""]
    if 0 < s["n"] < 30:
        lines += ["Note: with fewer than about 30 compared scores, kappa can swing a lot. Treat it as rough.", ""]

    lines += ["## By variable", "", "| Variable | Compared | Exact | One apart | Two apart |",
              "| --- | --- | --- | --- | --- |"]
    for var in VARIABLES:
        v = agreement_stats(pairs[pairs.variable == var])
        lines.append(f"| {var} | {v['n']} | {v['exact']} | {v['one_apart']} | {v['two_apart']} |")

    lines += ["", f"## Disagreements to settle ({len(dis)})", ""]
    if len(dis):
        cols = list(dis.columns)
        lines += ["| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]
        lines += ["| " + " | ".join(str(r[c]) for c in cols) + " |" for _, r in dis.iterrows()]
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n", dis


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=sorted(SHEETS))
    parser.add_argument("--dir", default=ROOT / "scoring", help="folder holding the two sheets")
    parser.add_argument("--write", action="store_true", help="save the report and disagreement list in results/")
    args = parser.parse_args()

    text, dis = report(args.kind, args.dir)
    print(text)
    if args.write:
        out = ROOT / "results"
        (out / f"agreement_{args.kind}.md").write_text(text, encoding="utf-8")
        dis.to_csv(out / f"disagreements_{args.kind}.csv", index=False)


if __name__ == "__main__":
    main()
