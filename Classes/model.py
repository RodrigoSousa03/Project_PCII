# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:11:56 2021

@author: User
"""

class Model():
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Constructor: Called when an object is instantiated
    # ['model','capacity','autonomy', 'staff', 'cargo', 'price', 'price', 'image_path']
    # for easy copy and paste
    
    def __init__(self, model, capacity, autonomy, staff, cargo, price, image_path):
        # Object attributes
        self._model = model
        self._capacity = capacity
        self._autonomy = autonomy
        self._staff = staff
        self._cargo = cargo
        self._price = price
        self._image_path = image_path
        # Add the new object to the User list
        if model not in Model.lst:
            print("I am here")
            Model.obj[model] = self
            Model.lst.append(model)
            #Model.write('Data/')
  
    
    @property
    def model(self):
        return self._model
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def autonomy(self):
        return self._autonomy
    
    @property
    def staff(self):
        return self._staff
    
    @property
    def cargo(self):
        return self._cargo
    
    @property
    def price(self):
        return self._price
    
    @property
    def image_path(self):
        return self._image_path
        
    
    
    
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
            print('não li')
            pass
    # Instance method to obtain object info
    def __str__(self):
        strprint = "f'"
        for att in list(self.__dict__.keys()):
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)