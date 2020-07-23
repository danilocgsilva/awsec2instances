#!/usr/bin/python3

from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper
from awsec2instances_includes.Talk import Talk
from awsec2instances_includes.Resume import Resume
from awsec2instances_includes.fn import getRawDataFromCli
from awsec2instances_includes.fn import get_region_list, get_regions_data_string
import sys

def main():

    talk = Talk()
    resume = Resume()

    string_region_data = get_regions_data_string()
    
    for region in get_region_list(string_region_data):

        instances = getRawDataFromCli(region)

        resume.add_instances_data(instances)

        talk.print_region_data(region, instances)
