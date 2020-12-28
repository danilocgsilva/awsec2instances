import unittest
import sys
sys.path.insert(1, "..")
from awsec2instances_includes.ScriptServiceAwsami import ScriptServiceAwsami
from awsec2instances_includes.UserScript import UserScript

class test_ScriptServiceAwsami(unittest.TestCase):

    def setUp(self):
        self.userScript = UserScript()
        self.scriptService = ScriptServiceAwsami().setUserScript(self.userScript)

    def testFirstEverScript(self):
        expected_script = "#!/bin/bash\n\nset -e\n"
        self.assertEqual(expected_script, self.userScript.get_user_script())

    def testFirstUpdate(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "yum update -y\n"

        self.scriptService.firstUpdate()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_httpd(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "yum install httpd -y\n\n"
        expected_result += "chkconfig httpd on\n\n"
        expected_result += "service httpd start\n"

        self.scriptService.install_httpd()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "amazon-linux-extras install php7.4 -y\n\n"
        expected_result += "service httpd restart\n"

        self.scriptService.install_php()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php_mbstring(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "yum install php-mbstring -y\n"
        self.scriptService.install_php_mbstring()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php_dom(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "yum install php-dom -y\n"
        
        self.scriptService.install_php_dom()

        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_https(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "yum -y install httpd mod_ssl\n\n"
        expected_result += "service httpd restart\n"
        
        self.scriptService.install_https()

        self.assertEqual(expected_result, self.userScript.get_user_script())


