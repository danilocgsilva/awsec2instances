class ProtocolService:

    def __init__(self, protocols = None):
        self.allowed_ones_with_protocol = {
            "with-ssh": 22, 
            "with-http": 80,
            "with-database": 3306,
            "with-desktop": 3389
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

    def is_have_http(self) -> bool:
        return 80 in self.ports

    def is_have_database(self) -> bool:
        return 3306 in self.ports

    def is_have_desktop(self) -> bool:
        return 3389 in self.ports

    def is_not_empty(self) -> bool:
        if len(self.ports) == 0:
            return False
        return True
            
    def ensure_port_80(self):
        if not 80 in self.ports:
            self.ports.append(80)

    def ensure_port_22(self):
        if not 22 in self.ports:
            self.ports.append(22)

    def ensure_port_3306(self):
        if not 3306 in self.ports:
            self.ports.append(3306)

    def ensure_port_3389(self):
        if not 3389 in self.ports:
            self.ports.append(3389)
