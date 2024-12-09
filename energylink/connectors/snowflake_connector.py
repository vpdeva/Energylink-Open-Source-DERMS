
import snowflake.connector

def query_snowflake(connection_params, query):
    """Execute a query on Snowflake."""
    conn = snowflake.connector.connect(**connection_params)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
            