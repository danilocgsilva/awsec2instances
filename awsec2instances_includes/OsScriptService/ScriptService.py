from awsec2instances_includes.OsFamily import OsFamily
from awsec2instances_includes.OsScriptService.ScriptServiceAwsami import ScriptServiceAwsami
from awsec2instances_includes.OsScriptService.ScriptServiceUbuntu import ScriptServiceUbuntu
from awsec2instances_includes.OsScriptService.ScriptServiceInterface import ScriptServiceInterface
from awsec2instances_includes.ProtocolService import ProtocolService

# Brings more inteligent methods to handle ScriptServiceInterface
#   implementation.
class ScriptService(ScriptServiceInterface):
    '''
    Automates writting to the script based on instance role
    '''

    def __init__(self, distro = None):

        os_family = OsFamily()

        if distro == None or distro == "aws-ami-old":
            self.scriptService = ScriptServiceAwsami()
        elif os_family.is_ubuntu_family(distro):
            self.scriptService = ScriptServiceUbuntu()
        else:
            raise Exception("The provided distro parameter " + distro + " is not known.")

    def setArch(self, arch: str):
        self.scriptService.setArch(arch)
        return self

    def firstUpdate(self):
        self.scriptService.firstUpdate()
        return self

    def setUserScript(self, userStript):
        self.scriptService.setUserScript(userStript)
        return self

    def install_httpd(self):
        self.scriptService.install_httpd()
        return self

    def install_https(self):
        self.scriptService.install_https()
        return self

    def install_php(self):
        self.scriptService.install_php()
        return self

    def install_php_mbstring(self):
        self.scriptService.install_php_mbstring()
        return self

    def install_php_dom(self):
        self.scriptService.install_php_dom()
        return self

    def install_php_zip(self):
        self.scriptService.install_php_zip()
        return self
        
    def install_php_crul(self):
        self.scriptService.install_php_curl()
        return self

    def enable_httpd(self):
        self.scriptService.enable_httpd()
        return self

    def database(self):
        self.scriptService.database()
        return self

    def assingWwwPermissionToLocalUser(self):
        self.scriptService.assingWwwPermissionToLocalUser()
        return self

    def openToMe(self):
        self.scriptService.openToMe()
        return self

    def setFirewall(self, protocolsService: ProtocolService):
        self.scriptService.setFirewall(protocolsService)
        return self
