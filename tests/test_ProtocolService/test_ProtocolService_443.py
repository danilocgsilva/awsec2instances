import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService_443(unittest.TestCase):

    def test_get_one_element(self):
        protocolService = ProtocolService("with-https")
        self.assertEqual(1, len(protocolService.get_ports()))

    def test_port_from_desktop(self):
        protocolService = ProtocolService("with-https")
        self.assertEqual(443, protocolService.get_ports()[0])

    def test_is_have_https_true(self):
        protocolService = ProtocolService("with-http,with-https")
        self.assertTrue(protocolService.is_have_https())

    def test_is_have_https_true_2(self):
        protocolService = ProtocolService("with-https")
        self.assertTrue(protocolService.is_have_https())

    def test_ensure_443_is_not_empty(self):
        protocolService = ProtocolService(None)
        protocolService.ensure_port_443()
        self.assertTrue(protocolService.is_not_empty())

    def test_ensure_443(self):
        protocolService = ProtocolService()
        protocolService.ensure_port_443()
        self.assertTrue(443 in protocolService.get_ports())

    def test_ensure_443_2(self):
        protocolService = ProtocolService("with-https")
        protocolService.ensure_port_443()
        self.assertTrue(443 in protocolService.get_ports())

    def test_ensure_443_3(self):
        protocolService = ProtocolService("with-desktop")
        protocolService.ensure_port_443()
        self.assertTrue(443 in protocolService.get_ports())

    def test_ensure_443_4(self):
        protocolService = ProtocolService("with-https,with-ssh")
        protocolService.ensure_port_443()
        self.assertTrue(443 in protocolService.get_ports())

    def test_ensure_443_5(self):
        protocolService = ProtocolService("")
        protocolService.ensure_port_443()
        self.assertTrue(443 in protocolService.get_ports())