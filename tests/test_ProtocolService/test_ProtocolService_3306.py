import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService(unittest.TestCase):

    def test_get_one_element(self):
        protocolServoce = ProtocolService("with-database")
        self.assertEqual(1, len(protocolServoce.get_ports()))

    def test_port_from_database(self):
        protocolServoce = ProtocolService("with-database")
        self.assertEqual(3306, protocolServoce.get_ports()[0])

    def test_is_have_database_true(self):
        protocolService = ProtocolService("with-http,with-database")
        self.assertTrue(protocolService.is_have_database())

    def test_is_have_database_true_2(self):
        protocolService = ProtocolService("with-database")
        self.assertTrue(protocolService.is_have_database())

    def test_ensure_3306_is_not_empty(self):
        protocolService = ProtocolService(None)
        protocolService.ensure_port_3306()
        self.assertTrue(protocolService.is_not_empty())

    def test_ensure_3306(self):
        protocolService = ProtocolService()
        protocolService.ensure_port_3306()
        self.assertTrue(3306 in protocolService.get_ports())

    def test_ensure_3306_2(self):
        protocolService = ProtocolService("with-database")
        protocolService.ensure_port_3306()
        self.assertTrue(3306 in protocolService.get_ports())

    def test_ensure_3306_3(self):
        protocolService = ProtocolService("with-http")
        protocolService.ensure_port_3306()
        self.assertTrue(3306 in protocolService.get_ports())

    def test_ensure_3306_4(self):
        protocolService = ProtocolService("with-http,with-ssh")
        protocolService.ensure_port_3306()
        self.assertTrue(3306 in protocolService.get_ports())

    def test_ensure_3306_5(self):
        protocolService = ProtocolService("")
        protocolService.ensure_port_3306()
        self.assertTrue(3306 in protocolService.get_ports())
