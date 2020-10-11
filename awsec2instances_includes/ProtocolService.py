class ProtocolService:

    def __init__(self, protocols = None):
        self.allowed_ones_with_protocol = {
            "with-ssh": 22, 
            "with-http": 80
        }
        self.ports = []
        if not protocols == None and not protocols == "": 
            for protocol_entered in protocols.split(","):
                if not protocol_entered in self.allowed_ones_with_protocol:
                    raise Exception("You entered an invalid option: " + protocol_entered)
                self.ports.append(self.allowed_ones_with_protocol[protocol_entered])

    def get_ports(self) -> list:
        return self.ports

    def is_have_ssh(self) -> bool:
        return 22 in self.ports

    def is_not_empty(self) -> bool:
        if len(self.ports) == 0:
            return False
        return True
            
