# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:36:53 2021

@author: User
"""

from Classes.airplane import Airplane
from Classes.client import Client
from Classes.employee import Employee
from Classes.model import Model
from Classes.pilot import Pilot
from Classes.reservation import Reservation
from Classes.staff import Staff
from Classes.user import User

from Openform import OpenForm

from tkinter import *

class Class_chooser:
    def __init__(self, filePath = './'):
    
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        # Set root title
        self.root.title('Class chooser')
        self.root.iconbitmap("Images/plane_takeoff_13263.ico")
            
        #root geometry
        self.app_width=850
        self.app_height=200
    
        #Find width and height screen's
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
    
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))  
        
        self.root.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        
        self.btn_user = Button(self.root, text='USER', command=call_user,bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_user.grid(row=0, column=0, padx = 20, pady = 20)
        
        self.btn_client = Button(self.root, text='CLIENT', command=call_client,bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_client.grid(row=0, column=1, padx = 20, pady = 20)
        
        self.btn_employee = Button(self.root, text='EMPLOYEE', command=call_employee, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_employee.grid(row=0, column=2, padx = 20, pady = 20)
        
        self.btn_staff = Button(self.root, text='STAFF', command=call_staff, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_staff.grid(row=0, column=3, padx = 20, pady = 20)
        
        self.btn_pilot = Button(self.root, text='PILOT', command=call_pilot, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_pilot.grid(row=1, column=0, padx = 20, pady = 20)
        
        self.btn_airplane = Button(self.root, text='AIRPLANE', command=call_airplane, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_airplane.grid(row=1, column=1, padx = 20, pady = 20)
        
        self.btn_model = Button(self.root, text='MODEL', command=call_model, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_model.grid(row=1, column=2, padx = 20, pady = 20)
        
        self.btn_reservation = Button(self.root, text='RESERVATION', command=call_reservation, bg='white',fg="black",font=("AIGDT",12),width=9)
        self.btn_reservation.grid(row=1, column=3, padx = 20, pady = 20)
        
       
        
        #read data files
        User.read('Data/')           
        Model.read('Data/')
        Airplane.read('Data/')
        Employee.read('Data/')
        Reservation.read('Data/')
        Pilot.read('Data/')
        Staff.read('Data/')
        Client.read('Data/')
        
        # loop until it is closed by the user
        self.root.mainloop()
        
def call_user():
    s1 = OpenForm(User, ['code','name','city','phone','NIF','dob','mail','senha','username','gender'], filePath='Data/')

def call_client():
    s2 = OpenForm(Client, ['code','name','city','phone','NIF','dob','mail','password','username','gender', 'payment card'], filePath='Data/')

def call_employee():
    s3 = OpenForm(Employee, ['code','name','city','phone','NIF','dob','mail','password','username','gender', 'salary', 'photo'], filePath='Data/')

def call_staff():
    s4 = OpenForm(Staff, ['code','name','city','phone','NIF','dob','mail','password','username','gender', 'salary', 'photo', 'role'], filePath='Data/')

def call_pilot():
    s5 = OpenForm(Pilot, ['code','name','city','phone','NIF','dob','mail','password','username','gender', 'salary', 'photo', 'airplanes', 'flight hours'], filePath='Data/')

def call_airplane():
    s6 = OpenForm(Airplane, ['model', 'capacity', 'autonomy', 'staff', 'cargo', 'price', 'image_path', 'code', 'dof'], filePath='Data/')

def call_model():
    s7 = OpenForm(Model, ['model','capacity','autonomy', 'staff', 'cargo', 'price', 'photo'], filePath='Data/')

def call_reservation():
    s8 = OpenForm(Reservation, ['code', 'initial date', 'final date', 'client', 'cargo', 'airplane', 'price'], filePath='Data/')



        
        