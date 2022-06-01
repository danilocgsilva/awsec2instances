## @todo: creates a getDistroData test

import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.GetPreferredIam import GetPreferredIam


class test_GetPreferredIam(unittest.TestCase):

    def setUp(self):
        self.getPreferredIam = GetPreferredIam()

    def test_preferred_iam_sa_east_1(self):
        region = "sa-east-1"
        self.getPreferredIam.setRegion(region)
        preferred_iam = "ami-018ccfb6b4745882a"
        returned_iam = self.getPreferredIam.getIamId()
        self.assertEqual(preferred_iam, returned_iam)

    def test_preferred_iam_us_east_1(self):
        region = "us-east-1"
        self.getPreferredIam.setRegion(region)
        preferred_iam = "ami-08f3d892de259504d"
        returned_iam = self.getPreferredIam.getIamId()
        self.assertEqual(preferred_iam, returned_iam)

if __name__ == '__main__':
    unittest.main()
    