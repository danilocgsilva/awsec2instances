from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsutils.AWSUtils import AWSUtils
from awsec2instances_includes.fn import print_instances_single_region
from awssg.Client import Client
from awssg.VPC_Client import VPC_Client
import boto3
from awssg.SG_Client import SG_Client
import os

class Commands:

    def __init__(self, profile, region = None):

        if region:
            os.environ['AWS_DEFAULT_REGION'] = region

        os.environ['AWS_PROFILE'] = profile

        self.aws_client = boto3.client('ec2')

    def list(self, region, filter_status = None, filter_name = None, fields = None):
        if region:
            print_instances_single_region(region, filter_status, filter_name, fields)
        else:
            for region in AWSUtils().get_regions_name():
                print("Content for region " + region)
                print_instances_single_region(region, filter_status, filter_name, fields)

    def new(
        self, 
        protocolService: ProtocolService, 
        user_script: str, 
        vpc,
        distro = None, 
    ):
        keypairname = None
        if protocolService.is_have_ssh():
            keypairname = AWSUtils().get_key_pair_name()
            if not keypairname:
                raise Exception('No keypair found to assign. You need it to access through ssh.')
        
        region = self.aws_client.meta.region_name
        aws_resource = boto3.resource('ec2', region_name=region)

        subnet = VPC_Client().get_first_subnet(vpc)

        return AwsClientUtils().create_new_instance_resource(
            aws_resource, 
            region, 
            keypairname, 
            user_script, 
            subnet,
            distro
        )

    def kill(self, id_to_kill):
        region_name = self.aws_client.meta.region_name
        aws_resource = boto3.resource('ec2', region_name=region_name)

        for id in id_to_kill.split(","):
            print("Will try terminate instance {} from region {}.".format(id, region_name))
            AwsClientUtils().kill_instance(aws_resource, id)

    def restart(self, id_to_restart):
        aws_resource = boto3.resource('ec2', region_name=self.aws_client.meta.region_name)
        AwsClientUtils().restart_instance(aws_resource, id_to_restart)

    def sleep(self, id_to_sleep):
        aws_resource = boto3.client('ec2', region_name=self.aws_client.meta.region_name)
        for id in id_to_sleep.split(","):
            AwsClientUtils().sleep_instance(aws_resource, id)

    def lists_vpcs(self):
        print("This comands will lists vpcs to be choosed when creating a new ec2 instance, in case of several vpcs registered in the account. Not yet implemented, as you could see...")

    def floating_parameters(self, args) -> bool:

        if args.access or args.user_data or args.lasts:
            if args.command != "new":
                return True
        return False
