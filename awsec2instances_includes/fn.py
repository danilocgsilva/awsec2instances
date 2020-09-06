from awsec2instances_includes.GetPreferredIam import GetPreferredIam
from awssg.Client import Client
from awssg.SGConfig import SGConfig
from awssg.SG_Client import SG_Client
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from wimiapi.Wimi import Wimi
import boto3
import datetime
import os
import re
import sys, json, subprocess


def extractPublicIpAddress( instanceInfos ):
    if "PublicIpAddress" in instanceInfos:
        return instanceInfos["PublicIpAddress"]
    else:
        return "---"

def extractInstanceType( instanceInfos ):
    return instanceInfos["InstanceType"]

def extractName(instanceInfos):
    if "Tags" in instanceInfos:
        listTags = instanceInfos["Tags"]

        for tag in listTags:
            if tag["Key"] == "Name":
                return tag["Value"]

    return "---"

def extracState ( instanceInfos ):
    return instanceInfos["State"]["Name"]

def extractInstanceId ( instanceInfos ):
    return instanceInfos["InstanceId"]

def getRawDataFromCli(region = None) -> dict:
    return getRawData(None, region)

def getRawData(profile = None, region = None) -> dict:

    if profile:
        os.environ['AWS_PROFILE'] = profile

    if region:
        os.environ['AWS_DEFAULT_REGION'] = region
    
    aws_client = boto3.client('ec2')
    raw_return = aws_client.describe_instances()
    return raw_return["Reservations"]

def get_region_list(json_formatted_string: str) -> list:

    region_entries = []

    j = json.loads(json_formatted_string)

    for region_data in j["Regions"]:
        region_entries.append(region_data["RegionName"])

    return region_entries

def get_regions_data_string() -> str:
    aws_client = boto3.client('ec2')
    raw_string = str(aws_client.describe_regions())
    return re.sub(r"'", "\"", raw_string)

def create_new_instance(aws_resource, region: str, keypairname = None):

    parameters = {
        "ImageId": GetPreferredIam().getIam(region),
        "MinCount": 1,
        "MaxCount": 1,
        "InstanceType": 't2.nano'
    }

    if keypairname:
        parameters["KeyName"] = keypairname

    instances_list_to_create = aws_resource.create_instances(**parameters)

    id_data = instances_list_to_create[0].id
    
    return id_data

def kill_instance(aws_resource, id_to_kill):
    aws_resource.instances.filter(InstanceIds=[id_to_kill]).terminate()

def restart_instance(aws_resource, id_to_restart):
    aws_resource.instances.filter(InstanceIds=[id_to_restart]).start()

def guess_profile() -> str:
    profile_list = boto3.session.Session().available_profiles
    if len(profile_list) == 1:
        return profile_list[0]
    if len(profile_list) > 1 and 'default' in profile_list:
        return 'default'
    return ""

def put_sg_to_instance(instance_id: str, access_type: str) -> str:

    ip = Wimi().get_ip('ipv4')

    group_name = 'securitygroup-for-' + instance_id + '-at-' + DcgsPythonHelpers().getHashDateFromDate(datetime.datetime.now())

    if access_type == 'with-ssh':
        port = 22
    elif access_type == 'with-http':
        port = 80
    else:
        raise Exception('Wrong value given')

    ec2 = Client()
    sg_client = SG_Client()
    sg_client.set_client(ec2).set_group_name(group_name).create_sg()

    sgid = sg_client.getGroupId()
    sg_client.set_rule(sgid, 'tcp', ip, str(port))

    assign_sg_to_ec2(sgid, instance_id)

    return group_name

def get_key_pair_name():

    aws_client = boto3.client('ec2')
    key_pairs_list = aws_client.describe_key_pairs()["KeyPairs"]

    if len(key_pairs_list) == 0:
        return None
    elif len(key_pairs_list) == 1:
        return key_pairs_list[0]["KeyName"]
    else:
        return choose_between_keypairs(key_pairs_list)


def assign_sg_to_ec2(sgid: str, instance_id: str):

    custom_filter = [{
        'Name': 'instance-id', 
        'Values': [instance_id]
    }]

    ec2 = boto3.resource('ec2')
    instances = list(ec2.instances.filter(Filters=custom_filter))
    instances[0].modify_attribute(Groups=[sgid], DryRun=False)

def choose_between_keypairs(keypairs_result):
    # print("There are several keypairs in the account.")
    # print(keypairs_result)
    # input("Choose one between them: ")
    raise Exception("Still not implemented.")
