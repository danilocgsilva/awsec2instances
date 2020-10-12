import unittest
from testsAssets.get_region_output_json_text import get_text
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.Formatter import Formatter

class test_Functions(unittest.TestCase):

    def setUp(self):
        self.formatter = Formatter()

    def test_extractName(self):

        instance_name = "InstanceName"

        instanceInfos = {'Tags': [
            {
                'Key': "Name",
                'Value': instance_name
            }
        ]}

        returned_name =  self.formatter.extractName(instanceInfos)

        self.assertEqual(instance_name, returned_name)

    def test_extractName_without_key_name(self):
        instanceInfos = {'Tags': []}
        returned_name =  self.formatter.extractName(instanceInfos)
        self.assertEqual("---", returned_name)

    def test_extractName_without_tags(self):
        instanceInfos = {}
        returned_name =  self.formatter.extractName(instanceInfos)
        self.assertEqual("---", returned_name)

