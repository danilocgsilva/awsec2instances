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
        expected_script = "#!/bin/bash\n\nset -e\n"
        self.assertEqual(expected_script, self.userScript.get_user_script())

    def testFirstUpdate(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "apt update -y\n\n"
        expected_result += "apt upgrade -y\n"

        self.scriptService.firstUpdate()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_httpd(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "apt install apache2 -y\n"

        self.scriptService.install_httpd()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "apt install php7.4 php7.4-mysql -y\n\n"
        expected_result += "service httpd restart\n"

        self.scriptService.install_php()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php_mbstring(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "apt install php-mbstring -y\n"

        self.scriptService.install_php_mbstring()
        
        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_php_dom(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "apt install php-dom -y\n"
        
        self.scriptService.install_php_dom()

        self.assertEqual(expected_result, self.userScript.get_user_script())

    def testInstall_https(self):
        expected_result = "#!/bin/bash\n\nset -e\n\n"
        expected_result += "a2enmod ssl\n\n"
        expected_result += "a2ensite default-ssl.conf\n\n"
        expected_result += "systemctl restart apache2\n"
        
        self.scriptService.install_https()

        self.assertEqual(expected_result, self.userScript.get_user_script())

if __name__ == '__main__':
    unittest.main()
    