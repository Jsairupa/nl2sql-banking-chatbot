import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.sql_validator import (
    validate_sql,
    SQLValidationError
)

# ---------------------------------------------------
# SAFE QUERY
# ---------------------------------------------------

safe_query = """
SELECT * FROM customers;
"""

# ---------------------------------------------------
# DANGEROUS QUERY
# ---------------------------------------------------

dangerous_query = """
DROP TABLE customers;
"""

# ---------------------------------------------------
# TEST SAFE QUERY
# ---------------------------------------------------

print("\nTesting SAFE query...\n")

try:

    result = validate_sql(safe_query)

    print("SAFE query PASSED")
    print(result)

except SQLValidationError as e:

    print("SAFE query FAILED")
    print(e)

# ---------------------------------------------------
# TEST DANGEROUS QUERY
# ---------------------------------------------------

print("\nTesting DANGEROUS query...\n")

try:

    result = validate_sql(dangerous_query)

    print("DANGEROUS query PASSED")
    print(result)

except SQLValidationError as e:

    print("DANGEROUS query BLOCKED")
    print(e)