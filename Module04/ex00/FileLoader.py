import pandas as pd


class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path):
        if not isinstance(path, str):
            print('Error: path must be string')
            return None
        try:
            dataset = pd.read_csv(path, sep=',')
            print(f"Loading dataset of dimensions {dataset.shape[0]} x {dataset.shape[1]}")
            return dataset
        except Exception as err:
            print(err)
            return None

    def display(self, df, n):
        if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
            print('Error: df must be pandas.DataFrame and n must be integer')
            return None
        if n >= 0:
            print(pd.DataFrame(data=df.head(n)))
        else:
            print(df.tail(n * -1))


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
loader.display(data, 60)