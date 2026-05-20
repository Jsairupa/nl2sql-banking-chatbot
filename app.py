import streamlit as st
import time

from src.schema_info import get_schema_text
from src.llm_client import generate_sql
from src.sql_validator import (
    validate_sql,
    SQLValidationError
)
from src.query_runner import run_query

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Banking Analytics Chatbot",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🏦 Banking Analytics Chatbot")

st.caption(
    "Ask questions about banking data using natural language."
)

# ---------------------------------------------------
# SIDEBAR EXAMPLES
# ---------------------------------------------------

with st.sidebar:

    st.header("Example Questions")

    st.markdown("""
    - How many customers do we have?
    - What is the average balance?
    - Show top 5 balances
    - Average balance by account type
    - Total transactions by category
    """)

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

question = st.text_input(
    "Ask a question:",
    placeholder="Example: What is the average account balance?"
)

# ---------------------------------------------------
# PROCESS QUESTION
# ---------------------------------------------------

if question:

    start_time = time.time()

    schema = get_schema_text()

    try:

        # Generate SQL
        with st.spinner("Generating SQL..."):

            sql_query = generate_sql(
                question=question,
                schema=schema
            )

        # Validate SQL
        validated_sql = validate_sql(
            sql_query
        )

        # Show SQL
        st.subheader("Generated SQL")

        st.code(
            validated_sql,
            language="sql"
        )

        # Run Query
        with st.spinner("Running query..."):

            result_df = run_query(
                validated_sql
            )

        # Show Results
        st.subheader("Query Results")

        st.dataframe(
            result_df,
            use_container_width=True
        )

        # Execution Time
        elapsed = round(
            time.time() - start_time,
            2
        )

        st.success(
            f"Completed in {elapsed} seconds"
        )

    except SQLValidationError as e:

        st.error(
            f"SQL Validation Error: {e}"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )