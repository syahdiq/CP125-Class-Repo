"""
Common Matplotlib Mistakes

Uncomment each section one at a time to see the error.
Then read the explanation and fix it.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# ERROR 1: Forgetting to import matplotlib
# ============================================
# Uncomment to see error:
# plt.plot([1, 2], [3, 4])
# NameError: name 'plt' is not defined

# Fix: Always import matplotlib.pyplot as plt at the top


# ============================================
# ERROR 2: Missing plt.show()
# ============================================
# Uncomment to see problem:
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title("My Chart")
# Nothing appears! Need plt.show()

# Fix: Always end with plt.show()


# ============================================
# ERROR 3: Wrong data format for histogram
# ============================================
# Uncomment to see error:
# plt.hist("85, 92, 78")
# TypeError: hist() argument must be a sequence

# Fix: Use a list instead
# plt.hist([85, 92, 78])
# plt.show()


# ============================================
# ERROR 4: Using label without legend
# ============================================
# Uncomment to see problem:
# data1 = [85, 92, 78, 88, 95]
# data2 = [78, 88, 75, 82, 91]
# plt.hist(data1, bins=5, alpha=0.5, label="Math")
# plt.hist(data2, bins=5, alpha=0.5, label="Science")
# plt.show()
# Labels exist but don't appear!

# Fix: Add plt.legend() before plt.show()


# ============================================
# ERROR 5: Wrong alpha range
# ============================================
# Uncomment to see error:
# plt.hist([85, 92, 78], alpha=2.0)
# plt.show()
# ValueError: alpha must be in range 0-1

# Fix: Use values between 0.0 and 1.0


print("Uncomment each error section one at a time to learn from mistakes!")
