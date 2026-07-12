from pyspark.sql import SparkSession

def spark_session():

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("Modern data Lakehouse")
        .getOrCreate()
    )

    return spark