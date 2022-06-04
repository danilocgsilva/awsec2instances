from crypt import METHOD_BLOWFISH
from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.Formatter import Formatter
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter

class Talk:

    def setInstanceData(self, instances_data: list):
        self.instances_data = instances_data

        self.fields = {
            "Id": "getInstanceId",
            "Name": "getInstanceName",
            "Status": "getStatus",
            "Type": "getInstanceType",
            "Ip": "getInstanceIp",
            "Key": "getInstanceKey",
            "Image Id": "getImageId",
            "Image Description": "getImageDescription"
        }

        return self

    def setImageDescription(self, imageDescription: str):
        self.imageDescription = imageDescription

    def chooseFields(self, fields: str):

        choosingFields = fields.split(",")
        
        newFields = {}
        for key in self.fields:
            #if fields == key:
            if key in choosingFields:
                newFields[key] = self.fields[key]

        self.fields = newFields

    def printData(self):

        instanceInterpreter = InstanceInterpreter()

        for instance_raw in self.instances_data:
            instanceInterpreter.setInstanceData(instance_raw)
            print('---')

            for key in self.fields:
                generatingFunction = getattr(instanceInterpreter, self.fields[key])
                print(key + ': ' + generatingFunction())

    def print_data_all_regions(self, resume: Resume, string_region_data, getRawDataFromCli, statusfilter):
        for region in Formatter().extractRegions(string_region_data):
            self.print_data_single_region(region, getRawDataFromCli, resume, statusfilter)

