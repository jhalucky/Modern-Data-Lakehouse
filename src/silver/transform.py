from transformations.fill_nulls import fill_nulls
from transformations.cast_datatypes import cast_datatypes
from transformations.trim_strings import trim_strings
from transformations.normalize_text import normalize_text
from transformations.derive_columns import derive_columns
from transformations.filter_records import filter_records
from transformations.drop_duplicates import drop_duplicates

def transform(df, schema, condition):

    df = fill_nulls(df)
    df = trim_strings(df)
    df = normalize_text(df)
    df = cast_datatypes(df, schema)
    df = filter_records(df, condition)
    df = drop_duplicates(df)
    df = derive_columns(df)

    return df