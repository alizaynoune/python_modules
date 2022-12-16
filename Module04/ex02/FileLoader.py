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
            print(
                f"Loading dataset of dimensions {dataset.shape[0]} x {dataset.shape[1]}")
            return dataset
        except Exception as err:
            print(err)
            return None
