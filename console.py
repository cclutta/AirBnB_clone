#!/usr/bin/python3
""" Console Module
"""

import cmd
import models


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
