from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session

def product_analytics(spark):

    products = read_silver(spark, "products")
    order_items = read_silver(spark, "order_items")

    