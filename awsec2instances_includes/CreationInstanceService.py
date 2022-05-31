from awsec2instances_includes.UserScript import UserScript
from awsec2instances_includes.ProtocolService import ProtocolService
from awsec2instances_includes.UserScript import UserScript

class CreationInstanceService:

    def __init__(self):
        self.needs_die_warnning = True
        self.die_time = 5

    def getCreationServices(self, accesses):
        '''
        Returns self ProtocolService and UsersScript
        '''
        return self, ProtocolService(accesses), UserScript()

    def setHarakiri(self, userScript: UserScript):
        userScript.add_scripts("shutdown -P +" + str(self.die_time))

    def ensureMinutesData(self, human_given_parameter = None):
        if not human_given_parameter:
            return
        self.needs_die_warnning = False
        try:
            self.die_time = int(human_given_parameter)
        except Exception:
            if human_given_parameter == "for-ten-minutes":
                self.die_time = 10
            elif human_given_parameter == "for-an-hour":
                self.die_time = 60
            elif human_given_parameter == "for-a-day":
                self.die_time = 1440
            elif human_given_parameter == "for-an-week":
                self.die_time = 10080
            elif human_given_parameter == "for-a-month":
                self.die_time = 43200
            elif human_given_parameter == "for-an-year":
                self.die_time = 525600
            elif human_given_parameter == "forever":
                self.die_time = 2102424
            else:
                raise Exception("The parameter given is not known.")

    def getHarakiriMessage(self) -> str:
        message = "Your instance are setted to make an harakiri in just five minutes! Somehing good to avoid unexpected useless instance consuming your money in AWS.\n"
        message += "If you are pretty sure that you will need an instance that must lasts for more time, use the argument \"--lasts\" with a value:\n"
        message += "* an arbitrary integer number: like 10, 20, 34, something else, that will be the number in minutes to lasts the instance.\n"
        message += "* for-ten-minutes: lasts for ten minutes. Really...\n"
        message += "* for-an-hour: lasts for an hour.\n"
        message += "* for-a-day: lasts for a day.\n"
        message += "* for-an-week: lasts for na week.\n"
        message += "* for-a-month: lasts for a month.\n"
        message += "* for-an-year: you are quite optimistic about the instance unchangability in the cloud services era...\n"
        message += "* forever: I will set to 4 years. Absolute nothing lasts forever, even more an ordinary VM in the cloud.\n"
        return message