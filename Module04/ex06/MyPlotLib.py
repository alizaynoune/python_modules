from FileLoader import FileLoader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn


class MyPlotLib:
    def __init__(self) -> None:
        pass

    def histogram(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            _, ax = plt.subplots(1, len(features))
            for (i, v) in enumerate(features):
                ax[i].hist(data[v].to_list())
                ax[i].set_title(v)
                ax[i].grid(True)
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None

    def density(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            lines = {}
            for i in features:
                lines[i] = data[i]
            ax = pd.DataFrame(lines).plot.kde()
            plt.show()
        except Exception as err:
            print('Error: ', err)
            return None

    def pair_plot(self, data, features):
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list) or not all(isinstance(i, str) for i in features):
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
        if not isinstance(data, pd.DataFrame) or not isinstance(features, list) or not all(isinstance(i, str) for i in features):
            print('Error')
            return None
        try:
            fig, axs = plt.subplots(2, len(features))
            # fig = plt.figure()
            # ax = fig.add_axes([0, 0, 1, 1])

            lst = []
            for (i, v) in enumerate(features):
                # lst.append(data[v].fillna(0).astype(int))
                axs[0, i].boxplot(data[v].fillna(0).astype(int))
                axs[0, i].set_title(v)
            # fig.subplots_adjust
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
mp = MyPlotLib()
features = ['Weight', 'Height']
mp.box_plot(data, features)


# Creating dataset
# np.random.seed(10)

# data_1 = np.random.normal(100, 10, 200)
# data_2 = np.random.normal(90, 20, 200)
# data_3 = np.random.normal(80, 30, 200)
# data_4 = np.random.normal(70, 40, 200)
# data = [data_1, data_2]

# fig = plt.figure()

# # Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])

# # Creating plot
# bp = ax.boxplot(data)

# # show plot
# plt.show()
