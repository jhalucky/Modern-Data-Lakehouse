from src.spark.spark_session import get_spark_session

from src.transformations.write_parquet import write_parquet
from src.published.read_gold import read_gold

from src.config.aws_config import PUBLISHED_PATH

def publish_clv_analytics(spark):

    clv_gold = read_gold(
        spark,
        "clv_analytics"
    )

    write_parquet(
        clv_gold,
        PUBLISHED_PATH+"clv_analytics"
    )

    print("CLV analytics published")


if __name__ == "__main__":
    spark = get_spark_session()
    publish_clv_analytics(spark)