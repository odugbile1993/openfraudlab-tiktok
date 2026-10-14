# Lesson 13: Sampling and sampling bias

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

A sample is the part of a population you actually observe. Random sampling helps a sample represent the population; sampling bias happens when some groups are more likely to be included than others.

## Key ideas

- **Why sample?:** We rarely get data on everyone — Population: the whole group · Sample: the part you observe
- **The goal:** A sample should look like the population
- **Random sampling:** Everyone has an equal chance of being picked — The simplest way to avoid picking favourites
- **Sampling bias:** When some groups are more likely to be included — An online-only survey misses people who aren't online
- **In fraud data:** You only see the cases that were caught — Fraud that slipped through never gets a label
- **Takeaway:** Ask: who is missing from my data?

## Try it yourself

Imagine a bank surveys customers only through its mobile app. Write down two groups of customers this survey might miss, and how that could skew the results.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson thirteen: sampling, and sampling bias.

We rarely get data on every single person or transaction we care about. The whole group is called the population. The part we actually observe is the sample, and we use it to learn about the whole.

A good sample looks like the population in the ways that matter. Then what's true in the sample is likely to be roughly true for everyone.

The simplest approach is a random sample, where every member of the population has an equal chance of being picked. That stops you, or your process, from choosing favourites.

Sampling bias happens when some groups are more likely to end up in your data than others. For example, an online-only survey misses people who aren't online, so its results can't speak for them.

Fraud data has a classic version of this. Your labelled fraud cases are usually the ones that were caught. Fraud that slipped through often never gets a label, so your data can quietly over-represent the easy-to-catch kinds.

So the takeaway: before you trust any result, ask who or what is missing from your data, and why.

Next lesson: probability basics for data science.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 12](lesson-12.md) · [Lesson 14 →](lesson-14.md)
