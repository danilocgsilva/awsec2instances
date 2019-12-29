#!/usr/bin/python3

from awsec2instances_includes.DataIterator import DataIterator
from awsec2instances_includes.fn import getRawDataFromCli
import sys

instances = getRawDataFromCli()

di = DataIterator()
di.showInstancesInfos(instances)
