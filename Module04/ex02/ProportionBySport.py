import pandas as pd


def proportion_by_sport(dataset, year, sport, gender):

    if not isinstance(dataset, pd.DataFrame) or not isinstance(year, int)\
            or not isinstance(sport, str) or gender not in ['F', 'M']:
        print('Error')
        return None
    try:
        total = dataset[(dataset['Year'] == year) & (dataset['Sex'] == gender)]
        total = total.drop_duplicates(subset=['ID'])
        g_filter = total[(total['Sport'] == sport)]
        return len(g_filter) / len(total)
    except Exception as e:
        print('Error: ', e)
