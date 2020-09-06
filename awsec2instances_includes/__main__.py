#!/usr/bin/python3

from awsec2instances_includes.fn import \
    get_region_list,\
    get_regions_data_string,\
    guess_profile,\
    assign_sg
from awsec2instances_includes.Commands import Commands
from awssg.SG_Client import SG_Client
from awssg.Client import Client
from awssg.SGConfig import SGConfig
from wimiapi.Wimi import Wimi
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers
import sys
import argparse
import datetime


def mass_parser_arguments(arguments_group_list: list, parser):
    for argument_list in arguments_group_list:
        parser.add_argument(
            "--" + argument_list[0],
            "-" + argument_list[1],
            required=argument_list[2],
            help=argument_list[3]
        )
    return parser


def main():

    parser = argparse.ArgumentParser()

    parser = mass_parser_arguments([
        ["region", "r", False, "Restrict search just for a single region"],
        ["command", "c", False, "Defines a specific action"],
        ["id-to-kill", "ik", False, "Set an instance id to terminate"],
        ["profile", "p", False, "Set the aws cli profile, if needed"],
        ["id-to-restart", "ir", False, "Set an existing stopped instance to restart"],
        ["access", "a", False, "Set a way to access the instance if you are creating a new one"]
    ], parser)

    args = parser.parse_args()

    if args.profile:
        profile = args.profile
    else:
        profile = guess_profile()

    if profile == "":
        print("I cound not guess credentials, sorry. Explicitly set a profile name using -p or --profile or set in the aws configuration using the command: \"aws configure --profile <your_profile>\".")
        exit()

    commands = Commands(profile, args.region)

    if not args.command or args.command == "list":
        commands.list(args.region)
    elif args.command == "new":
        instance_id = commands.new()
        if args.access:

            ip = Wimi().get_ip('ipv4')

            group_name = 'securitygroup-for-' + instance_id + '-at-' + DcgsPythonHelpers().getHashDateFromDate(datetime.datetime.now())

            if args.access == 'with-ssh':
                sgc = SGConfig(ip, 'tcp', 22, group_name)
            elif args.access == 'with-http':
                sgc = SGConfig(ip, 'tcp', 80, group_name)
            else:
                raise Exception('Wrong value given')

            ec2 = Client()
            sg_client = SG_Client()
            sg_client.set_client(ec2).set_group_name(group_name).create_sg()

            assign_sg(sg_client, sgc)

        print("The instance with id " + instance_id + " is about to be created.")
    elif args.command == "kill":
        commands.kill(args.id_to_kill)
    elif args.command == "restart":
        commands.restart(args.id_to_restart)
    else:
        print("The command " + args.command + " does not exists.")
