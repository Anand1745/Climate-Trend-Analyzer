def generate_kpis(df):
    return {
        "Avg Temp": df['temperature'].mean(),
        "Max Temp": df['temperature'].max(),
        "Min Temp": df['temperature'].min(),
        "Anomalies": int(df['anomaly'].sum())
    }