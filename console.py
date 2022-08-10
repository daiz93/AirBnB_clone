# contains the entry point of the command interpreter

import cmd, sys
from turtle import *

class HBNBCommand(cmd.Cmd):
    '''
    Init the consol
    Ars:
        Cmd:
    '''
    prompt = '(hbnb)'
    file = None

    def do_quit(self):
        ''' exit the program
        '''
        self.close()
        bye()
        return True

    def do_EOF(self,args):
        ''' exit the program
        '''
        if self.file:
            self.file.close()
            self.file = None
        return True

    def do_help(self):
        pass

    def do_emptyline(self):
        '''an empty line + ENTER shouldn’t execute anything'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()