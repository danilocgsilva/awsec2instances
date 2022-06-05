from awsec2instances_includes.DatabaseProcess.DatabaseProcessAwsami import DatabaseProcessAwsami
from awsec2instances_includes.DatabaseProcess.DatabaseProcessInterface import DatabaseProcessInterface
from awsec2instances_includes.DatabaseProcess.DatabaseProcessUbuntu import DatabaseProcessUbuntu
from awsec2instances_includes.OsFamily import OsFamily
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript

class DatabaseProcess(DatabaseProcessInterface):
    
    def __init__(self, distro = None):

        os_family = OsFamily()

        if distro == None or distro == "aws-ami-old":
            self.databaseService = DatabaseProcessAwsami()
        elif os_family.is_ubuntu_family(distro):
            self.databaseService = DatabaseProcessUbuntu()
        else:
            raise Exception("The provided distro parameter " + distro + " is not known.")

    def prepare(self, protocolService: ProtocolService, userScript: UserScript):
        self.databaseService.prepare(protocolService, userScript)
        return self
