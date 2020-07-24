from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import get_region_list, get_regions_data_string


class Talk:

    def get_instance_data(self, instance_data):
        self.instance_data = instance_data


    def printData(self):
        for instanceSingle in self.instance_data:
            print('---')
            print('Instance counting: ' + str(instanceSingle['count']))
            print('Id: ' + instanceSingle['id'])
            print('Name: ' + instanceSingle['name'])
            print('Status: ' + instanceSingle['status'])
            print('Type: ' + instanceSingle['type'])
            print('Ip: ' + instanceSingle['ip'])
    

    def print_region_data(self, region, instances):

        print("Getting data from region " + region)

        di = DataIterator()
        data_instances = di.getInstancesInfos(instances)

        self.get_instance_data(data_instances)
        self.printData()


    def print_data_all_regions(self, resume, string_region_data, getRawDataFromCli):
        for region in get_region_list(string_region_data):
            self.print_data_single_region(region, getRawDataFromCli, resume)


    def print_data_single_region(self, region, getRawDataFromCli, resume):
        instances = getRawDataFromCli(region)
        resume.add_instances_data(instances)
        self.print_region_data(region, instances)
