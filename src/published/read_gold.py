from src.config.aws_config import GOLD_PATH
from delta.tables import DeltaTable

def read_gold(spark, table_name):

    return (
        DeltaTable
        .forPath(
            spark,
            GOLD_PATH+table_name
        )
        .toDF()
    )

