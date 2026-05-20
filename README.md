# 🏦 NL2SQL Banking Analytics Chatbot

An end-to-end GenAI application that converts natural language questions into SQL queries for banking analytics using OpenAI, SQLite, and Streamlit.

---

# 🚀 Features

- Natural Language → SQL generation using OpenAI API
- SQLite banking database with synthetic customer/account/transaction data
- SQL guardrails for query safety
- Streamlit web interface
- Real-time SQL execution and result visualization
- Prompt-engineered SQL generation pipeline

---

# 🧠 Example Questions

- How many customers do we have?
- What is the average account balance?
- Show top 5 account balances
- Average balance by account type
- Total transactions by category

---

# 🏗️ Architecture

User Question
↓
OpenAI LLM
↓
SQL Generation
↓
SQL Validator
↓
SQLite Database
↓
Query Results in Streamlit

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| OpenAI API | LLM-powered SQL generation |
| SQLite | Banking database |
| Streamlit | Web UI |
| Pandas | Query result handling |
| Faker | Synthetic data generation |

---

# 📂 Project Structure

```text
nl2sql-banking-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── banking_demo.db
│
├── src/
│   ├── database.py
│   ├── llm_client.py
│   ├── query_runner.py
│   ├── schema_info.py
│   └── sql_validator.py
│
└── tests/
    └── test_validator.py