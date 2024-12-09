
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Detect anomalies using Isolation Forest.""" 
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    anomalies = model.predict(data)
    return anomalies
            