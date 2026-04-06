"""
Demo: Histogram with DataFrame

This demonstrates how to create a histogram from a DataFrame column.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/students.csv")

# Plot histogram of Math scores
plt.hist(df['Math'], bins=10)

plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.title("Math Score Distribution")

plt.show()
