# Lesson 10: Exploratory data analysis (EDA)

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Exploratory data analysis (EDA) means getting to know a dataset before modelling: check its shape and column types, summarize each column, plot columns one at a time, then compare pairs of columns. Patterns you find are questions to test, not proof.

## Key ideas

- **What it is:** Get to know your data before you model it — Look, summarize, ask questions
- **Step 1 · shape:** How many rows? / How many columns? — And what type is each column?
- **Step 2 · summarize:** Min, max, mean & median for each column — Counts for each category
- **Step 3 · one column:** Plot each column on its own — Histograms for numbers · bar charts for categories
- **Step 4 · pairs:** Then compare pairs of columns — Loan amounts: defaulters vs non-defaulters
- **Takeaway:** Explore first. Write down what you notice.

## Try it yourself

Take any small table you have, such as a list of your expenses with dates, categories and amounts. Write down the number of rows and columns, the type of each column, and the min, max and median of the amount column. Then note one question the data makes you want to ask.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson ten: exploratory data analysis, or E D A.

Exploratory data analysis means getting to know your data before you build anything. You look at it, summarize it, and ask questions, without a fixed answer in mind.

Step one: check the shape. How many rows, how many columns, and what type is each column? This alone often catches problems, like a number column stored as text.

Step two: summarize each column. For numbers, look at the minimum, maximum, mean, and median. For categories, count how often each value appears. A big gap between the mean and the median often hints at skew or outliers.

Step three: plot each column on its own. A histogram shows how a number column is distributed, and a bar chart shows the counts in a category.

Step four: look at pairs of columns. For example, in a loans dataset, compare loan amounts for customers who defaulted with those who didn't. Patterns you spot here are ideas to test, not proof.

So the takeaway: explore before you model, and write down every question and surprise you find.

Next lesson: choosing the right chart.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 9](lesson-09.md) · [Lesson 11 →](lesson-11.md)
