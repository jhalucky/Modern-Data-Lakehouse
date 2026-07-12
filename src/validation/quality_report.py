from src.validation.null_validator import validate_nulls
from src.validation.duplicate_validator import validate_duplicates
from src.validation.schema_validator import schema_validator
from src.validation.primary_key_validator import validate_duplicate_primary_keys


def generate_quality_report(df, table_name, primary_key, expected_schema):

    """Run all quality checks for a table."""

    print("="*50)
    print(f"QUALITY REPORT: {table_name.upper()}")
    print("="*50)

    print("\n1. Null Validation")
    validate_nulls(df).show()

    print("\n2. Duplicates Validation")
    validate_duplicates(df).show()

    print("\n3. Primary key validation")
    validate_duplicate_primary_keys(df, primary_key)

    print("\n4. Schema validation")
    schema_validator(df, expected_schema)


    print("="*50)

