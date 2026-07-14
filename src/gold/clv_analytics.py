from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session

from pyspark.sql.functions import when, col, countDistinct, avg, min, max, sum

def build_clv_analytics(spark):

    customers = read_silver(spark, "customers")
    orders = read_silver(spark, "orders")
    payments = read_silver(spark, "payments")


    customer_data = customers.join(
        orders,
        on="customer_id",
        how="left"
    )

    customer_transactions = customer_data.join(
        payments,
        on="order_id",
        how="left"
    )

    clv_gold = (

        customer_transactions

        .groupBy("customer_id", "customer_city", "customer_state")

        .agg(

            countDistinct("order_id")
            .alias("total_orders"),

            sum("payment_value")
            .alias("lifetime_value"),

            avg("payment_value")
            .alias("average_order_value"),

            min("order_purchase_timestamp")
            .alias("first_purchase"),

            max("order_purchase_timestamp")
            .alias("last_purchase")



        )
    )

    clv_gold = clv_gold.withColumn(
        "customer_segment",
        when(col("lifetime_value")<100, "Bronze")
        .when(col("lifetime_value")<500, "Silver")
        .when(col("lifetime_value")<1000, "Gold")
        .otherwise("Platinum")
    )

    clv_gold.show(5)
    print("Analysis done")
    return clv_gold


def main():

    spark = get_spark_session()

    build_clv_analytics(spark)


if __name__ == "__main__":
    main()