#!/usr/bin/python3
""" Console Module
"""

import cmd
import models
import shlex

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Console entry point. """
    prompt = "(hbnb) "

    classes = ["BaseModel", "Amenity",
               "City", "Place", "Review", "State", "User"]

    def default(self, line):
        """ Default of cmd. """

    def do_EOF(self, line):
        """Handles EOF """
        return True

    def do_quit(self, line):
        """When you want to quit the program. """
        return True

    def emptyline(self):
        """Handles the empty line behaviour."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel"""
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in self.classes:
            new = eval(args[0])()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance.
        """
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance. """
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.   """
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print([v.__str__() for v in models.storage.all().values()])
        elif args[0] in self.classes:
            print([v.__str__() for v in models.storage.all().values()
                   if type(v) is eval(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance by adding or updating attribute. """
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    if len(args) < 3:
                        print("** attribute name missing **")
                    else:
                        if len(args) < 4:
                            print("** value missing **")
                        else:
                            obj = models.storage.all()[key]
                            try:
                                attr_type = type(getattr(obj, args[2]))
                                args[3] = attr_type(args[3])
                            except Exception:
                                try:
                                    args[3] = int(args[3])
                                except Exception:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        pass

                            setattr(obj, args[2], args[3])
                            obj.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def count(self, line):
        """
        Prints the number of instances of a class. """
        args = shlex.split(line)
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] in self.classes:
            instances = str(models.storage.all().keys())
            print(instances.count(args[0]))
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Handles the default behaviour."""
        funcs = {"all": self.do_all, "count": self.count, "show": self.do_show,
                 "destroy": self.do_destroy, "update": self.do_update}
        cmd = line.split('.', 1)
        class_name = cmd[0]
        args = [None]
        if len(cmd) > 1:
            args = cmd[1].strip("()").split('(')
        if args[0] in funcs:
            func = funcs[args[0]]
            params = class_name + ' '
            if len(args) > 1:
                if args[0] == "update" and args[1][-1] == '}':
                    str_dict = args[1].split(' ', 1)[1]
                    upd_dict = ast.literal_eval(str_dict)
                    params += args[1].split(',', 1)[0] + ' '
                    for k, v in upd_dict.items():
                        fparams = '{} "{}" "{}"'.format(params, str(k), str(v))
                        func(fparams)
                    return
                else:
                    params += args[1].replace(',', '')
            func(params)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
