#!/usr/bin/python3

from awsec2instances_includes.fn import create_new_instance
from awsec2instances_includes.Commands import Commands
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsutils.AWSUtils import AWSUtils
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

def main():

    parser = argparse.ArgumentParser()

    parser = mass_parser_arguments([
        ["access", "a", False, "Set a way to access the instance if you are creating a new one"],
        ["command", "c", False, "Defines a specific action"],
        ["distro", "d", False, "A name of a distribuition, if required a specific one"],
        ["filter-name", "fn", False, "Search for instance with the tag name"],
        ["filter-status", "fs", False, "A status filter if desired"],
        ["id-to-kill", "ik", False, "Set an instance id to terminate"],
        ["id-to-restart", "ir", False, "Set an existing stopped instance to restart"],
        ["lasts", "l", False, "Say how much time the instance will lasts to avoid unexpected costs"],
        ["name", "n", False, "Set the names's tag"],
        ["profile", "p", False, "Set the aws cli profile, if needed"],
        ["region", "r", False, "Restrict search just for a single region"],
        ["status-filter", "sf", False, "Filter instance by status"],
        ["user-data", "u", False, "Path for user data as shell script for instance"],
    ], parser)

    args = parser.parse_args()

    if args.profile:
        profile = args.profile
    else:
        profile = AWSUtils().guessLocalProfile()

    if profile == "":
        print("I cound not guess credentials, sorry. Explicitly set a profile name using -p or --profile or set in the aws configuration using the command: \"aws configure --profile <your_profile>\".")
        exit()

    if not AwsClientUtils().region_exists(args.region):
        print("The given region does not exists. Exiting.")
        exit()

    commands = Commands(profile, args.region)

    if not args.command or args.command == "list":
        commands.list(args.region, args.filter_status, args.filter_name)
    elif args.command == "new":
        create_new_instance(args, commands)
    elif args.command == "kill":
        commands.kill(args.id_to_kill)
    elif args.command == "restart":
        commands.restart(args.id_to_restart)
    else:
        print("The command " + args.command + " does not exists.")
