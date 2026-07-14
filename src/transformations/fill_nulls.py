def fill_nulls(df, fill_values):

    df = df.fillna(fill_values)

    print("Null values filled.")

    return df