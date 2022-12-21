import pandas as pd


class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path):
        if not isinstance(path, str):
            print('Error: path must be string')
            return None
        try:
            fd = pd.read_csv(path, sep=',')
            print(
                f"Loading dataset of dimensions {fd.shape[0]} x {fd.shape[1]}")
            return fd
        except Exception as err:
            print(err)
            return None
