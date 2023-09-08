import pandas as pd


def pandas_descriptive_stat_mean(df: pd.DataFrame, col: str) -> float:
    return df[col].mean()

if __name__ == '__main__':
    cars = pd.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(pandas_descriptive_stat_mean(cars, 'mpg'))