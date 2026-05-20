from src.query_runner import run_query

sql = """
SELECT AVG(balance) AS average_balance
FROM accounts;
"""

result = run_query(sql)

print("\nQuery Result:\n")

print(result)