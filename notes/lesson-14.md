# Lesson 14: Probability basics for data science

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Probability measures how likely an event is on a scale from 0 to 1. We often estimate it from how often something happened in data, and conditional probability asks how likely A is given that B is true.

## Key ideas

- **What is it?:** How likely something is, from 0 to 1 — 0 = impossible · 1 = certain
- **From data:** Probability ≈ how often it happened — 30 late payments out of 1,000 loans ≈ 0.03
- **The complement:** P(not A) = 1 − P(A)
- **Conditional:** P(A | B): the chance of A, given B — Fraud rate among ALL transactions vs among overseas ones
- **Why it matters:** Many models output a probability — e.g. a fraud score between 0 and 1
- **Takeaway:** Probability turns uncertainty into numbers you can use

## Try it yourself

Flip a coin 20 times and record the results. Estimate the probability of heads from your data, then compute the probability of NOT getting heads using 1 − P(heads).

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson fourteen: probability basics for data science.

Probability measures how likely something is, on a scale from zero to one. Zero means impossible, one means certain, and zero point five means a fifty-fifty chance.

In data science, we often estimate probability from how often something happened. If thirty out of a thousand loans in a made-up example had a late payment, our estimate is about zero point zero three, or three percent.

The chance something does not happen is one minus the chance that it does. So if the chance of a late payment is zero point zero three, the chance of no late payment is zero point nine seven.

Conditional probability is the chance of A given that B is true. The fraud rate across all transactions can be very different from the fraud rate among, say, overseas transactions only.

This matters because many classification models output a probability, like a fraud score between zero and one. Then a person or a rule decides where to draw the line.

So the takeaway: probability turns uncertainty into numbers you can reason with.

Next lesson: why Python for data science.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 13](lesson-13.md) · [Lesson 15 →](lesson-15.md)
