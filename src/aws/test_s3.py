from s3_client import get_s3_client
from botocore.exceptions import ClientError

try:

    client = get_s3_client()

    response = client.list_buckets()

    for bucket in response['Buckets']:
        print(bucket['Name'])


except ClientError as e:

    print(e)

