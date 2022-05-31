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

    def getImageDescription(self, imageId) -> str:
        aws_client = boto3.client('ec2')
        image_id_properties = aws_client.describe_images(ImageIds=[imageId])
        print(image_id_properties)
        exit()
        return "image_id_properties"

    def create_new_instance_resource(
        self, 
        aws_resource, 
        region: str, 
        keypairname, 
        user_script: str,
        subnet,
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

        parameters["NetworkInterfaces"] = [{
            "SubnetId": subnet,
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": True
        }]

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
        
    def region_exists(self, region: str):
        available_regions = [
            "eu-north-1"
            "ap-south-1",
            "eu-west-3",
            "eu-west-2",
            "eu-west-1",
            "ap-northeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "ca-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "eu-central-1",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2"
        ]

        return region in available_regions

    def sleep_instance(self, awsresource, id: str):
        return awsresource.stop_instances(
            InstanceIds=[id]
        )
