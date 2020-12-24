from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.ScriptService import ScriptService
from awsec2instances_includes.UserScript import UserScript
from pathlib import Path
import unittest
import os
import sys

class UserDataProcess:

    def __init__(self, scriptService: ScriptService, protocolService: ProtocolService):
        self.scriptService = scriptService
        self.protocolService = protocolService

    def processWebserver(self) -> list:
        self.scriptService.install_httpd()
        self.protocolService.ensure_port_80()
        if self.protocolService.is_have_https:
            self.scriptService.install_https()
        return []

    def processWebserverPhp(self) -> list:
        self.processWebserver()
        self.scriptService.install_php()
        
    def processWordPress(self, userScript: UserScript) -> list:
        self.scriptService.\
            install_httpd().\
            install_php()
        userScript.add_scripts(self.__get_composer_scripts_download())
        userScript.add_scripts(self.__get_wordpress_installation())
        userScript.add_scripts("rm -r html")
        userScript.add_scripts("ln -s /var/www/wordpress/wordpress html")
        self.scriptService.database()
        userScript.add_scripts(self.__set_basic_and_unsecure_wordpress_database_config())
        self.protocolService.ensure_port_80()
        return []
        
    def processDatabase(self, userScript: UserScript) -> list:
        self.protocolService.ensure_port_3306()
        self.scriptService.database()
        userScript.add_scripts("systemctl enable --now mariadb")
        return []

    def processLaravel(self, userScript: UserScript) -> list:
        self.scriptService.\
            install_httpd().\
            install_php().\
            install_php_mbstring().\
            install_php_dom()
        userScript.add_scripts(self.__get_composer_scripts_download())
        userScript.add_scripts(self.__prepare_laravel_aws())
        userScript.add_scripts("rm -r /var/www/html")
        userScript.add_scripts("ln -s /var/www/laravel/public /var/www/html")
        userScript.add_scripts('sed -i /config/a"\\ \\ \\ \\ \\ \\ \\ \\ \\"platform-check\\":\\ false," /var/www/laravel/composer.json')
        userScript.add_scripts('cd /var/www/laravel')
        userScript.add_scripts('cp .env.example .env')
        userScript.add_scripts('php artisan key:generate --ansi')
        userScript.add_scripts('/usr/local/bin/composer install')
        userScript.add_scripts('chown -Rv apache /var/www/laravel/storage')
        self.protocolService.ensure_port_80()
        return []

    def processDesktop(self) -> list:
        self.protocolService.ensure_port_3389()
        return []

    def processWebserverHere(self) -> list:
        self.processWebserver()
        self.scriptService.assingWwwPermissionToLocalUser()
        self.protocolService.ensure_port_22()

        local_pem = self.__askLocalPem()

        return self.__postScriptList(local_pem)

    def __askLocalPem(self):
        local_pem = input("Where is the local pem file? ")
        if not os.path.isfile(local_pem):
            print("The givel local pem is not a file.")
            exit()
        return local_pem

    def __get_composer_scripts_download(self) -> str:
        string_to_return = '''export HOME=/root
curl -sS https://getcomposer.org/installer | sudo php
mv composer.phar /usr/local/bin/composer
chmod +x /usr/local/bin/composer'''
        return string_to_return

    def __set_basic_and_unsecure_wordpress_database_config(self) -> str:
        string_to_return = '''mysql -uroot -e "CREATE USER username@localhost identified by 'password'"
mysql -uroot -e "CREATE DATABASE wordpress"
mysql -uroot -e "GRANT ALL PRIVILEGES ON wordpress.* TO username@localhost"
mysql -uroot -e "FLUSH PRIVILEGES"
'''
        return string_to_return

    def __get_wordpress_installation(self) -> str:
        string_to_return = '''
cd /var/www
/usr/local/bin/composer create-project johnpbloch/wordpress
chown apache wordpress/wordpress
'''
        return string_to_return

    def __prepare_laravel_aws(self) -> str:
        string_to_return = '''cd /var/www
curl -Ls -o laravel-master.zip https://github.com/laravel/laravel/archive/master.zip
unzip laravel-master.zip
rm laravel-master.zip
mv laravel-master laravel
cd laravel
/usr/local/bin/composer install'''

        return string_to_return

    def __postScriptList(self, local_pem: str):
        list_to_execute = self.noCheckServerTemplate()
        for file in os.listdir():
            list_to_execute.append("scp -i " + local_pem + " " + file + " ec2-user@{0}://var/www/html")
        return list_to_execute

    def noCheckServerTemplate(self) -> list:
        return [
            "echo Host {0} >> " + os.path.join(str(Path.home()), ".ssh", "config"),
            "echo   StrictHostKeyChecking no >> " + os.path.join(str(Path.home()), ".ssh", "config")
        ]
