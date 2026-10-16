# Lesson 21: Overfitting vs underfitting

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Underfitting means a model is too simple and does poorly on both training and test data; overfitting means it memorises noise, scoring well on training data but poorly on new data. Comparing training and test scores is the usual way to tell them apart.

## Key ideas

- **The goal:** Generalise to new data
- **Underfitting:** Too simple — Bad on train and test
- **Overfitting:** Too clever — Great on train, poor on test
- **How to spot it:** Compare train vs test — Watch the gap
- **Fix overfitting:** Simplify or add data
- **Fix underfitting:** Add signal

## Try it yourself

A model scores 99% on its training data and 70% on its test data. A second model scores 72% on both. Write down which one is likely overfitting, which may be underfitting, and one thing you would try to improve each.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty one: overfitting versus underfitting.

A good model learns patterns that hold on new data it has never seen, not just on the data it was trained on. That's called generalising.

Underfitting means the model is too simple to capture the real pattern, like fitting a straight line to a clear curve. It does badly on training data and on test data.

Overfitting is the opposite. The model is so flexible it memorises the noise in the training data. It scores brilliantly in training, then disappoints on new data.

This is where your test set from lesson eighteen pays off. A big gap between training and test scores usually signals overfitting. Low scores on both usually signal underfitting.

To reduce overfitting, you can simplify the model, get more training data, use regularisation to penalise complexity, or check performance with cross validation.

To fix underfitting, give the model more to work with: better features, or a more flexible model.

Next lesson: why accuracy can lie, especially when fraud is rare.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 20](lesson-20.md)
