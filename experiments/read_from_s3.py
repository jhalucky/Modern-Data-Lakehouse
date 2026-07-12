from src.spark.spark_session import get_spark_session
from src.ingestion.read_csv import read_csv
from src.config.aws_config import BRONZE_PATH


spark = get_spark_session()

orders_df = read_csv(
    spark, file_path=BRONZE_PATH +"orders.csv"
)

orders_df.printSchema()
orders_df.show(5)