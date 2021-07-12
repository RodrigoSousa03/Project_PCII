# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:15:40 2021

@author: User
"""

import datetime
from Classes.user import User

class Client(User):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Constructor: Called when an object is instantiated
    # ['code', 'name', 'city', 'phone', 'dob', 'NIF', 'mail', 'password','username', 'gender','payment_card']
    # for easy copy and paste
    
    def __init__(self, code, name, city, phone, NIF, dob, mail, password, username, gender,payment_card):
        # Object attributes
        super().__init__(code, name, city, phone, NIF, dob, mail, password, username, gender)
        #self._buy_history = buy_history
        self._payment_card = payment_card
        # Add the new object to the User list
        Client.obj[code] = self
        Client.lst.append(code)
  

    #payment card property getter method
    @property
    def payment_card(self):
        return self._payment_card
    
    #payment card property setter method
    @payment_card.setter
    def payment_card(self, payment_card):
        self._payment_card = payment_card
    
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
            pass
    # Instance method to obtain object info
    def __str__(self):
        strprint = "f'"
        for att in list(self.__dict__.keys()):
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)


if __name__ == "__main__":    
    
  
    # Creates a customer
    Client.read()
    u1 = Client("12","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F","wrer")
    u1.write(path = '')
    # User.read()
    # u2=User("12","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F")
    # u2.write()
    
    # c1=Client(u1, "buy_history"," payment_card")
    # c2 = User("05","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F")
    # c2.write(path = '')
    # print(c1)