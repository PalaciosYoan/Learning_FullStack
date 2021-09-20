import matplotlib.pyplot as plt
import pandas as pd


def part3():
    filepath = r"C:\Users\Undergrad-Students\Documents\Learning_FullStack\Lab02\weather_data.txt"
    df = pd.read_csv(filepath, delimiter=",")
    
    df['date']=pd.to_datetime(df['date'])
    ax = plt.gca()
    df.plot(kind='line', x='date', y='actual_min_temp', color='blue', ax=ax)
    df.plot(kind='line', x='date', y='actual_max_temp', color='red', ax=ax)
    df.hist(column='actual_precipitation')
    print(df['actual_precipitation'].mean())
    plt.show()
    

part3()