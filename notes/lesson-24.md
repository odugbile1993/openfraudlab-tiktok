# Lesson 24: Decision trees

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

A decision tree predicts by asking a sequence of yes/no questions about the features, from the root down to a leaf that holds the prediction. Training picks the splits that best separate the classes; trees are easy to explain but can overfit if they grow too deep.

## Key ideas

- **The idea:** A flowchart of questions — Yes or no, step by step
- **Example:** Amount > 500? — A made-up fraud check
- **The parts:** Root · branches · leaves — Leaves hold the prediction
- **Learning splits:** Purest groups win — Gini impurity or entropy
- **Strength:** Easy to explain — You can read the rules
- **Watch out:** Deep trees overfit — Limit depth, test on new data

## Try it yourself

On paper, draw a decision tree with two questions that decides whether to bring an umbrella (for example: Is the sky cloudy? Is rain forecast?). Label the root, the branches and each leaf's prediction.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty four: decision trees, models that make predictions by asking questions.

A decision tree works like a flowchart. It asks a yes or no question about one feature, follows the answer down a branch, and keeps asking until it reaches a prediction.

Here's a made-up example. Is the transaction amount over five hundred? If yes, is it from a new device? If yes again, flag it for review. If not, let it through.

The first question is the root. Each answer is a branch. The end points are leaves, and each leaf holds the prediction, like fraud or not fraud, or a number for regression.

How does the tree choose its questions? During training, it tries many possible splits and picks the one that separates the classes most cleanly. Common measures of this are Gini impurity and entropy.

A big strength: a small tree is easy to explain. You can read its rules out loud, which helps when a decision needs to be justified.

The catch: a tree allowed to grow too deep can memorise the training data. That's overfitting. Limiting the depth, or the minimum rows per leaf, usually helps, and you always check on a test set.

Next lesson: feature engineering, turning raw data into inputs your model can actually learn from.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 23](lesson-23.md)
