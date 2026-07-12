from botocore.exceptions import ClientError
from s3_client import get_s3_client

def delete_file(client, bucket_name, s3_key):

    try:

        client.delete_object(
            Bucket = bucket_name,
            Key = s3_key
        )

        print(f"{s3_key} has been deleted.")


    except ClientError as e:

        print(f"Deletion failed: {e}")


client = get_s3_client()
delete_file(client, "modern-retail-lakehouse-lucky","bronze/test.txt")