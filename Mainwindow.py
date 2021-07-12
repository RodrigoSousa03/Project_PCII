# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:12:09 2021

@author: Asus-Pc
"""

from tkinter import *
from PIL import Image, ImageTk

from FormRegister import FormRegister
from DisplayFiles import exceldisplay
from Addplaneform import FormNewAirplane
from Reservation_form import form_reservation
from Stats import Statistics
from Tabs import Tabs
from class_choose import Class_chooser
from ProfilForm import profile_form

from Classes.client import Client
from Classes.employee import Employee
from Classes.user import User


class MainWindow:
    def __init__(self,code, filePath = './'):
        
        
        self.status=self.get_status(code)
        
        Client.read('Data/')
        Employee.read('Data/')
        
        self.root = Toplevel()
        self.root.configure(bg='#464646')
        
        
        
        self.classObj = User
        self.classObj.read(filePath)
        # Set attribute names and labels
        obj = self.classObj.first()
        
        
      
        # Set root title
        self.root.title('Main Window')
        self.root.iconbitmap("Images/plane_takeoff_13263.ico")
        
        #root geometry
        self.app_width=1300
        self.app_height=730
    
        #Find width and height screen's
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
    
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))        
        self.root.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        #label avilux
        self.aviluxlb=Label(self.root, text="A V I L U X", fg="white",bg="#464646", font=("AMGDT",50)).place(x=400,y=80)
        
        #new reservation button
        self.center=self.app_width/2
        self.button_newreservation = Button(self.root,text="NEW RESERVATION",  command=open_form_reservation ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=530,y=250)
        
        #name
        self.namet=self.classObj.obj[code].name
        self.NAME=self.namet.upper()
        print(self.NAME)
        
        #label to set lateral color
        self.profilelb=Label(self.root,bg="#999999", font=("AMGDT",10),height=730,width=50).place(x=1130,y=0)
        
        #label name
        self.profilebt=Button(self.root,text="PROFILE",command= lambda:open_form_profile(code),fg="white",bg="#464646",bd=0,font=("AMGDT",10,UNDERLINE)).place(x=1180,y=220)
        self.name=Label(self.root,text="HI, "+self.NAME,bg="#999999",fg="black", font=("AIGDT",10)).place(x=1170,y=180)
        
        
        #profile general pic
        self.bg=Image.open("Images/profile.jpg")
        self.bg=ImageTk.PhotoImage(self.bg)
        self.profpic=Label(self.root,image=self.bg,bd=0)
        self.profpic.place(x=1140,y=20)
        
        
        #buttons to employee
        if self.status=="Employee":
       
             self.button_newclient = Button(self.root,text="NEW CLIENT",  command=open_form_regist_client ,bg='white',padx=30,pady=8,fg="black",font=("AIGDT",12)).place(x=330,y=360)
             self.button_newplane = Button(self.root,text="NEW PLANE",  command=open_form_airplane,bg='white',padx=30,pady=8,fg="black",font=("AIGDT",12)).place(x=550,y=360)
             self.button_statistics = Button(self.root,text="STATISTICS",  command=open_stats ,bg='white',padx=40,pady=8,fg="black",font=("AIGDT",12)).place(x=760,y=360)
             self.button_employee = Button(self.root,text="NEW EMPLOYEE",  command= open_form_regist_employee,bg='white',padx=16,pady=8,fg="black",font=("AIGDT",12)).place(x=330,y=460)
             self.button_staff = Button(self.root,text="INFO",  command=open_form_class_choose,bg='white',padx=62,pady=8,fg="black",font=("AIGDT",12)).place(x=550,y=460)
             self.button_clients = Button(self.root,text="FILES",  command= open_form_tabs,bg='white',padx=62,pady=8,fg="black",font=("AIGDT",12)).place(x=760,y=460)
        
        self.root.mainloop()
        
        
    #returns client or employee
    def get_status(self,code):
        self.classClients = Client
        self.classClients.read('Data/')
        self.status="Employee"
        for client in self.classClients.lst:
            if client==code:
                self.status="Client"
        return self.status
    
    
    #returns upper name
    def upper_name(self,name):
        self.Name=""
        for letter in name:
            self.Name
    
    

#calls other forms

def open_form_regist_client():
    s1=FormRegister('Client', filePath = 'Data/')
    
def open_form_regist_employee():
    s2=FormRegister('Employee',filePath = 'Data/')
    
def open_form_excel_clients():
    s3=exceldisplay("Data/user.csv","Clients",40,90)

def open_form_tabs():
    s4=Tabs()

def open_form_class_choose():
    s5=Class_chooser()
    
def open_form_airplane():
    s6=FormNewAirplane(filePath ='Data/')
    
def open_stats():
    s7=Statistics(filePath ='Data/')
    
def open_form_reservation():
    s8=form_reservation(filePath ='Data/')
    
def open_form_profile(code):
    s9=profile_form(code)