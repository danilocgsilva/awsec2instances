import sys, json, subprocess
from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper
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
    arguments = sys.argv

    if len(arguments) > 1:
        return getRawData(arguments[1], region)
    else:
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
