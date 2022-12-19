from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn


class MyPlotLib:
    def __init__(self) -> None:
        pass

    def histogram(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list)\
                or not len(features) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            if len(features) == 1:
                plt.hist(data[features[0]].to_list())
                plt.title(features[0])
                plt.grid(True)
            else:
                _, ax = plt.subplots(
                    1, len(features), figsize=(5 * len(features), 5))
                for (i, v) in enumerate(features):
                    ax[i].hist(data[v].to_list())
                    ax[i].set_title(v)
                    ax[i].grid(True)
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None

    def density(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list)\
                or not len(features) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            lines = {}
            for i in features:
                lines[i] = data[i]
            pd.DataFrame(lines).plot.kde()
            plt.show()
        except Exception as err:
            print('Error: ', err)
            return None

    def pair_plot(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list)\
                or not len(features) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            lines = {}
            for i in features:
                lines[i] = data[i]
            pd.plotting.scatter_matrix(
                pd.DataFrame(lines), hist_kwds={'bins': 10})
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None

    def box_plot(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list)\
                or not len(features) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            _, ax = plt.subplots()
            data.boxplot(ax=ax, column=features, grid=False)
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
mp = MyPlotLib()
features = ['Weight', 'Height']
# features = []
for fc in [mp.histogram, mp.density, mp.pair_plot, mp.box_plot]:
    fc(data, features)

