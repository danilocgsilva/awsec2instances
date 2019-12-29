from awsec2instances_includes.fn import \
    extractInstanceType, \
    extractInstanceId, \
    extractPublicIpAddress, \
    extractName, \
    extracState


class DataIterator:

    def showInstancesInfos(self, instances):

        loopInteration = 0
        for instance in instances:

            instanceInfos = instance["Instances"][0]
            state = extracState( instanceInfos )

            loopInteration += 1
            tipoInstancia = extractInstanceType( instanceInfos )
            instanceId = extractInstanceId( instanceInfos )
            enderecoInstancia = extractPublicIpAddress( instanceInfos )
            identificacao = extractName( instanceInfos )
            

            print('Instance count:', loopInteration)
            print('Instance Id:', instanceId)
            print('Instance type:', tipoInstancia)
            print('PublicIp:', enderecoInstancia)
            print('Name:', identificacao)
            print('Status:', state)
            print('---')