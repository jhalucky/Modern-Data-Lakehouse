def fill_nulls(df):

    df =  df.na.fill("Unknown")

    print("Filled Null values with unknown")

    return df