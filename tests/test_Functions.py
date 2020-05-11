import unittest
from testsAssets.get_region_output_json_text import get_text
from awsec2instances_includes.fn import get_region_list

class test_Functions(unittest.TestCase):

    def test_get_region_list_us_east_2(self):
        json_string_data = get_text()
        region_list = get_region_list(json_string_data)
        region_to_exists = "us-east-2"
        self.assertTrue(region_to_exists in region_list)


    def test_get_region_list_us_east_1(self):
        json_string_data = get_text()
        region_list = get_region_list(json_string_data)
        region_to_exists = "us-west-1"
        self.assertTrue(region_to_exists in region_list)


    def test_get_region_list_us_west_2(self):
        json_string_data = get_text()
        region_list = get_region_list(json_string_data)
        region_to_exists = "us-west-2"
        self.assertTrue(region_to_exists in region_list)

