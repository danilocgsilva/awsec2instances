from awsec2instances_includes.DatabaseProcess.DatabaseProcessInterface import DatabaseProcessInterface
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript

class DatabaseProcessAwsami(DatabaseProcessInterface):

    def prepare(self, protocolService: ProtocolService, userScript: UserScript):
        self.__adds_mariadb_updated_to_os_repository()
        userScript.add_scripts("yum makecache")
        userScript.add_scripts("yum install mariadb-server mariadb-client -y")
        userScript.add_scripts("systemctl enable --now mariadb")
        return self

    def __adds_mariadb_updated_to_os_repository(self, userScript: UserScript):
        userScript.add_scripts('''tee /etc/yum.repos.d/mariadb.repo << EOF
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.5/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
EOF''')