from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.Commands import Commands
from awsec2instances_includes.CreationInstanceService import CreationInstanceService
from awsec2instances_includes.UserScript import UserScript
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsec2instances_includes.Talk import Talk
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

    if args.user_data:
        userScript.add_scripts(get_bootstrap_startup_mark())
        if args.user_data == "webserver":
            userScript.add_scripts(get_http_default_user_data())
            protocolsService.ensure_port_80()
        elif args.user_data == "wordpress":

            userScript.add_scripts("echo Updating OS and installing webserver at $(date) >> " + get_bootstrap_log_addres())
            userScript.add_scripts(get_http_default_user_data())

            userScript.add_scripts("echo Installing PHP at $(date) >> " + get_bootstrap_log_addres())
            userScript.add_scripts(get_php_installing())

            userScript.add_scripts("echo Installing Composer at $(date) >> " + get_bootstrap_log_addres())
            userScript.add_scripts(get_composer_scripts_download())

            userScript.add_scripts("echo Start sleep for 10 seconds at $(date) >> " + get_bootstrap_log_addres())
            userScript.add_scripts("sleep 10")
            userScript.add_scripts("echo /usr/local/bin directory content: $(ls /usr/local/bin) >> " + get_bootstrap_log_addres())
            userScript.add_scripts("echo Installing WordPress at $(date) >> " + get_bootstrap_log_addres())
            userScript.add_scripts("echo The composer version is $(/usr/local/bin/composer --version) >> " + get_bootstrap_log_addres())
            userScript.add_scripts(get_wordpress_installation())
            protocolsService.ensure_port_80()
    
    creationInstanceService.setHarakiri(userScript)
    if creationInstanceService.needs_die_warnning:
        print(creationInstanceService.getHarakiriMessage())

    userScript.add_scripts(get_bootstrap_log_end_mark())

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
service httpd start'''

def get_php_installing() -> str:
    string_to_return = "amazon-linux-extras install php7.4 -y\nservice httpd restart"
    return string_to_return

def get_bootstrap_log_end_mark() -> str:
    return "echo Bootstrap finished at $(date) >> " + get_bootstrap_log_addres()

def get_composer_scripts_download() -> str:
    string_to_return = '''curl -sS https://getcomposer.org/installer | sudo php
mv composer.phar /usr/local/bin/composer
chmod +x /usr/local/bin/composer'''
    return string_to_return

def get_enlarge_swap() -> str:
    return '''mkdir -p /var/_swap_
cd /var/_swap_
dd if=/dev/zero of=swapfile bs=1M count=2000
mkswap swapfile
swapon swapfile
chmod 600 swapfile
echo "/var/_swap_/swapfile none swap sw 0 0" >> /etc/fstab'''

def get_wordpress_installation() -> str:
    string_to_return = '''
cd /var/www/html
/usr/local/bin/composer create-project johnpbloch/wordpress .
'''
    return string_to_return

def get_bootstrap_startup_mark() -> str:
    return "echo Bootstrap script starting at $(date) >> " + get_bootstrap_log_addres()

def init_user_script() -> str:
    return "#!/bin/bash\n\n"

def get_bootstrap_log_addres() -> str:
    return "/home/ec2-user/log-bootstrap.txt"


def print_instances_single_region(region):
    talk = Talk()
    rawInstancesData = AwsClientUtils().listInstanceData(region)
    talk.setInstanceData(rawInstancesData)
    talk.printData()