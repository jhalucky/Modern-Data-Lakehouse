from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session

from pyspark.sql.functions import count, sum, avg

def build_product_analytics(spark):

    products = read_silver(spark, "products")
    order_items = read_silver(spark, "order_items")
    reviews = read_silver(spark, "reviews")
    categories = read_silver(spark, "categories")

    product_data = products.join(
        order_items,
        on="product_id",
        how="left"
    )

    product_data = product_data.join(
        reviews,
        on="order_id",
        how="left"
    )

    product_data = product_data.join(
        categories,
        on="product_category_name",
        how="left"
    )

    product_gold = (
        product_data

        .groupBy(
            "product_id",
            "product_category_name"
        )

        .agg(
           count("order_item_id")
           .alias("units_sold"),

           sum("price")
           .alias("total_revenue"),

           count("review_score")
           .alias("total_reviews"),

           avg("review_score")
           .alias("avg_rating")

        )
    )

    print("Product Analysis done!")

    return product_gold

def main():

    spark = get_spark_session()

    build_product_analytics(spark)


if __name__ == "__main__":
    main()
