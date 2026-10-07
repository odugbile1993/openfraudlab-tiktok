# Lesson 9: Data cleaning basics

**Data Science from Scratch** · Module 2 · Statistics & Exploring Data · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Start cleaning with four checks: duplicates, inconsistent labels, wrong data types and impossible values. Always keep the raw file untouched and record each cleaning step so it can be repeated.

## Key ideas

- **Why clean:** Messy data in, misleading answers out — Cleaning is usually a big part of the job
- **1 · duplicates:** The same record counted twice — Inflates counts and totals
- **2 · inconsistent labels:** 'Lagos', 'lagos', 'LAGOS ' — Three spellings, one city
- **3 · wrong types:** Numbers stored as text / Dates in mixed formats — '₦5,000' can't be averaged until it's a number
- **4 · impossible values:** Age 250? Negative loan amount? — Check values against real-world rules
- **Takeaway:** Keep the raw file. Record every step. — So anyone can repeat your cleaning

## Try it yourself

Make a 6-row list of transactions on paper that includes one duplicate, a city spelled three ways, an amount written as text with a currency sign, and a negative amount. Then write the cleaned version and list each change you made.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson nine: data cleaning basics.

Raw data is almost always messy, and messy data gives misleading answers. Cleaning is usually a big part of any data project. Here are four checks to start with.

One: duplicates. The same customer or transaction recorded twice will inflate your counts and totals. Check for repeated rows and repeated IDs.

Two: inconsistent labels. Lagos with a capital, lagos in lower case, and LAGOS with a trailing space look like three different cities to a computer. Standardise case, spacing, and spelling.

Three: wrong data types. An amount stored as text, with a currency sign and commas, can't be averaged until you convert it to a number. And dates written in different formats need to be made consistent.

Four: impossible values. An age of two hundred and fifty, or a negative loan amount, breaks real-world rules. Write simple checks to catch them.

So the takeaway: never overwrite the raw data. Clean a copy, and record every step, so you or anyone else can repeat it.

Next lesson: exploratory data analysis, or E D A.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 8](lesson-08.md)
