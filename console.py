#!/usr/bin/python3
"""This is for the console"""
import cmd
from sys import argv
import models


class HBNBCommand(cmd.Cmd):
    """I guess I'm doing things"""
    prompt = '(hbnb)'

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
