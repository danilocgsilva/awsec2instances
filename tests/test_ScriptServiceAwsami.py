import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.ScriptServiceUbuntu import ScriptServiceUbuntu
from awsec2instances_includes.UserScript import UserScript

class test_ScriptServiceUbuntu(unittest.TestCase):

    def setUp(self):
        self.userScript = UserScript()
        self.scriptService = ScriptServiceUbuntu().setUserScript(self.userScript)

    def testFirstEverScript(self):
        expected_script = "#!/bin/bash\n"
        self.assertEqual(expected_script, self.userScript.get_user_script())

    def testFirstUpdate(self):
        self.assertTrue(False)

    def testInstall_httpd(self):
        self.assertTrue(False)

    def testInstall_php_ami_aws(self):
        self.assertTrue(False)

    def testInstall_php_mbstring(self):
        self.assertTrue(False)

    def testInstall_php_dom(self):
        self.assertTrue(False)

    def testAdds_mariadb_updated_to_os_repository(self):
        self.assertTrue(False)
