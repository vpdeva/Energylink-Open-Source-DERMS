
import numpy as np
from scikit-learn.linear_model import LinearRegression

def forecast_energy_demand(data, look_back=3):
    """Forecast energy demand using linear regression."""
    X = np.array([data[i:i+look_back] for i in range(len(data) - look_back)])
    y = np.array(data[look_back:])
    model = LinearRegression().fit(X, y)
    predictions = model.predict(X)
    return predictions
            