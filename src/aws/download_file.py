from s3_client import get_s3_client
from botocore.exceptions import ClientError


def download_file(client, bucket_name, s3_key, local_file):

    """Download a file from AWS bucket"""

    try:

        client.download_file(Bucket=bucket_name, Key=s3_key, Filename=local_file)

        print("File downloaded!")

    
    except ClientError as e:

        print(f"Download failed: {e}")



client = get_s3_client()

download_file(client, "modern-retail-lakehouse-lucky","bronze/test.txt","data/raw/test.txt")