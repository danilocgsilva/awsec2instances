class GetPreferredIam:

    def __init__(self):

        self.distro = None

        self.region = None
        
        self.regionsIam = {
            "us-east-1": {
                "default": {
                    "id": "ami-0e449176cecc3e577",
                    "instance_type": "t4g.nano"
                },
                "aws-ami-old": {
                    "id": "ami-08f3d892de259504d",
                    "instance_type": "t2.nano"
                },
                "ubuntu": {
                    "id": "ami-02ddaf75821f25213",
                    "instance_type": "t4g.nano"
                },
                "ubuntu-20.04": {
                    "id": "ami-0dba2cb6798deb6d8",
                    "instance_type": "t2.nano"
                }
            },
            "us-east-2": {
                "default": {
                    "id": "ami-01aab85a5e4a5a0fe",
                    "instance_type": "t2.nano"
                } ,
                "ubuntu": {
                    "id": "ami-02aa7f3de34db391a",
                    "instance_type": "t2.nano"
                }
            },
            "sa-east-1": {
                "default": {
                    "id": "ami-018ccfb6b4745882a",
                    "instance_type": "t2.nano"
                },
                "ubuntu": {
                    "id": "ami-0c3c87b7d583d618f",
                    "instance_type": "t2.nano"
                } 
            }  
        }

    def getDistroData(self, region = None) -> dict:

        if not self.distro:
            self.distro = "default"
        
        return self.regionsIam[self.region][self.distro]

    def setRegion(self, region: str):
        self.region = region
        return self

    def setDistro(self, distro):
        self.distro = distro
        return self

    def getIamId(self):        
        if self.distro:
            return self.regionsIam[self.region][self.distro]["id"]
        return self.regionsIam[self.region]["default"]["id"]
