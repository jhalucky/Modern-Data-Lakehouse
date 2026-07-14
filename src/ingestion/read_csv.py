def read_csv(spark, file_path):

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", False)
        .option("quote", '"')
        .option("escape", '"')
        .option("multiLine", True)
        .option("encoding", "UTF-8")
        .csv(file_path)
    )

    return df