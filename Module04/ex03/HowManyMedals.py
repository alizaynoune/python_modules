import pandas as pd


def how_many_medals(dataset, name):

    if not isinstance(dataset, pd.DataFrame) or not isinstance(name, str):
        print('Error')
        return None
    try:
        total = pd.DataFrame(
            dataset[(dataset['Name'] == name)], columns=['Year', 'Medal'])
        ret = {}

        for _, row in total.drop_duplicates('Year').iterrows():
            ret[row['Year']] = {
                'G': (total[(total['Year'] == row['Year'])
                            & (total['Medal'] == 'Gold')])['Medal'].count(),
                'S': (total[(total['Year'] == row['Year'])
                            & (total['Medal'] == 'Silver')])['Medal'].count(),
                'B': (total[(total['Year'] == row['Year'])
                            & (total['Medal'] == 'Bronze')])['Medal'].count(),

            }

        return ret

    except Exception as err:
        print('Error: ', err)
        return None
