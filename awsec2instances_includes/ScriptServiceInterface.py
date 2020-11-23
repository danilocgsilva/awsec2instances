import abc

class ScriptServiceInterface(abc.ABC):

    @abc.abstractmethod
    def setUserScript(self, userStript):
        pass

    @abc.abstractmethod
    def firstUpdate(self):
        pass

    @abc.abstractmethod
    def install_httpd(self):
        pass

    @abc.abstractmethod
    def install_php_ami_aws(self):
        pass

    @abc.abstractmethod
    def install_php_mbstring(self):
        pass

    @abc.abstractmethod
    def install_php_dom(self):
        pass

    @abc.abstractmethod
    def database(self):
        pass

    @abc.abstractmethod
    def adds_mariadb_updated_to_os_repository(self):
        pass
