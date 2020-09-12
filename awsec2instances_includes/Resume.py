class Resume:


    def __init__(self):
        self.instances_data = []
        self.instanceCount = 0

    def add_instances_data(self, data: dict):
        self.instances_data.append(data)
        return self

    def get_instance_count(self):
        for instance_data in self.instances_data:
            self.instanceCount = self.instanceCount + len(instance_data)
        return self.instanceCount
