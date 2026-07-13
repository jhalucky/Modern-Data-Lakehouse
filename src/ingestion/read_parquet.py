def read_parquet(spark, file_path):

    return spark.read.parquet(file_path)