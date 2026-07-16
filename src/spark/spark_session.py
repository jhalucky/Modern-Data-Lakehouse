from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

from src.config.spark_config import APP_NAME, MASTER


def get_spark_session():

    builder = (
        SparkSession.builder
        .appName(APP_NAME)
        .master(MASTER)

        # Delta
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension"
        )
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog"
        )
        .config(
            "spark.delta.logStore.class",
            "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore"
        )

        # S3
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "s3.amazonaws.com"
        )
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider"
        )
    )

    spark = configure_spark_with_delta_pip(
        builder
        ).getOrCreate()

    return spark