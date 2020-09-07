import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.Resume import Resume


class test_Resume(unittest.TestCase):

    def setUp(self):
        self.resume = Resume()

    def test_add_instances_data(self):
        
