from src.spark.spark_session import get_spark_session

from src.gold.customer_analytics import build_customer_analytics
from src.gold.product_analytics import build_product_analytics
from src.gold.sales_analytics import build_sales_analytics
from src.gold.seller_analytics import build_seller_analytics
from src.gold.clv_analytics import build_clv_analytics

from src.transformations.write_delta import write_Delta

from src.config.aws_config import GOLD_PATH


def gold_pipeline(spark):

    spark = get_spark_session()

    customer_gold = build_customer_analytics(spark)

    product_gold = build_product_analytics(spark)

    sales_gold = build_sales_analytics(spark)

    seller_gold = build_seller_analytics(spark)

    clv_gold = build_clv_analytics(spark)


    write_Delta(
        customer_gold,
        GOLD_PATH+ "customer_analytics"
    )
    write_Delta(
        product_gold,
        GOLD_PATH+ "product_analytics"
    )
    write_Delta(
        sales_gold,
        GOLD_PATH+ "sales_analytics"
    )
    write_Delta(
        seller_gold,
        GOLD_PATH+ "seller_analytics"
    )
    write_Delta(
        clv_gold,
        GOLD_PATH+ "clv_analytics"
    )

    print("=" * 60)
    print("Gold Layer Pipeline Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    spark = get_spark_session()
    gold_pipeline(spark)