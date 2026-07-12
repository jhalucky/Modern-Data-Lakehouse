def drop_duplicates(df):

    total_rows = df.count()

    unique_rows = df.dropDuplicates().count()

    duplicate_rows = total_rows - unique_rows

    print(f"Duplicate rows : {duplicate_rows}")

    return df