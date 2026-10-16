# Lesson 20: Classification and logistic regression

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Classification predicts a category, like fraud or not fraud. Logistic regression turns a straight-line score into a probability between 0 and 1 using the S-shaped sigmoid curve, then a chosen threshold turns that probability into a decision.

## Key ideas

- **The task:** Pick a category — Fraud or not fraud?
- **Why not a line:** Lines overshoot — Probabilities stay between 0 and 1
- **The s-curve:** Sigmoid function
- **The output:** P(fraud) = 0.82 — A probability, not a verdict
- **Threshold:** Pick a cut-off — 0.5 is common, not required
- **Why it's loved:** Simple and explainable — Often a strong baseline

## Try it yourself

Imagine a model gives these fraud probabilities to five transactions: 0.10, 0.45, 0.55, 0.80, 0.95. Which ones get flagged with a 0.5 threshold? Which with 0.7? Write one sentence on why a bank might choose the higher threshold.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty: classification, and logistic regression.

Regression predicts a number. Classification predicts a category. Is this transaction fraud or not? Will this customer repay the loan or default?

A straight line can predict values below zero or above one, which make no sense as probabilities. So we need a different shape.

Logistic regression passes a straight-line score through an S-shaped curve called the sigmoid. That squeezes any score into a probability between zero and one.

So the model doesn't just say yes or no. It gives a probability, like zero point eight two, meaning it rates this case as quite likely to be fraud.

To make a decision, you choose a threshold. Above it, flag the case. Point five is common, but for fraud, teams often adjust it based on the cost of missed fraud versus false alarms.

Logistic regression is fast, and its weights show which inputs push the probability up or down. That's why it's often used as a first model, especially in credit and finance.

Next lesson: overfitting versus underfitting, and why a model can be too clever or too simple.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 19](lesson-19.md) · [Lesson 21 →](lesson-21.md)
