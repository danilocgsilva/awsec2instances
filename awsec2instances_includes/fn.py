from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsec2instances_includes.CreationInstanceService import CreationInstanceService
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter
from awsec2instances_includes.ScriptService import ScriptService
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.UserDataProcess import UserDataProcess
from awsec2instances_includes.UserScript import UserScript
from awssg.Client import Client
from awssg.SG_Client import SG_Client
from awssg.SGConfig import SGConfig
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from pathlib import Path
from wimiapi.Wimi import Wimi
import boto3, datetime, json, os, paramiko, requests, scp, subprocess, sys, time

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

    pem_file_path = ""

    if args.user_data:

        userDataProcess = UserDataProcess(scriptService, protocolsService)
        
        if args.user_data == "webserver":
            userDataProcess.processWebserver()
        elif args.user_data == "webserver-php":
            userDataProcess.processWebserverPhp()
        elif args.user_data == "wordpress":
            userDataProcess.processWordPress()
        elif args.user_data == "database":
            userDataProcess.processDatabase(userScript)
        elif args.user_data == "laravel":
            userDataProcess.processLaravel(userScript)
        elif args.user_data == "desktop":
            userDataProcess.processDesktop()
        elif args.user_data == "webserver-here":
            pem_file_path = userDataProcess.processWebserverHere()
        else:
            raise Exception("Sorry! I don't know this option for user data pattern.")

        userScript.add_scripts("echo \"#!/bin/bash\n\ntouch one.txt\" > /home/ec2-user/exec1.sh")
        userScript.add_scripts("chmod +x /home/ec2-user/exec1.sh")
        userScript.add_scripts("/home/ec2-user/exec1.sh")

    if creationInstanceService.needs_die_warnning:
        print(creationInstanceService.getHarakiriMessage())

    userScript.add_scripts(get_bootstrap_log_end_mark(args.distro))

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
    print("Waiting the instance be ready...")
    while not instance_is_running:
        instance_interpreter.loadById(instance_data.id)
        if not instance_interpreter.getStatus() == "running":
            print("Still waiting...")
            time.sleep(4)
        else:
            instance_is_running = True
    print("Your instance is running! Have a nice devops.")
    if protocolsService.is_have_ssh() or protocolsService.is_have_http():
        print("You can access your instance by the ip: " + instance_interpreter.getInstanceIp())
    if protocolsService.is_have_http():
        wait_http(instance_interpreter.getInstanceIp())
        self.__writeSshSkip(instance_interpreter.getInstanceIp())
        for file in os.listdir():
            self.__sendFile(file, pem_file_path, instance_interpreter.getInstanceIp())

def get_shell_install_httpd() -> str:
    return "yum install httpd -y"

def get_bootstrap_log_end_mark(distro = None) -> str:
    return "echo Bootstrap finished at $(date) >> " + get_bootstrap_log_addres(distro)

def get_enlarge_swap() -> str:
    return '''mkdir -p /var/_swap_
cd /var/_swap_
dd if=/dev/zero of=swapfile bs=1M count=2000
mkswap swapfile
swapon swapfile
chmod 600 swapfile
echo "/var/_swap_/swapfile none swap sw 0 0" >> /etc/fstab'''

def get_bootstrap_startup_mark(distro = None) -> str:
    return "echo Bootstrap script starting at $(date) >> " + get_bootstrap_log_addres(distro)

def init_user_script() -> str:
    return "#!/bin/bash\n\n"

def get_bootstrap_log_addres(distro = None) -> str:
    if distro == "ubuntu":
        return "/home/ubuntu/log-bootstrap.txt"
    else:
        return "/home/ec2-user/log-bootstrap.txt"

def print_instances_single_region(region, filter_status, filter_name):
    talk = Talk()
    rawInstancesData = AwsClientUtils().listInstanceData(region, filter_status, filter_name)
    talk.setInstanceData(rawInstancesData)
    talk.printData()

def wait_http(instance_ip: str):
    print("Right now, the http server still is not ready, but in a moment, it will be ready. I will check till it is ready...")
    http_is_on = False
    trials = 0
    while not http_is_on and trials < 20:
        try:
            requests.get('http://' + instance_ip)
            http_is_on = True
        except Exception:
            print("Waiting http to be ready...")
        trials = trials + 1
        time.sleep(12)
    if trials == 20:
        print("Oops! May the server is taking too long to restart or something nasty really hapenned... Anyway, tries to access in the browser the ip " + instance_ip + " some few times by a while. If not, something wrong really hapenned... :(.")
    else:
        print("Woah! The wait is over! Access the address type the ip in the address: " + instance_ip)

    def __writeSshSkip(serverAddress: str):
        path_config_ssh = os.path.join(str(Path.home()), ".ssh", "config")
        f = open(path_config_ssh, "a")
        f.write("Host " + serverAddress)
        f.write("  StrictHostKeyChecking no")
        f.close()

    def __sendFile(file: str, pem_file_path: str, serveraddress: str):
        pemKey = paramiko.RSAKey.from_private_key_file(pem_file_path)
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(
            hostname=serveraddress,
            username="ec2-user",
            pkey=pem_file_path
        )
        scp = SCPClient(ssh.get_transport())
        scp.put(file, file)
