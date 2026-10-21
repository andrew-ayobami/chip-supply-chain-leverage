"""Build the blank scoring sheets in scoring/ (one per person, so neither sees the other's scores).

Every score cell is left empty. Refuses to overwrite a sheet that already holds any score.
Run from the repo root:  python src/make_scoring_sheets.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SCORING = ROOT / "scoring"
CHOKEPOINT_ROWS = ROOT / "results" / "chokepoint_rows.csv"

PEOPLE = ["andrew", "ayodele"]
VARIABLES = ["concentration", "substitutability", "time_to_replace",
             "cohesion", "dependence_on_target", "state_control"]
TAIL = ["evidence", "sources"]

# Who scores which chokepoint row (Andrew, 2026-10-21): a shared set both score, for the
# agreement figure; the rest split. Fixed seed so the draw can be repeated.
SHARED_ROWS = 10
SEED = 20261021

# Cases from research_plan.md, Step 3. "target" is the side the leverage was aimed at
# (draft wording; Andrew and Ayodele to confirm before scoring).
CASES = [
    ("K1", "Arab oil embargo, 1973-74", "Arab oil producers (OAPEC)",
     "US, Netherlands and other states seen as backing Israel"),
    ("K2", "CIPEC, from 1967", "Copper exporters", "Copper-importing countries"),
    ("K3", "International Tin Council, 1985", "Tin producers, with consumer members", "Tin buyers (world market)"),
    ("K4", "China's rare-earth squeeze on Japan, 2010", "China", "Japan"),
    ("K5", "Japan's materials restrictions on Korea, 2019-2023", "Japan", "South Korea"),
]


def cases_sheet():
    df = pd.DataFrame(CASES, columns=["case_id", "case", "who_used_leverage", "target"])
    df.insert(1, "assigned_to", "both")  # reading is split; both score every case
    return add_blank_score_columns(df)


def chokepoints_sheet():
    rows = pd.read_csv(CHOKEPOINT_ROWS)
    df = rows[["row_id", "country", "step", "input", "share", "year"]].copy()
    df.insert(df.columns.get_loc("year") + 1, "target", "United States")
    df.insert(1, "assigned_to", assign_rows(df))
    return add_blank_score_columns(df)


def assign_rows(df):
    """One random row per country plus random top-ups make the shared set; the rest alternate."""
    shared = set(df.groupby("country").sample(n=1, random_state=SEED).row_id)
    if len(shared) > SHARED_ROWS:
        raise ValueError(f"{len(shared)} countries but only {SHARED_ROWS} shared rows")
    rest = df[~df.row_id.isin(shared)]
    shared |= set(rest.sample(n=SHARED_ROWS - len(shared), random_state=SEED).row_id)
    out, turn = [], 0
    for row_id in df.row_id:
        if row_id in shared:
            out.append("both")
        else:
            out.append(PEOPLE[turn % 2])
            turn += 1
    return out


def add_blank_score_columns(df):
    for col in VARIABLES + TAIL:
        df[col] = ""
    return df


def has_scores(path):
    if not path.exists():
        return False
    existing = pd.read_csv(path, dtype=str).fillna("")
    present = [c for c in VARIABLES if c in existing.columns]
    return (existing[present].apply(lambda s: s.str.strip()) != "").any().any()


def main():
    SCORING.mkdir(exist_ok=True)
    sheets = {"cases": cases_sheet(), "chokepoints": chokepoints_sheet()}
    for kind, sheet in sheets.items():
        for person in PEOPLE:
            path = SCORING / f"{kind}_{person}.csv"
            if has_scores(path):
                print(f"skipped {path.name}: it already holds scores")
                continue
            sheet.to_csv(path, index=False)
            print(f"wrote {path.name} ({len(sheet)} rows, score cells empty)")


if __name__ == "__main__":
    main()
