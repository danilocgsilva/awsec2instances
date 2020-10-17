class InstanceInterpreter:

    def __init__(self):
        self.instanceData = None

    def setInstanceData(self, instanceData: dict):
        self.instanceData = instanceData
        return self

    def getInstanceId(self):
        return self.instanceData["InstanceId"]

    def getInstanceName(self):
        if "Tags" in self.instanceData:
            for tagData in self.instanceData["Tags"]:
                print(tagData)
                if tagData["Key"] == "Name":
                    return tagData["Value"]
            return "---"
        return "---"

    def getStatus(self) -> str:
        return self.instanceData["State"]["Name"]

    def getInstanceType(self):
        return self.instanceData["InstanceType"]

    def getInstanceIp(self):
        if "PublicIpAddress" in self.instanceData:
            return self.instanceData["PublicIpAddress"]
        return "---"
