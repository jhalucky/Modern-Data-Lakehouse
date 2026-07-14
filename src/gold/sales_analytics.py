from src.gold.read_silver import read_silver
from src.spark.spark_session import get_spark_session

from pyspark.sql.functions import to_date, countDistinct, sum, avg, col, round

def build_sales_analytics(spark):

    orders = read_silver(spark, "orders")
    payments = read_silver(spark, "payments")
    
    
    sales_data = orders.join(
        payments,
        on="order_id",
        how="left"
    )

    
    sales_data = sales_data.withColumn(
        "order_date",
        to_date(col("order_purchase_timestamp"))
    )


    order_gold = (
        
        
        sales_data

        .groupBy(
            "order_date"
        )

        .agg(
            countDistinct("order_id")
            .alias("total_orders"),

            countDistinct("customer_id")
            .alias("total_customers"),

            round(sum("payment_value"), 2)
            .alias("total_revenue"),

            round(avg("payment_value"), 2)
            .alias("average_order_value")
        )


    )

    print("Order analysis done successfully")
    

    return order_gold

def main():

    spark = get_spark_session()

    build_sales_analytics(spark)


if __name__ == "__main__":
    main()