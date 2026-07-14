from src.transformations.fill_nulls import fill_nulls
from src.transformations.cast_datatypes import cast_datatypes
from src.transformations.trim_strings import trim_strings
from src.transformations.normalize_text import normalize_text
# from src.transformations.derive_columns import derive_columns 
from src.transformations.filter_records import filter_records
from src.transformations.drop_duplicates import drop_duplicates

def transform(df, schema, fill_values):

    df = drop_duplicates(df)

    df = fill_nulls(df, fill_values)

    df = trim_strings(df)

    df = cast_datatypes(df, schema)

    return df