"""Render a long-form (16:9) lesson from longform/dsNN.json.

Every code segment is executed for real (in one shared namespace, like a notebook)
and the actual output is drawn on screen, so nothing in the video is made up.

Usage: python3 scripts/longform.py longform/ds01.json videos/long/ds01.mp4 [voice]
Env:   TTS_DIR (kokoro model folder), FONT_DIR (IBM Plex .ttf files)
"""
import ast, hashlib, io, json, os, subprocess, sys, tempfile, contextlib
import numpy as np, soundfile as sf
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from pygments.lexers import PythonLexer
from pygments.token import Token

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
def _first(*paths):
    return next((p for p in paths if os.path.exists(p)), paths[0])
TTS = os.environ.get("TTS_DIR") or _first(os.path.join(ROOT, "tts", "kokoro-v1.0.onnx"), os.path.join(ROOT, "..", "tts", "kokoro-v1.0.onnx")).rsplit(os.sep, 1)[0]
FONTS = os.environ.get("FONT_DIR", os.path.join(ROOT, "assets", "fonts"))
DATA_URL = "https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/data/loans.csv"
LOCAL_DATA = os.path.join(ROOT, "data", "loans.csv")

W, H, RAIL = 1920, 1080, 440
MX0, MX1 = RAIL + 110, W - 110          # main content left/right
INK, PAPER, BLUE, GREEN, AMBER = "#0E1A2B", "#FAFBFD", "#2453E6", "#0E9F6E", "#B45309"
MUTED, LINE, NAVY2 = "#5B6B82", "#DCE3EE", "#16263D"
EDITOR, EDITOR2 = "#0F1724", "#162033"
CACHE = os.environ.get("VOICE_CACHE", os.path.join(ROOT, ".voice_cache"))
os.makedirs(CACHE, exist_ok=True)
SR, LEAD, TAIL = 24000, 0.45, 0.75

def F(w, size):
    names = {"r": "IBMPlexSans-Regular", "m": "IBMPlexSans-Medium", "s": "IBMPlexSans-SemiBold",
             "b": "IBMPlexSans-Bold", "mono": "IBMPlexMono-Regular", "monom": "IBMPlexMono-Medium"}
    return ImageFont.truetype(os.path.join(FONTS, names[w] + ".ttf"), size)

def wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = wd
    if cur: lines.append(cur)
    return lines

def text_block(draw, xy, text, font, fill, width, gap=1.28):
    x, y = xy
    for ln in wrap(draw, text, font, width):
        draw.text((x, y), ln, font=font, fill=fill)
        y += int(font.size * gap)
    return y

# ---------- code execution (real) ----------
NS = {}
def run_code(src):
    src = src.replace(DATA_URL, LOCAL_DATA).replace(DATA_URL.rsplit("/", 1)[0] + "/", os.path.dirname(LOCAL_DATA) + "/")
    tree = ast.parse(src)
    last = None
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        last = ast.Expression(tree.body.pop().value)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(tree, "<lesson>", "exec"), NS)
        val = eval(compile(last, "<lesson>", "eval"), NS) if last else None
    return buf.getvalue(), val

# ---------- syntax colours (one-dark style) ----------
def tok_colour(t):
    if t in Token.Keyword or t in Token.Keyword.Namespace: return "#C792EA"
    if t in Token.Name.Builtin: return "#82AAFF"
    if t in Token.Name.Function: return "#82AAFF"
    if t in Token.Literal.String: return "#C3E88D"
    if t in Token.Literal.Number: return "#F78C6C"
    if t in Token.Comment: return "#6B7A90"
    if t in Token.Operator or t in Token.Punctuation: return "#89DDFF"
    return "#E6EDF7"

