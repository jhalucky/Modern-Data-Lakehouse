from pyspark.sql.functions import col

def cast_datatypes(df, schema):

    for column, datatype in schema.items():
        df = df.withColumn(
            column,
            col(column).cast(datatype)
        )

    print("Datatypes casted!")

    return df