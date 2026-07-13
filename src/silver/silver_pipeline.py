from pyspark.sql.functions import col
from src.spark.spark_session import get_spark_session

from src.bronze.bronze_pipeline import load_bronze_tables

from src.transformations.transform import transform
from src.transformations.write_delta import write_Delta

from src.config.aws_config import SILVER_PATH

from schemas import CUSTOMER_SCHEMA, ORDER_SCHEMA

spark = get_spark_session()

tables = load_bronze_tables(spark)

customers = tables["customers"]

orders = tables["orders"]

customers = transform(orders, ORDER_SCHEMA, col("order_status") != "cancelled")

write_Delta(
    orders,
    SILVER_PATH="orders"
)

print("Orders silver layer completed.")