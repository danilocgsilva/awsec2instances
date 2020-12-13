from awsec2instances_includes.ScriptServiceInterface import ScriptServiceInterface

class ScriptServiceUbuntu(ScriptServiceInterface):

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
        return self

    def install_php_ami_aws(self):
        self.userScript.add_scripts("apt install php7.4 -y")
        self.userScript.add_scripts("service httpd restart")
        return self

    def install_php_mbstring(self):
        self.userScript.add_scripts("apt install php-mbstring -y")
        return self

    def install_php_dom(self):
        self.userScript.add_scripts("apt install php-dom -y")
        return self

    def enable_httpd(self):
        self.userScript.add_scripts("chkconfig httpd on")
        self.userScript.add_scripts("service httpd start")
        return self

    

    def database(self):
        self.adds_mariadb_updated_to_os_repository()
        self.userScript.add_scripts("apt install MariaDB-server MariaDB-client -y")
        self.userScript.add_scripts("systemctl enable --now mariadb")
        return self

    def adds_mariadb_updated_to_os_repository(self):
        self.userScript.add_scripts('''tee /etc/yum.repos.d/mariadb.repo << EOF
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.5/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
EOF''')
