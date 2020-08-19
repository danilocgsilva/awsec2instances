#!/usr/bin/python3

from awsec2instances_includes.fn import get_region_list, get_regions_data_string
from awsec2instances_includes.Commands import Commands
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
        ["region", "r", False, "Restrict search just for a single region"],
        ["command", "c", False, "Defines a specific action"],
        ["id-to-kill", "ik", False, "Set an instance id to terminate"],
        ["profile", "p", False, "Set the aws cli profile, if needed"]
    ], parser)

    args = parser.parse_args()
    commands = Commands(args.region, args.profile)

    if not args.command or args.command == "list":
        commands.list(args.region)
    elif args.command == "new":
        commands.new()
    elif args.command == "kill":
        commands.kill(args.id_to_kill)
    else:
        print("The command " + args.command + " does not exists.")

    
