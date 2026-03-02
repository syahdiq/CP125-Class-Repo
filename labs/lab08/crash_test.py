# Common File Handling Mistakes
# Uncomment each section to see the error

import os

# Mistake 1: Reading a file that doesn't exist
# f = open("data/missing.txt", "r")  # FileNotFoundError!

# Mistake 2: Wrong mode destroys data
# f = open("data/scores.txt", "w")  # Overwrites everything!
# f.write("100\n")
# f.close()

# Mistake 3: Missing \n causes lines to merge
# f = open("data/test.txt", "w")
# f.write("Ali")
# f.write("Sara")  # Result: "AliSara"
# f.close()

# Mistake 4: Missing import csv
# f = open("data/test.csv", "r")
# reader = csv.reader(f)  # NameError: csv is not defined

# Mistake 5: Missing newline="" for CSV creates extra blank lines
# f = open("data/test.csv", "w")  # Should be: open(..., newline="")
# import csv
# writer = csv.writer(f)
# writer.writerow(["A", "B"])
# f.close()

# Mistake 6: Not closing file
# f = open("data/test.txt", "w")
# f.write("hello\n")
# # Forgot f.close() - data may not be saved!

print("Crash test ready. Uncomment sections to see errors.")
