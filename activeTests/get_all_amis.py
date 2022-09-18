'''
Prints in the terminal the haw data from aws amis
Needs prides *--profile* and *--region* as argument
'''
import boto3
import argparse
import os
import json
from botocore.config import Config

parser = argparse.ArgumentParser()
parser.add_argument(
    "--profile",
    "-p"
)
parser.add_argument(
    "--region",
    "-r"
)
args = parser.parse_args()

os.environ['AWS_PROFILE'] = args.profile

my_config = Config(
    region_name = 'sa-east-1',
)

client = boto3.client('ec2', config=my_config)

results = client.describe_images()

print(json.dumps(results['Images'], indent=4))
