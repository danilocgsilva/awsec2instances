import sys
sys.path.insert(1, "..")
from awsec2instances_includes.InstanceInterpreter import InstanceInterpreter
from tests.get_single_sample_instance import get_single_sample
import unittest

class test_InstanceInterpreter(unittest.TestCase):

    def test_getInstanceKey(self):
        instanceInterpreter = InstanceInterpreter()
        instanceInterpreter.setInstanceData(get_single_sample())
        expected_result = "some-key"
        returned_result = instanceInterpreter.getInstanceKey()
        self.assertEqual(expected_result, returned_result)

    def test_getInstanceKeyEmpty(self):
        raw_single_data = get_single_sample()
        raw_single_data.pop("KeyName", None)

        instanceInterpreter = InstanceInterpreter()
        instanceInterpreter.setInstanceData(raw_single_data)
        expected_result = "---"
        returned_result = instanceInterpreter.getInstanceKey()
        self.assertEqual(expected_result, returned_result)
