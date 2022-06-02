class OsFamily:

    def is_debian_family(self, designation: str) -> bool:
        if designation == "ubuntu" or designation == "ubuntu-20.04":
            return True
        return False

    def is_ubuntu_family(self, designation: str) -> bool:
        if designation == "ubuntu" or designation == "ubuntu-20.04":
            return True
        return False