#!/usr/bin/python3

# importing datetime module for uuid4()
import uuid
# importing datetime module for now()
import datetime

class BaseModel:
'''
defines all common attributes/methods for other classes
'''

    id = str(uuid.uuid4())

    def __init__(self):
    '''Initialze instance'''
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        ''' print: [<class name>] (<self.id>) <self.__dict__>
        '''
        return '[' + type(self).__name__ + '] (' + str(self.id) + ') ' + self.__dict__

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime
        '''
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of the instance
        '''
        
