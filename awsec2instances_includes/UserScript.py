class UserScript:

    def __init__(self):
        self.script = "#!/bin/bash\n"
        self.script += "\nset -e\n"

    def add_scripts(self, scripts):
        self.script += "\n" + scripts + "\n"

    def get_user_script(self) -> str:
        return self.script
