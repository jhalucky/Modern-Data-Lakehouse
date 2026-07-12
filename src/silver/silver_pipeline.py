from src.spark.spark_session import get_spark_session

spark = get_spark_session()

print(
    spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()
)