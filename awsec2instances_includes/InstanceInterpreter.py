import boto3

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

    def loadById(self, instance_id: str):
        client = boto3.client("ec2")
        request_data = self.instanceData = client.describe_instances(
            InstanceIds=[instance_id]
        )
        self.instanceData = request_data["Reservations"][0]["Instances"][0]

    def getInstanceKey(self):
        if "KeyName" in self.instanceData:
            return self.instanceData["KeyName"]
        return "---"
            
    def getImageId(self):
        return self.instanceData["ImageId"]

    def getImageDescription(self):
        return self.instanceData["imageIdDescription"]
        
