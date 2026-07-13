from pyspark.sql.functions import col, initcap
from pyspark.sql.types import StringType

def normalize_text(df):

    for field in df.schema.fields:

        if isinstance(field.dataType, StringType):

            df = df.withColumn(
                field.name,
                initcap(col(field.name))
            )

    print("Text normalized")

    return df

