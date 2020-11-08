import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService_3389(unittest.TestCase):

    def test_get_one_element(self):
        protocolService = ProtocolService("with-desktop")
        self.assertEqual(1, len(protocolService.get_ports()))

    def test_port_from_desktop(self):
        protocolService = ProtocolService("with-desktop")
        self.assertEqual(3389, protocolService.get_ports()[0])

    def test_is_have_desktop_true(self):
        protocolService = ProtocolService("with-http,with-desktop")
        self.assertTrue(protocolService.is_have_desktop())

    def test_is_have_desktop_true_2(self):
        protocolService = ProtocolService("with-desktop")
        self.assertTrue(protocolService.is_have_desktop())

    def test_ensure_3389_is_not_empty(self):
        protocolService = ProtocolService(None)
        protocolService.ensure_port_3389()
        self.assertTrue(protocolService.is_not_empty())

    def test_ensure_3389(self):
        protocolService = ProtocolService()
        protocolService.ensure_port_3389()
        self.assertTrue(3389 in protocolService.get_ports())

    def test_ensure_3389_2(self):
        protocolService = ProtocolService("with-desktop")
        protocolService.ensure_port_3389()
        self.assertTrue(3389 in protocolService.get_ports())

    def test_ensure_3389_3(self):
        protocolService = ProtocolService("with-desktop")
        protocolService.ensure_port_3389()
        self.assertTrue(3389 in protocolService.get_ports())

    def test_ensure_3389_4(self):
        protocolService = ProtocolService("with-http,with-ssh")
        protocolService.ensure_port_3389()
        self.assertTrue(3389 in protocolService.get_ports())

    def test_ensure_3389_5(self):
        protocolService = ProtocolService("")
        protocolService.ensure_port_3389()
        self.assertTrue(3389 in protocolService.get_ports())