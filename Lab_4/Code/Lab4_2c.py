"""
Lab 4: Q2C: Upload files to an Amazon S3 Bucket
"""
import boto3

s3_client = boto3.client("s3")

filename = "README.md"
bucket_name = "ama067lab42abucket"

s3_client.upload_file(filename,bucket_name,filename)