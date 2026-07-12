import csv

def read_csv(spark, file_path):

    df = (
        spark.read
        .option("header",True)
        .option("inferschema",True)
        .csv(file_path)
    )

    return df
