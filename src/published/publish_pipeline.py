from src.spark.spark_session import get_spark_session

from src.published.customer_analytics import publish_customer_analytics
from src.published.product_analytics import publish_product_analytics
from src.published.sales_analytics import publish_sales_analytics
from src.published.seller_analytics import publish_seller_analytics
from src.published.clv_analytics import publish_clv_analytics


def publish_pipeline(spark):

    print("\nPublishing Gold Analytics...\n")

    publish_customer_analytics(spark)
    publish_product_analytics(spark)
    publish_sales_analytics(spark)
    publish_seller_analytics(spark)
    publish_clv_analytics(spark)

    print("\nPublished Layer completed successfully!")


def main():

    spark = get_spark_session()

    publish_pipeline(spark)

    spark.stop()


if __name__ == "__main__":
    main()