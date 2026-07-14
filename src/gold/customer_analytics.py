from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session
from pyspark.sql.functions import (
    countDistinct,
    sum,
    avg,
    min,
    max
)


def build_customer_analytics(spark):

    customers = read_silver(spark, "customers")
    orders = read_silver(spark, "orders")
    payments = read_silver(spark, "payments")


    customer_orders = customers.join(
        orders,
        on="customer_id",
        how="left"
    )

    customer_transactions = customer_orders.join(
        payments,
        on="order_id",
        how="left"
    )

    customer_gold = (
        customer_transactions

        .groupBy(
            "customer_id",
            "customer_city",
            "customer_state"
        )

        .agg(
            countDistinct("order_id")
            .alias("total_orders"),

            round(sum("payment_value"),2)
            .alias("total_spent"),

            round(avg("payment_value"),2)
            .alias("average_order_value"),

            min("order_purchase_timestamp")
            .alias("first_order"),

            max("order_purchase_timestamp")
            .alias("last_order")
        )
    )
    
    print("Customer analysis done!")
    return customer_gold


def main():

    spark = get_spark_session()

    build_customer_analytics(spark)


if __name__ == "__main__":
    main()