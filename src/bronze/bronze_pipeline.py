from src.config.aws_config import BRONZE_PATH
from src.ingestion.read_csv import read_csv
from src.spark.spark_session import get_spark_session

def load_bronze_tables(spark):

    datasets = {
        "customers": read_csv(spark, BRONZE_PATH+ "customers.csv"),
        "orders":read_csv(spark, BRONZE_PATH+"orders.csv"),
        "order_items":read_csv(spark, BRONZE_PATH+"order_items.csv"),
        "payments":read_csv(spark, BRONZE_PATH+"order_payments.csv"),
        "products": read_csv(spark, BRONZE_PATH+"products.csv"),
        "categories":read_csv(spark, BRONZE_PATH+"categories.csv"),
        "reviews": read_csv(spark, BRONZE_PATH+"reviews.csv"),
        "sellers": read_csv(spark, BRONZE_PATH+"sellers.csv"),
        "geolocation": read_csv(spark, BRONZE_PATH+"geolocation.csv")
    }



    return datasets

spark = get_spark_session()
reviews = read_csv(spark, BRONZE_PATH + "reviews.csv")

reviews.printSchema()

reviews.select(
    "review_comment_message",
    "review_creation_date",
    "review_answer_timestamp"
).show(20, truncate=False)