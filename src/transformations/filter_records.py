from pyspark.sql.functions import col

def filter_records(df, condition):

    df = df.filter(condition)

    return df