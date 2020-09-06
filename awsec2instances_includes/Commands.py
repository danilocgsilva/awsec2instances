from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.fn import \
    get_regions_data_string, \
    getRawDataFromCli, \
    create_new_instance, \
    kill_instance, \
    restart_instance, \
    get_key_pair_name
from awsec2instances_includes.Resume import Resume
import boto3
import os


class Commands:

    def __init__(self, profile, region = None):

        if region:
            os.environ['AWS_DEFAULT_REGION'] = region

        os.environ['AWS_PROFILE'] = profile

        self.aws_client = boto3.client('ec2')

    def list(self, excplit_region = None):
        talk = Talk()
        resume = Resume()

        if excplit_region:
            talk.print_data_single_region(excplit_region, getRawDataFromCli, resume)
        else:
            string_region_data = get_regions_data_string()
            talk.print_data_all_regions(resume, string_region_data, getRawDataFromCli)

    def new(self, access_arguments = None):

        keypairname = None
        if access_arguments and access_arguments == "with-ssh":
            keypairname = get_key_pair_name()
        
        region = self.aws_client.meta.region_name
        aws_resource = boto3.resource('ec2', region_name=region)
        return create_new_instance(aws_resource, region, keypairname)

    def kill(self, id_to_kill):
        aws_resource = boto3.resource('ec2', region_name=self.aws_client.meta.region_name)
        kill_instance(aws_resource, id_to_kill)

    def restart(self, id_to_restart):
        aws_resource = boto3.resource('ec2', region_name=self.aws_client.meta.region_name)
        restart_instance(aws_resource, id_to_restart)
