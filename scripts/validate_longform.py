"""Check a long-form lesson before rendering: every code segment runs, every exercise's
starter code fails its check and its solution passes.  python3 scripts/validate_longform.py longform/ds01.json"""
import json, os, sys, io, contextlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL = os.path.join(ROOT, "data", "loans.csv")
URL = "https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/data/loans.csv"

def run(src, ns):
    with contextlib.redirect_stdout(io.StringIO()):
        exec(src.replace(URL, LOCAL), ns)

def check(spec):
    ok = True
    ns = {}
    for ch in spec["chapters"]:
        for sg in ch["segments"]:
            if sg["type"] == "code":
                try: run(sg["code"], ns)
                except Exception as e: ok = False; print("  CODE FAILS:", sg["code"][:40], e)
    exs = spec.get("exercises") or [spec["practice"]]
    for i, ex in enumerate(exs, 1):
        for kind, want in (("starter", False), ("solution", True)):
            ns = {"DATA_URL": LOCAL}
            try:
                run(ex[kind], ns); run(ex["check"], ns); passed = True
            except Exception as e:
                passed = False; msg = e
            if passed != want:
                ok = False; print(f"  exercise {i} {kind}: expected {'pass' if want else 'fail'}", "" if passed else msg)
    print(("OK  " if ok else "FAIL"), spec["lesson"], spec["title"], f"({len(exs)} exercises)")
    return ok

if __name__ == "__main__":
    sys.exit(0 if all([check(json.load(open(p))) for p in sys.argv[1:]]) else 1)
