#!/usr/bin/python3
"""contains the entry point of the command interpreter:"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    '''HBNB Consol
    Attr:
        custom_prompt (str): command line prompt
    '''
    prompt = '(hbnb)'


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        '''Exit the program'''
        print("")
        return True

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything
        '''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        args:
            self
        '''
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel"]:
            print("* class doesn't exist **")
        else:
            New_BaseModel = BaseModel()
            New_BaseModel.save()
            print(New_BaseModel.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        print('{}{}'.format(arg ,len(arg)))
        if not arg:
            print("** class name missing **")
        else:
            number_of_argument = len(arg)
            if number_of_argument < 1:
               print("** class name missing **") 
            elif number_of_argument < 2:
                print("** instance id missing **")
            else:
                if arg[1] not in ['BaseModel']:
                    print("** class doesn't exist **")
                else:
                    Object_List = storage.al()
                    print (Object_List)


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.

        If the class name is missing, print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        pass
    def all(self, arg): 
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
    pass

    def do_update(self): 
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
        If the class name is missing, print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
        All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
        id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
