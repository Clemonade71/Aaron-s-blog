import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load dataset
penguins = sns.load_dataset("penguins")

# Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs Body Mass")
plt.savefig("scatter_plot.png")
plt.close()

# Bar Chart
plt.figure(figsize=(6, 4))
sns.barplot(data=penguins, x="species", y="body_mass_g", ci=None)
plt.title("Average Body Mass of Penguin Species")
plt.savefig("bar_chart.png")
plt.close()

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(data=penguins, x="flipper_length_mm", kde=True, hue="species", bins=20)
plt.title("Distribution of Flipper Lengths")
plt.savefig("histogram.png")
plt.close()

# Line Plot (Synthetic Data)
plt.figure(figsize=(6, 4))
data = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
    "y": np.sin(np.linspace(0, 10, 100))
})
sns.lineplot(data=data, x="x", y="y")
plt.title("Example Line Plot")
plt.savefig("line_plot.png")
plt.close()

print("All images have been generated and saved successfully!")
