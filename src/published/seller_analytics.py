from src.spark.spark_session import get_spark_session

from src.transformations.write_parquet import write_parquet
from src.published.read_gold import read_gold

from src.config.aws_config import PUBLISHED_PATH

def publish_seller_analytics(spark):

    seller_gold = read_gold(
        spark,
        "seller_analytics"
    )

    write_parquet(
        seller_gold,
        PUBLISHED_PATH+"seller_analytics"
    )

    print("Seller analytics published!")



