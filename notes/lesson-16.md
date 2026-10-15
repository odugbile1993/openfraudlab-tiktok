# Lesson 16: Meet the pandas DataFrame

**Data Science from Scratch** · Module 3 · Tools of the Trade · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

A pandas DataFrame is a labelled table of rows and columns, where each column is a Series. Load data with pd.read_csv, inspect it with head, shape, info and describe, then select columns and filter rows with square brackets.

## Key ideas

- **What it is:** A table inside Python — Rows · columns · labels
- **Load it:** pd.read_csv() — Turns a CSV file into a table
- **First look:** head · shape · info — First rows · size · column types
- **Summary stats:** df.describe() — Quick stats for number columns
- **Select & filter:** Pick & filter — df["amount"] > 1000
- **Takeaway:** Look before you analyse

## Try it yourself

Write down, on paper, the five commands you would run first on a new CSV called loans.csv (load it, then four ways to look at it). Next to each, write in one sentence what it tells you.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson sixteen: meet the pandas DataFrame.

A DataFrame is how pandas holds a table in Python. It has rows and columns, just like a spreadsheet, and every row and column has a label. Each single column is called a Series.

Most of the time you start by loading a file. After importing pandas as p d, one line, read underscore csv, turns a CSV file into a DataFrame, usually named d f.

Then take a first look. head shows the first five rows. shape tells you how many rows and columns you have. And info lists each column's data type and how many values are not missing.

describe gives quick summary statistics for your numeric columns: the count, mean, standard deviation, minimum, quartiles, and maximum. It's a fast way to spot strange values.

To pick one column, put its name in square brackets. To filter rows, put a condition in the brackets instead. For example, keep only transactions where the amount is above one thousand.

So the takeaway: load your data, take a first look with head, shape, info, and describe, and only then start asking questions.

Next lesson: SQL basics. Select, where, and group by.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 15](lesson-15.md) · [Lesson 17 →](lesson-17.md)
