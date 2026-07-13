from pyspark.sql.functions import col

def filter_records(df, condition):

    df = df.filter(condition)

    print("Records filtered")

    return df