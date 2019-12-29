from awsec2instances_includes.fn import \
    extractInstanceType, \
    extractInstanceId, \
    extractPublicIpAddress, \
    extractName, \
    extracState


class DataIterator:

    def showInstancesInfos(self, instances):
        iteration_loop = 1
        for instance in instances:
            instanceInfos = instance["Instances"][0]
            array_data = self.__get_data_to_print__(instanceInfos)
            self.__print_data_single_instance__(array_data, iteration_loop)
            iteration_loop += 1


    def __get_data_to_print__(self, instanceInfos):
        state = extracState( instanceInfos )
        tipoInstancia = extractInstanceType( instanceInfos )
        instanceId = extractInstanceId( instanceInfos )
        enderecoInstancia = extractPublicIpAddress( instanceInfos )
        identificacao = extractName( instanceInfos )

        return [instanceId, tipoInstancia, enderecoInstancia, identificacao, state]


    def __print_data_single_instance__(self, list_data: list, iteration_loop: int):
        print('Instance counted:',  iteration_loop)
        print('Instance Id:', list_data[0])
        print('Instance type:', list_data[1])
        print('PublicIp:', list_data[2])
        print('Name:', list_data[3])
        print('Status:', list_data[4])
        print('---')
