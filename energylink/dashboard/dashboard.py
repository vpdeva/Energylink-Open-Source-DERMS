
import streamlit as st
import requests

st.title("EnergyLink Dashboard")

# IoT Data
st.header("IoT Data")
iot_data = requests.get("http://localhost:8000/iot-data").json()
st.json(iot_data)

# SCADA Data
st.header("SCADA Data")
scada_data = requests.get("http://localhost:8000/scada-data").json()
st.json(scada_data)

# Forecast
st.header("Energy Demand Forecast")
forecast = requests.get("http://localhost:8000/forecast").json()
st.line_chart(forecast["forecast"])
            