# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:42:30 2021

@author: User
"""
#%% Class User

import datetime

class User:
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    num = 0
    # Constructor: Called when an object is instantiated
    # ['code', 'name', 'address', 'phone', 'NIF', 'dob', 'mail', 'password','username', 'gender']
    #code, name, address, phone, NIF, dob, mail, password, username, gender
    # for easy copy and paste
    
    def __init__(self, code, name, address, phone, NIF, dob, mail, password, username, gender, status = ""):
        # Object attributes
        code = str(User.num)            
        self._code = code
        self._name = name
        self._address = address
        val = User.phone_check(phone)
        if val:
            self._phone = phone
        else:
            #error message
            print('Phone number is not valid.')
        
        self._NIF = NIF
        datelist = list(map(int, dob.split('-')))
        self._dob = datetime.date(datelist[0], datelist[1], datelist[2]) #yyyy-mm-dd
        self._mail = mail
        self._password = password
        self._username = username
        self._gender = gender
        # Add the new object to the User list
        User.obj[code] = self
        User.lst.append(code)
        
    # Object properties
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # address property getter method
    @property
    def address(self):
        return self._address
    
    # phone property getter method
    @property
    def phone(self):
        return self._phone
    # dob property getter method
    @property
    def dob(self):
        return self._dob
    
    # NIF property getter method
    @property
    def NIF(self):
        return self._NIF
   
    # mail property getter method
    @property
    def mail(self):
        return self._mail
    
    @property
    def password(self):
        return self._password
    
    @property
    def username(self):
        return self._username
    
    @property
    def gender(self):
        return self._gender
    
    # idade property getter method
    @property
    def idade(self):
        yb = int(self.dob[:4])
        mb = int(self.dob[5:7])
        db = int(self.dob[8:])
        
        td = datetime.date.today()
        
        yt = td.year
        mt = td.month
        dt = td.day
        
        if mt>mb or (mt == mb and dt >= db):
            return yt - yb
        else:
            return yt - yb - 1
    # address property setter method
    @address.setter
    def address(self, address):
        self._address = address
    
    # phone property setter method
    @phone.setter
    def phone(self, phone):
        val = User.phone_check(phone)
        if val:
            self._phone = phone
        else:
            #error message
            print('Phone number is not valid.')
        
    @password.setter
    def password(self, password):
        val = User.password_check(password)
        if val:
            self._password = password
        else:
            #error message
            print('Password is not valid.')
            
            
##############################################
#static methods, functions for input validation
#to be used in setters
        
    @staticmethod
    def phone_check(phone):
        val = True
        if not all(char.isdigit() for char in phone):
            print('phone should only have numerals')
            val = False
        return val
        

    @staticmethod
    def password_check(password):
      
        SpecialSym =['$', '@', '#', '%']
        val = True
          
        if len(password) < 6:
            print('length should be at least 6')
            val = False
              
        if len(password) > 20:
            print('length should be not be greater than 20')
            val = False
              
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False
              
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False
              
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False
              
        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#%')
        
        return val
    
    @staticmethod
    def code_maker():
        td = datetime.date.today()
        yt = td.year
        count = str(User.count_lines('Classes'))
        code = ""
        while True:
            if len(count) < 5:
                count = "0" + count
            else:
                break
        
        code = str(yt) + count
        
        return code
    
    
        
    
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
            User.num = 0
            for p in fh:
                p1 = cls.from_string(p.strip())
                if p1.code > User.num:
                    User.num = p1.code
            fh.close()
            User.num += 1
            return User.num
        except:
            print("não li")
            pass
    # Instance method to obtain object info
    def __str__(self):
        strprint = "f'"
        for att in list(self.__dict__.keys()):
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)
    
    @classmethod
    def count_lines(cls, path = ''):
        try:
            fh = open(path + cls.__name__ + '.csv', 'r')
            count = len(fh.readlines())
            return count
        except:
            pass
        
        
    
    
