from awsec2instances_includes.OsScriptService.ScriptServiceInterface import ScriptServiceInterface
from wimiapi.Wimi import Wimi
from awsec2instances_includes.ProtocolService import ProtocolService

class ScriptServiceUbuntu(ScriptServiceInterface):

    def __init__(self):
        self.arch = None
        self.data = {}

    def setArch(self, arch: str):
        self.arch = arch
        return self

    def setUserScript(self, userStript):
        self.userScript = userStript
        return self

    def firstUpdate(self):
        self.userScript.add_scripts("apt update -y")
        self.userScript.add_scripts("apt upgrade -y")
        return self

    def install_httpd(self):
        self.userScript.add_scripts("apt install apache2 -y")
        return self

    def install_https(self):
        self.userScript.add_scripts("a2enmod ssl")
        self.userScript.add_scripts("a2ensite default-ssl.conf")
        self.userScript.add_scripts("systemctl restart apache2")
        return self

    def install_php(self):

        if not self.arch:
            self.userScript.add_scripts("apt install php php-mysql -y")
        else:
            self.userScript.add_scripts("apt install php7.4 php7.4-mysql -y")

        self.userScript.add_scripts("service apache2 restart")

        return self

    def install_php_mbstring(self):
        self.userScript.add_scripts("apt install php-mbstring -y")
        return self

    def install_php_dom(self):
        self.userScript.add_scripts("apt install php-dom -y")
        return self

    def install_php_zip(self):
        self.userScript.add_scripts("apt install php-zip -y")
        return self

    def install_php_curl(self):
        self.userScript.add_scripts("apt install php-curl -y")
        return self

    def enable_httpd(self):
        self.userScript.add_scripts("chkconfig httpd on")
        self.userScript.add_scripts("service httpd start")
        return self
    
    # Install and enable mariadb
    def database(self):
        self.userScript.add_scripts("apt install mariadb-server mariadb-client -y")
        self.userScript.add_scripts("systemctl enable --now mariadb")
        return self

    def assingWwwPermissionToLocalUser(self):
        self.userScript.add_scripts("chmod 775 /var/www/html")
        self.userScript.add_scripts("chgrp ubuntu /var/www/html")
        return self

    def openToMe(self):

        dbUserName = "eroot"
        
        scriptTextPlaceholder = '''mysql <<EOF
CREATE USER {0}@'{1}';
GRANT ALL ON *.* TO eroot@'{1}';
EOF
'''
        scriptText = scriptTextPlaceholder.format(
            dbUserName,
            Wimi().get_ip('ipv4')
        )

        self.userScript.add_scripts(scriptText)
        
        self.data = {"dbUserName": dbUserName}

        return self
    
    def getData(self) -> dict:
        return self.data

    def setFirewall(self, protocolService: ProtocolService):
        if protocolService.is_not_empty():
            if protocolService.is_have_http():
                self.userScript.add_scripts("ufw allow 80")
            if protocolService.is_have_ssh():
                self.userScript.add_scripts("ufw allow 22")
            if protocolService.is_have_https():
                self.userScript.add_scripts("ufw allow 443")
            if protocolService.is_have_database():
                self.userScript.add_scripts("ufw allow 3306")
            if protocolService.is_have_desktop():
                self.userScript.add_scripts("ufw allow 3389")
            self.userScript.add_scripts("ufw enable")

