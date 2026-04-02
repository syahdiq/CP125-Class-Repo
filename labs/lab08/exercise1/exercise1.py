# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    # Read
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    passing_count = 0

    # Write
    f = open(output_file, "w")
    for line in lines:
        parts = line.strip().split()
        student_id = parts[0]
        score = int(parts[1])

        if score >= 80:
            f.write(f"{student_id} {score}\n")
            passing_count += 1

    f.close()

    return passing_count


# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
