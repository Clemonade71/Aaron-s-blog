---
layout: post
title: "A Fresh Guide to Data Visualization with Matplotlib and Seaborn"
date: 2025-02-04
categories: [data-science, visualization]
---
## Introduction
Data visualization is a critical skill in data science. In this post, we explore how to create clear and informative graphs using Matplotlib and Seaborn.

## Installing Matplotlib and Seaborn
Install both libraries using pip:
```bash
pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs. Body Mass")
plt.show()
