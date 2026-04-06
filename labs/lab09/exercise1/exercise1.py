import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)
    
    total_students = len(df)
    subjects = ["Math", "Science", "English"]
    
    # Make math_average a pure Python float
    math_average = float(round(df["Math"].mean(), 1))
    
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]
    
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }
result = explore_data("labs/lab09/data/students.csv")
print(result)

