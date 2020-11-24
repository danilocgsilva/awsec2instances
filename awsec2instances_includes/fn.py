from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.CreationInstanceService import CreationInstanceService
from awsec2instances_includes.UserScript import UserScript
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.ScriptService import ScriptService
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
import time

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

def create_new_instance(args, commands):
    creationInstanceService, protocolsService, userScript = CreationInstanceService().getCreationServices(args.access)
    creationInstanceService.ensureMinutesData(args.lasts)
    creationInstanceService.setHarakiri(userScript)
    scriptService = ScriptService(args.distro).setUserScript(userScript)
    scriptService.firstUpdate()

    if args.user_data:

        if args.user_data == "webserver":
            scriptService.install_httpd()
            protocolsService.ensure_port_80()
        elif args.user_data == "wordpress":
            scriptService.\
                install_httpd().\
                install_php_ami_aws()
            userScript.add_scripts(get_composer_scripts_download())
            userScript.add_scripts(get_wordpress_installation())
            userScript.add_scripts("rm -r html")
            userScript.add_scripts("ln -s /var/www/wordpress/wordpress html")
            scriptService.database()
            userScript.add_scripts(set_basic_and_unsecure_wordpress_database_config())
            protocolsService.ensure_port_80()
        elif args.user_data == "database":
            protocolsService.ensure_port_3306()
            scriptService.database()
            userScript.add_scripts("systemctl enable --now mariadb")
        elif args.user_data == "laravel":
            scriptService.\
                install_httpd().\
                install_php_ami_aws().\
                install_php_mbstring().\
                install_php_dom()
            userScript.add_scripts(get_composer_scripts_download())
            userScript.add_scripts(prepare_laravel_aws())
            userScript.add_scripts("rm -r /var/www/html")
            userScript.add_scripts("ln -s /var/www/laravel/public /var/www/html")
            userScript.add_scripts('sed -i /config/a"\\ \\ \\ \\ \\ \\ \\ \\ \\"platform-check\\":\\ false," /var/www/laravel/composer.json')
            userScript.add_scripts('cd /var/www/laravel')
            userScript.add_scripts('cp .env.example .env')
            userScript.add_scripts('php artisan key:generate --ansi')
            userScript.add_scripts('/usr/local/bin/composer install')
            userScript.add_scripts('chown -Rv apache /var/www/laravel/storage')
            protocolsService.ensure_port_80()
        elif args.user_data == "desktop":
            protocolsService.ensure_port_3389()

    if creationInstanceService.needs_die_warnning:
        print(creationInstanceService.getHarakiriMessage())

    userScript.add_scripts(get_bootstrap_log_end_mark())

    instance_data = commands.new(protocolsService, userScript.get_user_script(), args.distro)

    print("The instance with id " + instance_data.id + " is about to be created.")
    if protocolsService.is_not_empty():
        print("Setting security group for instance...")
        security_group_name = put_sg_to_instance(instance_data.id, protocolsService)
        print("The new security group name is " + security_group_name)
    if args.name:
        print("Wanting to starts the instance, so I can add its name...")
        instance_data.wait_until_running()
        boto3.resource('ec2').create_tags(Resources=[instance_data.id], Tags=[{'Key':'Name', 'Value':args.name}])
    instance_interpreter = InstanceInterpreter()

    instance_is_running = False
    print("Waiting the stance be ready...")
    while not instance_is_running:
        instance_interpreter.loadById(instance_data.id)
        if not instance_interpreter.getStatus() == "running":
            print("Still waiting...")
            time.sleep(1)
        else:
            instance_is_running = True
    print("Your instance is running! Have a nice devops.")
    if protocolsService.is_have_ssh() or protocolsService.is_have_http():
        print("You can access your instance by the ip: " + instance_interpreter.getInstanceIp())

# def get_update_system_bash_script() -> str:
#     return "yum update -y"

def get_shell_install_httpd() -> str:
    return "yum install httpd -y"

def get_bootstrap_log_end_mark() -> str:
    return "echo Bootstrap finished at $(date) >> " + get_bootstrap_log_addres()

def get_composer_scripts_download() -> str:
    string_to_return = '''export HOME=/root
curl -sS https://getcomposer.org/installer | sudo php
mv composer.phar /usr/local/bin/composer
chmod +x /usr/local/bin/composer'''
    return string_to_return

def prepare_laravel_aws() -> str:
    string_to_return = '''cd /var/www
curl -Ls -o laravel-master.zip https://github.com/laravel/laravel/archive/master.zip
unzip laravel-master.zip
rm laravel-master.zip
mv laravel-master laravel
cd laravel
/usr/local/bin/composer install'''

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
cd /var/www
/usr/local/bin/composer create-project johnpbloch/wordpress
chown apache wordpress/wordpress
'''
    return string_to_return

def get_bootstrap_startup_mark() -> str:
    return "echo Bootstrap script starting at $(date) >> " + get_bootstrap_log_addres()

def init_user_script() -> str:
    return "#!/bin/bash\n\n"

def get_bootstrap_log_addres() -> str:
    return "/home/ec2-user/log-bootstrap.txt"

def print_instances_single_region(region, filter_status, filter_name):
    talk = Talk()
    rawInstancesData = AwsClientUtils().listInstanceData(region, filter_status, filter_name)
    talk.setInstanceData(rawInstancesData)
    talk.printData()

def get_adds_mariadb_updated_to_os_repository() -> str:
    return '''tee /etc/yum.repos.d/mariadb.repo<<EOF
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.5/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
EOF'''

def set_basic_and_unsecure_wordpress_database_config() -> str:
    string_to_return = '''mysql -uroot -e "CREATE USER username@localhost identified by 'password'"
mysql -uroot -e "CREATE DATABASE wordpress"
mysql -uroot -e "GRANT ALL PRIVILEGES ON wordpress.* TO username@localhost"
mysql -uroot -e "FLUSH PRIVILEGES"
'''
    return string_to_return
