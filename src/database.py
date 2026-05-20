import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

# Create Faker object
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect("data/banking_demo.db")

# Create cursor
cursor = conn.cursor()

# ---------------------------------------------------
# DROP TABLES IF THEY ALREADY EXIST
# ---------------------------------------------------

cursor.execute("DROP TABLE IF EXISTS transactions")
cursor.execute("DROP TABLE IF EXISTS accounts")
cursor.execute("DROP TABLE IF EXISTS customers")

# ---------------------------------------------------
# CREATE CUSTOMERS TABLE
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT,
    city TEXT,
    signup_date DATE
)
""")

# ---------------------------------------------------
# CREATE ACCOUNTS TABLE
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    account_type TEXT,
    balance REAL,
    opened_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# ---------------------------------------------------
# CREATE TRANSACTIONS TABLE
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    amount REAL,
    txn_type TEXT,
    category TEXT,
    txn_date DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
""")

# ---------------------------------------------------
# INSERT FAKE CUSTOMERS
# ---------------------------------------------------

print("Creating fake customers...")

for _ in range(100):

    full_name = fake.name()
    email = fake.email()
    city = fake.city()

    signup_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    cursor.execute("""
    INSERT INTO customers (
        full_name,
        email,
        city,
        signup_date
    )
    VALUES (?, ?, ?, ?)
    """, (
        full_name,
        email,
        city,
        signup_date
    ))

# ---------------------------------------------------
# INSERT FAKE ACCOUNTS
# ---------------------------------------------------

print("Creating fake accounts...")

account_types = [
    "checking",
    "savings",
    "credit"
]

for customer_id in range(1, 101):

    number_of_accounts = random.randint(1, 3)

    for _ in range(number_of_accounts):

        account_type = random.choice(account_types)

        balance = round(
            random.uniform(100, 50000),
            2
        )

        opened_date = fake.date_between(
            start_date="-3y",
            end_date="today"
        )

        cursor.execute("""
        INSERT INTO accounts (
            customer_id,
            account_type,
            balance,
            opened_date
        )
        VALUES (?, ?, ?, ?)
        """, (
            customer_id,
            account_type,
            balance,
            opened_date
        ))

# ---------------------------------------------------
# INSERT FAKE TRANSACTIONS
# ---------------------------------------------------

print("Creating fake transactions...")

categories = [
    "groceries",
    "salary",
    "shopping",
    "utilities",
    "restaurant",
    "travel",
    "fuel"
]

# Get all account IDs
cursor.execute("SELECT account_id FROM accounts")

account_ids = cursor.fetchall()

for account in account_ids:

    account_id = account[0]

    number_of_transactions = random.randint(10, 40)

    for _ in range(number_of_transactions):

        amount = round(
            random.uniform(10, 5000),
            2
        )

        txn_type = random.choice([
            "debit",
            "credit"
        ])

        category = random.choice(categories)

        txn_date = fake.date_between(
            start_date="-1y",
            end_date="today"
        )

        cursor.execute("""
        INSERT INTO transactions (
            account_id,
            amount,
            txn_type,
            category,
            txn_date
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            account_id,
            amount,
            txn_type,
            category,
            txn_date
        ))

# ---------------------------------------------------
# SAVE CHANGES
# ---------------------------------------------------

conn.commit()

# ---------------------------------------------------
# CLOSE CONNECTION
# ---------------------------------------------------

conn.close()

print("Database created successfully!")
print("File saved as:")
print("data/banking_demo.db")