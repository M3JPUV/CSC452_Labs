"""
Lab 4: Q1J: Delete security group
"""
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.delete_security_group(GroupName="Lab41I")
    print("Success",response)
except ClientError as e:
    print(e)