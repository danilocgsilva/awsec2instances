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

    def testInstall_php(self):
        self.assertTrue(False)

    def testInstall_php_mbstring(self):
        expected_result = "#!/bin/bash\n\n"
        expected_result += "yum install php-mbstring -y"
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php_dom(self):
        self.assertTrue(False)

    def testAdds_mariadb_updated_to_os_repository(self):
        expected_value = "#!/bin/bash\n\n"
        expected_value += "tee /etc/yum.repos.d/mariadb.repo << EOF"
        expected_value += "\n[mariadb]"
        expected_value += "\nname = MariaDB"
        expected_value += "\nbaseurl = http://yum.mariadb.org/10.5/centos7-amd64"
        expected_value += "\ngpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB"
        expected_value += "\ngpgcheck=1"

        self.scriptService.adds_mariadb_updated_to_os_repository()

        self.assertEqual(expected_value, self.userScript.get_user_script())
