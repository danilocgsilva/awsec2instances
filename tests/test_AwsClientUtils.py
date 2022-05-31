import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.AwsClientUtils import AwsClientUtils

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

    def testGetImageDescription(self):
        self.assertSame("The Image description, a Slackware from 2012!", self.awsClientUtils.getImageDescription())
    

if __name__ == '__main__':
    unittest.main()
    