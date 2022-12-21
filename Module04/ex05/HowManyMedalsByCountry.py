import pandas as pd


def how_many_medals_by_country(dataset, cuntryName):
    if not isinstance(dataset, pd.DataFrame)\
            or not isinstance(cuntryName, str) or not len(cuntryName):
        print('Error')
        return None
    team_sports = ['Basketball', 'Football',  'Tug-Of-War',
                   'Badminton', 'Sailing', 'Handball', 'Water Polo',
                   'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                   'Volleyball', 'Synchronized Swimming', 'Baseball',
                   'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

    ret = {}
    team_data = dataset[(dataset['Team'] == cuntryName) & (dataset['Medal'])]
    sport_data = (team_data[team_data['Sport'].isin(
        team_sports)]).drop_duplicates(['Year', 'Medal', 'Event'])
    other_sport = team_data[~team_data['Sport'].isin(team_sports)]
    team_data = pd.concat([sport_data, other_sport])
    for _, row in team_data.drop_duplicates(
            subset=['Year']).sort_values('Year').iterrows():
        ret[row['Year']] = {
            'G': (team_data[(team_data['Year'] == row['Year']) & (
                team_data['Medal'] == 'Gold')])['Medal'].count(),
            'S': (team_data[(team_data['Year'] == row['Year']) & (
                team_data['Medal'] == 'Silver')])['Medal'].count(),
            'B': (team_data[(team_data['Year'] == row['Year']) & (
                team_data['Medal'] == 'Bronze')])['Medal'].count(),

        }
    return ret
