import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

def plot_temperature(df):
    fig = px.line(df, x='date', y='temperature')
    fig.write_html("outputs/plots/temp.html")

def plot_anomalies(df):
    fig = px.scatter(df, x='date', y='temperature', color='anomaly')
    fig.write_html("outputs/plots/anomaly.html")

def plot_forecast(df, forecast):
    plt.figure()
    plt.plot(df['date'], df['temperature'])

    future_dates = pd.date_range(df['date'].iloc[-1], periods=len(forecast)+1)[1:]
    plt.plot(future_dates, forecast)

    plt.savefig("outputs/plots/forecast.png")