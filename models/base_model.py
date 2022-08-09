#!/usr/bin/python3

# importing datetime module for uuid4()
import uuid
# importing datetime module for now()
from datetime import datetime

class BaseModel:
    '''
    defines all common attributes/methods for other classes
    '''


    def __init__(self, *args, **kwargs):
        '''Initialze instance'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if (kwargs is not None):
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at','updated_at']
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        ''' print: [<class name>] (<self.id>) <self.__dict__>
        '''
        return '[' + type(self).__name__ + '] (' + str(self.id) + ') ' + str(self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime
        '''
        self.updated_at = datetime.now()
    def to_dict(self):
        '''returns a dictionary containing all keys
        /values of __dict__ of the instance
        '''
        dict_dictdictionary = self.__dict__.copy()
        dict_dictdictionary["__class__"] = self.__class__.__name__
        dict_dictdictionary["created_at"] = dict_dictdictionary["created_at"].isoformat()
        dict_dictdictionary["updated_at"] = dict_dictdictionary["updated_at"].isoformat()
        return dict_dictdictionary

