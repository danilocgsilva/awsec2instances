import sys, json, subprocess
import boto3
import re
import os


def extractPublicIpAddress( instanceInfos ):
    if "PublicIpAddress" in instanceInfos:
        return instanceInfos["PublicIpAddress"]
    else:
        return "---"

def extractInstanceType( instanceInfos ):
    return instanceInfos["InstanceType"]

def extractName(instanceInfos):
    if "Tags" in instanceInfos:
        listTags = instanceInfos["Tags"]

        for tag in listTags:
            if tag["Key"] == "Name":
                return tag["Value"]

    return "---"

def extracState ( instanceInfos ):
    return instanceInfos["State"]["Name"]

def extractInstanceId ( instanceInfos ):
    return instanceInfos["InstanceId"]

def getRawDataFromCli(region = None) -> dict:
    return getRawData(None, region)

def getRawData(profile = None, region = None) -> dict:

    if profile:
        os.environ['AWS_PROFILE'] = profile

    if region:
        os.environ['AWS_DEFAULT_REGION'] = region
    
    aws_client = boto3.client('ec2')
    raw_return = aws_client.describe_instances()
    return raw_return["Reservations"]

def get_region_list(json_formatted_string: str) -> list:

    region_entries = []

    j = json.loads(json_formatted_string)

    for region_data in j["Regions"]:
        region_entries.append(region_data["RegionName"])

    return region_entries

def get_regions_data_string() -> str:
    aws_client = boto3.client('ec2')
    raw_string = str(aws_client.describe_regions())
    return re.sub(r"'", "\"", raw_string)

def create_new_instance(aws_resource):

    aws_resource.create_instances(
        ImageId='ami-08f3d892de259504d',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.nano'
    )

def kill_instance(aws_resource, id_to_kill):
    aws_resource.instances.filter(InstanceIds=[id_to_kill]).terminate()

def restart_instance(aws_resource, id_to_restart):
    aws_resource.instances.filter(InstanceIds=[id_to_restart]).start()

