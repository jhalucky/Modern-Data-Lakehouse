from src.config.aws_config import BRONZE_PATH

def read_bronze(spark, table_name):

    df = (
        spark.read
        .format("delta")
        .load(BRONZE_PATH + table_name)
    )

    return df