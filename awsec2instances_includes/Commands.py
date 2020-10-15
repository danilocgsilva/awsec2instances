from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.DataExtractor import DataExtractor
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
import boto3
import os

class Commands:

    def __init__(self, profile, region = None):

        if region:
            os.environ['AWS_DEFAULT_REGION'] = region

        os.environ['AWS_PROFILE'] = profile

        self.aws_client = boto3.client('ec2')

    def list(self, region):
        awsClientUtils = AwsClientUtils()
        if region:
            rawInstanceData = awsClientUtils.listInstanceData(region)
        else:
            for region in awsClientUtils.get_regions_name():
                print("Content for region " + region)
                instancesData = awsClientUtils.listInstanceData(region)
                print(instancesData)

    def new(self, protocolService: ProtocolService, user_script: str):
        awsClientUtils = AwsClientUtils()
        keypairname = None
        if protocolService.is_have_ssh():
            keypairname = awsClientUtils.get_key_pair_name()
            if not keypairname:
                raise Exception('No keypair found to assign. You need it to access through ssh.')
        
        region = self.aws_client.meta.region_name
        aws_resource = boto3.resource('ec2', region_name=region)
        return awsClientUtils.create_new_instance_resource(aws_resource, region, keypairname, user_script)

    def kill(self, id_to_kill):
        aws_resource = boto3.resource('ec2', region_name=self.aws_client.meta.region_name)

        for id in id_to_kill.split(","):
            AwsClientUtils().kill_instance(aws_resource, id)

    def restart(self, id_to_restart):
        aws_resource = boto3.resource('ec2', region_name=self.aws_client.meta.region_name)
        AwsClientUtils().restart_instance(aws_resource, id_to_restart)
