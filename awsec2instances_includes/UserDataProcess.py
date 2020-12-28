from awsec2instances_includes.ProtocolService import ProtocolService
# from awsec2instances_includes.ScriptService import ScriptService
from awsec2instances_includes.UserScript import UserScript
import os
import re

class UserDataProcess:

    # def __init__(self, scriptService: ScriptService, protocolService: ProtocolService):
    #     self.scriptService = scriptService
    #     self.protocolService = protocolService

    def __init__(self, scriptService, protocolService: ProtocolService):
        self.scriptService = scriptService
        self.protocolService = protocolService

    def processWebserver(self):
        self.scriptService.install_httpd()
        self.protocolService.ensure_port_80()
        if self.protocolService.is_have_https:
            self.scriptService.install_https()

    def processWebserverPhp(self) -> list:
        self.processWebserver()
        self.scriptService.install_php()
        
    def processWordPress(self, userScript: UserScript):
        self.scriptService.checkpointType("Starting WordPress processing...")
        self.scriptService.\
            install_httpd().\
            install_php()
        userScript.add_scripts(self.__get_composer_scripts_download())
        userScript.add_scripts(self.__get_wordpress_installation())
        userScript.add_scripts("rm -r html")
        userScript.add_scripts("ln -s /var/www/wordpress/wordpress html")
        self.scriptService.database()
        userScript.add_scripts(self.__set_basic_and_unsecure_local_database_config("wordpress"))
        self.protocolService.ensure_port_80()
        self.scriptService.checkpointType("Finished WordPress processing!")

        
    def processDrupal(self, userScript: UserScript):
        self.scriptService.checkpointType("Starting Drupal processing preparations...")
        self.scriptService.\
            install_httpd().\
            install_php().\
            install_php_mbstring().\
            install_php_dom().\
            install_php_gd()
        userScript.add_scripts(self.__get_composer_scripts_download())
        self.scriptService.checkpointType("Composer installed with success.")
        userScript.add_scripts("COMPOSER_MEMORY_LIMIT=-1 composer install")
        userScript.add_scripts(self.__enlargeGitTollerance())
        userScript.add_scripts(self.__get_drupal_installation())
        self.scriptService.checkpointType("Drupal created from composer with success.")
        userScript.add_scripts("rm -r html")
        userScript.add_scripts("ln -s /var/www/drupal/web html")
        userScript.add_scripts("chown www-data html/sites/default")
        self.scriptService.database()
        userScript.add_scripts(self.__set_basic_and_unsecure_local_database_config("drupal"))
        self.protocolService.ensure_port_80()
        self.scriptService.checkpointType("Finished Drupal processing!")
        
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

    def processWebserverHere(self):
        self.processWebserver()
        self.scriptService.assingWwwPermissionToLocalUser()
        self.protocolService.ensure_port_22()

        filelist = os.listdir()
        install_php = False
        for file in filelist:
            if re.search(".php$", file):
                install_php = True
        if install_php:
            self.scriptService.install_php()

        return self.__askLocalPem(), filelist

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

    def __set_basic_and_unsecure_local_database_config(self, database_name: str) -> str:
        string_to_return = '''mysql -uroot -e "CREATE USER username@localhost identified by 'password'"
mysql -uroot -e "CREATE DATABASE {0}"
mysql -uroot -e "GRANT ALL PRIVILEGES ON wordpress.* TO username@localhost"
mysql -uroot -e "FLUSH PRIVILEGES"
'''
        return string_to_return.format(database_name)

    def __get_wordpress_installation(self) -> str:
        string_to_return = '''
cd /var/www
/usr/local/bin/composer create-project johnpbloch/wordpress
chown apache wordpress/wordpress
'''
        return string_to_return

    def __get_drupal_installation(self) -> str:
        string_to_return = '''cd /var/www
/usr/local/bin/composer create-project drupal/recommended-project drupal
chown www-data drupal/web
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

    def __enlargeGitTollerance(self):
        string_to_return = '''git config --global pack.windowMemory "100m"
git config --global pack.packSizeLimit "100m"
git config --global pack.threads "1"
'''
        return string_to_return
