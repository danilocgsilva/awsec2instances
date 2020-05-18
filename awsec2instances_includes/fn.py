import sys, json, subprocess
from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper
import boto3

def extractPublicIpAddress( instanceInfos ):
    if "PublicIpAddress" in instanceInfos:
        return instanceInfos["PublicIpAddress"]
    else:
        return "---"


def extractInstanceType( instanceInfos ):
    return instanceInfos["InstanceType"]


def extractName( instanceInfos ):
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

    command = Command_Line_Wrapper()

    command.set_command_string('aws ec2 describe-instances')

    if profile:
        command.append_command_string('--profile ' + profile)

    if region:
        command.append_command_string('--region ' + region)

    try:
        outputBytes = command.execute()
    except:
        print("Exception returned in the AWS request. The current system may need the profile name to proceed.")
        exit()

    jsonString = outputBytes.decode("utf-8")
    j = json.loads(jsonString)
    return j['Reservations']


def get_region_list(json_formatted_string: str) -> list:

    region_entries = []

    j = json.loads(json_formatted_string)

    for region_data in j["Regions"]:
        region_entries.append(region_data["RegionName"])

    return region_entries


def get_regions_data_string() -> str:
    aws_client = boto3.client('ec2')
    return str(aws_client.describe_regions())
