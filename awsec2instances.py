#!/usr/bin/python3

import sys, json, subprocess

from awsec2instances_includes.fn import extractPublicIpAddress 
from awsec2instances_includes.fn import extractInstanceType 
from awsec2instances_includes.fn import extractName
from awsec2instances_includes.fn import extracState
from awsec2instances_includes.fn import extractInstanceId

arguments = sys.argv
commandLine = ['aws', 'ec2', 'describe-instances']

if len(arguments) > 1:
    commandLine.append('--profile')
    commandLine.append(arguments[1])

outputBytes = subprocess.check_output(commandLine)
jsonString = outputBytes.decode("utf-8")
j = json.loads(jsonString)
instances = j['Reservations']

loopInteration = 0
for instance in instances:

    loopInteration += 1
    instanceInfos = instance["Instances"][0]

    tipoInstancia = extractInstanceType( instanceInfos )
    instanceId = extractInstanceId( instanceInfos )
    enderecoInstancia = extractPublicIpAddress( instanceInfos )
    identificacao = extractName( instanceInfos )
    state = extracState( instanceInfos )

    print('Instance count:', loopInteration)
    print('Instance Id:', instanceId)
    print('Instance type:', tipoInstancia)
    print('PublicIp:', enderecoInstancia)
    print('Name:', identificacao)
    print('Status:', state)
    print('---')
    