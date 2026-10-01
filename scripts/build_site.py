"""Build learner-facing study notes and the README course table from lesson specs.

Usage: python3 scripts/build_site.py
- Writes notes/lesson-NN.md for every lesson that has lessons/dsNN.json
- Rewrites the block between <!-- COURSE-TABLE:START --> and <!-- COURSE-TABLE:END --> in README.md
"""
import glob, json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CURRICULUM = json.load(open(os.path.join(ROOT, "curriculum.json")))
SKIP_TAGS = {"NEXT LESSON", "THANKS FOR WATCHING", "NEXT"}

MODULES = [
    (1, 3, "Module 1 · Foundations"),
    (4, 14, "Module 2 · Statistics & Exploring Data"),
    (15, 17, "Module 3 · Tools of the Trade"),
    (18, 27, "Module 4 · Machine Learning Essentials"),
    (28, 30, "Module 5 · Responsible Data Science & Next Steps"),
]

def module_for(n):
    for lo, hi, name in MODULES:
        if lo <= n <= hi:
            return name
    return "Module 6 · Going Further"

def video_for(n):
    hits = sorted(glob.glob(os.path.join(ROOT, "videos", f"ds{n:02d}_*.mp4")))
    return os.path.basename(hits[0]) if hits else None

def spec_for(n):
    p = os.path.join(ROOT, "lessons", f"ds{n:02d}.json")
    return json.load(open(p)) if os.path.exists(p) else None

def clean(t):
    return " ".join(t.replace("\n", " / ").split())

def title_of(n):
    for l in CURRICULUM["lessons"]:
        if l["n"] == n:
            return l["title"]
    s = spec_for(n)
    return clean(s["slides"][0]["text"]) if s else f"Lesson {n}"

def all_numbers():
    nums = {l["n"] for l in CURRICULUM["lessons"]}
    for p in glob.glob(os.path.join(ROOT, "lessons", "ds*.json")):
        m = re.search(r"ds(\d+)\.json$", p)
        if m:
            nums.add(int(m.group(1)))
    return sorted(nums)

def write_note(n, spec, nums):
    title = title_of(n)
    video = video_for(n)
    lines = [f"# Lesson {n}: {title}", "",
             f"**Data Science from Scratch** · {module_for(n)} · by Ayodele Odugbile, OpenFraudLab", ""]
    nav = []
    if video:
        nav.append(f"[▶ Watch the video](../videos/{video})")
    nav.append("[📚 Course map](../README.md#-course-map)")
    lines += [" · ".join(nav), ""]
    if spec.get("summary"):
        lines += ["## In a nutshell", "", spec["summary"], ""]
    key = [s for s in spec["slides"][1:] if s.get("tag", "").upper() not in SKIP_TAGS]
    if key:
        lines += ["## Key ideas", ""]
        for s in key:
            item = f"- **{s['tag'].capitalize()}:** {clean(s['text'])}"
            if s.get("sub"):
                item += f" — {clean(s['sub'])}"
            lines.append(item)
        lines.append("")
    if spec.get("practice"):
        lines += ["## Try it yourself", "", spec["practice"], ""]
    lines += ["## Transcript", "", "<details>", "<summary>Show the full narration</summary>", ""]
    for s in spec["slides"]:
        lines += [s["say"], ""]
    lines += ["</details>", ""]
    i = nums.index(n)
    prev_n = nums[i - 1] if i > 0 and spec_for(nums[i - 1]) else None
    next_n = nums[i + 1] if i + 1 < len(nums) and spec_for(nums[i + 1]) else None
    foot = []
    if prev_n:
        foot.append(f"[← Lesson {prev_n}](lesson-{prev_n:02d}.md)")
    if next_n:
        foot.append(f"[Lesson {next_n} →](lesson-{next_n:02d}.md)")
    if foot:
        lines += ["---", "", " · ".join(foot), ""]
    open(os.path.join(ROOT, "notes", f"lesson-{n:02d}.md"), "w").write("\n".join(lines))

def course_table(nums):
    out, current = [], None
    for n in nums:
        mod = module_for(n)
        if mod != current:
            if current:
                out.append("")
            out += [f"#### {mod}", "", "| # | Lesson | Watch | Study notes |", "|:-:|:--|:-:|:-:|"]
            current = mod
        spec, video = spec_for(n), video_for(n)
        watch = f"[▶ Video](videos/{video})" if video else "🔜 Soon"
        notes = f"[📝 Notes](notes/lesson-{n:02d}.md)" if spec else "—"
        out.append(f"| {n} | {title_of(n)} | {watch} | {notes} |")
    released = sum(1 for n in nums if video_for(n))
    out += ["", f"<sub>{released} of {len(nums)} planned lessons released · new lessons are added daily.</sub>"]
    return "\n".join(out)

def main():
    os.makedirs(os.path.join(ROOT, "notes"), exist_ok=True)
    nums = all_numbers()
    for n in nums:
        spec = spec_for(n)
        if spec:
            write_note(n, spec, nums)
    readme = os.path.join(ROOT, "README.md")
    text = open(readme).read()
    block = "<!-- COURSE-TABLE:START -->\n" + course_table(nums) + "\n<!-- COURSE-TABLE:END -->"
    text = re.sub(r"<!-- COURSE-TABLE:START -->.*?<!-- COURSE-TABLE:END -->", lambda m: block, text, flags=re.S)
    open(readme, "w").write(text)
    print(f"notes for {sum(1 for n in nums if spec_for(n))} lessons; table has {len(nums)} rows")

if __name__ == "__main__":
    main()
