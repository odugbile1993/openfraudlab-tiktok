# Lesson 32: Project 1 · Part 2: Credit risk — what drives default?

**Data Science from Scratch** · Module 6 · Going Further · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

To explore what drives a 0/1 target like default, group the data and compare the mean (the default rate) in each group. In the practice data, higher debt-to-income and past late payments go with more defaults, but always check group sizes and remember patterns are not proof of cause.

## Key ideas

- **Start simple:** Default rate by group — Group, then average
- **In pandas:** groupby + mean — Mean of 0/1 = rate
- **Affordability:** Higher DTI, more defaults — Top quarter: about 17%
- **History:** Past late payments matter — None: about 7% default
- **Group size:** Count the rows — Few rows, noisy rates
- **Caution:** Pattern isn't cause — Synthetic data, for practice

## Try it yourself

Make a small table of 10 imaginary loans with two columns: 'has late payments' (yes/no) and 'defaulted' (1/0). Work out the default rate for each group by hand, then ask yourself whether 10 rows is enough to trust the difference.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson thirty-two: project one, part two. Credit risk: what drives default?

Exploring a target like default usually starts simple. Split the applications into groups, then compare the default rate in each group.

In pandas, that's a groupby, followed by the mean of the defaulted column. Because defaulted is zero or one, its mean is simply the default rate for each group.

Start with debt to income. Split it into four equal groups. In our practice data, the lowest quarter defaults about four percent of the time, and the highest quarter about seventeen percent.

Repayment history matters too. Applicants with no previous late payments default about seven percent of the time. With two late payments, it's nearer thirty percent, though that group is small.

So always check how many rows sit behind each rate. With only a dozen people in a group, one or two defaults can swing the rate a lot.

And remember: these are patterns, not proof of cause. They tell us which features are worth giving to a model. This dataset is also synthetic, built for practice, so don't apply its numbers to real borrowers.

Next lesson: part three. A default model, and an approval policy.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 31](lesson-31.md) · [Lesson 33 →](lesson-33.md)
