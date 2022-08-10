#!/usr/bin/python3

import json
from os.path import exists


class FileStorage:
    ''' a class that serializes instances to a JSON 
    file and deserializes JSON file to instances
    '''

    __file_path = "file.json"
    __objects = {}


    def all(self):
        '''returns the dictionary __objects
        Args:
            self
        Returns: 
            dictionary __objects
        '''
        return FileStorage.__objects
    
    def new(self, obj): 
        '''sets in __objects the obj with key <obj class name>.id
        Args: 
            self:
            obj:
        '''
        FileStorage.__objects[obj.__class__.__name__ +'.' + str(obj.id)] = obj

    def save(self): 
        '''serializes __objects to the JSON file (path: __file_path)'''
        new__objects = {}
        for key, value in FileStorage.__objects:
            new__objects[key] = FileStorage.__objects[key].to_dict()
        with open( FileStorage.__file_path,'w') as json_text:
            json.dump(new__objects,json_text)

    def reload(self): 
        '''deserializes the JSON file to __objects (only if the JSON 
        file (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)
        '''
        if exists(FileStorage.__file_path):
            with open (FileStorage.__file_path,'r') as f:
                data = json.load(f)
                for obj in data.values():
                    class_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))
