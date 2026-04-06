"""
Sandbox for experimenting with DataFrames

Use this file to try out different DataFrame operations
as you work through the lab.
"""

import pandas as pd

# Example: Create a simple DataFrame
students = pd.DataFrame({
    'Name': ["Ali", "Sara", "Ahmad", "Fatimah"],
    'Math': [85, 92, 78, 88],
    'Science': [78, 88, 82, 91]
})

print(students)
print(f"\nAverage Math: {students['Math'].mean()}")
