# Lesson 7: Outliers: errors, or the most interesting rows?

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

An outlier is a value far from the rest of the data, caused by a typo, a measurement error or a genuine rare event. The IQR rule flags values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR; investigate them before deciding to fix, keep or remove.

## Key ideas

- **Outlier:** A value far from the rest of the data — One loan of 50 million in a column of 50 thousands
- **Where they come from:** Typos / Measurement errors / Real rare events
- **Iqr rule:** Below Q1 − 1.5×IQR / Above Q3 + 1.5×IQR — IQR = Q3 − Q1, the middle 50% of the data
- **Why it matters:** Outliers pull the mean. The median barely moves. — Remember lesson 4
- **Fraud angle:** Sometimes the outlier is the story — Unusual is a reason to look, not proof of fraud
- **Takeaway:** Investigate before you delete. — Fix errors · keep real values · write down what you did

## Try it yourself

Write down these 10 numbers: 12, 15, 14, 13, 16, 15, 14, 13, 15, 95. Find Q1, Q3 and the IQR, use the 1.5×IQR rule to check whether 95 is an outlier, then compare the mean and the median with and without it.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson seven: outliers. Are they errors, or the most interesting rows in your data?

An outlier is a value that sits far away from the rest of your data. Picture one loan of fifty million in a column where most loans are around fifty thousand.

Outliers usually come from one of three places. A typo, like an extra zero. A measurement or system error. Or a real, rare event that actually happened.

A common way to flag them is the IQR rule. The interquartile range is the spread of the middle half of your data. Values more than one and a half times that range below the first quartile, or above the third quartile, get flagged as possible outliers.

Why care? A single extreme value can drag the mean a long way, while the median barely moves. That's why one outlier can make an average misleading.

In fraud work, the unusual transaction is often exactly what you want to find. But be careful: unusual is a reason to investigate, not proof that something is wrong.

So the takeaway: never delete outliers automatically. Fix the errors, keep the real values, and write down what you decided.

Next lesson: missing data, and what to do about it.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 6](lesson-06.md) · [Lesson 8 →](lesson-08.md)
