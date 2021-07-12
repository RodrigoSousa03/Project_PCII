# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Customer

"""""
#%% Class Customer
import datetime


class User:
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    num=0
    # Constructor: Called when an object is instantiated
    #for easy copy and paste
    #code,name,city,phone,NIF, dob, mail,password,username,gender
    def __init__(self, code,name,city,phone,NIF, dob, mail,password,username,gender):
        # Object attributes
        #code = str(User.num)  #just reads parts of the file dont know why
        self._code = code
        self._name = name
        self._city = city
        val = User.phone_check(phone)
        if val:
            self._phone = phone
        else:
            #error message
            
            print('Phone number is not valid.')
        self._phone = phone
        self._NIF = NIF
        # datelist = list(map(int, dob.split('-')))
        # self._dob = datetime.date(datelist[0], datelist[1], datelist[2]) #yyyy-mm-dd
        self._dob = dob
        self._mail = mail
        self._password = password
        self._username = username
        self._gender=gender

        # Add the new object to the Customer list
        User.obj[code] = self
        User.lst.append(code)
        
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # city property getter method
    @property
    def city(self):
        return self._city
    # phone property getter method
    @property
    def phone(self):
        return self._phone
    # NIF property getter method
    @property
    def NIF(self):
        return self._NIF
    # dob property getter method
    @property
    def dob(self):
        return self._dob
     # mail property getter method
    @property
    def mail(self):
        return self._mail
    
    # password property getter method
    @property
    def password(self):
        return self._password
    #username property getter method
    @property
    def username(self):
        return self._username
    #gender property getter method
    @property
    def gender(self):
        return self._gender
    #property idade getter method
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
        
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # city property setter method
    @city.setter
    def city(self, city):
        self._city = city
    # phone property setter method
    @phone.setter
    def phone(self, phone):
        self._phone = phone
    #mail property setter method
    @mail.setter
    def mail(self, mail):
        self._mail = mail
    # password property setter method
    @password.setter
    def password(self, password):
        self._password = password
    # username property setter method
    @username.setter
    def username(self, username):
        self._username = username
    #gender property setter method
    @gender.setter
    def gender(self, gender):
        self._gender = gender
#code,name,city,phone,NIF, dob, mail,password,username,gender
    
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
            print("erro ler -------------",path + cls.__name__ + '.csv')
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
##############################################
#static methods, functions for input validation
#to be used in setters
        
    @staticmethod
    def phone_check(phone):
        val = True
        if not all(char.isdigit() for char in phone):
            
            print('phone should only have numbers')
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
        






   

# if __name__ == "__main__":    
    
  
#     # Creates a customer
#     c1 = User("04","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F")
#     c1.write(path = '')
#     c2 = User("05","manel","rua11","232132","1232","2000-12-31","fghft@gmail.com","mm","234","F")
#     c2.write(path = '')
#     print(c1)
    
   