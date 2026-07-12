from schemas import CUSTOMER_SCHEMA

def schema_validator(df, expected_schema):

    actual_schema = {
        field.name: field.dataType.simpleString()
        for field in df.schema.fields
    }

    

    if actual_schema == expected_schema:

        print("\nSchema validation passed")
        return "Passed"
    
    print("\nSchema validation failed")
    
    return "Failed"

