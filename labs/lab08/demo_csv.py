# Demo: Working with CSV files
import csv

# Read CSV file
print("=== Reading CSV ===")
f = open("data/students.csv", "r", newline="")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()

# Write CSV file
print("\n=== Writing CSV ===")
f = open("data/output.csv", "w", newline="")
writer = csv.writer(f)

# Write header
writer.writerow(["Name", "Score", "Grade"])

# Write data
writer.writerow(["Ali", 85, "A"])
writer.writerow(["Sara", 92, "A+"])
writer.writerow(["Ahmad", 78, "B"])

f.close()
print("CSV written to data/output.csv")
