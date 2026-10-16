# Lesson 19: Linear regression intuition

**Data Science from Scratch** · Module 4 · Machine Learning Essentials · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Linear regression predicts a number by fitting the straight line y = a + b·x that minimises squared errors (least squares). The slope tells you how much the prediction changes per unit of x, but the method assumes a roughly straight-line relationship, so plot your data first.

## Key ideas

- **The idea:** Fit a straight line
- **The formula:** y = a + b·x — Intercept plus slope times x
- **Best fit:** Smallest squared errors — Least squares
- **Read the slope:** Slope = change per unit — Easy to explain
- **More inputs:** Many features, one line
- **Watch out:** Lines can't bend — Plot your data first

## Try it yourself

Write down five pairs of (hours studied, test score) from imagination or your own life, plot them on paper, and draw the straight line you think fits best. Estimate its slope: how many points does one extra hour add?

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson nineteen: linear regression, the intuition behind one of the oldest and most useful models in data science.

Linear regression predicts a number by fitting a straight line through your data. For example, predicting a loan amount from a customer's income.

The line has two parts. The intercept, a, is where the line starts when x is zero. The slope, b, is how much y changes when x goes up by one.

How does it choose the line? The usual method, called least squares, picks the line that makes the squared gaps between the points and the line as small as possible.

If the slope is two hundred, each extra unit of x adds about two hundred to the prediction, on average. That makes the model easy to explain to others.

You can use many inputs at once, like income, age and loan term. This is called multiple regression, and each input gets its own slope.

The catch: it assumes a roughly straight-line relationship. If the real pattern curves, or there are big outliers, the line can mislead you. Always plot your data first.

Next lesson: classification, and logistic regression, for predicting yes or no answers like fraud or not fraud.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 18](lesson-18.md) · [Lesson 20 →](lesson-20.md)
