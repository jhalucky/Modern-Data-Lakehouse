from pyspark.sql.functions import col, count, when

def validate_nulls(df):

    report =  df.select([
        count(when(col(column).isNull(), column)).alias(column)
        for column in df.columns
    ])

    return report