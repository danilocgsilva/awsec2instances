import sys
import unittest
sys.path.append("..")
from awsec2instances_includes.DataExtractor import DataExtractor
from testsAssets.mocked_single_instance_data import mocked_single_instance_data

class test_DataExtractorTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_DataExtractorTest, self).__init__(*args, **kwargs)
        self.dataExtractor = DataExtractor()
        self.dataExtractor.set_instance_raw_data(mocked_single_instance_data)


    def testCanExtractInstanceId(self):
        instance_id = self.dataExtractor.extract_instance_id()
        self.assertEqual(instance_id, "i-0aef91c9532fbbcfd")


    def testCanExtractInstanceType(self):
        instance_type = self.dataExtractor.extract_instance_type()
        self.assertEqual(instance_type, "t2.nano")


    def testCanExtractPublicIpAddress(self):
        instance_type = self.dataExtractor.extract_public_ip_address()
        self.assertEqual(instance_type, "---")


    def testCanExtractName(self):
        instance_name = self.dataExtractor.extract_name()
        self.assertEqual(instance_name, "opsworks")


if __name__ == '__main__':
    unittest.main()