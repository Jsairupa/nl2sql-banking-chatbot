def get_schema_text():

    schema = """

    TABLE: customers
    --------------------------------
    customer_id INTEGER PRIMARY KEY
    full_name TEXT
    email TEXT
    city TEXT
    signup_date DATE

    TABLE: accounts
    --------------------------------
    account_id INTEGER PRIMARY KEY
    customer_id INTEGER
    account_type TEXT
    balance REAL
    opened_date DATE

    TABLE: transactions
    --------------------------------
    transaction_id INTEGER PRIMARY KEY
    account_id INTEGER
    amount REAL
    txn_type TEXT
    category TEXT
    txn_date DATE

    RELATIONSHIPS:
    --------------------------------
    accounts.customer_id -> customers.customer_id

    transactions.account_id -> accounts.account_id

    """

    return schema