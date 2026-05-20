from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---------------------------------------------------
# PROMPT TEMPLATE
# ---------------------------------------------------

PROMPT_TEMPLATE = """
You are an expert SQL analyst.

Convert the user's question into a valid SQLite SQL query.

DATABASE SCHEMA:

{schema}

RULES:
- Output ONLY SQL
- No explanations
- No markdown
- Use only SELECT queries
- Never use DELETE, DROP, UPDATE, INSERT

EXAMPLES:

Q: How many customers do we have?
A:
SELECT COUNT(*) FROM customers;

Q: What is the average balance by account type?
A:
SELECT account_type, AVG(balance)
FROM accounts
GROUP BY account_type;

USER QUESTION:
{question}

SQL:
"""

# ---------------------------------------------------
# GENERATE SQL FUNCTION
# ---------------------------------------------------

def generate_sql(question, schema):

    prompt = PROMPT_TEMPLATE.format(
        schema=schema,
        question=question
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql_query = response.choices[0].message.content

    return sql_query.strip()