from FileLoader import FileLoader
import pandas as pd

def youngest_fellah(dataset, year):

    if not isinstance(dataset, pd.DataFrame) or not isinstance(year, int) or year <= 0:
        print('Error: dataset must be pandas.DataFrame and year must be positive integer')
        return None
    if not hasattr(dataset, 'Year') or not hasattr(dataset, 'Sex') or not hasattr(dataset, 'Age'):
        print('Error: dataset must be contain [Year, Sex, Age] attr')
        return None
    women = dataset[(dataset['Year'] == year) & (dataset['Sex'] == 'F')]
    men = dataset[(dataset['Year'] == year) & (dataset['Sex'] == 'M')]

    ret = {
        'f':'NA' if not len(women) else min(women['Age']),
        'm': 'NA' if not len(men) else min(men['Age']),
    }
    return ret





loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
print(youngest_fellah(data, 20))
