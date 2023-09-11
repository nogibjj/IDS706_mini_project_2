import pandas as pd
import numpy as np
import matplotlib as plt


def pandas_descriptive_stat_mean(df: pd.DataFrame, col: str) -> float:
    return df[col].mean()

def pandas_descriptive_stat_median(df: pd.DataFrame, col: str) -> float:
    return df[col].median()

def pandas_descriptive_stat_std(df: pd.DataFrame, col: str) -> float:
    return df[col].std()

def visualize_data(df, x_column, y_column):
    plt.scatter(df["mpg"], df["cyl"])
    plt.xlabel("Weight, lbs")
    plt.ylabel("Miles per Gallon, miles")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()


if __name__ == '__main__':
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(cars.head())
    print(pandas_descriptive_stat_mean(cars, 'mpg'))
    print(pandas_descriptive_stat_median(cars, 'mpg'))
    print(pandas_descriptive_stat_std(cars, 'mpg'))
    visualize_data(cars, 'mpg', 'cyl')
