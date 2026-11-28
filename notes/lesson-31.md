# Lesson 31: Project 1 · Part 1: Credit risk — framing the problem and preparing the data

**Data Science from Scratch** · Module 6 · Going Further · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

A data science project starts with a clear question. Here we predict loan default at application time, using a synthetic dataset of 3,000 applications: we define the target, avoid leakage, handle missing values and build a debt-to-income feature.

## Key ideas

- **The question:** Will this loan default? — Predict risk at application
- **The data:** 3,000 loan applications — Synthetic practice data, 2024–2025
- **The target:** defaulted = 1 or 0 — About 9% defaulted
- **No leakage:** Only what's known at application — No future information
- **Missing values:** Check, then fill — Employment, months at employer
- **New feature:** Debt-to-income ratio — Repayments ÷ income

## Try it yourself

Imagine you are a lender. Write down 5 pieces of information you would know on the day someone applies for a loan, and 2 pieces you would only know later. Explain why the later ones must not be used to predict default.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson thirty-one: project one, credit risk. Framing the problem, and preparing the data.

Every project starts with a clear question. Here it is: when someone applies for a loan, how likely are they to default? A lender can use that answer to decide who to approve.

Our practice dataset has three thousand synthetic loan applications, from 2024 and 2025. Each row is one application, with income, existing debt, loan amount, employment, and repayment history.

The target column is called defaulted: one if the loan went bad, zero if it didn't. Only about nine percent defaulted, so this is an imbalanced problem, like the ones in lesson twenty-seven.

A key rule: only use information you would actually have on the day someone applies. Anything recorded after the loan was given would leak the answer, and make the model look better than it really is.

Next, check for missing values. A few columns, like employment type and months at employer, have gaps. Fill them with a sensible value, like the median, or an unknown category, and write down what you did.

Then build a useful feature: the debt to income ratio. That's monthly repayments, including existing debt, divided by monthly income. Lenders often use a measure like this to judge affordability.

Next lesson: part two of the project. Exploring the data, to see what drives default.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 30](lesson-30.md) · [Lesson 32 →](lesson-32.md)
