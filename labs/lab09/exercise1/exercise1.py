import pandas as pd


def explore_data(filename):
    df = pd.read_csv(filename)
    math_average = df["Math"].mean()
    subjects = df.loc[,()]




