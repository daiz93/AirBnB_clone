#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    ''' Commande interpreter
    Args : 
        cmd
    '''
    prompt = '(hbnb)'

    def do_quit(self,args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self,args):
        '''Exit the program'''
        print("")
        return True

    def do_emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
