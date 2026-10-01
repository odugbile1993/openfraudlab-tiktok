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
6. **Academy lesson (long-form, one per run).** The website plays the full ~10-minute lessons, not the TikTok cuts, so this step never touches Supabase for the TikTok lessons above. Take M = `state.json` → `academy_next`. If `M` is greater than the highest TikTok lesson that exists, skip this step.
   - Read `docs/LONGFORM.md`, then `longform/ds02.json` and `longform/ds03.json` as the quality bar. Write `longform/dsMM.json` for lesson M with the title from `curriculum.json`: 7–9 chapters, 1,350–1,500 words of narration in total (about 10 minutes), at least 6 code segments on `data/loans.csv` (use `data/loans_raw.csv` for cleaning lessons), two or three "Quick check" pauses, a practice segment, recap and the standard outro (quiz, follow Open Fraud Labs, like, share, comment). Add three `exercises` (each with starter, solution, check, hint) and the Markdown `reading`.
   - Install pandas 2.3.3 (`pip install --break-system-packages pandas==2.3.3`) so outputs match the in-browser lab. Run each code segment yourself first, and make every number in `say`/`run_say` and `reading` match the real output exactly. Never state a figure you didn't compute.
   - `python3 scripts/validate_longform.py longform/dsMM.json` must print OK (code runs, every starter fails its check, every solution passes). Do not continue until it does.
   - Render `python3 scripts/longform.py longform/dsMM.json videos/long/dsMM_<slug>.mp4` (about 20–30 minutes) and `python3 scripts/make_notebook.py longform/dsMM.json`. Check with ffprobe (1920x1080, video + audio, 540–720 s) and look at the extracted frame of every code segment (the script prints the frames folder) to confirm the output fits on screen.
   - Commit and push `longform/`, `videos/long/` and `notebooks/`, and confirm the video's raw URL returns HTTP 200.
   - Supabase (`execute_sql`, project `virxrqwxvgsbcnmhdwlp`): `update public.lessons set released = true, video_url = 'https://raw.githubusercontent.com/Odugbile1993/openfraudlab-tiktok/main/videos/long/<file>.mp4', video_seconds = <whole seconds> where course_slug = 'data-science' and n = M;` then add 7 multiple-choice questions (4 options, exactly one correct, one-sentence explanation, at least two about the code) using:
     `with ins as (insert into public.quiz_questions (course_slug, lesson_n, position, question, options, explanation) values ('data-science', M, P, '<question>', '["A","B","C","D"]'::jsonb, '<explanation>') returning id) insert into private.quiz_answers (question_id, correct_index) select id, <correct_index> from ins;`
     Escape single quotes by doubling them, vary the correct position, and check with `select lesson_n, count(*) from public.quiz_questions where course_slug='data-science' group by 1 order by 1;`.
   - **Never commit quiz answers to this repo**: the repo is public and the answers must stay private.
   - Only after all of the above succeeds, set `academy_next` = M+1. If anything fails, leave the lesson unreleased and report exactly what failed.
7. Bump `state.json` → `next_lesson` = N+3 (and `academy_next` if step 6 succeeded), add the scheduled posts to `log`, commit and push.

## Website
The Open Fraud Labs Academy at https://openfraudlabs.com/academy/ (repo OpenFraudLabs/lab-docs) reads `curriculum.json`, `state.json` and `longform/dsNN.json` (reading notes and practice exercises) from this repo, and uses Supabase for accounts, lesson release, video, quizzes and certificates. A lesson appears in the Academy only when it is released in Supabase with its long-form video. No website code edits are needed for daily lessons.

## Caption format
Professional, confident, beginner-friendly tone (a data professional teaching, not hype). Three short lines, then hashtags:

```
Lesson N · <Title> | Data Science from Scratch
<One-sentence takeaway a beginner gets from this lesson.>
Follow @_drhola for 3 data science lessons a day 📊 Like & share if this helped.

#datascience #machinelearning #learnontiktok <2–3 topical tags> #datasciencefromscratch #OpenFraudLab
```
Max one emoji. No clickbait, no exaggerated claims.
