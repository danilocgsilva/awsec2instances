#!/usr/bin/python3

from awsec2instances_includes.fn import get_region_list, get_regions_data_string
from awsec2instances_includes.Commands import Commands
import sys
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--region",
        "-r",
        required=False,
        help="Restrict search just for a single region"
    )

    parser.add_argument(
        "--command",
        "-c",
        required=False,
        help="Defines a specific action"
    )

    parser.add_argument(
        "--id-to-kill",
        "-ik",
        required=False,
        help="Set an instance id to terminate"
    )

    parser.add_argument(
        "--profile",
        "-p",
        required=False,
        help="Set the aws cli profile, if needed"
    )

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

    
