#!/usr/bin/python3
"""console v0.0.1
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter of AirBnB project
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Ctrl D - the program will exit cleanly
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """is the empty line is entered
        in response to the prompt
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
