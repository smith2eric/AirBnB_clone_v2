#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
<<<<<<< HEAD
        if cls is None:
            return FileStorage.__objects
        store = {}
        for key, value in FileStorage.__objects.items():
            if value.__class__ == cls:
                store[key] = value
        return store
=======

        if cls:
            all = dict()
            for i in self.__objects.keys():
                if i.split('.')[0] == cls.__name__:
                    all[i] = self.__objects[i]
            
            return all

        return FileStorage.__objects
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        with open(self.__file_path, 'w') as f:
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as fo:
                tmp = json.load(fo)
            for key in tmp.items():
                self.__objets[key] = classes[tmp[key]['__class__']](**tmp[key])
        except:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """ Delete obj from __objects if it’s inside
        - if obj is equal to None """
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            del FileStorage.__objects[key]

    def close(self):
        """method to reload"""
        self.reload()
=======
        """delete obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything"""

        if obj:
            del(self.__objects["{}.{}".format(type(obj).__name__, obj.id)])
            del(obj)
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
