def validate_duplicate_primary_keys(df, column_name):

    total_rows = df.count()

    unique_rows = df.dropDuplicates([column_name]).count()

    duplicate_rows = total_rows - unique_rows

    print(f"Duplicate primary key rows: {duplicate_rows}")

    return duplicate_rows