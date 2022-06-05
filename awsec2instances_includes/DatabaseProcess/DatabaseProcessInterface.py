import abc
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript

class DatabaseProcessInterface(abc.ABC):

    @abc.abstractmethod
    def prepare(self, protocolService: ProtocolService, userScript: UserScript):
        '''
        Alters ports, installs database and enable the database service
        '''
        pass