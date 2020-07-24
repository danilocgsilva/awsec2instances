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

    args = parser.parse_args()
    commands = Commands()

    if not args.command or args.command == "list":
        commands.list(args.region)
    elif args.command == "new":
        commands.new(args.region)
    else:
        print("The command " + args.command + " does not exists.")

    
