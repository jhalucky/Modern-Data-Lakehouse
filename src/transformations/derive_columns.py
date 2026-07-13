from pyspark.sql.functions import year, month, dayofmonth

def derive_columns(df):
    df = (

        df.withColumn(
           "purchase_year",
           year("order_purchase_timestamp")
        )

        .withColumn(
           "purchase_month",
           month("order_purchase_timestamp")
        )

        .withColumn(
           "purchase_day",
           dayofmonth("order_purchase_timestamp")
        )
    )

    print("Columns Derived!")
    return df