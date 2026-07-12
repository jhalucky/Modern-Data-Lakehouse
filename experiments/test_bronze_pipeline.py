from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session
from src.validation.null_validator import validate_nulls

spark = get_spark_session()

tables = load_bronze_tables(spark)

customers = tables["customers"]

null_report = validate_nulls(customers)


# for name, df in tables.items():
#     print("="*50)
#     print(name.upper())
#     df.printSchema()
#     df.show(5)

null_report.show()