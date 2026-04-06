"""
Demo: Your First Histogram

This demonstrates how to create a basic histogram to show data distribution.
"""

import matplotlib.pyplot as plt

# Sample data: All student scores
scores = [85, 92, 78, 88, 95, 72, 68, 81, 87, 90,
          76, 84, 89, 91, 73, 86, 94, 77, 82, 88]

# Create histogram with 10 bins (score ranges)
plt.hist(scores, bins=10)

plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.title("Math Score Distribution")

plt.show()
