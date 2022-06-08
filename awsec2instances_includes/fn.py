from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsec2instances_includes.CreationInstanceService import CreationInstanceService
from awsec2instances_includes.OsFamily import OsFamily
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter
from awsec2instances_includes.OsScriptService.ScriptService import ScriptService
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.UserDataProcess import UserDataProcess
from awsec2instances_includes.UserScript import UserScript
from awssg.Client import Client
from awssg.SG_Client import SG_Client
from awssg.SGConfig import SGConfig
from awssg.VPC_Client import VPC_Client
from cli_ask.Ask import Ask
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
from pathlib import Path
from wimiapi.Wimi import Wimi
import boto3, datetime, os, paramiko, requests, time
from scp import SCPClient
import re
from awsec2instances_includes.DatabaseProcess.DatabaseProcess import DatabaseProcess

def assign_sg_to_ec2(sgid: str, instance_id: str):

    custom_filter = [{
        'Name': 'instance-id', 
        'Values': [instance_id]
    }]

    ec2 = boto3.resource('ec2')
    instances = list(ec2.instances.filter(Filters=custom_filter))
    instances[0].modify_attribute(Groups=[sgid], DryRun=False)

def create_new_instance(args, commands):

    os_family = OsFamily()
    if not os_family.is_ubuntu_family(args.distro)\
        and args.add_firewall:
        message = "You cannot set a firewall in the current Linux distro: " + os_family.default_os() + ". Not working yet. Sorry. Tries to use --distro ubuntu."
        print(message)
        exit()
    
    creationInstanceService, protocolsService, userScript = CreationInstanceService()\
        .getCreationServices(args.access)
    creationInstanceService.ensureMinutesData(args.lasts)
    creationInstanceService.setHarakiri(userScript)

    '''
    Instantiating the ScriptService based on distro, the script will know
    from what distro the script configurations must be done.
    '''
    scriptService = ScriptService(args.distro).\
        setUserScript(userScript)
    
    scriptService.firstUpdate()

    if args.user_data:

        userDataProcess = UserDataProcess(scriptService, protocolsService)

        user_datas = args.user_data.split(",")

        for role in user_datas:
            __user_data_process(role, userDataProcess, userScript, args.distro, protocolsService)

    if args.add_firewall:
        scriptService.setFirewall(protocolsService)

    if creationInstanceService.needs_die_warnning:
        print(creationInstanceService.getHarakiriMessage())

    userScript.add_scripts(get_bootstrap_log_end_mark(args.distro))

    sg_client = SG_Client()
    vpc_choosed = __get_vpc(sg_client)
    print("The deploy will be performed to a VPC with id {}.".format(vpc_choosed))
    sg_client.set_vpc(vpc_choosed)

    security_group_name = None
    if protocolsService.is_not_empty():
        print("Setting security group...")
        security_group_name, sgid = create_security_group(protocolsService, sg_client)
        print("The new security group name is " + security_group_name)  

    '''
    Important to notice that the scripts generated for the instance
    bootstraping are consumed here. So, in case of script change,
    necessarily must be done before here.
    '''
    instance_data = commands.new(
        protocolsService, 
        userScript.get_user_script(), 
        vpc_choosed,
        args.distro
    )
    if security_group_name != None:
        assign_sg_to_ec2(sgid, instance_data.id)

    print("The instance with id " + instance_data.id + " is about to be created.")

    if args.name:
        print("Waiting to starts the instance, so I can add its name...")
        instance_data.wait_until_running()
        boto3.resource('ec2').create_tags(
            Resources=[instance_data.id], 
            Tags=[{'Key':'Name', 'Value':args.name}]
        )

    instance_interpreter = InstanceInterpreter()
    instance_is_running = False
    print("Waiting the instance be ready...")

    '''
    After command that triggers the instance creation, loops in an time
    time interval to check if the instance is ready and prints
    in the console.
    '''
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
        if args.user_data == "webserver-here":
            __writeSshSkip(instance_interpreter.getInstanceIp())
            for file in filelist:
                __sendFile(file, pem_file_path, instance_interpreter.getInstanceIp())

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

    os_family = OsFamily()
    
    if os_family.is_ubuntu_family(distro):
        return "/home/ubuntu/log-bootstrap.txt"
    else:
        return "/home/ec2-user/log-bootstrap.txt"

def print_instances_single_region(region, filter_status, filter_name, fields):
    talk = Talk()
    awsCliUtils = AwsClientUtils()
    rawInstancesData = awsCliUtils.listInstanceData(region, filter_status, filter_name)
    awsCliUtils.addImageDescriptionToInstanceData(rawInstancesData)
    talk.setInstanceData(rawInstancesData)

    if fields:
        fields_treated = re.sub('_', r' ', fields)
        talk.chooseFields(fields_treated)

    talk.printData()

