"""Print every code segment's real output and the narration around it, plus word counts.
Use it to check that each run_say matches the output exactly.  python3 scripts/lesson_report.py longform/ds05.json"""
import json, sys, os
sys.argv, path = [sys.argv[0]], sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import longform as lf
import pandas as pd
spec = json.load(open(path))
words = 0
for ch in spec["chapters"]:
    for g in ch["segments"]:
        for k in ("say", "run_say"):
            if k in g: words += len(g[k].split())
        for st in g.get("steps", []): words += len(st["say"].split())
        if g["type"] == "code":
            printed, val, fig = lf.run_code(g["code"])
            print("=" * 70); print(g["code"]); print("--- output ---")
            if printed: print(printed.rstrip())
            if fig is not None: print("[chart]")
            elif val is not None:
                if hasattr(val, "item") and getattr(val, "ndim", 1) == 0: val = val.item()
                print(val.to_string() if isinstance(val, (pd.DataFrame, pd.Series)) else repr(val))
            print("--- run_say ---"); print(g["run_say"])
print("=" * 70)
print(f"narration words: {words} (aim 1,450-1,550 for about 10 minutes)")
print(f"chapters: {len(spec['chapters'])}, code segments: {sum(1 for c in spec['chapters'] for g in c['segments'] if g['type']=='code')}, exercises: {len(spec.get('exercises', []))}")
