import unittest
import sys
sys.path.insert(1, "..")
from testsAssets.get_region_output_json_text import get_text
from awsec2instances_includes.Formatter import Formatter

class test_Formatter(unittest.TestCase):

    def setUp(self):
        self.formatter = Formatter()

    def test_extractRegions_us_east_2(self):
        json_string_data = get_text()
        region_list = self.formatter.extractRegions(json_string_data)
        region_to_exists = "us-east-2"
        self.assertTrue(region_to_exists in region_list)

    def test_extractRegions_us_east_1(self):
        json_string_data = get_text()
        region_list = self.formatter.extractRegions(json_string_data)
        region_to_exists = "us-west-1"
        self.assertTrue(region_to_exists in region_list)

    def test_extractRegions_us_west_2(self):
        json_string_data = get_text()
        region_list = self.formatter.extractRegions(json_string_data)
        region_to_exists = "us-west-2"
        self.assertTrue(region_to_exists in region_list)
