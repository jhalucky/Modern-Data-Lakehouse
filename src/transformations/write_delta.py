from pyspark.sql import DataFrame

def write_Delta(df: DataFrame, path: str):

    print(f"\nWriting -> {path}")

    (
        df.write
          .format("delta")
          .mode("overwrite")
          .save(path)
    )

    print(f"Finished -> {path}")