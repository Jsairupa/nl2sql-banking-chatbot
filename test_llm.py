from src.schema_info import get_schema_text
from src.llm_client import generate_sql

schema = get_schema_text()

question = "What is the average account balance?"

sql = generate_sql(
    question=question,
    schema=schema
)

print("\nGenerated SQL:\n")
print(sql)