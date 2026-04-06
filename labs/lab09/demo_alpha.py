"""
Demo: Overlapping Histograms with Alpha (Transparency)

This demonstrates how to compare two distributions on the same chart
using transparency to see where they overlap.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/students.csv")

# Plot both subjects on same chart with transparency
plt.hist(df['Math'], bins=10, alpha=0.5, label="Math")
plt.hist(df['Science'], bins=10, alpha=0.5, label="Science")

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Math vs Science Score Distribution")
plt.legend()  # Shows which color is which

plt.show()
