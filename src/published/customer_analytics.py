from src.published.read_gold import read_gold
from src.transformations.write_parquet import write_parquet
from src.spark.spark_session import get_spark_session


from src.config.aws_config import PUBLISHED_PATH

def publish_customer_analytics(spark):

    customer_gold = read_gold(
        spark, "customer_analytics"
    )

    write_parquet(
        customer_gold,
        PUBLISHED_PATH+"customer_analytics"
    )



    print("Customer analytics published.")

