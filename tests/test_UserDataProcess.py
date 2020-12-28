import sys
import unittest
sys.path.insert(1, "..")
from awsec2instances_includes.ScriptService import ScriptService
from awsec2instances_includes.UserDataProcess import UserDataProcess
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript

class test_UserDataProcess(unittest.TestCase):

    def test_processWebserverHere(self):
        userDataProcess = UserDataProcess(
            ScriptService().setUserScript(UserScript()), 
            ProtocolService())
        expected_count = 2
        results_script = userDataProcess.noCheckServerTemplate()
        self.assertEqual(expected_count, len(results_script))
