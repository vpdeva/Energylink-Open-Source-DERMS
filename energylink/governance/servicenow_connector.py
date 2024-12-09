
import requests

def create_servicenow_incident(instance, username, password, short_description):
    """Create a ServiceNow incident for governance tasks."""
    url = f"https://{instance}.service-now.com/api/now/table/incident"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"short_description": short_description}
    response = requests.post(url, auth=(username, password), headers=headers, json=data)
    return response.json()
            