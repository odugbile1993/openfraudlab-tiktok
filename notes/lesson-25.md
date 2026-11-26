# Lesson 25: Feature engineering

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Feature engineering creates or reshapes input columns so patterns are easier to learn: extracting parts of dates, building ratios and counts, and encoding categories. Only use information that is available at prediction time, to avoid leakage.

## Key ideas

- **The idea:** Raw data into signals — Features are the model's inputs
- **From dates:** Timestamp to hour — Night-time activity can matter
- **Ratios:** Amount / usual amount — Context beats raw numbers
- **Counts:** Payments in last hour — Aggregates capture behaviour
- **Categories:** One-hot encoding — One column per category
- **Watch out:** Don't leak the answer — Use only what's known in time

## Try it yourself

Write down a timestamp such as 2026-11-26 23:45. List three features you could create from it (for example hour of day, day of week, is it a weekend) and say which one might help spot unusual card activity, and why.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty five: feature engineering, turning raw data into inputs a model can actually learn from.

A feature is any input column your model uses. Feature engineering means creating or reshaping those columns, so the patterns you care about are easier for the model to see.

Take a transaction timestamp. On its own, a long date string tells a model very little. But pull out the hour of day, or the day of the week, and the model can learn that activity at unusual hours may be riskier.

Ratios add context. A payment of fifty thousand naira means different things for different customers. Dividing it by that customer's usual payment shows how unusual it is for them.

Counts and aggregates capture behaviour over time, like the number of payments on a card in the last hour. A sudden burst of activity is something fraud teams often look for.

Many models need numbers, so categories get encoded. One-hot encoding turns a column like payment method into separate yes or no columns, one per category, without inventing a fake order.

One big warning: data leakage. Only build features from information that would really be available at prediction time. If a feature secretly contains the answer, your test score looks great, and the real model disappoints.

Next lesson: cross-validation, a fairer way to test how well your model really performs.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 24](lesson-24.md) · [Lesson 26 →](lesson-26.md)
