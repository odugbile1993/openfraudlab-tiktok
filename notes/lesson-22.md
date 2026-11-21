# Lesson 22: Why accuracy can lie

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Accuracy is the share of predictions a model gets right, but with imbalanced classes it can look excellent while the model misses every rare case. A model that always predicts the majority class sets the baseline any useful model must beat.

## Key ideas

- **Accuracy:** Correct ÷ total — Share of right answers
- **Imagine:** 1 fraud in 100 — A made-up example
- **The lazy model:** Always "not fraud"
- **The result:** 99% accurate — Catches zero fraud
- **Why:** Imbalanced classes — The majority class dominates
- **What to do:** Check each class — Not just one number

## Try it yourself

Out of 200 loan applications, 10 end in default. Work out the accuracy of a model that always predicts "no default", then write down how many defaults it catches and why that score is misleading.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty two: why accuracy can lie.

Accuracy is the simplest score for a classifier: the number of correct predictions divided by the total number of predictions. It sounds like all you need. But it can fool you.

Imagine a made-up dataset of one hundred transactions where only one is fraud. In real fraud data, the fraud class is often this rare, or rarer.

Now build a lazy model that ignores the data and always predicts not fraud. It gets ninety nine of the hundred right.

That's ninety nine percent accuracy, and it catches exactly zero fraud. The one case you actually cared about slipped straight through.

This happens with imbalanced classes. When one class is much bigger, accuracy is mostly a score on that big class, so it hides how the model does on the rare one.

So always check how many of each class there are, compare against a simple baseline like always guessing the majority, and look at how the model does on the rare class itself.

Next lesson: the confusion matrix, precision and recall, the tools that show what accuracy hides.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 21](lesson-21.md) · [Lesson 23 →](lesson-23.md)
