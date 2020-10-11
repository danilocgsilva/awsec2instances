#!/usr/bin/python3

from awsec2instances_includes.fn import \
    get_region_list,\
    get_regions_data_string,\
    put_sg_to_instance,\
    get_key_pair_name
from awsec2instances_includes.Commands import Commands
from awsec2instances_includes.ProtocolService import ProtocolService
from awsguesslocalprofile.AWSGuessLocalProfile import AWSGuessLocalProfile
import sys
import argparse


def mass_parser_arguments(arguments_group_list: list, parser):
    for argument_list in arguments_group_list:
        parser.add_argument(
            "--" + argument_list[0],
            "-" + argument_list[1],
            required=argument_list[2],
            help=argument_list[3]
        )
    return parser

def create_new_instance(args_access, commands):
    protocols = ProtocolService(args_access)
    instance_id = commands.new(protocols)
    print("The instance with id " + instance_id + " is about to be created.")
    if protocols.is_not_empty():
        print("Setting security group for instance...")
        put_sg_to_instance(instance_id, protocols)

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
        profile = AWSGuessLocalProfile().guess()

    if profile == "":
        print("I cound not guess credentials, sorry. Explicitly set a profile name using -p or --profile or set in the aws configuration using the command: \"aws configure --profile <your_profile>\".")
        exit()

    commands = Commands(profile, args.region)

    if not args.command or args.command == "list":
        commands.list(args.region)
    elif args.command == "new":
        create_new_instance(args.access, commands)
    elif args.command == "kill":
        commands.kill(args.id_to_kill)
    elif args.command == "restart":
        commands.restart(args.id_to_restart)
    else:
        print("The command " + args.command + " does not exists.")
