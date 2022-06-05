from awsec2instances_includes.OsScriptService.ScriptServiceInterface import ScriptServiceInterface
from wimiapi.Wimi import Wimi

from awsec2instances_includes.ProtocolService import ProtocolService

class ScriptServiceAwsami(ScriptServiceInterface):
        
    def setArch(self, arch: str):
        self.scriptService.setArch(arch)
        return self

    def setUserScript(self, userStript):
        self.userScript = userStript
        return self

    def firstUpdate(self):
        self.userScript.add_scripts("yum update -y")
        return self

    def install_httpd(self):
        self.userScript.add_scripts("yum install httpd -y")
        self.__enable_httpd()
        return self

    def install_https(self):
        self.userScript.add_scripts("yum -y install httpd mod_ssl")
        self.userScript.add_scripts("service httpd restart")
        return self

    def install_php(self):
        self.userScript.add_scripts("amazon-linux-extras install php7.4 -y")
        self.userScript.add_scripts("service httpd restart")
        return self

    def install_php_mbstring(self):
        self.userScript.add_scripts("yum install php-mbstring -y")
        return self

    def install_php_dom(self):
        self.userScript.add_scripts("yum install php-dom -y")
        return self

    def install_php_zip(self):
        self.userScript.add_scripts("yum install php-zip -y")
        return self

    def install_php_curl(self):
        self.userScript.add_scripts("yum install php-curl -y")
        return self

    # def database(self):
    #     self.__adds_mariadb_updated_to_os_repository()
    #     self.userScript.add_scripts("yum makecache")
    #     self.userScript.add_scripts("yum install mariadb-server mariadb-client -y")
    #     self.userScript.add_scripts("systemctl enable --now mariadb")
    #     return self

    def assingWwwPermissionToLocalUser(self):
        self.userScript.add_scripts("chmod 775 /var/www/html")
        self.userScript.add_scripts("chgrp ec2-user /var/www/html")
        return self

    def openToMe(self):

        scriptTextPlaceholder = '''mysql <<EOF
CREATE USER eroot@'{0}';
GRANT ALL ON *.* TO eroot@'{0}';
EOF
'''
        scriptText = scriptTextPlaceholder.format(
            Wimi().get_ip('ipv4')
        )

        self.userScript.add_scripts(scriptText)

        return self

    def setFirewall(self, protocolService: ProtocolService):
        '''
        Not working! Needs be checked.
        '''

        if protocolService.is_not_empty():

            self.userScript.add_scripts("amazon-linux-extras install epel -y")
            self.userScript.add_scripts('yum install --enablerepo="epel" ufw -y')

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
            self.userScript.add_scripts('echo "y" | ufw enable')

        raise Exception("This method must be reviewd. Not working.")

#    def __adds_mariadb_updated_to_os_repository(self):
#        self.userScript.add_scripts('''tee /etc/yum.repos.d/mariadb.repo << EOF
#[mariadb]
#name = MariaDB
#baseurl = http://yum.mariadb.org/10.5/centos7-amd64
#gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
#gpgcheck=1
#EOF''')

    def __enable_httpd(self):
        self.userScript.add_scripts("chkconfig httpd on")
        self.userScript.add_scripts("service httpd start")
        return self