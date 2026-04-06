"""
Demo: Your First Line Chart

This demonstrates how to create a basic line chart using matplotlib.
"""

import matplotlib.pyplot as plt

# Sample data: Student numbers and their Math scores
students = [1, 2, 3, 4, 5]
scores = [85, 92, 78, 88, 95]

# Create the line chart
plt.plot(students, scores)

# Add labels
plt.xlabel("Student Number")
plt.ylabel("Math Score")
plt.title("Math Score Trends")

# Display the chart
plt.show()
