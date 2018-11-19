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