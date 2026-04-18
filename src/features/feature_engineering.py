def create_features(df):
    df['month'] = df['date'].dt.month
    df['temp_roll'] = df['temperature'].rolling(7).mean()
    return df.dropna()