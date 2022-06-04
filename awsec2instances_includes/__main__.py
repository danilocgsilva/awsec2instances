#!/usr/bin/python3

from awsec2instances_includes.fn import create_new_instance
from awsec2instances_includes.Commands import Commands
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from awsutils.AWSUtils import AWSUtils
import argparse

def mass_parser_arguments(arguments_group_list: list, parser):
    for argument_list in arguments_group_list:
        parser.add_argument(
            "--" + argument_list[0],
            "-" + argument_list[1],
            required=argument_list[2],
            help=argument_list[3],
            action=argument_list[4]
        )
    return parser

def main():

    parser = argparse.ArgumentParser()

    parser = mass_parser_arguments([
        ["access", "a", False, "Set a way to access the instance if you are creating a new one", "store"],
        ["add-firewall", "af", False, "If it is required to setup an firewall", "store_true"],
        ["command", "c", False, "Defines a specific action", "store"],
        ["distro", "d", False, "A name of a distribuition, if required a specific one", "store"],
        ["filter-name", "fn", False, "Search for instance with the tag name", "store"],
        ["filter-status", "fs", False, "A status filter if desired", "store"],
        ["id", "i", False, "The instance id required for some commands", "store"],
        ["key", "k", False, "If required, antecipates the need to provides a key to be accessible by ssh,", "store"],
        ["lasts", "l", False, "Say how much time the instance will lasts to avoid unexpected costs", "store"],
        ["name", "n", False, "Set the names's tag", "store"],
        ["profile", "p", False, "Set the aws cli profile, if needed", "store"],
        ["region", "r", False, "Restrict search just for a single region", "store"],
        ["status-filter", "sf", False, "Filter instance by status", "store"],
        ["user-data", "u", False, "Path for user data as shell script for instance", "store"],
    ], parser)

    args = parser.parse_args()

    if args.profile:
        profile = args.profile
    else:
        profile = AWSUtils().guessLocalProfile()

    if profile == "":
        print("I cound not guess credentials, sorry. Explicitly set a profile name using -p or --profile or set in the aws configuration using the command: \"aws configure --profile <your_profile>\".")
        exit()

    if args.region != None and not AwsClientUtils().region_exists(args.region):
        print("The given region does not exists. Exiting.")
        exit()

    commands = Commands(profile, args.region)

    if not args.command:
        if commands.floating_parameters(args):
            print("You may have forgetted the action that script must takes. You provided arguments compatible to an action not provided - do you forget to call --command new?")
            exit()
        else:
            commands.list(args.region, args.filter_status, args.filter_name)
            exit()
    if args.command == "list":
        commands.list(args.region, args.filter_status, args.filter_name)
    elif args.command == "new":
        create_new_instance(args, commands)
    elif args.command == "sleep":
        commands.sleep(args.id)
    elif args.command == "kill":
        commands.kill(args.id)
    elif args.command == "restart":
        commands.restart(args.id_to_restart)
    elif args.command == "lists_vpcs":
        commands.lists_vpcs()
    else:
        print("The command " + args.command + " does not exists.")
