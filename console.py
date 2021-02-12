#!/usr/bin/python3
""" CMD module to take commands from user """

import cmd, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ This class creates a simple shell
    for the user to input info
    """
    prompt = '(hbnb) '
    file = None

    @staticmethod
    def test_tty():
        """ test for interactive vs non-interactive """
        if not sys.stdin.isatty():
            print()

    @staticmethod
    def parse(arg):
        """ parses args passed """
        return arg.split()

    def do_quit(self, arg):
        """ quits the prompt on quit: (prompt) quit """
        self.test_tty()
        quit()
        return True

    def do_EOF(self, line):
        """ quits prompt on EOF: Ctrl + D """
        print()
        return True

    def emptyline(self):
        """ does nothing on ENTER """
        self.test_tty()
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel """
        largs = self.parse(arg)
        if largs[0] == "BaseModel":
            BM = BaseModel()
            BM.save()
            print(BM.id)
        else:
            print("** class doesn't exist **")

    def close(self):
        """ closes prompt """
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()