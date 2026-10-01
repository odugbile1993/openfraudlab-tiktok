# Lesson 3: Your first dataset: rows, columns & features

**Data Science from Scratch** · Module 1 · Foundations · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.linkedin.com/in/ayodele-odugbile-939b97185) · [📚 Course map](../README.md#-course-map)

## In a nutshell

In a dataset, each row is one observation, each column is one variable, features are the inputs and the target is what you want to predict. Rows x columns is the shape.

## Key ideas

- **The shape:** Most data science starts with a table.
- **Rows:** Each row = one observation — One customer, one transaction, one loan
- **Columns:** Each column = one variable — Age, income, loan amount, repaid?
- **Features vs target:** Features: what you know / Target: what you want to predict — Features: age, income, loan amount · Target: repaid, yes or no
- **Quick check:** Rows × columns = the shape of your data — 1,000 customers with 8 columns → shape (1000, 8)
- **Takeaway:** Rows are examples. / Columns are variables. / The target is your question.

## Try it yourself

Sketch a small table for predicting whether a student passes an exam. Name 4 features and the target, and write down the shape if you had 200 students.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson three: your first dataset. Rows, columns, and features.

Most data science projects start with a simple table of data. Once you can read that table, everything else gets easier.

Each row is one observation. That could be one customer, one transaction, or one loan.

Each column is one variable: something you recorded about every observation, like age, income, or loan amount.

In machine learning, the columns you use as inputs are called features. The column you want to predict is called the target. For a lender, the features might be age, income, and loan amount, and the target might be: did they repay, yes or no?

The number of rows and columns together is called the shape of your data. A thousand customers with eight columns has a shape of one thousand by eight.

So remember: rows are examples, columns are variables, and the target is the question you're trying to answer.

Next lesson: mean, median, and mode. How to describe your data with a single number.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 2](lesson-02.md)
