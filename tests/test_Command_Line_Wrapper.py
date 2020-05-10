import unittest
from awsec2instances_includes.Command_Line_Wrapper import Command_Line_Wrapper

class test_Command_Line_Wrapper(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_Command_Line_Wrapper, self).__init__(*args, **kwargs)
        self.command = Command_Line_Wrapper()


    def test_assing_command_line_test_one(self):
        command_to_assing = "ls"
        self.command.set_command_string(command_to_assing)
        command_assigned = self.command.get_command_string()
        self.assertEqual(command_to_assing, command_assigned)


    def test_assing_command_line_test_two(self):
        command_to_assing = "aws ec2 describe-instances"
        self.command.set_command_string(command_to_assing)
        command_assigned = self.command.get_command_string()
        self.assertEqual(command_to_assing, command_assigned)


    def test_append_command_line_test(self):
        command_to_assing = "aws ec2 describe-instances"
        self.command.set_command_string(command_to_assing)
        command_suffix = '--profile my_profile'
        self.command.append_command_string(command_suffix)
        expected_file_command = command_to_assing + ' ' + command_suffix
        returned_command = self.command.get_command_string()
        self.assertEqual(expected_file_command, returned_command)


if __name__ == '__main__':
    unittest.main()