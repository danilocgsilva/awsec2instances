from awsec2instances_includes.ScriptServiceAwsami import ScriptServiceAwsami
from awsec2instances_includes.ScriptServiceUbuntu import ScriptServiceUbuntu
from awsec2instances_includes.ScriptServiceInterface import ScriptServiceInterface

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

    def install_php_ami_aws(self):
        self.scriptService.install_php_ami_aws()
        return self

    def install_php_mbstring(self):
        self.scriptService.install_php_mbstring()
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

    def adds_mariadb_updated_to_os_repository(self):
        self.scriptService.adds_mariadb_updated_to_os_repository()
        return self
