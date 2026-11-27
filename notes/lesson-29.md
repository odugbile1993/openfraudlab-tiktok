# Lesson 29: Data ethics and bias in models

**Data Science from Scratch** · Module 5 · Responsible Data Science & Next Steps · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Models learn from historical data, so they can repeat past unfairness. Check who is in the data, watch for proxy features, compare errors across groups, protect privacy, and keep humans involved in high-stakes decisions.

## Key ideas

- **The risk:** Models learn from the past — Including its unfairness
- **Where bias hides:** Bias enters early — Who's in the data?
- **Proxies:** Removing a column isn't enough — Postcode can stand in
- **Check it:** Compare results by group — Errors, approvals, alerts
- **Privacy:** Collect only what you need — Consent · security
- **People first:** Keep humans involved — Let people appeal

## Try it yourself

Pick a model that could decide loan approvals. List three features it might use, and for each one write whether it could act as a proxy for a sensitive attribute like age, gender or location, and why.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty nine: data ethics, and bias in models.

Models learn patterns from historical data. If past decisions were unfair to some group, a model trained on them can learn that unfairness and repeat it, at scale and very quickly.

Bias often enters before any modelling. Maybe some groups are missing from the sample, as in lesson thirteen, or the labels themselves reflect past human judgements rather than the truth.

Dropping a sensitive column, like gender or ethnicity, usually is not enough. Other features, such as postcode or shopping patterns, can act as proxies and carry the same information.

So test for it. Compare your model's results across groups: approval rates, false alarms, and missed cases. If one group gets far more false fraud flags, that is a problem to investigate.

Ethics is also about privacy. Collect only the data you need, use it for the purpose people agreed to, keep it secure, and follow the data protection laws where you work.

For decisions that matter, like loans or blocked accounts, keep a human in the loop where you can, explain decisions clearly, and give people a way to challenge them.

Next lesson: your data science roadmap. Where to go from here.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 28](lesson-28.md) · [Lesson 30 →](lesson-30.md)
