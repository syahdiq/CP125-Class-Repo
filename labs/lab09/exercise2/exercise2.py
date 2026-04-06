import pandas as pd
import matplotlib.pyplot as plt

def show_math_trend(filename):
    # Load CSV
    df = pd.read_csv(filename)
    
    # Extract Math scores
    math_scores = df["Math"]
    
    # Create line chart
    plt.plot(df.index, math_scores, marker='o')
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")
    
    # Show the chart
    plt.show()
    
    # Return number of students
    return len(df)
result = show_math_trend("labs/lab09/data/students.csv")
print (result)
