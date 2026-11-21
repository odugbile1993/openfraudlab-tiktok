# Lesson 23: The confusion matrix, precision & recall

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

A confusion matrix splits predictions into true positives, false positives, false negatives and true negatives. Precision measures how many flagged cases were real; recall measures how many real cases were caught, and moving the threshold usually trades one for the other.

## Key ideas

- **Four boxes:** TP · FP · FN · TN — Every prediction lands in one
- **Precision:** TP ÷ (TP + FP) — Of my alerts, how many were right?
- **Recall:** TP ÷ (TP + FN) — Of real fraud, how much caught?
- **Example:** 10 flagged, 8 real — A made-up example
- **The trade-off:** Move the threshold — One usually rises, one falls
- **Which matters?:** Depends on the cost — Missed fraud vs false alarms

## Try it yourself

A model reviews 500 transactions containing 25 real frauds. It flags 30, and 15 of those are real fraud. Fill in the four boxes of the confusion matrix, then calculate precision and recall.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty three: the confusion matrix, precision and recall.

A confusion matrix sorts every prediction into four boxes. True positive: flagged as fraud, and it was fraud. False positive: flagged, but it was fine. False negative: fraud you missed. True negative: a normal case correctly left alone.

Precision asks: of everything the model flagged, how much was really fraud? Low precision means lots of false alarms.

Recall asks: of all the real fraud, how much did the model catch? Low recall means fraud slipping through.

A made-up example. There are twenty real fraud cases. The model flags ten, and eight are real. Precision is eight out of ten, eighty percent. Recall is eight out of twenty, just forty percent.

There's usually a trade-off. Lower the threshold and recall goes up, but false alarms rise, so precision often drops.

Which matters more depends on the cost of each mistake. Missed fraud loses money. Too many false alarms annoy honest customers and swamp reviewers.

Next lesson: decision trees, models that make predictions by asking a series of yes or no questions.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 22](lesson-22.md)
