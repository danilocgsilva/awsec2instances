from awsec2instances_includes.Formatter import Formatter

class DataIterator:

    def __init__(self):
        self.formatter = Formatter()
        self.allow_stopped = True


    def set_allow_stopped(self, allow_stopped: bool):
        self.allow_stopped = allow_stopped


    def getInstancesInfos(self, instances):

        array_data = []

        iteration_loop = 1
        for instance in instances:
            instanceInfos = instance["Instances"][0]

            status = self.formatter.extracState(instanceInfos)
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
        dataInfo['id'] = self.formatter.extractInstanceId(list)
        dataInfo['type'] = self.formatter.extractInstanceType(list)
        dataInfo['ip'] = self.formatter.extractPublicIpAddress(list)
        dataInfo['name'] = self.formatter.extractName(list)
        dataInfo['status'] = status

        return dataInfo

