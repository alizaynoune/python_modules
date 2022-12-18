from FileLoader import FileLoader
import pandas as pd
from deepdiff import DeepDiff
from pprint import pprint


def how_many_medals_by_country(dataset, cuntryName):
    if not isinstance(dataset, pd.DataFrame) or not isinstance(cuntryName, str) or not len(cuntryName):
        print('Error')
        return None
    team_sports = ['Basketball', 'Football',  'Tug-Of-War',
                   'Badminton', 'Sailing', 'Handball', 'Water Polo',
                   'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                   'Volleyball', 'Synchronized Swimming', 'Baseball',
                   'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

    ret = {}
    team_data = dataset[(dataset['Team'] == cuntryName) & (dataset['Medal'])]
    sport_data = (team_data[team_data['Sport'].isin(team_sports)]).drop_duplicates(
        ['Year', 'Medal', 'Event'])
    other_sport = team_data[~team_data['Sport'].isin(team_sports)]
    team_data = pd.concat([sport_data, other_sport])
    for _, row in team_data.drop_duplicates(subset=['Year']).sort_values('Year').iterrows():
        ret[row['Year']] = {
            'G': (team_data[(team_data['Year'] == row['Year']) & (team_data['Medal'] == 'Gold')])['Medal'].count(),
            'S': (team_data[(team_data['Year'] == row['Year']) & (team_data['Medal'] == 'Silver')])['Medal'].count(),
            'B': (team_data[(team_data['Year'] == row['Year']) & (team_data['Medal'] == 'Bronze')])['Medal'].count(),

        }
    return ret


loader = FileLoader()
data = loader.load("../data/athlete_events.csv")

d = {
    1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13},
    1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6},
    1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36},
    1920: {'G': 87, 'S': 41, 'B': 35}, 1924: {'G': 65, 'S': 41, 'B': 36},
    1928: {'G': 39, 'S': 22, 'B': 18}, 1932: {'G': 60, 'S': 57, 'B': 43},
    1936: {'G': 30, 'S': 29, 'B': 28}, 1948: {'G': 57, 'S': 34, 'B': 30},
    1952: {'G': 55, 'S': 38, 'B': 25}, 1956: {'G': 39, 'S': 57, 'B': 21},
    1960: {'G': 83, 'S': 27, 'B': 19}, 1964: {'G': 75, 'S': 36, 'B': 28},
    1968: {'G': 86, 'S': 36, 'B': 35}, 1972: {'G': 70, 'S': 58, 'B': 33},
    1976: {'G': 62, 'S': 46, 'B': 30}, 1980: {'G': 24, 'S': 4, 'B': 2},
    1984: {'G': 143, 'S': 75, 'B': 33}, 1988: {'G': 66, 'S': 48, 'B': 36},
    1992: {'G': 79, 'S': 46, 'B': 52}, 1994: {'G': 6, 'S': 8, 'B': 5},
    1996: {'G': 98, 'S': 41, 'B': 28}, 1998: {'G': 25, 'S': 2, 'B': 3},
    2000: {'G': 69, 'S': 34, 'B': 48}, 2002: {'G': 9, 'S': 52, 'B': 9},
    2004: {'G': 65, 'S': 66, 'B': 38}, 2006: {'G': 9, 'S': 7, 'B': 32},
    2008: {'G': 64, 'S': 61, 'B': 47}, 2010: {'G': 8, 'S': 61, 'B': 20},
    2012: {'G': 82, 'S': 44, 'B': 38}, 2014: {'G': 8, 'S': 28, 'B': 16},
    2016: {'G': 95, 'S': 52, 'B': 45}}
f = how_many_medals_by_country(data, "United States")
# pprint(DeepDiff(f, d))
print(f == d)
