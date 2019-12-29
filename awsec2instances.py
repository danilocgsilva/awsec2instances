#!/usr/bin/python3

import sys, json, subprocess
from awsec2instances_includes.DataIterator import DataIterator

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

di = DataIterator()
di.showInstancesInfos(instances)

# getInstancesData(instances)