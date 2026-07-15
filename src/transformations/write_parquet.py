from pyspark.sql import DataFrame

def write_parquet(df: DataFrame, path: str):

    (
        df.write
        .format("parquet")
        .mode("overwrite")
        .save(path)
    )

    print(f"Published successfully -> {path}")