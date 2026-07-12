def validate_foreign_key(child_df, parent_df, child_column, parent_column):


    invalid_rows = (
        child_df.join(
            parent_df,
            child_df[child_column] == parent_df[parent_column],
            how="left_anti"
        )
    )

    invalid_count = invalid_rows.count()

    if invalid_count == 0:
        print("Foreign key validation passed.")

    else:

        print("Foreign key validation failed.")
        print(f"Invalid foreign keys: {invalid_count}")

        invalid_rows.show()

    return invalid_count