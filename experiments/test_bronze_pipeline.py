from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session

spark = get_spark_session()

tables = load_bronze_tables(spark)

for name, df in tables.items():
    print("="*50)
    print(name.upper())
    df.printSchema()
    df.show(5)