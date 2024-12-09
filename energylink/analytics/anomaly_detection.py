
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Detect anomalies in energy data using Isolation Forest."""
    model = IsolationForest(contamination=0.05)
    data = np.array(data).reshape(-1, 1)
    predictions = model.fit_predict(data)
    return predictions
            