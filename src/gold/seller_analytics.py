from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session

from pyspark.sql.functions import countDistinct, count, sum, avg

def build_seller_analytics(spark):

    sellers = read_silver(spark, "sellers")
    order_items = read_silver(spark, "order_items")
    reviews = read_silver(spark, "reviews")

    sellers_data = sellers.join(
        order_items,
        on="seller_id",
        how="left"
    )

    sellers_data = sellers_data.join(
        reviews,
        on="order_id",
        how="left"
    )

    sellers_gold = (
        sellers_data

        .groupBy(
            "seller_id","seller_city","seller_state"
        )

        .agg(
           
           countDistinct("order_id")
           .alias("total_orders"),

           count("order_item_id")
           .alias("total_products_sold"),

           sum("price")
           .alias("total_revenue"),

           avg("review_score")
           .alias("average_rating")
        )
    )

    print("Sellers Analysis Done!")
    

    return sellers_gold



