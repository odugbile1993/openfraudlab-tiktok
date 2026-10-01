# OpenFraudLab TikTok — "Data Science from Scratch"

AI-voiced, captioned vertical lesson videos (1080x1920, 60–90s) for TikTok **@_drhola**, by **Ayodele Odugbile · OpenFraudLab**. Videos in `videos/` are hosted here so Metricool can fetch them by public URL.

## Daily pipeline (what each scheduled run does)

1. Read `state.json` → `next_lesson` (N). Make lessons N, N+1, N+2 from `curriculum.json`. If the curriculum runs out, append new lessons that continue the series logically (intermediate data science / ML, with credit, fraud and finance examples where natural).
2. Write each lesson spec as `lessons/dsNN.json` (NN = 2-digit lesson number), matching the format of `lessons/ds02.json`:
   - `series`: "Data Science from Scratch", `lesson`: N
   - 8–9 slides, each `{tag, text, sub?, size?, say}`; `say` is the narration (spoken, natural, ~70–90s total).
   - Slide 1 hook: tag `LESSON N`, size 86–90, narration starts "Data Science from Scratch, lesson N: ..."
   - Second-to-last slide: tag `NEXT LESSON`, teasing lesson N+1's title.
   - Last slide is always exactly:
     `{"tag": "THANKS FOR WATCHING", "text": "Follow, like & share for more", "size": 92, "sub": "Ayodele Odugbile · OpenFraudLab", "say": "Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab."}`
   - Keep `text` short (fits ~4 lines at size 78). Spell numbers out in `say` ("one point five"), write "AI" as "AI".
   - Accuracy matters: no invented statistics, quotes, studies or tools. Hedge general claims ("often", "usually").
3. Render: `python3 scripts/narrate.py lessons/dsNN.json videos/dsNN_<slug>.mp4 am_michael`
   - Needs `pip install --break-system-packages kokoro-onnx soundfile` and the voice model in `tts/` (gitignored):
     `curl -sSL -C - -o tts/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx` (≈325 MB; repeat the same command with `-C -` if the connection resets until it loads) and `.../voices-v1.0.bin` (≈28 MB).
   - Check each video with ffprobe (has video + audio, 50–120 s).
4. Commit and push the specs and videos to `main`. Public URL pattern:
   `https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/videos/<file>.mp4`
5. Schedule each in Metricool (brand blogId `7180686`, timezone `Africa/Lagos`, provider `tiktok`) at 08:00, 13:00 and 20:00 Lagos time the same day, with `tiktokData.isAigc: true`, `autoPublish: true`, and a caption (see below).
6. Bump `state.json` → `next_lesson` = N+3, add the scheduled posts to `log`, commit and push.

## Caption format
`Data Science from Scratch, Lesson N: <title> <one emoji> <short hook / follow CTA>`
newline, then hashtags: `#datascience #learnontiktok` + 3–4 topical tags + `#datasciencefromscratch #OpenFraudLab`