def wait_http(instance_ip: str):
    print("Right now, the http server still is not ready, but in a moment, it will be ready. I will check till it is ready...")
    dcgsPythonHelpers = DcgsPythonHelpers()
    print(dcgsPythonHelpers.getHashDateFromDate())
    http_is_on = False
    trials = 0
    limit_trials = 30
    while not http_is_on and trials < limit_trials:
        try:
            requests.get('http://' + instance_ip)
            http_is_on = True
        except Exception:
            print("Waiting http to be ready...")
        trials = trials + 1
        time.sleep(12)
    if trials >= limit_trials:
        print(dcgsPythonHelpers.getHashDateFromDate())
        print("Oops! May the server is taking too long to restart or something nasty really hapenned... Anyway, tries to access in the browser the ip " + instance_ip + " some few times by a while. If not, something wrong really hapenned... :(.")
    else:
        print(dcgsPythonHelpers.getHashDateFromDate())
        print("Woah! The wait is over! Access the address type the ip in the address: " + instance_ip)

def create_security_group(protocolsService, sg_client) -> str:
    ip = Wimi().get_ip('ipv4')
    group_name = 'securitygroup-at-' + DcgsPythonHelpers().getHashDateFromDate(datetime.datetime.now())
    ec2 = Client()
    sg_client.set_client(ec2).set_group_name(group_name)
    
    sg_client.create_default_sg()
    sgid = sg_client.getGroupId()
    for port in protocolsService.get_ports():
        sg_client.set_rule(sgid, 'tcp', ip, str(port))
    return group_name, sgid

def __writeSshSkip(serverAddress: str):
    path_config_ssh = os.path.join(str(Path.home()), ".ssh", "config")
    f = open(path_config_ssh, "a")
    f.write(os.linesep + "Host " + serverAddress + os.linesep)
    f.write("  StrictHostKeyChecking no" + os.linesep)
    f.close()

def __sendFile(file: str, pem_file_path: str, serveraddress: str):
    pemKey = paramiko.RSAKey.from_private_key_file(pem_file_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(
        hostname=serveraddress,
        username="ec2-user",
        pkey=pemKey
    )
    scp = SCPClient(ssh.get_transport())
    scp.put(file, remote_path="/var/www/html/" + file)

def __get_vpc(sg_client):

    vpc_client = VPC_Client()

    default_vpc = __get_default_vpc(vpc_client)
    if default_vpc:
        print("ATENTION: VPC HAS BEEN choosed by a environment variable called DEFAULT_AWS_VPC. You may change it anytime.")
        return default_vpc

    vpc_choosed = None

    if vpc_client.is_multiples_vpcs():
        vps_list = sg_client.set_client(Client()).fetch_vpcs_list_names()
        ask = Ask(vps_list)
        try:
            multiples_vpc_message = '''There are multiples vpcs in the current account, so it is required to ask which one you will use.
If there are a default vpc suitable, you can add system variable called DEFAULT_AWS_VPC containing the default vpc id.'''
            print(multiples_vpc_message)
            vpc_choosed = ask.ask("Which vpc do you would like to setup the security group?:")
        except AskException:
            print("You choosed an invalid option. Quiting, nothing done.")
            exit()
        sg_client.set_vpc(vpc_choosed)
    else:
        vpc_choosed = vpc_client.get_first_vpc_name()
    return vpc_choosed

def __get_default_vpc(vpc_client):
    default_vpc = os.environ.get('DEFAULT_AWS_VPC')

    if default_vpc:
        if vpc_client.vpc_exists(default_vpc):
            return default_vpc
        else:
            print("WARNNING: the environment have the variable called DEFAULT_AWS_VPC, which points to which vpc to choose, if multiple present. But the current value does not corresponds to an existing vpc in the environemnt. You may manuallu inform which one to choose.")
    return None

def __user_data_process(
        role: str, 
        userDataProcess: UserDataProcess, 
        userScript: UserScript, 
        distro: str,
        protocolsService: ProtocolService
    ):
    if role == "webserver":
        userDataProcess.processWebserver()
    elif role == "webserver-php":
        userDataProcess.processWebserverPhp()
    elif role == "wordpress":
        userDataProcess.processWordPress(userScript)
    elif role == "database":
        databaseProcess = DatabaseProcess(distro)
        databaseProcess.prepare(protocolsService, userScript)
    elif role == "laravel":
        userDataProcess.processLaravel(userScript)
    elif role == "desktop":
        userDataProcess.processDesktop()
    elif role == "webserver-here":
        pem_file_path, filelist = userDataProcess.processWebserverHere()
    else:
        raise Exception("Sorry! I don't know this option for user data pattern.")
