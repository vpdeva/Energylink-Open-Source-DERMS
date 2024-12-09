
from databricks import sql

def query_databricks(sql_query, server_hostname, http_path, access_token):
    """Query Databricks SQL endpoint."""
    with sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()
            