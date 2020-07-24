from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.fn import get_regions_data_string, getRawDataFromCli, create_new_instance
from awsec2instances_includes.Resume import Resume
import boto3

class Commands:

    def list(self, region = None):
        talk = Talk()
        resume = Resume()

        if region:
            talk.print_data_single_region(region, getRawDataFromCli, resume)
        else:
            string_region_data = get_regions_data_string()
            talk.print_data_all_regions(resume, string_region_data, getRawDataFromCli)


    def new(self, region = None):
        create_new_instance(region)

