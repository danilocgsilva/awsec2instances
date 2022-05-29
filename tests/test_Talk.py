from awsec2instances_includes.Talk import Talk
import unittest
from io import StringIO
import sys
from tests.get_single_sample_instance import get_single_sample
from aws_api_mock.Instance_Single_Generator import Instance_Single_Generator

class test_Talk(unittest.TestCase):

    def setUp(self):
        self.talk = Talk()

    def test_printData(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        instance_generator = Instance_Single_Generator()
        instance_generator.setInstanceId("887cdb040ddfb0288")
        instance_generator.addTag("Name", "Orion")
        instance_generator.setPublicIp("27.229.225.250")

        self.talk.setInstanceData([instance_generator.generate()])
        self.talk.printData()
        sys.stdout = sys.__stdout__

        expected_string = '''---
Id: i-887cdb040ddfb0288
Name: Orion
Status: stopped
Type: t2.micro
Ip: 27.229.225.250
Key: my-secret-key\n'''
        
        self.assertEqual(expected_string, captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()