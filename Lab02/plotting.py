import matplotlib as plt
import pandas as pd


def part3():
    filepath = r"C:\Users\Undergrad-Students\Documents\Learning_FullStack\Lab02\weather_data.txt"
    df = pd.read_csv(filepath, delimiter=",")
    
    df['date']=pd.to_datetime(df['date'])
    
    plt.scatter(df['actual_min_temp'], df['actual_max_temp'])
    plt.show()
    

part3()