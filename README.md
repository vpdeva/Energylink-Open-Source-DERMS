
# EnergyLink - Open Source Energy Data Exchange and DERMS

EnergyLink is a comprehensive open-source platform for energy data management and Distributed Energy Resource Management System (DERMS).

## Features
- **Cloud Connectors**: AWS S3, Azure Blob, Google Cloud Storage.
- **Data Platforms**: Databricks, DBT, Snowflake.
- **GIS Integration**: GE Smallworld GIS.
- **Energy Management**: Zepben Energy Workbench, SAP HANA.
- **Blockchain Smart Contracts**: Deploy and manage energy exchange contracts.
- **AI and Analytics**: Forecasting and anomaly detection.
- **Governance**: Data mesh manager, JIRA, and ServiceNow integration.
- **Dashboard**: Interactive dashboard with IoT, SCADA, and forecast visualisation.

## Installation
Run the following:
```
pip install .
```

## Usage
### Start the Backend
Run the backend with FastAPI:
```
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Start the Dashboard
Run the Streamlit dashboard:
```
streamlit run dashboard.py
```

### Example: Query Snowflake
```python
from energylink.connectors.snowflake_connector import query_snowflake

connection_params = {
    "user": "your_user",
    "password": "your_password",
    "account": "your_account"
}
data = query_snowflake(connection_params, "SELECT * FROM energy_data")
print(data)
```
    