class Lesson:
    def __init__(self, spec):
        self.s = spec
        self.chapters = [c["title"] for c in spec["chapters"]]

    # rail + background, shared by every frame
    def base(self, chap, progress):
        im = Image.new("RGB", (W, H), PAPER)
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, RAIL, H], fill=INK)
        d.rectangle([56, 64, 74, 82], fill=BLUE)
        d.text((88, 58), "Open Fraud Labs Academy", font=F("s", 24), fill="white")
        d.text((56, 128), f"DATA SCIENCE FROM SCRATCH  ·  LESSON {self.s['lesson']}", font=F("m", 17), fill="#8FA3C0")
        y = text_block(d, (56, 160), self.s["title"], F("s", 34), "white", RAIL - 100, 1.22)
        y += 34
        d.line([56, y, RAIL - 56, y], fill=NAVY2, width=2)
        y += 30
        for i, t in enumerate(self.chapters):
            done, cur = i < chap, i == chap
            if cur:
                d.rounded_rectangle([40, y - 10, RAIL - 40, y + 40], 8, fill=NAVY2)
            if done:
                d.ellipse([56, y + 4, 78, y + 26], fill=GREEN)
                d.line([61, y + 15, 66, y + 20, 74, y + 10], fill="white", width=3)
            else:
                d.ellipse([56, y + 4, 78, y + 26], outline=BLUE if cur else "#3A4C68", width=3)
            d.text((96, y + 1), t, font=F("m" if cur else "r", 23),
                   fill="white" if cur else ("#B8C6DA" if done else "#7487A3"))
            y += 58
        d.text((56, H - 118), "Ayodele Odugbile", font=F("s", 22), fill="white")
        d.text((56, H - 84), "openfraudlabs.com/academy", font=F("r", 19), fill="#8FA3C0")
        # progress
        d.rectangle([RAIL, H - 8, W, H], fill=LINE)
        d.rectangle([RAIL, H - 8, RAIL + int((W - RAIL) * progress), H], fill=BLUE)
        d.text((MX0, 58), self.chapters[chap].upper(), font=F("s", 18), fill=BLUE)
        return im, d

    # ----- segment frames -----
    def title(self, d):
        d.text((MX0, 300), f"Lesson {self.s['lesson']}", font=F("s", 30), fill=BLUE)
        y = text_block(d, (MX0, 350), self.s["title"], F("b", 84), INK, MX1 - MX0, 1.12)
        y = text_block(d, (MX0, y + 20), self.s["subtitle"], F("r", 38), MUTED, MX1 - MX0)
        d.line([MX0, y + 40, MX0 + 120, y + 40], fill=BLUE, width=6)
        d.text((MX0, y + 80), "Ayodele Odugbile  ·  Open Fraud Labs", font=F("m", 28), fill=INK)

    def slide(self, d, seg, upto):
        d.text((MX0, 110), seg["heading"], font=F("b", 58), fill=INK)
        steps = seg["steps"]
        y = 230 if len(steps) <= 4 else 215
        gap = 34 if len(steps) <= 4 else 18
        for i, st in enumerate(steps[:upto + 1]):
            cur = i == upto
            col = INK if cur else "#3A4A60"
            if seg.get("numbered"):
                d.ellipse([MX0, y + 2, MX0 + 46, y + 48], fill=BLUE if cur else "#E6ECF7")
                n = str(i + 1)
                f = F("s", 24)
                d.text((MX0 + 23 - d.textlength(n, font=f) / 2, y + 9), n, font=f, fill="white" if cur else BLUE)
            else:
                d.rounded_rectangle([MX0 + 8, y + 14, MX0 + 26, y + 32], 4, fill=BLUE if cur else "#AFC0E0")
            x = MX0 + 72
            y2 = text_block(d, (x, y), st["bullet"], F("s" if cur else "m", 40), col, MX1 - x, 1.2)
            if st.get("sub"):
                y2 = text_block(d, (x, y2 + 2), st["sub"], F("r", 28), MUTED, MX1 - x, 1.25)
            y = y2 + gap

    def big(self, d, seg):
        y = 300
        d.line([MX0, y, MX0 + 120, y], fill=BLUE, width=8)
        y = text_block(d, (MX0, y + 50), seg["text"], F("b", 70), INK, MX1 - MX0, 1.16)
        if seg.get("sub"):
            text_block(d, (MX0, y + 30), seg["sub"], F("r", 36), MUTED, MX1 - MX0 - 80)

    def code(self, d, im, seg, result):
        x0, x1 = MX0, MX1
        lines = seg["code"].split("\n")
        longest = max(lines, key=len)
        size = 30
        while size > 16 and d.textlength("00  " + longest, font=F("mono", size)) > (x1 - x0) - 70:
            size -= 1
        mono = F("mono", size)
        lh = int(mono.size * 1.55)
        top = 110
        h = 70 + lh * len(lines) + 30
        d.rounded_rectangle([x0, top, x1, top + h], 14, fill=EDITOR)
        d.rounded_rectangle([x0, top, x1, top + 50], 14, fill=EDITOR2)
        d.rectangle([x0, top + 36, x1, top + 50], fill=EDITOR2)
        for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
            d.ellipse([x0 + 22 + i * 26, top + 18, x0 + 36 + i * 26, top + 32], fill=c)
        d.text((x0 + 120, top + 13), "lesson.py  ·  Python", font=F("r", 19), fill="#8FA3C0")
        y = top + 70
        for ln_no, ln in enumerate(lines, 1):
            d.text((x0 + 28, y), f"{ln_no:>2}", font=mono, fill="#4A5A74")
            x = x0 + 28 + d.textlength("00  ", font=mono)
            for t, v in PythonLexer().get_tokens(ln):
                v = v.rstrip("\n")
                if not v: continue
                d.text((x, y), v, font=mono, fill=tok_colour(t))
                x += d.textlength(v, font=mono)
            y += lh
        if result is None:
            d.text((x0, top + h + 30), "Read the code first, then we run it.", font=F("r", 24), fill=MUTED)
            return
        out_top = top + h + 34
        d.text((x0, out_top), "OUTPUT", font=F("s", 18), fill=GREEN)
        self.output(d, result, x0, out_top + 36, x1)

    def output(self, d, result, x0, y, x1):
        printed, val = result
        if isinstance(val, pd.DataFrame):
            df = val
            cols = list(df.columns[:6])
            more = len(df.columns) - len(cols)
            f, fb = F("mono", 21), F("monom", 21)
            cells = [[str(i) for i in df.index]] + [[str(v) for v in df[c]] for c in cols]
            heads = [""] + [str(c) for c in cols]
            widths = [max(d.textlength(h, font=fb), *(d.textlength(v, font=f) for v in col)) + 34
                      for h, col in zip(heads, cells)]
            rh = 44
            tw = sum(widths)
            d.rounded_rectangle([x0, y, x0 + tw, y + rh * (len(df) + 1)], 8, fill="white", outline=LINE, width=2)
            d.rectangle([x0 + 2, y + 2, x0 + tw - 2, y + rh], fill="#EEF2F9")
            x = x0
            for h, col, w in zip(heads, cells, widths):
                d.text((x + 17, y + 10), h, font=fb, fill=INK)
                for r, v in enumerate(col):
                    d.text((x + 17, y + rh * (r + 1) + 10), v, font=fb if h == "" else f, fill=MUTED if h == "" else INK)
                x += w
            for r in range(1, len(df) + 1):
                d.line([x0 + 2, y + rh * r, x0 + tw - 2, y + rh * r], fill=LINE, width=1)
            if more:
                d.text((x0, y + rh * (len(df) + 1) + 16),
                       f"+ {more} more columns: " + ", ".join(map(str, df.columns[6:])), font=F("r", 22), fill=MUTED)
        elif isinstance(val, pd.Series):
            s = val
            avail = H - 40 - y
            show_head = isinstance(s.name, str) or bool(s.index.name)
            n_rows = len(s) + (1 if show_head else 0)
            rh = max(34, min(52, avail // max(n_rows, 1)))
            size = max(18, min(26, int(rh * 0.5)))
            f, fb = F("mono", size), F("monom", size)
            pad = int((rh - size * 1.2) / 2)
            idx = [str(i) for i in s.index]
            # pandas' own formatting, so the screen matches what learners see
            vals = [v.strip() for v in s.to_frame().to_string(header=False, index=False).split("\n")]
            hn, hv = (str(s.index.name or ""), str(s.name)) if show_head else ("", "")
            w1 = max(d.textlength(t, font=fb) for t in idx + [hn]) + 60
            w2 = max(d.textlength(t, font=f) for t in vals + [hv]) + 60
            tw = w1 + w2
            d.rounded_rectangle([x0, y, x0 + tw, y + rh * n_rows], 8, fill="white", outline=LINE, width=2)
            off = 0
            if show_head:
                d.rectangle([x0 + 2, y + 2, x0 + tw - 2, y + rh], fill="#EEF2F9")
                d.text((x0 + 22, y + pad), hn, font=fb, fill=INK)
                d.text((x0 + w1 + 22, y + pad), hv, font=fb, fill=INK)
                off = 1
            for r, (a, b) in enumerate(zip(idx, vals)):
                yy = y + rh * (r + off)
                if r + off: d.line([x0 + 2, yy, x0 + tw - 2, yy], fill=LINE, width=1)
                d.text((x0 + 22, yy + pad), a, font=fb, fill=INK)
                d.text((x0 + w1 + 22, yy + pad), b, font=f, fill=INK)
        else:
            if hasattr(val, "item") and getattr(val, "ndim", 1) == 0:
                val = val.item()  # numpy scalar -> plain Python number
            txt = (printed or "") + ("" if val is None else repr(val))
            lines = txt.rstrip("\n").split("\n")
            size = 40 if len(txt) < 30 else 28
            while size > 16 and max(d.textlength(l, font=F("mono", size)) for l in lines) > (x1 - x0) - 70:
                size -= 1
            f = F("mono", size)
            bh = int(f.size * 1.5) * len(lines) + 44
            tw = max(d.textlength(l, font=f) for l in lines) + 60
            d.rounded_rectangle([x0, y, x0 + max(tw, 220), y + bh], 8, fill="white", outline=LINE, width=2)
            for i, l in enumerate(lines):
                d.text((x0 + 30, y + 22 + i * int(f.size * 1.5)), l, font=f, fill=INK)

    def practice(self, d, seg):
        d.rounded_rectangle([MX0, 160, MX1, 760], 18, fill="white", outline=LINE, width=2)
        d.rectangle([MX0, 160, MX0 + 10, 760], fill=AMBER)
        d.text((MX0 + 60, 210), "YOUR TURN", font=F("s", 24), fill=AMBER)
        y = text_block(d, (MX0 + 60, 260), seg["task"], F("s", 46), INK, MX1 - MX0 - 120, 1.22)
        y = text_block(d, (MX0 + 60, y + 24), seg["hint"], F("mono", 28), MUTED, MX1 - MX0 - 120)
        d.text((MX0 + 60, 680), "Pause the video  ·  Open the Practice tab  ·  Check your answers", font=F("m", 26), fill=BLUE)

    def outro(self, d, seg):
        d.text((MX0, 150), "NEXT UP", font=F("s", 24), fill=BLUE)
        y = text_block(d, (MX0, 196), seg["next"], F("b", 56), INK, MX1 - MX0, 1.16)
        y += 40
        d.line([MX0, y, MX1, y], fill=LINE, width=2)
        y += 50
        d.text((MX0, y), "Before you go", font=F("s", 30), fill=INK)
        y += 60
        pills = ["Take the lesson quiz", "Follow Open Fraud Labs", "Like", "Share", "Comment your questions"]
        x = MX0
        f = F("m", 28)
        for p in pills:
            w = d.textlength(p, font=f) + 56
            if x + w > MX1:
                x, y = MX0, y + 84
            d.rounded_rectangle([x, y, x + w, y + 62], 31, fill=BLUE if p.startswith("Follow") else "#E6ECF7")
            d.text((x + 28, y + 13), p, font=f, fill="white" if p.startswith("Follow") else BLUE)
            x += w + 18
        y += 130
        d.text((MX0, y), "TikTok  @_drhola", font=F("s", 32), fill=INK)
        d.text((MX0, y + 52), "Notes, quizzes and the code lab:  openfraudlabs.com/academy", font=F("r", 28), fill=MUTED)


def main():
    spec_path, out_path = sys.argv[1], sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "am_michael"
    spec = json.load(open(spec_path))
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(TTS, "kokoro-v1.0.onnx"), os.path.join(TTS, "voices-v1.0.bin"))
    L = Lesson(spec)
    tmp = tempfile.mkdtemp()

    # 1) build the shot list: (chapter, kind, payload, narration)
    shots = []
    for ci, ch in enumerate(spec["chapters"]):
        for seg in ch["segments"]:
            t = seg["type"]
            if t == "slide":
                for si, st in enumerate(seg["steps"]):
                    shots.append((ci, "slide", (seg, si), st["say"]))
            elif t == "code":
                res = run_code(seg["code"])
                shots.append((ci, "code", (seg, None), seg["say"]))
                shots.append((ci, "code", (seg, res), seg["run_say"]))
            else:
                shots.append((ci, t, seg, seg["say"]))

    # 2) narration per shot
    audio, durs = [], []
    for i, (_, _, _, say) in enumerate(shots):
        key = hashlib.sha1(f"{voice}|{say}".encode()).hexdigest()[:16]
        cp = os.path.join(CACHE, key + ".wav")
        if os.path.exists(cp):
            a, sr = sf.read(cp, dtype="float32")
        else:
            a, sr = k.create(say, voice=voice, speed=1.0, lang="en-us")
            sf.write(cp, a, sr)
        seg = np.concatenate([np.zeros(int(LEAD * sr), np.float32), a.astype(np.float32), np.zeros(int(TAIL * sr), np.float32)])
        audio.append(seg); durs.append(len(seg) / sr)
        print(f"  voice {i + 1}/{len(shots)}  {durs[-1]:.1f}s", flush=True)
    sf.write(os.path.join(tmp, "voice.wav"), np.concatenate(audio), SR)
    total = sum(durs)

    # 3) frames
    lines, t = [], 0.0
    for i, ((ci, kind, payload, _), dur) in enumerate(zip(shots, durs)):
        im, d = L.base(ci, (t + dur) / total)
        if kind == "title": L.title(d)
        elif kind == "slide": L.slide(d, *payload)
        elif kind == "big": L.big(d, payload)
        elif kind == "code": L.code(d, im, *payload)
        elif kind == "practice": L.practice(d, payload)
        elif kind == "outro": L.outro(d, payload)
        p = os.path.join(tmp, f"f{i:03d}.png")
        im.save(p)
        lines += [f"file '{p}'", f"duration {dur:.3f}"]
        t += dur
    lines.append(f"file '{p}'")
    open(os.path.join(tmp, "list.txt"), "w").write("\n".join(lines) + "\n")

    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"),
                    "-i", os.path.join(tmp, "voice.wav"), "-map", "0:v", "-map", "1:a",
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "20",
                    "-af", "highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=2,loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", "-movflags", "+faststart", out_path], check=True)
    print(f"done: {out_path}  {total / 60:.1f} min  ({len(shots)} shots)  frames in {tmp}")

if __name__ == "__main__":
    main()
