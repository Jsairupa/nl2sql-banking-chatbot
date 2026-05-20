import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect(
    "data/banking_demo.db"
)

# Check customers table
query = """
SELECT *
FROM customers
LIMIT 5;
"""

df = pd.read_sql_query(
    query,
    conn
)

print("\nCUSTOMERS TABLE:\n")

print(df)

conn.close()