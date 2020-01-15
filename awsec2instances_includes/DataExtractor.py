class DataExtractor():

    def set_instance_raw_data(self, instance_raw_data):
        self.instance_raw_data = instance_raw_data


    def extract_instance_id(self):
        return self.instance_raw_data["InstanceId"]


    def extract_instance_type(self):
        return self.instance_raw_data["InstanceType"]


    def extract_public_ip_address(self):
        if "PublicIpAddress" in self.instance_raw_data:
            return self.instance_raw_data["PublicIpAddress"]
        else:
            return "---"


    def extract_name(self):
        listTags = self.instance_raw_data["Tags"]

        for tag in listTags:
            if tag["Key"] == "Name":
                return tag["Value"]

        return "---"