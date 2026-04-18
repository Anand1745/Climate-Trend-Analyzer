import pandas as pd

def clean_data(df):
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df