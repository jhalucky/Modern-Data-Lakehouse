from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session
from src.transformations.drop_duplicates import drop_duplicates

spark = get_spark_session()
tables = load_bronze_tables(spark)

customers = tables["customers"]

drop_duplicates(customers)