import abc
from awsec2instances_includes.UserScript import UserScript

class ScriptServiceInterface(abc.ABC):

    # The dump object that will lists all commands for the VM must be
    #   injected in the class before anything to be done
    @abc.abstractmethod
    def setUserScript(self, userStript: UserScript):
        pass

    # The VM may be outdated, so this is a convenient method to update
    #   and it is expected to be the first thing to be puttend in the
    #   script. But the higher level script implementation may have the
    #   choose to do not update the system VM.
    @abc.abstractmethod
    def firstUpdate(self):
        pass

    # Prepare VM to manage http responses
    @abc.abstractmethod
    def install_httpd(self):
        pass

    # Enables web server to handle secure http
    @abc.abstractmethod
    def install_https(self):
        pass

    @abc.abstractmethod
    def install_php(self):
        pass

    @abc.abstractmethod
    def install_php_mbstring(self):
        pass

    @abc.abstractmethod
    def install_php_dom(self):
        pass

    @abc.abstractmethod
    def install_php_gd(self):
        pass

    @abc.abstractmethod
    def database(self):
        pass

    @abc.abstractmethod
    def assingWwwPermissionToLocalUser(self):
        pass

