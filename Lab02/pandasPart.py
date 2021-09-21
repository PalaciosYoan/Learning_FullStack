import pandas as pd
from pdb import set_trace
def part1():
    filepath = r"C:\Users\Undergrad-Students\Documents\Learning_FullStack\Lab02\weather_data.txt"
    df = pd.read_csv(filepath, delimiter=",")
    
    df['date']=pd.to_datetime(df['date'])
    df1 = df.loc[df["actual_precipitation"].idxmax()]["date"]
    print(df1)
    
    
    df2 = df[(df['date'] >= '2014-07-01') & (df['date'] < '2014-8-01') ]
    print(df2['actual_max_temp'].mean())
    
    df3 = df[(df['actual_max_temp'] == df['record_max_temp'])]
    print(df3[['date','actual_max_temp', 'record_max_temp']])
    
    df4 = df[(df['date'] >= '2014-10-01') & (df['date'] < '2014-11-01')]
    df4 = df4['actual_precipitation'].sum()
    print(df4)
    
    df5 = df[(df['actual_min_temp'] < 60) & (df['actual_max_temp'] > 90)]
    print(df5[['actual_min_temp','actual_max_temp']])
    
    
    
part1()