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
            print('Key: ' + instanceInterpreter.getInstanceKey())
            print('Image Id: ' + instanceInterpreter.getImageId())

    def print_data_all_regions(self, resume: Resume, string_region_data, getRawDataFromCli, statusfilter):
        for region in Formatter().extractRegions(string_region_data):
            self.print_data_single_region(region, getRawDataFromCli, resume, statusfilter)

