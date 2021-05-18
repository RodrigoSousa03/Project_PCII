# -*- coding: utf-8 -*-
"""
Created on Mon May 10 08:51:21 2021

@author: User
"""

import datetime
from client import Client
class Reservation:
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Constructor: Called when an object is instantiated
    def __init__(self, code, date_init, date_final, client, cargo, airplane):
        # Object attributes
        # Check the customer referential integrity
        if client in Client.lst:
            self._code = code
            datelist = list(map(int, date_init.split('-')))
            self._date_init = datetime.date(datelist[0], datelist[1], datelist[2])
            self._client = client
            self._cargo = cargo
            self._airplane = airplane
            # Add the new object to the Order list
            Reservation.obj[code] = self
            Reservation.lst.append(code)
        else:
            print('Customer ', client, ' not found')
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # date_init property getter method
    @property
    def date_init(self):
        return self._date_init
    # date_init property setter method
    @date_init.setter
    def date_init(self, date_init):
        self._date_init = date_init
    # customer property getter method
    @property
    def customer(self):
        return self._customer
    # customer property setter method
    @customer.setter
    def customer(self, client):
        if client in Client.lst:
            self._client = client
        else:
            print('Customer ', client, ' not found')   
            
    @property
    def days(self):
        delta = self.date_final - self.date_init
        return delta.days



    @classmethod
    def date_checker(date):
        pass
        
    
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
    # Object delete class method
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
        
    # Write object to csv file class method
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
    # Read objects from csv file class method
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