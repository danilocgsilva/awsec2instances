#!/usr/bin/python3

import sys, json, subprocess

from awsec2instances_includes.fn import extractPublicIpAddress 
from awsec2instances_includes.fn import extractInstanceType 
from awsec2instances_includes.fn import extractName
from awsec2instances_includes.fn import extracState
from awsec2instances_includes.fn import extractInstanceId
from awsec2instances_includes.fn import getInstancesData

arguments = sys.argv
commandLine = ['aws', 'ec2', 'describe-instances']

if len(arguments) > 1:
    commandLine.append('--profile')
    commandLine.append(arguments[1])

try:
    outputBytes = subprocess.check_output(commandLine)
except:
    print("Exception returned in the AWS request.")
    exit()

jsonString = outputBytes.decode("utf-8")
j = json.loads(jsonString)
instances = j['Reservations']

getInstancesData(instances)