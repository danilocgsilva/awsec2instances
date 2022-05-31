from awsec2instances_includes.Talk import Talk
import unittest
from io import StringIO
import sys
from tests.get_single_sample_instance import get_single_sample
from aws_api_mock.Instance_Single_Generator import Instance_Single_Generator
from aws_api_mock.EC2_Client import EC2_Client
from awsec2instances_includes.AwsClientUtils import AwsClientUtils

class test_Talk(unittest.TestCase):

    def setUp(self):
        self.talk = Talk()

    def test_printData(self):

        instance_generator = Instance_Single_Generator()\
            .setInstanceId("887cdb040ddfb0288")\
            .addTag("Name", "Orion")\
            .setPublicIp("27.229.225.250")\
            .setImageId("ami-b4eaf27063e2a1e6b")

        captured_output = StringIO()
        sys.stdout = captured_output
        instanceData = [instance_generator.generate()]

        AwsClientUtils().addImageDescriptionToInstanceData(instanceData, EC2_Client())

        self.talk.setInstanceData(instanceData)
        self.talk.printData()
        sys.stdout = sys.__stdout__

        expected_string = '''---
Id: i-887cdb040ddfb0288
Name: Orion
Status: stopped
Type: t2.micro
Ip: 27.229.225.250
Key: my-secret-key
Image Id: ami-b4eaf27063e2a1e6b
Image Description: Canonical, Ubuntu, 20.04 LTS, amd64 focal image build on 2020-09-07\n'''
        
        self.assertEqual(expected_string, captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()