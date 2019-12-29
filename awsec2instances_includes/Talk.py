class Talk:

    def get_instance_data(self, instance_data):
        self.instance_data = instance_data


    def printData(self):
        for instanceSingle in self.instance_data:
            print('---')
            print('Instance counting: ' + str(instanceSingle['count']))
            print('Id: ' + instanceSingle['id'])
            print('Name: ' + instanceSingle['name'])
            print('Status: ' + instanceSingle['status'])
            print('Type: ' + instanceSingle['type'])
            print('Ip: ' + instanceSingle['ip'])
            
            