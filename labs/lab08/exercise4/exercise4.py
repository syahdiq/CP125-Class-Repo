# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    pass


# Test your code here
result = calculate_final_grades("data/scores.csv", "data/grades.csv")
print(f"Average final grade: {result:.2f}")
