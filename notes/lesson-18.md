# Lesson 18: Train/test split: why we hide data from the model

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Split data into a training set the model learns from and a hidden test set used only to score it, often around 80/20 or 70/30. Stratify for rare events like fraud, and split by date when data changes over time.

## Key ideas

- **The problem:** Models can memorise — High scores on old data can mislead
- **The fix:** Learn on one part. / Test on the other.
- **How much:** 80/20 or 70/30 — A common rule of thumb
- **Rare events:** Stratify the split — Same fraud rate in both sets
- **Time matters:** Train on the past. / Test on the future. — Split by date when patterns shift
- **Takeaway:** Keep the test set hidden

## Try it yourself

You have 1,000 past transactions, 20 of them fraud, from January to December. Write down how you would split them into training and test sets, and explain why a random split could mislead you.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson eighteen: the train test split, and why we hide data from the model.

A model can do very well on the data it learned from, partly by memorising it. That tells you little about how it will do on new data, which is the whole point.

The fix is simple. Split your data in two. The model learns from the training set, and the test set stays hidden until the end, when you use it to score the model.

A common choice is eighty percent for training and twenty for testing, or seventy and thirty. These are rules of thumb, not laws.

With rare events like fraud, a random split can leave the test set with very few fraud cases. Stratifying keeps the share of fraud roughly the same in both sets.

When data changes over time, as fraud patterns often do, it's usually better to split by date. Train on older data and test on newer data, just like the model will face in real life.

So the takeaway: keep the test set hidden while the model learns, or your scores will look better than reality.

Next lesson: linear regression, the intuition.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 17](lesson-17.md) · [Lesson 19 →](lesson-19.md)
