from pyspark.sql.functions import col, upper, lower, initcap
from pyspark.sql.types import StringType

def normalize_text(df):

    for column in df.schema:

        if isinstance(column.dataType, StringType):

            if column.name == "customer_state":
                df = df.withColumn(
                    column.name,
                    upper(col(column.name))
                )

            

