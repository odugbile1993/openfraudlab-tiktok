# Lesson 26: Cross-validation

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Cross-validation tests a model on several different splits of the data and averages the scores, giving a more stable estimate than a single train/test split. Stratified folds keep rare classes represented in every fold.

## Key ideas

- **The problem:** One split can mislead — Lucky or unlucky test sets
- **The idea:** Test on every part — Rotate the held-out piece
- **K-fold:** Split into 5 folds — Train on 4, test on 1
- **The result:** Average and spread — Mean score and its variation
- **Rare classes:** Stratified folds — Same class balance per fold
- **Watch out:** Keep a final test set — Do data prep inside each fold

## Try it yourself

Write the numbers 1 to 10 on paper and split them into 5 folds of 2. For each of the 5 rounds, write which numbers are used for training and which for testing, then check that every number was tested exactly once.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty six: cross-validation, a fairer way to test your model.

In lesson eighteen we split data into a training set and a test set. But one split can be lucky or unlucky. By chance, the test set might be unusually easy, or unusually hard, and your score moves with it.

Cross-validation fixes this by testing on several different parts of the data, then combining the results.

The most common version is k-fold. With five folds, you split the data into five equal parts. Train on four, test on the one left out, and repeat five times, so every part gets a turn as the test set.

You get five scores. Their average is a more stable estimate of performance, and how much they vary tells you how far to trust it.

When one class is rare, like fraud, use stratified folds. They keep roughly the same share of each class in every fold, so no fold ends up with almost no fraud cases.

Two cautions. Fit steps like scaling inside each fold, using only that fold's training data, to avoid leakage. And if you use cross-validation to tune your model, keep a separate final test set for an honest last check. For time-ordered data, use splits that respect time.

Next lesson: imbalanced data, and why it sits at the heart of fraud detection.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 25](lesson-25.md) · [Lesson 27 →](lesson-27.md)
