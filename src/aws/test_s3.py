from s3_client import get_s3_client
from botocore.exceptions import ClientError

try:

    client = get_s3_client()

    buckets = client.list_buckets()

    for bucket in buckets['Buckets']:
        print(bucket['Name'], bucket[""])


except ClientError as e:

    print(e)

