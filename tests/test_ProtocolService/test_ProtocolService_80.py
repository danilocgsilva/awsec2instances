import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService(unittest.TestCase):

    def test_get_one_element(self):
        protocolServoce = ProtocolService("with-http")
        self.assertEqual(1, len(protocolServoce.get_ports()))

    def test_port_from_http(self):
        protocolServoce = ProtocolService("with-http")
        self.assertEqual(80, protocolServoce.get_ports()[0])

    def test_is_have_http_true(self):
        protocolService = ProtocolService("with-ssh,with-http")
        self.assertTrue(protocolService.is_have_http())

    def test_is_have_http_true_2(self):
        protocolService = ProtocolService("with-http")
        self.assertTrue(protocolService.is_have_http())

    def test_is_have_http_false(self):
        protocolService = ProtocolService("with-ssh")
        self.assertFalse(protocolService.is_have_http())

    def test_is_have_http_false_2(self):
        protocolService = ProtocolService()
        self.assertFalse(protocolService.is_have_http())

    def test_is_have_http_false_3(self):
        protocolService = ProtocolService("")
        self.assertFalse(protocolService.is_have_http())

    def test_ensure_80(self):
        protocolService = ProtocolService()
        protocolService.ensure_port_80()
        self.assertTrue(80 in protocolService.get_ports())

    def test_ensure_80_2(self):
        protocolService = ProtocolService("with-ssh")
        protocolService.ensure_port_80()
        self.assertTrue(80 in protocolService.get_ports())

    def test_ensure_80_3(self):
        protocolService = ProtocolService("with-http")
        protocolService.ensure_port_80()
        self.assertTrue(80 in protocolService.get_ports())

    def test_ensure_80_4(self):
        protocolService = ProtocolService("with-http,with-ssh")
        protocolService.ensure_port_80()
        self.assertTrue(80 in protocolService.get_ports())

    def test_ensure_80_5(self):
        protocolService = ProtocolService("")
        protocolService.ensure_port_80()
        self.assertTrue(80 in protocolService.get_ports())

    def test_ensure_80_is_not_empty(self):
        protocolService = ProtocolService(None)
        protocolService.ensure_port_80()
        self.assertTrue(protocolService.is_not_empty())
