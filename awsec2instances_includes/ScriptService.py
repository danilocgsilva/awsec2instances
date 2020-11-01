class ScriptService:
    
    def setUserScript(self, userStript):
        self.userScript = userStript
        return self

    def install_httpd(self):
        self.userScript.add_scripts("yum install httpd -y")
        return self

    def enable_httpd(self):
        self.userScript.add_scripts('''chkconfig httpd on
service httpd start''')

    def __get_httpd_enable(self) -> str:
        return 

