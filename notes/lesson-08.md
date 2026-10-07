# Lesson 8: Missing data and what to do about it

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Missing values can appear as blanks, NA or NaN, or hide behind placeholders like 0 or -999. Ask why data is missing, then drop, impute (e.g. median or most common value) or flag it, and document the choice.

## Key ideas

- **Spot it:** Blanks, NA, NaN… and sneaky placeholders — 0, -999 or 'unknown' can also mean missing
- **Ask why:** Missing is often not random — The pattern of gaps can carry information
- **Option 1: drop:** Remove rows with gaps — Simple, but you can lose data and add bias
- **Option 2: fill:** Impute a sensible value — Median for numbers · most common value for categories
- **Option 3: flag:** Add a 'was missing' column — Keeps the pattern visible to you and your model
- **Takeaway:** Find it, ask why, then choose and document.

## Try it yourself

Write a small table of 8 people with columns age, city and income, leaving 3 cells empty. For each gap, decide whether you would drop the row, fill it (and with what), or add a 'was missing' flag, and write one sentence explaining why.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson eight: missing data, and what to do about it.

Missing values show up as blanks, N A, or N a N. But watch for sneaky placeholders too. A zero, minus nine nine nine, or the word unknown can quietly stand in for missing, and they'll distort your averages.

Before fixing anything, ask why it's missing. Gaps are often not random. For example, an income field might be skipped more by some groups of applicants than others, and that pattern can bias your results.

Option one: drop the rows with missing values. It's simple, but you can throw away a lot of data, and if the gaps aren't random, what's left may not represent everyone.

Option two: fill the gaps, which is called imputation. A common start is the median for numeric columns, and the most common value for categories.

Option three: flag it. Add a yes or no column that records whether the value was missing. That keeps the pattern visible, and models can sometimes learn from it.

So the takeaway: find every kind of missing value, ask why it's missing, then choose a strategy and write it down.

Next lesson: data cleaning basics.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 7](lesson-07.md) · [Lesson 9 →](lesson-09.md)
