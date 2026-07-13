from pyspark.sql import DataFrame

def write_Delta(df: DataFrame, table_name: str, mode: str = "overwrite"):

    df = (
        df.write
    .format("delta")
    .mode(mode)
    .saveAsTable(table_name)
    )

    return df