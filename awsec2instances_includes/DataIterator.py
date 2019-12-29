from awsec2instances_includes.fn import \
    extractInstanceType, \
    extractInstanceId, \
    extractPublicIpAddress, \
    extractName, \
    extracState


class DataIterator:

    def getInstancesInfos(self, instances):

        array_data = []

        iteration_loop = 1
        for instance in instances:
            instanceInfos = instance["Instances"][0]
            array_data.append(
                self.__build_dataInfo_entry__(instanceInfos, iteration_loop)
            )
            iteration_loop += 1

        return array_data


    def __build_dataInfo_entry__(self, list: list, count: int):
        dataInfo = {}
        dataInfo['count'] = count
        dataInfo['id'] = extractInstanceId(list)
        dataInfo['type'] = extractInstanceType(list)
        dataInfo['ip'] = extractPublicIpAddress(list)
        dataInfo['name'] = extractName(list)
        dataInfo['status'] = extracState(list)

        return dataInfo

