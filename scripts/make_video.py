"""Render a captioned vertical (1080x1920) TikTok lesson video with PIL + ffmpeg."""
import subprocess, sys, json
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 24
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BG_TOP, BG_BOT = (12, 18, 38), (32, 20, 64)
ACCENT = (0, 214, 170)
WHITE = (245, 247, 250)
MUTED = (170, 178, 200)
BRAND = "OpenFraudLab"
AUTHOR = "Ayodele Odugbile"

def wrap(draw, text, font, max_w):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            test = (cur + " " + w).strip()
            if draw.textlength(test, font=font) <= max_w:
                cur = test
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines

def base_bg():
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(BG_TOP[i] * (1 - t) + BG_BOT[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img

def render_slide(bg, slide, series, lesson_no, total):
    img = bg.copy()
    d = ImageDraw.Draw(img)
    # header
    hf = ImageFont.truetype(BOLD, 40)
    d.text((80, 150), BRAND.upper(), font=hf, fill=ACCENT)
    d.text((80, 205), f"{series}  ·  Lesson {lesson_no}", font=ImageFont.truetype(REG, 38), fill=MUTED)
    # tag (section label)
    if slide.get("tag"):
        tf = ImageFont.truetype(BOLD, 36)
        tw = d.textlength(slide["tag"], font=tf)
        d.rounded_rectangle([80, 520, 80 + tw + 60, 590], radius=35, fill=ACCENT)
        d.text((110, 533), slide["tag"], font=tf, fill=(10, 20, 30))
    # main text
    size = slide.get("size", 78)
    mf = ImageFont.truetype(BOLD, size)
    lines = wrap(d, slide["text"], mf, W - 160)
    y = 650
    for ln in lines:
        d.text((80, y), ln, font=mf, fill=WHITE)
        y += int(size * 1.28)
    # sub text
    if slide.get("sub"):
        sf = ImageFont.truetype(REG, 50)
        y += 40
        for ln in wrap(d, slide["sub"], sf, W - 160):
            d.text((80, y), ln, font=sf, fill=MUTED)
            y += 68
    # footer
    d.line([(80, H - 260), (W - 80, H - 260)], fill=(70, 80, 110), width=2)
    d.text((80, H - 230), AUTHOR, font=ImageFont.truetype(BOLD, 40), fill=WHITE)
    d.text((80, H - 175), BRAND, font=ImageFont.truetype(REG, 36), fill=ACCENT)
    return img

def main(spec_path, out_path):
    spec = json.load(open(spec_path))
    bg = base_bg()
    slides = spec["slides"]
    total = sum(s["dur"] for s in slides)
    rendered = [render_slide(bg, s, spec["series"], spec["lesson"], total) for s in slides]
    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
         "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-movflags", "+faststart", out_path],
        stdin=subprocess.PIPE)
    elapsed = 0.0
    fade = int(FPS * 0.35)
    for idx, (s, img) in enumerate(zip(slides, rendered)):
        n = int(s["dur"] * FPS)
        for f in range(n):
            frame = img
            if f < fade:  # fade in from background
                frame = Image.blend(bg, img, (f + 1) / fade)
            frame = frame.copy()
            d = ImageDraw.Draw(frame)
            prog = (elapsed + f / FPS) / total
            d.rectangle([0, H - 14, int(W * prog), H], fill=ACCENT)
            proc.stdin.write(frame.tobytes())
        elapsed += s["dur"]
    proc.stdin.close(); proc.wait()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
