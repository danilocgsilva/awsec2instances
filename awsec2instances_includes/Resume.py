class Resume:


    def __init__(self):
        self.instances_data = []

    def add_instances_data(self, data: dict):
        self.instances_data.append(data)
        return self

    def get_instance_count(self):
        instance_cout = 0
        for instance_data in self.instances_data:
            instance_cout = instance_cout + len(instance_data)
        return instance_cout

