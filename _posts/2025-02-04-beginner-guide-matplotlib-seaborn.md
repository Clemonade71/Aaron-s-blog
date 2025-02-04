---
layout: post
title: "A Beginner's Guide to Visualizing Data with Matplotlib and Seaborn"
date: 2025-02-04
categories: [data-science, visualization]
---
## Introduction
Data visualization is a key skill for data scientists. In this post, we'll explore how to use Matplotlib and Seaborn to create effective visualizations.

## Installing Libraries
Run this command to install the required libraries:
```bash
pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs. Body Mass")
plt.show()
