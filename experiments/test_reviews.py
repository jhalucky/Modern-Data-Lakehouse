from src.spark.spark_session import get_spark_session
from src.bronze.bronze_pipeline import load_bronze_tables

spark = get_spark_session()

tables = load_bronze_tables(spark)

reviews = tables["reviews"]

reviews.write \
    .mode("overwrite") \
    .parquet("s3a://modern-retail-lakehouse-lucky/reviews_test")

print("Local parquet write successful!")