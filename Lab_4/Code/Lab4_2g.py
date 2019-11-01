"""
Lab 4: Q2G: Retrieve a Bucket Policy
"""
import boto3
import json

s3 = boto3.client("s3")

bucket_name = "ama067lab42abucket"

response = s3.get_bucket_acl(Bucket=bucket_name)
    
print(response["Policy"])