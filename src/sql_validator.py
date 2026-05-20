import re

# ---------------------------------------------------
# ALLOWED TABLES
# ---------------------------------------------------

ALLOWED_TABLES = {
    "customers",
    "accounts",
    "transactions"
}

# ---------------------------------------------------
# FORBIDDEN SQL KEYWORDS
# ---------------------------------------------------

FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE"
]

# ---------------------------------------------------
# CUSTOM ERROR
# ---------------------------------------------------

class SQLValidationError(Exception):
    pass

# ---------------------------------------------------
# VALIDATION FUNCTION
# ---------------------------------------------------

def validate_sql(sql):

    # Remove spaces and semicolon
    cleaned_sql = sql.strip().rstrip(";")

    # Convert to uppercase
    upper_sql = cleaned_sql.upper()

    # ---------------------------------------------------
    # MUST START WITH SELECT
    # ---------------------------------------------------

    if not upper_sql.startswith("SELECT"):

        raise SQLValidationError(
            "Only SELECT queries are allowed."
        )

    # ---------------------------------------------------
    # BLOCK FORBIDDEN KEYWORDS
    # ---------------------------------------------------

    for keyword in FORBIDDEN_KEYWORDS:

        pattern = rf"\b{keyword}\b"

        if re.search(pattern, upper_sql):

            raise SQLValidationError(
                f"Forbidden keyword detected: {keyword}"
            )

    # ---------------------------------------------------
    # CHECK TABLE NAMES
    # ---------------------------------------------------

    tables = re.findall(
        r"\bFROM\s+(\w+)|\bJOIN\s+(\w+)",
        upper_sql
    )

    used_tables = {
        table
        for pair in tables
        for table in pair
        if table
    }

    allowed_upper = {
        table.upper()
        for table in ALLOWED_TABLES
    }

    if not used_tables.issubset(allowed_upper):

        raise SQLValidationError(
            "Query uses unauthorized tables."
        )

    return cleaned_sql