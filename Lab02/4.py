import matplotlib.pyplot as plt
import pandas as pd


def part4():
    filepath = r"weather_data.txt"
    df = pd.read_csv(filepath, delimiter=",")
    
    df['date']=pd.to_datetime(df['date'])
    ax = plt.gca()
    df.plot(kind='line', x='date', y='actual_min_temp', color='blue', ax=ax)
    df.plot(kind='line', x='date', y='actual_max_temp', color='red', ax=ax)
    df.hist(column='actual_precipitation')

    plt.show()
    

part4()