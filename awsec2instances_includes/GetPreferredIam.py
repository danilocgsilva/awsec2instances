class GetPreferredIam:

    def __init__(self):
        self.regionsIam = {
            "us-east-1": {
                "default": "ami-08f3d892de259504d",
                "ubuntu": "ami-0dba2cb6798deb6d8"
            },
            "sa-east-1": {
                "default": "ami-018ccfb6b4745882a",
                
                "ubuntu": "ami-0c3c87b7d583d618f"
            }  
        }

    def getIam(self, region: str, distro = None):
        if distro:
            return self.regionsIam[region][distro]
        return self.regionsIam[region]["default"]
