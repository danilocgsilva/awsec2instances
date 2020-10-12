from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.Commands import Commands
from awsec2instances_includes.CreationInstanceService import CreationInstanceService
from awsec2instances_includes.UserScript import UserScript
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

def put_sg_to_instance(instance_id: str, protocols: ProtocolService) -> str:

    ip = Wimi().get_ip('ipv4')

    group_name = 'securitygroup-for-' + instance_id + '-at-' + DcgsPythonHelpers().getHashDateFromDate(datetime.datetime.now())

    ec2 = Client()
    sg_client = SG_Client()
    sg_client.set_client(ec2).set_group_name(group_name).create_sg()

    sgid = sg_client.getGroupId()

    for port in protocols.get_ports():
        sg_client.set_rule(sgid, 'tcp', ip, str(port))

    assign_sg_to_ec2(sgid, instance_id)

    return group_name

def assign_sg_to_ec2(sgid: str, instance_id: str):

    custom_filter = [{
        'Name': 'instance-id', 
        'Values': [instance_id]
    }]

    ec2 = boto3.resource('ec2')
    instances = list(ec2.instances.filter(Filters=custom_filter))
    instances[0].modify_attribute(Groups=[sgid], DryRun=False)


def create_new_instance(args, commands: Commands):
    creationInstanceService, protocolsService, userScript = CreationInstanceService().getCreationServices(args.access)
    creationInstanceService.ensureMinutesData(args.lasts)

    if args.user_data and args.user_data == "webserver":
        userScript.add_scripts(get_http_default_user_data())
        protocolsService.ensure_port_80()

    creationInstanceService.setHarakiri(userScript)
    if creationInstanceService.needs_die_warnning:
        print(creationInstanceService.getHarakiriMessage())

    instance_data = commands.new(protocolsService, userScript.get_user_script())

    print("The instance with id " + instance_data.id + " is about to be created.")
    if protocolsService.is_not_empty():
        print("Setting security group for instance...")
        put_sg_to_instance(instance_data.id, protocolsService)
    if args.name:
        print("Wanting to starts the instance, so I can add its name...")
        instance_data.wait_until_running()
        boto3.resource('ec2').create_tags(Resources=[instance_data.id], Tags=[{'Key':'Name', 'Value':args.name}])

def get_http_default_user_data() -> str:
    return '''yum update -y
yum install httpd -y
chkconfig httpd on
service httpd start
'''

def init_user_script() -> str:
    return "#!/bin/bash\n\n"