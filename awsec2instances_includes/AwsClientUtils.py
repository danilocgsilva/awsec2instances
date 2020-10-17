import boto3
import re
import os
from awsec2instances_includes.GetPreferredIam import GetPreferredIam

class AwsClientUtils:

    def get_regions_name(self) -> list:
        aws_client = boto3.client('ec2')
        region_names = []
        for region_name in aws_client.describe_regions()["Regions"]:
            region_names.append(region_name["RegionName"])
        return region_names

    def get_regions_data_string(self) -> str:
        aws_client = boto3.client('ec2')
        raw_string = str(aws_client.describe_regions())
        return re.sub(r"'", "\"", raw_string)

    def getRawDataFromCli(self, filterstatus = None, region = None) -> dict:
        return self.getRawData(None, region=region, filterstatus=filterstatus)

    def getRawData(self, filterstatus, profile = None, region = None) -> dict:

        if profile:
            os.environ['AWS_PROFILE'] = profile

        print("----region " + region)

        if region:
            os.environ['AWS_DEFAULT_REGION'] = region
        
        aws_client = boto3.client('ec2')

        if filterstatus:
            raw_return = aws_client.describe_instances(Filters=[
                {
                    'Name': 'state',
                    'Values': [
                        filterstatus,
                    ]
                },
            ])
        else:
            raw_return = aws_client.describe_instances()

        return raw_return["Reservations"]

    def create_new_instance_resource(
        self, 
        aws_resource, 
        region: str, 
        keypairname, 
        user_script: str
    ):
        parameters = {
            "ImageId": GetPreferredIam().getIam(region),
            "MinCount": 1,
            "MaxCount": 1,
            "InstanceType": 't2.nano'
        }

        if keypairname:
            parameters["KeyName"] = keypairname

        if user_script:
            parameters["UserData"] = user_script

        instances_list_to_create = aws_resource.create_instances(**parameters)
        
        return instances_list_to_create[0]

    def kill_instance(self, aws_resource, id_to_kill):
        aws_resource.instances.filter(InstanceIds=[id_to_kill]).terminate()

    def restart_instance(self, aws_resource, id_to_restart):
        aws_resource.instances.filter(InstanceIds=[id_to_restart]).start()

    def get_key_pair_name(self):

        aws_client = boto3.client('ec2')
        key_pairs_list = aws_client.describe_key_pairs()["KeyPairs"]

        if len(key_pairs_list) == 0:
            return None
        elif len(key_pairs_list) == 1:
            return key_pairs_list[0]["KeyName"]
        else:
            return self.choose_between_keypairs(key_pairs_list)

    def choose_between_keypairs(self, keypairs_result):
        raise Exception("Still not implemented.")

    def listInstanceData(self, region, filter_status) -> list:
        os.environ['AWS_DEFAULT_REGION'] = region
        instancesData = []

        if filter_status:
            instance_filter_status_list = [
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        filter_status,
                    ]
                },
            ]
        else:
            instance_filter_status_list = []

        ec2Data = boto3.client('ec2').describe_instances(Filters=instance_filter_status_list)
        for instanceData in ec2Data["Reservations"]:
            instancesData.append(instanceData["Instances"][0])
        return instancesData
        

