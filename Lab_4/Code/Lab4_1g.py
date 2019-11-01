"""
Lab 4: Q1G: Delete a new key pair
"""
import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_key_pair(KeyName="ama067Lab41fKey")
print("Success",response)