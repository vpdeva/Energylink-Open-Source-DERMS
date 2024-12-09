
from zepben_sdk import EnergyWorkbench

def fetch_zepben_data(connection_params, query):
    """Fetch data from Zepben Energy Workbench."""
    energy_workbench = EnergyWorkbench(**connection_params)
    data = energy_workbench.query(query)
    return data
            