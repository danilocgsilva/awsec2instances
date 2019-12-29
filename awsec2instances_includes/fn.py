import sys, json, subprocess

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

    commandLine = ['aws', 'ec2', 'describe-instances']

    if profile:
        commandLine.append('--profile')
        commandLine.append(profile)

    try:
        outputBytes = subprocess.check_output(commandLine)
    except:
        print("Exception returned in the AWS request.")
        exit()

    jsonString = outputBytes.decode("utf-8")
    j = json.loads(jsonString)
    return j['Reservations']
