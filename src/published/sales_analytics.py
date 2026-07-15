from src.spark.spark_session import get_spark_session

from src.published.read_gold import read_gold
from src.config.aws_config import PUBLISHED_PATH

from src.transformations.write_parquet import write_parquet


def publish_sales_analytics(spark):

    sales_gold = read_gold(
        spark,
        "sales_analytics"
    )

    write_parquet(
        sales_gold,
        PUBLISHED_PATH+"sales_analytics"
    )

    
    print("Sales analytics published.")


if __name__=="__main__":
    spark = get_spark_session()
    publish_sales_analytics(spark)
