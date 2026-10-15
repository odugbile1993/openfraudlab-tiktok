# Lesson 17: SQL basics: SELECT, WHERE, GROUP BY

**Data Science from Scratch** · Module 3 · Tools of the Trade · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

SELECT chooses columns and FROM names the table, WHERE filters individual rows, and GROUP BY with functions like COUNT, SUM and AVG produces one summary row per group. Use HAVING to filter groups after grouping.

## Key ideas

- **Why sql:** Ask a database questions — Much business data lives there
- **Select:** Choose your columns — SELECT amount FROM transactions
- **Where:** Filter the rows — WHERE amount > 1000
- **Group by:** Summarise groups — GROUP BY city
- **Watch out:** WHERE vs HAVING — Rows before grouping · groups after
- **Takeaway:** Columns, rows, then groups

## Try it yourself

Draw a small table of 8 transactions with columns city and amount. By hand, work out the result of: SELECT city, COUNT(*) FROM transactions WHERE amount > 500 GROUP BY city.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson seventeen: SQL basics. Select, where, and group by.

A lot of business data, like customers and transactions, lives in relational databases. SQL is the standard language for asking those databases questions, so it's one of the most useful skills a data scientist can have.

Every query starts with select. You list the columns you want, then say which table they come from, using from.

Where filters the rows. Here we keep only transactions where the amount is greater than one thousand. Rows that don't match are left out.

Group by puts rows into groups and gives you one summary row per group. Combine it with functions like count, sum, or average, and you get, say, the number of transactions and the average amount for each city.

One thing that trips beginners up: where filters individual rows before they are grouped. To filter the groups themselves, like cities with more than fifty transactions, you use having.

So the takeaway: select chooses columns, where filters rows, and group by summarises groups.

Next lesson: the train test split, and why we hide data from the model.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 16](lesson-16.md) · [Lesson 18 →](lesson-18.md)
