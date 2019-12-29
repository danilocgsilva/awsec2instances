#!/usr/bin/python3

from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import getRawData

instances = getRawData()

di = DataIterator()
di.showInstancesInfos(instances)
