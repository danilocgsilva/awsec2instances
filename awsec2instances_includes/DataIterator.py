from awsec2instances_includes.fn import \
    extractInstanceType, \
    extractInstanceId, \
    extractPublicIpAddress, \
    extractName, \
    extracState


class DataIterator:

    def __init__(self):
        self.allow_stopped = True


    def set_allow_stopped(self, allow_stopped: bool):
        self.allow_stopped = allow_stopped


    def getInstancesInfos(self, instances):

        array_data = []

        iteration_loop = 1
        for instance in instances:
            instanceInfos = instance["Instances"][0]

            status = extracState(instanceInfos)
            if not self.allow_stopped and status == 'stopped':
                continue

            array_data.append(
                self.__build_dataInfo_entry__(instanceInfos, iteration_loop, status)
            )
            iteration_loop += 1

        return array_data


    def __build_dataInfo_entry__(self, list: list, count: int, status: str):
        dataInfo = {}
        dataInfo['count'] = count
        dataInfo['id'] = extractInstanceId(list)
        dataInfo['type'] = extractInstanceType(list)
        dataInfo['ip'] = extractPublicIpAddress(list)
        dataInfo['name'] = extractName(list)
        dataInfo['status'] = status

        return dataInfo

