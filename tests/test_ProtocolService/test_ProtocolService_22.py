import unittest
import sys
sys.path.insert(2, "..")
from awsec2instances_includes.ProtocolService import ProtocolService

class test_ProtocolService(unittest.TestCase):

    def test_get_one_element(self):
        protocolService = ProtocolService("with-ssh")
        self.assertEqual(1, len(protocolService.get_ports()))

    def test_port_from_ssh(self):
        protocolService = ProtocolService("with-ssh")
        self.assertEqual(22, protocolService.get_ports()[0])

    def test_is_have_ssh_true(self):
        protocolService = ProtocolService("with-http,with-ssh")
        self.assertTrue(protocolService.is_have_ssh())

    def test_is_have_ssh_true_2(self):
        protocolService = ProtocolService("with-ssh")
        self.assertTrue(protocolService.is_have_ssh())

    def test_is_have_ssh_false(self):
        protocolService = ProtocolService("with-http")
        self.assertFalse(protocolService.is_have_ssh())

    def test_is_have_ssh_false_2(self):
        protocolService = ProtocolService("")
        self.assertFalse(protocolService.is_have_ssh())

    def test_is_have_ssh_false_3(self):
        protocolService = ProtocolService()
        self.assertFalse(protocolService.is_have_ssh())

    def test_ensure_22_is_not_empty(self):
        protocolService = ProtocolService(None)
        protocolService.ensure_port_22()
        self.assertTrue(protocolService.is_not_empty())
