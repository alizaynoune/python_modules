from FileLoader import FileLoader
import pandas as pd


def how_many_medals(dataset, name):
    
    if not isinstance(dataset, pd.DataFrame) or not isinstance(name, str):
        print('Error')
        return None
    try:
        total = pd.DataFrame(dataset[(dataset['Name'] == name)], columns=['Year', 'Medal'])
        # group = total.groupby(['Year'] ,as_index=False).agg({'Medal': 'count'})
        # total['count'] = total.groupby(['Year', 'Medal'])['Medal'].transform('count')
        total = total.set_index('Year')
        total = total.groupby(['Year','Medal'])['Medal'].transform(lambda x: ','.join(x))
        # total = total.groupby(['Year'])['Year'].transform(lambda x: ','.join(x))
        total = total.drop_duplicates()
        # total["Period"] = total[["Medal", "count"]].apply(lambda x: "-".join(str(x)), axis=1)
        # total['tt'] = total['Medal'] + '_' + (total.groupby(['Year', 'Medal'])['Medal'].transform('count')).astype(str)
        # aggregation_functions = {'Year': 'first', 'Medal': ' '.join}
        # df_new = df.groupby(df['id']).aggregate(aggregation_functions)
        # total = total.groupby(total['Year']).aggregate(aggregation_functions)
        # total = total.groupby('Year').agg(lambda x: ''.join(set(x)))
        # total = total.agg({'count': lambda c : c if not isinstance(c, (int, float)) else int(c)})

        
        # group['count'] = group.gr.transform('count')
        # print(total.columns)
        print(total)
        # total = total.set_index('Year')
        # # print(group.first())
        # # print(total.to_dict())
        # for i, v in total.iterrows():
        #     print(i)
            # print(v['Year'], v['Medal'], v['count'])
            # if not v['count']:
                # print('<<<<<')
            # print(i[0],'<<<<', i[1], v['Medal'])
        # print(group.set_index('Year'))

    except Exception as err:
        print('Error: ', err)




loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
res = how_many_medals(data, 'Kjetil Andr Aamodt')
# print(res)
