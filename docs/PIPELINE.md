# Automation pipeline (for the daily scheduled task)

AI-voiced, captioned vertical lesson videos (1080x1920, 60–90s) for TikTok **@_drhola**, by **Ayodele Odugbile · OpenFraudLab**. The root `README.md` is the public, learner-facing course page — don't rewrite it beyond what `build_site.py` updates. Videos in `videos/` are hosted here so Metricool can fetch them by public URL.

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
   - Also add two top-level fields used for the learner notes on GitHub:
     `summary` (1–2 sentence recap of the lesson) and `practice` (one small, concrete exercise a beginner can do without special software or data).
3. Render: `python3 scripts/narrate.py lessons/dsNN.json videos/dsNN_<slug>.mp4 am_michael`
   - Needs `pip install --break-system-packages kokoro-onnx soundfile` and the voice model in `tts/` (gitignored):
     `curl -sSL -C - -o tts/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx` (≈325 MB; repeat the same command with `-C -` if the connection resets until it loads) and `.../voices-v1.0.bin` (≈28 MB).
   - Check each video with ffprobe (has video + audio, 50–120 s).
4. Run `python3 scripts/build_site.py` to regenerate `notes/` and the course table in the root `README.md` (never hand-edit the table between the `COURSE-TABLE` markers). Then commit and push the specs, videos, notes and README to `main`. Public URL pattern:
   `https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/videos/<file>.mp4`
5. Schedule each in Metricool (brand blogId `7180686`, timezone `Africa/Lagos`, provider `tiktok`) at 08:00, 13:00 and 20:00 Lagos time the same day, with `autoPublish: true`, `tiktokData.title` (REQUIRED — e.g. "Lesson N: <short title>"), `tiktokData.isAigc: true`, `privacyOption: PUBLIC_TO_EVERYONE`, media = the raw GitHub URL, and a caption (see below). Metricool copies the video to its own storage when you schedule, so the push in step 4 must finish first.
6. **Website quizzes (Supabase).** For each new lesson, write 5 multiple-choice questions (4 options each, exactly one correct, plain beginner language, each with a one-sentence explanation) that test only what the lesson taught. Load them with the Supabase connector's `execute_sql` on project `virxrqwxvgsbcnmhdwlp`:
   - `update public.lessons set released = true, video_url = 'https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/videos/<file>.mp4', video_seconds = <whole seconds from ffprobe> where course_slug = 'data-science' and n = N;` (the Academy lesson player plays this video and requires it to be watched before the notes and quiz unlock, so video_url and video_seconds must be correct) (for lessons above 30, first `insert into public.lessons (course_slug, n, title, released, video_url, video_seconds) values ('data-science', N, '<title>', true, '<url>', <secs>)`; they are bonus lessons and don't change certificate requirements).
   - For each question at position P (1–5), with `correct_index` 0–3:
     `with ins as (insert into public.quiz_questions (course_slug, lesson_n, position, question, options, explanation) values ('data-science', N, P, '<question>', '["A","B","C","D"]'::jsonb, '<explanation>') returning id) insert into private.quiz_answers (question_id, correct_index) select id, <correct_index> from ins;`
   - Escape single quotes by doubling them. Vary which option is correct across questions.
   - Check: `select lesson_n, count(*) from public.quiz_questions where course_slug='data-science' group by 1 order by 1;` shows 5 for each new lesson.
   - **Never commit quiz answers to this repo**: the repo is public and the answers must stay private.
7. Bump `state.json` → `next_lesson` = N+3, add the scheduled posts to `log`, commit and push.

## Website
The Open Fraud Labs Academy at https://openfraudlabs.com/academy/ (repo OpenFraudLabs/lab-docs) reads `curriculum.json` and `state.json` from this repo to list lessons, and uses Supabase for accounts, quizzes and certificates. No website edits are needed for daily lessons.

## Caption format
Professional, confident, beginner-friendly tone (a data professional teaching, not hype). Three short lines, then hashtags:

```
Lesson N · <Title> | Data Science from Scratch
<One-sentence takeaway a beginner gets from this lesson.>
Follow @_drhola for 3 data science lessons a day 📊 Like & share if this helped.

#datascience #machinelearning #learnontiktok <2–3 topical tags> #datasciencefromscratch #OpenFraudLab
```
Max one emoji. No clickbait, no exaggerated claims.
