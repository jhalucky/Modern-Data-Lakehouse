from botocore.exceptions import ClientError
from s3_client import get_s3_client

def list_objects(client, bucket_name, prefix):

    try:

        response = client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix
        )

        if "Contents" not in response:
            print("No objects found")

        for obj in response["Contents"]:
            print(obj["Key"])


    except ClientError as e:

        print(e)



client = get_s3_client()
list_objects(client, "modern-retail-lakehouse-lucky","bronze")