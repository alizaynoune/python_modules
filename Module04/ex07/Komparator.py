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
            self.data.boxplot(column=numerical_var, by=categorical_var,)
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None

    def density(self, categorical_var, numerical_var):

        try:
            categories = self.data[categorical_var].dropna().unique()
            lines = {}
            for c in categories:
                lines[c] = self.data[self.data[categorical_var]
                                     == c][numerical_var]
            pd.DataFrame(lines).plot.kde()
            plt.xlabel(numerical_var)
            plt.show()
        except Exception as err:
            print('Error: ', err)

    def compare_histograms(self, categorical_var, numerical_var):
        try:
            categories = self.data[categorical_var].dropna().unique()
            cat_len = len(categories)
            for i, c in enumerate(categories):
                x = self.data.loc[self.data[categorical_var]
                                  == c, [numerical_var]]
                plt.hist(x[numerical_var], label=c,  rwidth=(
                    cat_len - i) / cat_len, edgecolor='black')
            plt.gca().set(xlabel=numerical_var)
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception as err:
            print('Error :', err)
            return None


if __name__ == '__main__':
    data = pd.read_csv('../data/athlete_events.csv')
    komp = Komparator(data)
    # komp.compare_box_plots('Medal', 'Height')
    # komp.density('Medal', 'Height')
    komp.compare_histograms('Medal', 'Height')
