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


# def getInstancesData(instances):
#     loopInteration = 0
#     for instance in instances:

#         loopInteration += 1
#         instanceInfos = instance["Instances"][0]

#         tipoInstancia = extractInstanceType( instanceInfos )
#         instanceId = extractInstanceId( instanceInfos )
#         enderecoInstancia = extractPublicIpAddress( instanceInfos )
#         identificacao = extractName( instanceInfos )
#         state = extracState( instanceInfos )

#         print('Instance count:', loopInteration)
#         print('Instance Id:', instanceId)
#         print('Instance type:', tipoInstancia)
#         print('PublicIp:', enderecoInstancia)
#         print('Name:', identificacao)
#         print('Status:', state)
#         print('---')
    
