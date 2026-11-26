# Lesson 27: Imbalanced data: the fraud detection problem

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

In imbalanced data one class, like fraud, is rare, so models can ignore it and accuracy hides the misses. Measure with precision and recall, rebalance only the training data, use class weights, and tune the decision threshold.

## Key ideas

- **The problem:** Fraud is rare — Few positives, many negatives
- **Why it hurts:** Models ignore the minority — Accuracy hides the misses
- **Measure right:** Use precision and recall — Not plain accuracy
- **Resampling:** Rebalance training data — Oversample the rare class
- **Class weights:** Make misses cost more — Weight the rare class higher
- **Thresholds:** Tune the threshold — Fewer misses or fewer alarms

## Try it yourself

Imagine 1,000 transactions that include 5 frauds. Work out the accuracy of a model that always says 'not fraud', then its recall for fraud. Write one sentence explaining why accuracy alone is misleading here.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty seven: imbalanced data, the core problem in fraud detection.

In many fraud datasets, fraud cases are a tiny share of all transactions, often less than one percent. When one class is that rare, we call the data imbalanced.

A model trained on this data can learn that predicting not fraud is almost always a safe bet. As we saw in lesson twenty two, accuracy then looks great while real fraud slips through.

So first, measure the right thing. Track precision and recall from lesson twenty three, or the area under the precision recall curve, instead of plain accuracy.

Second, you can rebalance the training data. Oversampling repeats or creates extra fraud examples, for example with a method called SMOTE. Undersampling keeps fewer normal examples. Only do this to the training data, never the test set.

Third, use class weights. Many libraries, including scikit-learn, let you tell the model that missing a fraud case costs more than a false alarm, so it pays more attention to the rare class.

Finally, adjust the decision threshold. A lower threshold usually catches more fraud, but raises more false alarms. The right balance depends on the cost of each mistake, and how many alerts your team can review.

Next lesson: explainable AI. Why did the model decide that?

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 26](lesson-26.md)
