# -*- coding: utf-8 -*-
"""
Created on Mon May 10 08:51:21 2021

@author: User
"""

import datetime
from Classes.client import Client
from Classes.airplane import Airplane
class Reservation:
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Constructor: Called when an object is instantiated
    def __init__(self, code, date_init, date_final, client, cargo, airplane, price):
        # Object attributes
        # Check the customer referential integrity
        #if client in Client.lst:
         
            #if airplane in Airplane.lst:
        self._code = code
        datelist1 = list(map(int, date_init.split('-')))
        self._date_init =datetime.date(datelist1[0], datelist1[1], datelist1[2])
        datelist2 = list(map(int, date_final.split('-')))
        self._date_final = datetime.date(datelist2[0], datelist2[1], datelist2[2])
        self._client = client
        self._cargo = cargo
        self._airplane = airplane
        
        self._price = price
        # Add the new object to the Order list
        Reservation.obj[code] = self
        Reservation.lst.append(code)
        #     else:
        #         print('Airplane ', airplane, ' not found' )
        # else:
        #     print('Customer ', client, ' not found')
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # date_init property getter method
    @property
    def date_init(self):
        return self._date_init
    
    @property
    def date_final(self):
        return self._date_final
    
    @property
    def client(self):
        return self._client
    
    @property
    def cargo(self):
        return self._cargo
    
    @property
    def airplane(self):
        return self._airplane
    
    @property
    def price(self):
        return self._price
    
    # customer property getter method
    @property
    def customer(self):
        return self._customer
    #days property getter method
    @property
    def days(self):
        delta = self.date_final - self.date_init
        return delta.days
    
    # date_init property setter method
    @date_init.setter
    def date_init(self, date_init):
        self._date_init = date_init
        
    # date_init property setter method
    @date_final.setter
    def date_final(self, date_final):
        self._date_final = date_final
    
    # customer property setter method
    @customer.setter
    def customer(self, client):
        if client in Client.lst:
            self._client = client
        else:
            print('Customer ', client, ' not found') 
    
    
    
    
    
    
    def date_checker(self, init_temp, final_temp): #returns True if the reservation is possible and False otherwise
        reserve = self.__class__.first() 
        print(reserve)                      #get first class object
        while True:
            if reserve.airplane == self.airplane:              #check if its the same airplane
                init  = reserve.date_init
                final = reserve.date_final
                if init_temp < datetime.date.today():
                    return False
                
                if (init_temp >= init) and (init_temp <= final):  #correct date validation
                    return False
                
                if (final_temp >= init) and (final_temp <= final):
                    return False
                
                if (init_temp <= init) and (final_temp >= final):
                    return False
                
                if self.__class__.pos == len(self.__class__.lst) - 1:  #if it is the last reservation, end cycle
                    break
                
                reserve = Reservation.next()   #next  vai 
        return True
        
    
    def available_planes(cls, init_temp, final_temp):    #list of available airplanes
        lista = Airplane.lst.copy()
        reserve=cls.first()
        print(lista)
        l = len(cls.lst)
        print(l)
        #for i in range(l):
        i=1
        if init_temp < datetime.date.today():
            lista=[]
       
        while i<l:
            #reserve = cls.lst[i]
            print(reserve)
            
            init  = reserve.date_init
            print(init)
            final = reserve.date_final
            print(final)
            airplane=str(reserve.airplane)
            print(airplane)
            print(lista)
            if reserve.airplane in lista:
            
                
                if (init_temp >= init) and (init_temp <= final):  #correct date validation
                    lista.remove(reserve.airplane)
                    print("here")
                    print(lista)
                    reserve = Reservation.next()
                    i=i+1
                    continue
                    
                if (final_temp >= init) and (final_temp <= final):
                    lista.remove(reserve.airplane)
                    i=i+1
                    print(lista)
                    print("2here")
                    reserve = Reservation.next()
                    continue
                        
                if (init_temp <= init) and (final_temp >= final):
                    lista.remove(str(reserve.airplane))
                    print("2here")
                    print(lista)
                    i=i+1
                    reserve = Reservation.next()
                    continue
            reserve = Reservation.next() 
            i=i+1
                
        return lista
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
    
if __name__ == "__main__":    
    
  
    # Creates a reservation
    Airplane.read('Data/')
    Reservation.read('Data/')
    a1 = Reservation( "04", "2021-5-21", "2021-6-21", "04", "9039", "1","83902")
    lista_airplanes=Reservation.available_planes(self.classObj,self.date_init,self.date_final)
    #value=a1.date_checker(a1.date_init,a1.date_final)
    # lista=a1.available_planes(a1.date_init,a1.date_final)
    # print(lista)
    # if value==True:
    #   a1.write(path = './')
    # else:
    #     Reservation.remove(a1.code)
    #     print(Reservation.lst)