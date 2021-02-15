#!/usr/bin/python3
""" CMD module to take commands from user """

import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ This class creates a simple shell
    for the user to input info
    """
    prompt = '(hbnb) '
    file = None
    cl_names = {"BaseModel": BaseModel, "User": User}

    @staticmethod
    def test_tty():
        """ test for interactive vs non-interactive """
        if not sys.stdin.isatty():
            print()

    @staticmethod
    def parse(arg):
        """ parses args passed """
        return shlex.split(arg)

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

    def select_obj(self, arg):
        """ finds the correct object in dicitonary """
        if arg not in self.cl_names:
            return False
        else:
            return self.cl_names.get(arg)

    def check_class(self, arg):
        """ checks to make sure class name is present and valid """
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif arg[0] not in self.cl_names:
            print("** class doesn't exist **")
            return False
        else:
            return True

    @staticmethod
    def check_id(arg):
        """ checks id of object to see if valid """
        objs = storage.all()
        if len(arg) < 2:
            print("** instance id missing **")
            return False
        key = arg[0] + '.' + arg[1]
        if key not in objs:
            print("** no instance found **")
            return False
        else:
            return True

    def do_create(self, arg):
        """ creates a new instance of BaseModel """
        largs = self.parse(arg)
        if not self.check_class(largs):
            return
        cls = self.select_obj(largs[0])
        new_obj = cls()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """prints the string representation of an instance based on the
        class name and id"""
        largs = self.parse(arg)
        if not self.check_class(largs):
            return
        if not self.check_id(largs):
            return
        objs = storage.all()
        key = largs[0] + '.' + largs[1]
        obj = objs.get(key)
        print(obj)

    def do_destroy(self, arg):
        """destroy the given instance. ID tells us which
        instance to destory """
        largs = self.parse(arg)
        if not self.check_class(largs):
            return
        if not self.check_id(largs):
            return
        objs = storage.all()
        key = largs[0] + '.' + largs[1]
        del objs[key]
        storage.save()

    def do_all(self, arg):
        """ prints all instances using there __str__ method
        in a list of instances """
        largs = self.parse(arg)
        if len(largs) == 0:
            pass
        elif largs[0] not in self.cl_names:
            print("** class doesn't exit **")
            return
        dict_of_obs = storage.all()
        list_of_obs = []
        for key in dict_of_obs:
            list_of_obs.append(str(dict_of_obs.get(key)))
        print(list_of_obs)

    def do_update(self, arg):
        """ updates an instance based on the class name and id by adding or
        updating attribute """
        largs = self.parse(arg)
        if not self.check_class(largs):
            return
        if not self.check_id(largs):
            return
        if len(largs) < 3:
            print("** attribute name missing **")
            return
        if len(largs) < 4:
            print("** value missing **")
            return
        dict_of_obs = storage.all()
        key = largs[0] + '.' + largs[1]
        obj = dict_of_obs.get(key)
        setattr(obj, largs[2], largs[3])
        obj.save()

    def close(self):
        """ closes prompt """
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
