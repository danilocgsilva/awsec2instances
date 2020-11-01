class ScriptService:
    
    def setUserScript(self, userStript):
        self.userScript = userStript
        return self

    def install_httpd(self):
        self.userScript.add_scripts("yum install httpd -y")
        return self

    def install_php_ami_aws(self):
        self.userScript.add_scripts("amazon-linux-extras install php7.4 -y")
        self.userScript.add_scripts("service httpd restart")
        return self

    def install_php_mbstring(self):
        self.userScript.add_scripts("yum install php-mbstring -y")
        return self

    def install_php_dom(self):
        self.userScript.add_scripts("yum install php-dom -y")
        return self

    def enable_httpd(self):
        self.userScript.add_scripts('''chkconfig httpd on
service httpd start''')
        return self

    def __get_httpd_enable(self) -> str:
        return 

