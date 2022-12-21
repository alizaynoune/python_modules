import pandas as pd


class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path):
        if not isinstance(path, str):
            print('Error: path must be string')
            return None
        try:
            df = pd.read_csv(path, sep=',')
            print(
                f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
            return df
        except Exception as err:
            print(err)
            return None

    def display(self, df, n):
        if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
            print('Error: df must be pandas.DataFrame and n must be integer')
            return None
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(n * -1))
