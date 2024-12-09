
from hdbcli import dbapi

def fetch_hana_data(connection_params, query):
    """Fetch data from SAP HANA."""
    conn = dbapi.connect(
        address=connection_params['host'],
        port=connection_params['port'],
        user=connection_params['user'],
        password=connection_params['password']
    )
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data
            