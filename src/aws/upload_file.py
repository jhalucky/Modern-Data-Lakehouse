from s3_client import get_s3_client
from botocore.exceptions import ClientError

def upload_file(client, local_file, bucket_name, s3_key):

    try:

        client.upload_file(Filename=local_file, Bucket=bucket_name,Key=s3_key)

        print("Uploaded successfully")

    except ClientError as e:

        print(f"upload failed: {e}")

    

client = get_s3_client()   

upload_file(client, "test.txt", "modern-retail-lakehouse-lucky", "bronze/test.txt")

