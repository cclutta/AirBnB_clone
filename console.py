#!/usr/bin/python3
""" Console Module
"""

import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ Console entry point. """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
