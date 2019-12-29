#!/usr/bin/python3

from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import getRawData
import sys

arguments = sys.argv

if len(arguments) > 1:
    instances = getRawData(arguments[1])
else:
    instances = getRawData()

di = DataIterator()
di.showInstancesInfos(instances)
