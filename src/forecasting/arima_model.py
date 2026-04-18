from statsmodels.tsa.arima.model import ARIMA

def train_arima(series):
    model = ARIMA(series, order=(2,1,2))
    return model.fit()

def forecast_future(model, steps=30):
    return model.forecast(steps=steps)