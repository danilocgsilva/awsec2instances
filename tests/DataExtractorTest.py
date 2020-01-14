import sys
import unittest
sys.path.append("..")
from awsec2instances_includes.DataExtractor import DataExtractor
from testsAssets.get_mocked_single_instance_data import mocked_single_instance

class DataExtractorTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DataExtractorTest, self).__init__(*args, **kwargs)
        self.dataExtractor = DataExtractor()
        self.dataExtractor.set_instance_raw_data(mocked_single_instance)


    def testCanExtractInstanceId(self):
        instance_id = self.dataExtractor.extract_instance_id()
        self.assertEqual(instance_id, "i-0aef91c9532fbbcfd")


    def testCanExtractInstanceType(self):
        instance_type = self.dataExtractor.extract_instance_type()
        self.assertEqual(instance_type, )


    def testCanExtractPublicIpAddress(self):


    def testCanExtractName(self):


if __name__ == '__main__':
    unittest.main()