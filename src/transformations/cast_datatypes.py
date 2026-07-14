from pyspark.sql.functions import (
    col,
    to_timestamp,
    when
)

ISO_COLUMNS = {
    "shipping_limit_date",
    "review_creation_date",
    "review_answer_timestamp"
}

US_COLUMNS = {
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
}


def cast_datatypes(df, schema):

    print("\n" + "=" * 60)
    print("CAST DATATYPES")
    print("=" * 60)

    print("\nDataFrame Columns:")
    print(df.columns)

    print("\nExpected Schema:")
    for column, datatype in schema.items():
        print(f"{column:<35} ---> {datatype}")

    print()

    for column, datatype in schema.items():

        print(f"Casting '{column}' -> {datatype}")

        if datatype == "timestamp":

            if column in ISO_COLUMNS:

                df = df.withColumn(
                    column,
                    to_timestamp(
                        col(column),
                        "yyyy-MM-dd HH:mm:ss"
                    )
                )

            elif column in US_COLUMNS:

                df = df.withColumn(
                    column,
                    to_timestamp(
                        col(column),
                        "M/d/yyyy H:mm"
                    )
                )

            else:

                print(f"⚠ No timestamp format configured for {column}")

        elif datatype == "int":

            # Only cast numeric values
            df = df.withColumn(
                column,
                when(
                    col(column).rlike(r"^[0-9]+$"),
                    col(column).cast("int")
                ).otherwise(None)
            )

        elif datatype == "double":

            df = df.withColumn(
                column,
                when(
                    col(column).rlike(r"^[0-9]+(\.[0-9]+)?$"),
                    col(column).cast("double")
                ).otherwise(None)
            )

        else:

            df = df.withColumn(
                column,
                col(column).cast(datatype)
            )

        print(f"✓ {column}")

    print("\nDatatypes casted!\n")

    return df