from src.bronze.bronze_pipeline import load_bronze_tables
from src.spark.spark_session import get_spark_session
from src.validation.null_validator import validate_nulls
# from src.validation.duplicate_validator import validate_duplicates
from src.validation.schema_validator import schema_validator
from schemas import CUSTOMER_SCHEMA

spark = get_spark_session()

tables = load_bronze_tables(spark)

customers = tables["customers"]

orders = tables["orders"]

# null_report = validate_nulls(customers)
# null_report = validate_nulls(orders)
# duplicate_report = drop_duplicates(customers)
schema_report = schema_validator(customers, CUSTOMER_SCHEMA)


for name, df in tables.items():
    print("="*50)
    print(name.upper())
    df.printSchema()
    df.show(5)

print(f"Schema test passed or failed: {schema_report}")


    



