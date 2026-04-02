# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:

import csv

def calculate_final_grades(input_file, output_file):
    f = open(input_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)  # skip header

    results = []
    total = 0
    count = 0

    for row in reader:
        student_id = row[0]
        midterm = float(row[1])
        final = float(row[2])

        final_grade = (midterm * 0.4) + (final * 0.6)

        total += final_grade
        count += 1

        results.append([student_id, f"{final_grade:.2f}"])

    f.close()

    average = total / count

    f = open(output_file, "w", newline="")
    writer = csv.writer(f)

    writer.writerow(["student_id", "final_grade"])
    writer.writerows(results)

    f.close()

    return average

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
