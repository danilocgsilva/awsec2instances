#!/usr/bin/python3

from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper
from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import getRawDataFromCli, get_region_list
from awsec2instances_includes.Talk import Talk
import sys

def main():

    command = Command_Line_Wrapper()
    command.set_command_string("aws ec2 describe-regions")

    if sys.argv[1]:
        command.append_command_string("--profile " + sys.argv[1])

    region_stream_data = command.execute()
    string_region_data = region_stream_data.decode("utf-8")

    for region in get_region_list(string_region_data):

        print("Getting data from region " + region)

        instances = getRawDataFromCli(region)

        di = DataIterator()
        data_instances = di.getInstancesInfos(instances)

        talk = Talk()
        talk.get_instance_data(data_instances)
        talk.printData()
