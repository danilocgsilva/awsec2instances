#!/usr/bin/python3

from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.fn import get_region_list, get_regions_data_string, getRawDataFromCli
import sys
import argparse

def main():

    resume = Resume()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--region",
        "-r",
        required=False,
        help="Restrict search just for a single region"
    )
    args = parser.parse_args()
    talk = Talk()

    if args.region:
        talk.print_data_single_region(args.region, getRawDataFromCli, resume)
    else:
        string_region_data = get_regions_data_string()
        talk.print_data_all_regions(resume, string_region_data, getRawDataFromCli)
