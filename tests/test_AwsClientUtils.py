import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.AwsClientUtils import AwsClientUtils
from aws_api_mock.Instance_Single_Generator import Instance_Single_Generator
from aws_api_mock.EC2_Client import EC2_Client

class test_AwsClientUtils(unittest.TestCase):

    def setUp(self):
        self.awsClientUtils = AwsClientUtils()

    def testregion_exists_true(self):
        regionUsEast1 = "us-east-1"
        self.assertTrue(self.awsClientUtils.region_exists(regionUsEast1))
        regionSaEast1 = "sa-east-1"
        self.assertTrue(self.awsClientUtils.region_exists(regionSaEast1))

    def testregion_exists_false(self):
        regionNoWhere = "nw-east-1"
        self.assertFalse(self.awsClientUtils.region_exists(regionNoWhere))

    def testAddImageDescriptionToInstanceData(self):

        instance_single_generator = Instance_Single_Generator()
        instanceDataGenerated = instance_single_generator.generate()
        self.awsClientUtils.addImageDescriptionToInstanceData([instanceDataGenerated], EC2_Client())
        
        self.assertEqual("Canonical, Ubuntu, 20.04 LTS, amd64 focal image build on 2020-09-07", instanceDataGenerated["imageIdDescription"])
    

if __name__ == '__main__':
    unittest.main()
    