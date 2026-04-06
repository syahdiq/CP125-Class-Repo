import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv(filename)

    math_scores = df["Math"]

    plt.plot(df.index, math_scores, marker='o')
    plt.xlabel("Student Index")
    plt.ylabel("Math Scores")
    plt.title("Math Score Trends")

    plt.show()

    return len(df)
result = show_math_trend("labs/lab09/data/students.csv")
print(result)