"""
Lab 4: Q2B: List Existing Amazon S3 Buckets
"""
import boto3

s3_client = boto3.client("s3")
response = s3_client.list_buckets()

# Output the bucket names
print("Existing buckets:")
for bucket in response["Buckets"]:
    print(f' {bucket["Name"]}')