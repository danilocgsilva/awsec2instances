from awsec2instances_includes.ScriptServiceAwsami import ScriptServiceAwsami
from awsec2instances_includes.ScriptServiceUbuntu import ScriptServiceUbuntu
from awsec2instances_includes.ScriptServiceInterface import ScriptServiceInterface

# Brings more inteligent methods to handle ScriptServiceInterface
#   implementation.
class ScriptService(ScriptServiceInterface):

    def __init__(self, distro = None):

        if distro == None:
            self.scriptService = ScriptServiceAwsami()
        elif distro == "ubuntu":
            self.scriptService = ScriptServiceUbuntu()
        else:
            raise Exception("The provided distro parameter " + distro + " is not known.")

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

    def install_php_gd(self):
        self.scriptService.install_php_gd()
        return self

    def install_php_dom(self):
        self.scriptService.install_php_dom()
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
