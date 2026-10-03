# Lesson 4: Mean, median & mode: describing data with one number

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

The mean is the sum divided by the count, the median is the middle sorted value, and the mode is the most frequent value. Extreme values can pull the mean a long way, while the median is much less affected.

## Key ideas

- **Why it matters:** One number to describe the 'typical' value
- **Mean:** Mean: add them up, divide by the count — 2k, 3k, 3k, 4k, 88k → mean = 20k
- **Median:** Median: the middle value when sorted — 2k, 3k, [3k], 4k, 88k → median = 3k
- **Mode:** Mode: the most frequent value — 3k appears twice → mode = 3k
- **Watch out:** One extreme value can drag the mean — Mean 20k vs median 3k: four of five transfers are 4k or less
- **Takeaway:** Skewed data? Report the median too.

## Try it yourself

Write down how many minutes you spent on your phone each day for the last 7 days (estimates are fine). Work out the mean, median and mode by hand, then check which one best describes a typical day.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson four: mean, median, and mode. Describing data with one number.

Often you want one number that sums up a whole column: the typical value. There are three common ways to get it, and they can tell very different stories.

The mean is the average. Add all the values and divide by how many there are. Take five transfers: two thousand, three thousand, three thousand, four thousand, and eighty-eight thousand naira. The mean is twenty thousand.

The median is the middle value once you sort the data. For those same five transfers, the median is three thousand. With an even count, you take the average of the two middle values.

The mode is the value that appears most often. Here, three thousand appears twice, so it's the mode. The mode also works for categories, like the most common payment method.

Notice the problem. One large transfer pulled the mean up to twenty thousand, even though four of the five transfers were four thousand or less. The median barely noticed.

So the takeaway: when your data has extreme values, like incomes or transaction amounts often do, look at the median as well as the mean.

Next lesson: spread. Range, variance, and standard deviation.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 3](lesson-03.md) · [Lesson 5 →](lesson-05.md)
