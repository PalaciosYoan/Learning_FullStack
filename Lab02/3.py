import pandas as pd

def part3():
    filepath = r"weather_data.txt"
    df = pd.read_csv(filepath, delimiter=",")
    
    print("a. Highest actual precipitation")
    df['date']=pd.to_datetime(df['date'])
    df1 = df.loc[df["actual_precipitation"].idxmax()]["date"]
    print(df1)
    
    print("\n\nb. avg actual max temp july 2014")
    df2 = df[(df['date'] >= '2014-07-01') & (df['date'] < '2014-8-01') ]
    print(df2['actual_max_temp'].mean())
    
    print("\n\nc. record max temp")
    df3 = df[(df['actual_max_temp'] == df['record_max_temp'])]
    print(df3[['date','actual_max_temp', 'record_max_temp']])
    
    print("\n\nd. Rain in october 2014")
    df4 = df[(df['date'] >= '2014-10-01') & (df['date'] < '2014-11-01')]
    df4 = df4['actual_precipitation'].sum()
    print(df4)
    
    print("\n\ne.temp below 60 and above 90")
    #x = input()
    #y = input()
    df5 = df[(df['actual_min_temp'] < 60) & (df['actual_max_temp'] > 90)]
    print(df5[['actual_min_temp','actual_max_temp']])
    
    
    
part3()