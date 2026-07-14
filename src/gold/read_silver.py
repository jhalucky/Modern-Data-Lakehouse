from src.config.aws_config import SILVER_PATH

def read_silver(spark, table_name):

    df = (
        spark.read
        .format("delta")
        .load(SILVER_PATH + table_name)
    )

    return df



