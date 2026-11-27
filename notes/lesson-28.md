# Lesson 28: Explainable AI: why did the model decide that?

**Data Science from Scratch** · Module 5 · Responsible Data Science & Next Steps · by Ayodele Odugbile, OpenFraudLab

[▶ Watch the video](https://www.tiktok.com/@_drhola) · [📚 Course map](../README.md#-course-map)

> 👉 **First things first:** [follow @_drhola on TikTok](https://www.tiktok.com/@_drhola), then **like**, **share** and **comment** on this lesson so more people can learn with you.

## In a nutshell

Explainable AI helps answer why a model made a decision. Simple models like linear regression and small trees are readable on their own; for complex models, use global tools like feature importance and local tools like SHAP or LIME, remembering they explain the model, not real-world causes.

## Key ideas

- **The question:** Not just what, but why — Trust needs reasons
- **Glass box:** Some models explain themselves — Linear models, small trees
- **Black box:** Others are harder — Big ensembles, neural networks
- **Global view:** Feature importance — Which inputs matter overall?
- **Local view:** Explain one prediction — SHAP · LIME
- **Caution:** Explanations aren't causes — They describe the model

## Try it yourself

Write down a simple fraud rule with three features, for example amount, hour of day and new device. For one made-up transaction, write a one-sentence explanation a customer could understand of why it was flagged.

## Transcript

<details>
<summary>Show the full narration</summary>

Data Science from Scratch, lesson twenty eight: explainable AI. Why did the model decide that?

A model flags a transaction as fraud, or declines a loan. The next question is always: why? If nobody can answer, it is hard to trust the model, fix it, or explain the decision to a customer.

Some models are fairly easy to read. In linear or logistic regression, each feature has a weight. A small decision tree is a set of yes or no rules you can follow by hand.

Others, like large tree ensembles or neural networks, often predict better, but their reasoning is spread across thousands of steps. For these, we use explanation tools after training.

A global explanation asks which features matter most across all predictions. Feature importance, or permutation importance, which shuffles one feature and measures how much the score drops, are common ways to see this.

A local explanation asks why the model made one specific decision. Tools such as SHAP and LIME estimate how much each feature pushed this one prediction up or down. For example: a large amount at three a.m. from a new device raised the fraud score.

One warning. These tools explain what the model learned, not what causes fraud in the real world. If the data is biased, the explanation will faithfully show you that bias.

Next lesson: data ethics, and bias in models.

Follow, like, and share for more. This lesson was brought to you by Ayodele Odugbile, of OpenFraudLab.

</details>

---

[← Lesson 27](lesson-27.md) · [Lesson 29 →](lesson-29.md)
