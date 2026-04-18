import pandas as pd
import numpy as np
import os

def generate_data():
    os.makedirs("data/raw", exist_ok=True)

    dates = pd.date_range("2015-01-01", "2022-12-31")

    df = pd.DataFrame({
        "date": dates,
        "temperature": 25 + np.sin(np.arange(len(dates))/365*2*np.pi)*5 + np.random.randn(len(dates)),
        "rainfall": np.random.rand(len(dates))*10,
        "humidity": np.random.rand(len(dates))*100
    })

    df.to_csv("data/raw/climate_data.csv", index=False)

if __name__ == "__main__":
    generate_data()