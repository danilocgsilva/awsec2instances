class UserScript:

    def __init__(self):
        self.script = ""

    def add_scripts(self, scripts):
        if self.script == "":
            self.script += "#!/bin/bash\n\nset -e\n"
        self.script += "\n" + scripts + "\n"

    def get_user_script(self) -> str:
        return self.script
