import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService(unittest.TestCase):

    def test_execption_wrong_argument(self):
        wrong_argument = "some-invalid"
        with self.assertRaises(Exception):
            ProtocolService(wrong_argument)

    def test_get_zero_element_string(self):
        protocolServoce = ProtocolService("")
        self.assertEqual(0, len(protocolServoce.get_ports()))

    def test_get_zero_element_none(self):
        protocolServoce = ProtocolService()
        self.assertEqual(0, len(protocolServoce.get_ports()))

    def test_port_both_options(self):
        protocolService = ProtocolService("with-ssh,with-http")
        returned_ports = protocolService.get_ports()
        self.assertEqual(22, returned_ports[0])
        self.assertEqual(80, returned_ports[1])

    def test_port_three_options(self):
        protocolService = ProtocolService("with-ssh,with-http,with-database")
        returned_ports = protocolService.get_ports()
        self.assertEqual(22, returned_ports[0])
        self.assertEqual(80, returned_ports[1])
        self.assertEqual(3306, returned_ports[2])

    def test_one_option_wrong(self):
        one_option_wrong = "with-ssh,with-cassandra"
        with self.assertRaises(Exception):
            ProtocolService(one_option_wrong)
    
    def test_three_options_one_wrong(self):
        three_options = "with-ssh,with-http,with-cassandra"
        with self.assertRaises(Exception):
            ProtocolService(three_options)

    def test_is_not_empty_false(self):
        protocolService = ProtocolService()
        self.assertFalse(protocolService.is_not_empty())

    def test_is_not_empty_true(self):
        protocolService = ProtocolService("with-ssh")
        self.assertTrue(protocolService.is_not_empty())

    def test_is_not_empty_true2(self):
        protocolService = ProtocolService("with-ssh,with-http")
        self.assertTrue(protocolService.is_not_empty())

