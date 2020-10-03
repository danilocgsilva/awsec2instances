import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.Resume import Resume
from awsapimock.Instance_Request_Generator import Instance_Request_Generator


class test_Resume(unittest.TestCase):

    def setUp(self):
        self.resume = Resume()

    def test_add_instances_data__get_instance_count(self):
        instance_data_sample = Instance_Request_Generator().generate()
        self.resume.add_instances_data(instance_data_sample)
        counting_instances = 1
        returned_instances = self.resume.get_instance_count()
        self.assertEqual(counting_instances, returned_instances)
