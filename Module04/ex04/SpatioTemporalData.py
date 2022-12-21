import pandas as pd


class SpatioTemporalData:
    def __init__(self, data) -> None:
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Error: data must be pandas.DataFrame')
        self.data = data

    def when(self, location):
        if not isinstance(location, str) or not len(location)\
                or not isinstance(self.data, pd.DataFrame):
            print('Error')
            return None
        try:
            date = self.data[(self.data['City'] == location)
                             ].drop_duplicates(subset='Year')
            return date['Year'].to_list()
        except Exception as err:
            print('Error: ', err)
            return None

    def where(self, date):
        if not isinstance(date, int) or date <= 0\
                or not isinstance(self.data, pd.DataFrame):
            print('Error')
            return None
        try:
            loacation = self.data[(self.data['Year'] == date)]
            loacation = loacation.drop_duplicates(subset='City')
            return loacation['City'].to_list()
        except Exception as err:
            print('Error: ', err)
            return None
