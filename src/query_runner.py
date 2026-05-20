import sqlite3
import pandas as pd

# ---------------------------------------------------
# RUN QUERY FUNCTION
# ---------------------------------------------------

def run_query(sql_query):

    # Connect to database
    conn = sqlite3.connect(
        "data/banking_demo.db"
    )

    # Execute query
    df = pd.read_sql_query(
        sql_query,
        conn
    )

    # Close connection
    conn.close()

    return df