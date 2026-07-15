from src.spark.spark_session import get_spark_session
from src.published.read_gold import read_gold
from src.transformations.write_parquet import write_parquet
from src.config.aws_config import GOLD_PATH

def publish_build_analytics(spark):

    product_gold = read_gold(
        spark,
        "product_analytics"
    )

    write_parquet(
        product_gold,
        GOLD_PATH+"product_analytics"
    )

    print("Product analytics published")