
import numpy as np
from sklearn.linear_model import LinearRegression

def time_series_forecasting(data, look_back=3):
    """Forecast energy demand using linear regression.""" 
    X = np.array([data[i:i+look_back] for i in range(len(data) - look_back)])
    y = np.array(data[look_back:])
    model = LinearRegression().fit(X, y)
    predictions = model.predict(X)
    return predictions
            