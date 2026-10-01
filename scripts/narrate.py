"""Generate per-slide AI narration with Kokoro, time slides to it, render video, mux audio."""
import json, sys, os, subprocess, tempfile, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

spec_path, out_path, voice = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "am_michael")
spec = json.load(open(spec_path))
HERE = os.path.dirname(os.path.abspath(__file__))
TTS = os.environ.get("TTS_DIR", os.path.join(HERE, "..", "tts"))
TMP = tempfile.mkdtemp()
k = Kokoro(os.path.join(TTS, "kokoro-v1.0.onnx"), os.path.join(TTS, "voices-v1.0.bin"))

LEAD, TAIL = 0.35, 0.55  # silence before speech (lets slide fade in) and after
chunks, sr = [], 24000
for s in spec["slides"]:
    audio, sr = k.create(s["say"], voice=voice, speed=1.0, lang="en-us")
    lead = np.zeros(int(LEAD * sr), dtype=np.float32)
    tail = np.zeros(int(TAIL * sr), dtype=np.float32)
    seg = np.concatenate([lead, audio.astype(np.float32), tail])
    s["dur"] = len(seg) / sr
    chunks.append(seg)
full = np.concatenate(chunks)
sf.write(os.path.join(TMP, "narration.wav"), full, sr)

timed = os.path.join(TMP, "timed.json")
json.dump(spec, open(timed, "w"))
subprocess.run(["python3", os.path.join(HERE, "make_video.py"), timed, os.path.join(TMP, "silent.mp4")], check=True)

# polish voice (light EQ + loudness for social, ~-14 LUFS) and mux
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(TMP, "silent.mp4"),
                "-i", os.path.join(TMP, "narration.wav"), "-map", "0:v", "-map", "1:a",
                "-af", "highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=2,loudnorm=I=-14:TP=-1.5:LRA=11",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest",
                "-movflags", "+faststart", out_path], check=True)
print(f"total {sum(s['dur'] for s in spec['slides']):.1f}s")
