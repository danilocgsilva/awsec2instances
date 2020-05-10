import sys, json, subprocess
from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper

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


def getRawDataFromCli():
    arguments = sys.argv

    if len(arguments) > 1:
        return getRawData(arguments[1])
    else:
        return getRawData()


def getRawData(profile = None):

    command = Command_Line_Wrapper()

    command.set_command_string('aws ec2 describe-instances')

    if profile:
        command.append_command_string('--profile ' + profile)

    try:
        outputBytes = command.execute()
    except:
        print("Exception returned in the AWS request. The current system may need the profile name to proceed.")
        exit()

    jsonString = outputBytes.decode("utf-8")
    j = json.loads(jsonString)
    return j['Reservations']
