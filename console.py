#!/usr/bin/python3
"""contains the entry point of the command interpreter:"""
import cmd


class HBNBCommand(cmd.Cmd):
    '''HBNB Consol
    Attr:
        custom_prompt (str): command line prompt
    '''
    prompt = '(hbnb)'

    def do_nothing(self,arg):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        '''Exit the program'''
        print("")
        return True

    def do_emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
