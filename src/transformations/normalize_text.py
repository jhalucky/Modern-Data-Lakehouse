from pyspark.sql.functions import initcap, col
from pyspark.sql.types import StringType

def normalize_text(df):

    TIMESTAMP_COLUMNS = {
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "shipping_limit_date",
        "review_creation_date",
        "review_answer_timestamp"
    }

    for field in df.schema.fields:

        if (
            isinstance(field.dataType, StringType)
            and field.name not in TIMESTAMP_COLUMNS
        ):

            df = df.withColumn(
                field.name,
                initcap(col(field.name))
            )

    print("Text normalized")

    return df