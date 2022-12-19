import pandas as pd
import matplotlib.pyplot as plt


class Komparator:
    def __init__(self, data) -> None:
        if not isinstance(data, pd.DataFrame):
            return None
        self.data = data
        pass

    def compare_box_plots(self, categorical_var, numerical_var):
        try:
            self.data.boxplot(column=[numerical_var], by=categorical_var,)
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None
    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        pass


if __name__ == '__main__':
    data = pd.read_csv('../data/athlete_events.csv')
    komp = Komparator(data)
    komp.compare_box_plots('Sex', 'Height')
    # komp.compare_histograms('Medal', 'Height')
    # komp.density('Medal', 'Weight')
