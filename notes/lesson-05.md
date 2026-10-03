# Lesson 5: Spread: range, variance & standard deviation

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Spread describes how far values sit from the centre. The range is maximum minus minimum, the variance is the average squared distance from the mean, and the standard deviation is its square root, in the original units.

## Key ideas

- **Why it matters:** Same average, very different data — Branch A: 48, 50, 52 · Branch B: 10, 50, 90
- **Range:** Range = maximum − minimum — A: 52 − 48 = 4 · B: 90 − 10 = 80
- **Variance:** Variance: average squared distance from the mean
- **Standard deviation:** Standard deviation = √variance — Back in the original units
- **Good to know:** Samples usually divide by n − 1 — Software often does this for you
- **Takeaway:** Report the average and the spread together.

## Try it yourself

Take two small lists, 48, 50, 52 and 10, 50, 90. For each, compute the mean, the range, and the standard deviation by hand (square each distance from the mean, average them, then take the square root). Compare the results.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson five: spread. Range, variance, and standard deviation.

Two branches both average fifty transactions a day. Branch A had forty-eight, fifty, and fifty-two. Branch B had ten, fifty, and ninety. Same mean, very different stories. Spread measures that difference.

The simplest measure is the range: the biggest value minus the smallest. Branch A has a range of four. Branch B has a range of eighty. But the range only uses two values, so one extreme point can distort it.

Variance uses every value. For each one, measure how far it is from the mean, square that distance, then average the squares. Squaring stops negative and positive distances cancelling out.

The standard deviation is the square root of the variance. That brings it back to the original units, so you can read it as a typical distance from the mean. A small standard deviation means values sit close together.

One detail: when you work with a sample rather than the whole population, the variance is usually divided by n minus one instead of n. Many tools do this by default, so check which one yours uses.

So the takeaway: an average on its own hides a lot. Always look at the spread alongside it.

Next lesson: distributions, and the normal curve.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 4](lesson-04.md) · [Lesson 6 →](lesson-06.md)
