"""Build a Colab/Jupyter notebook for a long-form lesson: python3 scripts/make_notebook.py longform/ds01.json"""
import json, os, sys

DATA_URL = "https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/data/loans.csv"

def md(text): return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n").splitlines(True)}
def code(text): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text.strip("\n").splitlines(True)}

def build(spec):
    n = spec["lesson"]
    cells = [md(f"# Lesson {n}: {spec['title']}\n\n"
                f"**Data Science from Scratch** · Open Fraud Labs Academy · Ayodele Odugbile\n\n"
                f"Follow along with the video lesson at [openfraudlabs.com/academy](https://openfraudlabs.com/academy/). "
                f"Run each cell with **Shift + Enter**.\n\n"
                "**In this lesson you will:**\n\n" + "\n".join(f"- {o}" for o in spec["objectives"]))]
    for ch in spec["chapters"]:
        codes = [s for s in ch["segments"] if s["type"] == "code"]
        if not codes: continue
        cells.append(md(f"## {ch['title']}"))
        for s in codes:
            cells.append(md(s["say"]))
            cells.append(code(s["code"]))
    exs = spec.get("exercises") or [spec["practice"]]
    cells.append(md("## Practice\n\nTry each exercise, then run the check cell under it. "
                    "`DATA_URL` is the address of the practice dataset."))
    cells.append(code(f'DATA_URL = "{DATA_URL}"'))
    for i, p in enumerate(exs, 1):
        cells.append(md(f"### Exercise {i}: {p['title']}\n\n{p['prompt']}\n\n*Hint: {p['hint']}*"))
        cells.append(code(p["starter"]))
        cells.append(code("# Check your answer\n" + p["check"] + 'print("Correct! Well done.")'))
    cells.append(md("---\nIf this helped, follow **@_drhola** on TikTok, like and share the lesson, and comment with your questions. "
                    "Then take the lesson quiz on [openfraudlabs.com/academy](https://openfraudlabs.com/academy/)."))
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                         "language_info": {"name": "python"}, "colab": {"provenance": []}},
            "nbformat": 4, "nbformat_minor": 5}

if __name__ == "__main__":
    for path in sys.argv[1:]:
        spec = json.load(open(path))
        out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(path))), "notebooks", f"lesson-{spec['lesson']:02d}.ipynb")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump(build(spec), open(out, "w"), indent=1)
        print(out)
