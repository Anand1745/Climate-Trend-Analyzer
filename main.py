import sys, os
import pandas as pd

sys.path.append(os.path.abspath("."))

from src.ingestion.data_loader import load_data
from src.preprocessing.cleaner import clean_data
from src.features.feature_engineering import create_features
from src.anomaly.isolation_forest import detect_anomalies
from src.forecasting.arima_model import train_arima, forecast_future
from src.visualization.plots import plot_temperature, plot_anomalies, plot_forecast

def main():
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)

    df = load_data("data/raw/climate_data.csv")

    df = clean_data(df)
    df = create_features(df)
    df = detect_anomalies(df)

    df.to_csv("data/processed/cleaned.csv", index=False)

    # Forecast (FIXED)
    series = df.set_index('date')['temperature']
    model = train_arima(series)
    forecast = forecast_future(model)

    future_dates = pd.date_range(df['date'].iloc[-1], periods=len(forecast)+1)[1:]

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "forecast": forecast.values
    })

    forecast_df.to_csv("outputs/forecast.csv", index=False)

    plot_temperature(df)
    plot_anomalies(df)
    plot_forecast(df, forecast)

if __name__ == "__main__":
    main()