import boto3
import re
import os
from awsec2instances_includes.GetPreferredIam import GetPreferredIam

class AwsClientUtils:

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
        user_script: str,
        distro = None
    ):
        parameters = {
            "ImageId": GetPreferredIam().getIam(region, distro),
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

    def listInstanceData(self, region, filter_status, filter_name) -> list:
        os.environ['AWS_DEFAULT_REGION'] = region
        instancesData = []

        instance_filter_status_list = []

        if filter_status:
            instance_filter_status_list.append(
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        filter_status,
                    ]
                }
            )

        if filter_name:
            instance_filter_status_list.append(
                {
                    'Name': 'tag:Name',
                    'Values': [
                        filter_name,
                    ]
                }
            )

        ec2Data = boto3.client('ec2').describe_instances(Filters=instance_filter_status_list)
        for instanceData in ec2Data["Reservations"]:
            instancesData.append(instanceData["Instances"][0])
        return instancesData
        

