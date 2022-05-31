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

        instance_generator = Instance_Single_Generator()\
            .setInstanceId("887cdb040ddfb0288")\
            .addTag("Name", "Orion")\
            .setPublicIp("27.229.225.250")\
            .setImageId("ami-b4eaf27063e2a1e6b")

        captured_output = StringIO()
        sys.stdout = captured_output

        self.talk.setInstanceData([instance_generator.generate()])
        self.talk.setImageDescription("The image description")
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
Image Description: The image description\n'''
        
        self.assertEqual(expected_string, captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()