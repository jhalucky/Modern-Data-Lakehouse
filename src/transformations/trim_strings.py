from pyspark.sql.functions import col, trim

def trim_strings(df):

    for c in df.columns:
        df = df.withColumn(c, trim(col(c)))

    print("\nStrings trimmed.")
    return df