
def connect_to_ge_smallworld(api_url, api_key):
    """Connect to GE Smallworld GIS system."""
    import requests
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError("Failed to connect to GE Smallworld GIS.")
            