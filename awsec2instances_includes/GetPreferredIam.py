class GetPreferredIam:

    def __init__(self):
        self.regionsIam = {
            "us-east-1": "ami-08f3d892de259504d",
            "sa-east-1": "ami-018ccfb6b4745882a" 
        }

    def getIam(self, region: str):
        return self.regionsIam[region]
