from FileLoader import FileLoader
import pandas as pd


def proportion_by_sport(dataset, year, sport, gender):

    if not isinstance(dataset, pd.DataFrame) or not isinstance(year, int) or not isinstance(sport, str) or gender not in ['F', 'M']:
        print('Error')
        return None
    try:
        total = data[(dataset['Year'] == year) & (dataset['Sex'] == gender)]
        total = total.drop_duplicates(subset=['ID'])
        g_filter = total[(total['Sport'] == sport)]
        return len(g_filter) / len(total)
    except Exception as e:
        print('Error: ', e)


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
res = proportion_by_sport(data, 2004, 'Tennis', 'F')
print(res)

