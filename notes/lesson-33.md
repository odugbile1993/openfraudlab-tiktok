# Lesson 33: Project 1 · Part 3: Credit risk — a default model and an approval policy

**Data Science from Scratch** · Module 6 · Going Further · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Split by time (train on the past, test on the future), fit a logistic regression to get default probabilities, check ranking quality with AUC, then turn scores into an approval policy by choosing a cut-off that balances missed defaults against lost good customers.

## Key ideas

- **Split by time:** Train 2024, test 2025 — Past → future
- **The model:** Logistic regression — A probability of default
- **How good?:** AUC ≈ 0.72 — 0.5 = guessing · 1 = perfect
- **Score to policy:** Pick a cut-off — Decline or review the riskiest
- **The trade-off:** Fewer defaults, fewer loans — Riskiest 20%: about half of defaults
- **Write it up:** Explain your decision — Question · data · method · limits

## Try it yourself

A lender loses 1,000 when a loan defaults and earns 150 on a loan that is repaid. Out of 100 applicants, a cut-off would decline 20 people: 5 who would default and 15 who would repay. Work out whether declining that group gains or loses money overall.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson thirty-three: project one, part three. A default model, and an approval policy.

First, split by time. Train on the 2024 applications, and test on 2025. That mimics real life: you build a model on the past, then use it on new applicants.

We start with logistic regression, from lesson twenty. It turns features like debt to income and past late payments into a probability of default for each applicant.

To measure how well it ranks applicants, we use AUC. Zero point five is no better than guessing, and one is perfect. Our simple model scored about zero point seven two on the 2025 test set. Useful, but far from perfect.

A probability isn't a decision. The lender needs a policy. For example: decline, or manually review, the riskiest twenty percent of applicants.

In our test, the riskiest twenty percent of applicants held about half of all the defaults. But that cut-off also turns away many good customers. The right choice depends on what a default costs, compared with a lost good loan.

Finally, write it up: the question, the data, how you tested the model, the policy you'd suggest, and its limits. That write-up is what turns this into a portfolio project.

Next lesson, we start project two: clinic no-shows. Framing the problem, and preparing the data.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 32](lesson-32.md)
