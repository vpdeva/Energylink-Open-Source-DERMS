
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/iot-data")
def get_iot_data():
    with open("energylink/dummy_data/iot_data.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/scada-data")
def get_scada_data():
    with open("energylink/dummy_data/scada_data.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/forecast")
def get_forecast():
    forecast = [200, 220, 230, 250]
    return {"forecast": forecast}
            