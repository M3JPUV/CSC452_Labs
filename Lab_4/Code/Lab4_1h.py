"""
Lab 4: Q1H: Get info about security groups
"""
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=["sg-06f0d329744eb00f0"])
    print("Success",response)
except ClientError as e:
    print(e)