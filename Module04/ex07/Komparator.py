import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



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
            
            # # Converting to wide dataframe
            # data_wide = self.data.pivot(columns = 'Age', values = 'Sex')
            # print(data_wide)

            # # plotting multiple density plot
            # data_wide.plot.kde(figsize = (8, 6), linewidth = 3)
            # Set figure size for the notebook
            plt.rcParams["figure.figsize"]=12,8

            # set seaborn whitegrid theme
            sns.set(style="whitegrid")

            # Without transparency
            sns.kdeplot(data=self.data, x="Sex", hue="Height", cut=0, fill=True, common_norm=False, alpha=1)
            plt.show()

        except Exception as err:
            print('Error :', err)
            return None

    def compare_histograms(self, categorical_var, numerical_var):
        try:
            print('done')
        except Exception as err:
            print('Error :', err)
            return None


if __name__ == '__main__':
    data = pd.read_csv('../data/athlete_events.csv')
    komp = Komparator(data)
    # komp.compare_box_plots('Sex', ['Height', 'Weight'])
    komp.density('Medal', 'Weight')
    # komp.compare_histograms('Medal', 'Height')
