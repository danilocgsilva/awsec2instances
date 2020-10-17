from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.Formatter import Formatter
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter

class Talk:

    def setInstanceData(self, instances_data: list):
        self.instances_data = instances_data

    def printData(self):
        instanceInterpreter = InstanceInterpreter()
        for instance_raw in self.instances_data:
            instanceInterpreter.setInstanceData(instance_raw)
            print('---')
            print('Id: ' + instanceInterpreter.getInstanceId())
            print('Name: ' + instanceInterpreter.getInstanceName())
            print('Status: ' + instanceInterpreter.getStatus())
            print('Type: ' + instanceInterpreter.getInstanceType())
            print('Ip: ' + instanceInterpreter.getInstanceIp())

    # def print_region_data(self, region, instances):

    #     print("Getting data from region " + region)

    #     di = DataIterator()
    #     data_instances = di.getInstancesInfos(instances)

    #     self.get_instance_data(data_instances)
    #     self.printData()

    def print_data_all_regions(self, resume: Resume, string_region_data, getRawDataFromCli, statusfilter):
        for region in Formatter().extractRegions(string_region_data):
            self.print_data_single_region(region, getRawDataFromCli, resume, statusfilter)

    # def print_data_single_region(self, region, getRawDataFromCli, resume, statusfilter):
    #     instances = getRawDataFromCli(region, statusfilter)
    #     resume.add_instances_data(instances)
    #     self.print_region_data(region, instances)
