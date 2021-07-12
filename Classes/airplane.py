# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:06:11 2021

@author: User
"""
#%% Class Airplane

import datetime
from Classes.model import Model

class Airplane(Model):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    num = 0
    # Constructor: Called when an object is instantiated
    # ['code','model']
    # for easy copy and paste
    
    def __init__(self, model, capacity, autonomy, staff, cargo, price,image_path, code, dof):
        # Object attributes
        super().__init__(model, capacity, autonomy, staff, cargo, price,image_path)
        self._code = code
        # datelist = list(map(int, dof.split('-')))
        # self._dof = datetime.date(datelist[0], datelist[1], datelist[2])
        self._dof=dof
        # Add the new object to the User list
        Airplane.obj[code] = self
        Airplane.lst.append(code)
  
    
    @property
    def code(self):
        return self._code
    
    @property
    def dof(self):
        return self._dof
            
#################################################        
# generic code: no need to change for a new class    
    # Class method to implement constructor overloading

        
    @classmethod
    def from_string(cls, str_data):
        str_list = str_data.split(";")
        strarg = 'cls(str_list[0]'
        for i in range(1, len(str_list)):
            strarg += ',str_list[' + str(i) + ']'
        strarg += ')'
        return eval(strarg)
    # Class methods to iterate (forward and backward) through the class objects
    @classmethod
    def next(cls):
        cls.pos += 1
        return cls.current()
    @classmethod
    def previous(cls):
        cls.pos -= 1
        return cls.current()
    @classmethod
    def current(cls):
        if cls.pos < 0:
            cls.pos = 0
            return None
        elif cls.pos >= len(cls.lst):
            cls.pos = len(cls.lst) - 1
            return None
        else:
            code = cls.lst[cls.pos]
            return cls.obj[code]
    @classmethod
    def first(cls):
        cls.pos = 0
        return cls.current()
    @classmethod
    def last(cls):
        cls.pos = len(cls.lst) - 1
        return cls.current()
    # Object delete method
    @classmethod
    def remove(cls, p):
        cls.lst.remove(p)
        del cls.obj[p]
    # Sort objects by attribute class methods
    @classmethod
    def orderfunc(cls, e):
        return getattr(cls.obj[e], cls.sortkey)
    @classmethod
    def sort(cls, att):
        cls.sortkey = att
        cls.lst.sort(key=cls.orderfunc)
    # Write object to csv file
    @classmethod
    def write(cls, path = ''):
        if len(cls.lst) > 0:
            fh = open(path + cls.__name__ + '.csv', 'w')
            p = cls.obj[cls.lst[0]]
            strprint = ""
            for att in list(p.__dict__.keys()):
                strprint += att[1:] + ';'
            fh.write(strprint[:-1] + '\n')
            for p in cls.obj.values():
                fh.write(p.__str__() + '\n')
            fh.close()
    # Read objects from csv file
    # 
    @classmethod
    def read(cls, path = ''):
        cls.obj = dict()
        cls.lst = list()
        try:
            fh = open(path + cls.__name__ + '.csv', 'r')
            fh.readline()
            for p in fh:
                cls.from_string(p.strip())
            fh.close()
            
        except:
            print("erro ler -------------",path + cls.__name__ + '.csv')
            pass
   
    # Instance method to obtain object info
    def __str__(self):
        strprint = "f'"
        for att in list(self.__dict__.keys()):
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)
    
    
# if __name__ == "__main__":    
    
  
#     # Creates a plane
#     a1 = Airplane( "ModelA", "3hours", "9 hours", "4 pilots", "903920 toneladas", "9032839", "89", "25-12-2009")
#     a1.write(path = './')
#     # c2 = User("05","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F")
#     # c2.write(path = '')
#     print(a1)
#     a2=Airplane("ModelB","3hours","9 hours","4 pilots","903920 toneladas","9032839","90","25-12-20")
#     a2.write(path = './')
#     a3=Airplane("ModelA","3hours","9 hours","4 pilots","903920 toneladas","9032839","91","25-12-20")
#     a3.write(path = './')
    