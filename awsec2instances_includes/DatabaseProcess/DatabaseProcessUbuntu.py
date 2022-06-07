from awsec2instances_includes.DatabaseProcess.DatabaseProcessInterface import DatabaseProcessInterface
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript
from wimiapi.Wimi import Wimi

class DatabaseProcessUbuntu(DatabaseProcessInterface):

    def prepare(self, protocolService: ProtocolService, userScript: UserScript):
        protocolService.ensure_port_3306()

        userScript.add_scripts("apt install mariadb-server mariadb-client -y")
        userScript.add_scripts(self.__bind_script())
        userScript.add_scripts("systemctl enable --now mariadb")

        return self

    def __bind_script(self) -> str:
        return "sed -i /bind-address/s/127.0.0.1/0.0.0.0/g /etc/mysql/mariadb.conf.d/50-server.cnf"