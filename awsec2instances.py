#!/usr/bin/python3

from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import getRawDataFromCli
from awsec2instances_includes.Talk import Talk
import sys

instances = getRawDataFromCli()

di = DataIterator()
data_instances = di.getInstancesInfos(instances)

talk = Talk()
talk.get_instance_data(data_instances)
talk.printData()
