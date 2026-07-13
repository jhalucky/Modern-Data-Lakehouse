from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session
from src.transformations.drop_duplicates import drop_duplicates
from src.transformations.fill_nulls import fill_nulls
from src.transformations.cast_datatypes import cast_datatypes

spark = get_spark_session()
tables = load_bronze_tables(spark)

customers = tables["customers"]

cast_datatypes(customers)
drop_duplicates(customers)
fill_nulls(customers)