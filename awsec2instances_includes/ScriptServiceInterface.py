import abc

class ScriptServiceInterface(abc.ABC):

    # The dump object that will lists all commands for the VM must be
    #   injected in the class before anything to be done
    @abc.abstractmethod
    def setUserScript(self, userStript):
        pass

    # The VM may be outdated, so this is a convenient method to update
    #   and it is expected to be the first thing to be puttend in the
    #   script. But the higher level script implementation may have the
    #   choose to do not update the system VM.
    @abc.abstractmethod
    def firstUpdate(self):
        pass

    @abc.abstractmethod
    def install_httpd(self):
        pass

    @abc.abstractmethod
    def install_httpds(self):
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
