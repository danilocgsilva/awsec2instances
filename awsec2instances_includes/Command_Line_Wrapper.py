class Command_Line_Wrapper:

    def set_command_string(self, command_string: str):
        self.command_string = command_string

    def append_command_string(self, commands_string_to_append: str):
        self.command_string = self.command_string + ' ' + commands_string_to_append

    def get_command_string(self) -> str:
        return self.command_string