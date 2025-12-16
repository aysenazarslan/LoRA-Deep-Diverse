"""
eval.py - LiveCodeBench evaluation outputs -> best checkpoint table.
"""
import json
import argparse
from pathlib import Path
import pandas as pd

TOTAL = 41

def best_from_evaluations(eval_dir: str, prefix: str):
    eval_dir = Path(eval_dir)
    files = sorted(eval_dir.glob(f"{prefix}_checkpoint-*_results.json"))
    if not files:
        raise FileNotFoundError(f"No evaluation files found for {prefix} in {eval_dir}")
    rows = []
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            obj = json.load(f)
        stats = obj.get("stats", obj)
        rows.append({
            "model_name": obj.get("model_name", fp.stem.replace("_results","")),
            "pass_at_1": float(stats["pass_at_1"]),
            "passed": int(stats["passed"])
        })
    df = pd.DataFrame(rows)
    return df.loc[df["pass_at_1"].idxmax()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eval_dir", default="results/livecodebench/evaluations")
    ap.add_argument("--out_csv", default="best_checkpoints.csv")
    args = ap.parse_args()

    deep_best = best_from_evaluations(args.eval_dir, "deep_instruction")
    diverse_best = best_from_evaluations(args.eval_dir, "diverse_instruction")

    final = pd.DataFrame([
        {"Model":"deep_instruction",
         "En İyi Checkpoint": deep_best["model_name"].replace("deep_instruction_",""),
         "Pass@1 (%)": round(deep_best["pass_at_1"]*100,1),
         "Çözülen Soru": f'{deep_best["passed"]}/{TOTAL}'},
        {"Model":"diverse_instruction",
         "En İyi Checkpoint": diverse_best["model_name"].replace("diverse_instruction_",""),
         "Pass@1 (%)": round(diverse_best["pass_at_1"]*100,1),
         "Çözülen Soru": f'{diverse_best["passed"]}/{TOTAL}'},
    ])
    final.to_csv(args.out_csv, index=False)
    print(final)

if __name__ == "__main__":
    main()
