from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session
from src.validation.quality_report import generate_quality_report
from schemas import CUSTOMER_SCHEMA

spark = get_spark_session()

tables = load_bronze_tables(spark)

customers = tables["customers"]

orders = tables["orders"]

generate_quality_report(
    customers,
    table_name="customers",
    primary_key="customer_id",
    expected_schema=CUSTOMER_SCHEMA
)