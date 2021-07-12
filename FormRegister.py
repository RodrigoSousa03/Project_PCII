# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:23:02 2021

@author: Asus-Pc
"""

from tkinter import *
from random import randint
from tkcalendar import DateEntry

from Classes.user import User
from Classes.client import Client
from Classes.employee import Employee
from Classes.pilot import Pilot
from Classes.staff import Staff
from Classes.model import Model
from tkinter import ttk
from tkinter import filedialog

import tkinter.messagebox as MessageBox

class FormRegister:
    def __init__(self,status, filePath = './'):
        
        User.read('Data/')
        Client.read('Data/')
        Employee.read('Data/')
        Staff.read('Data/')
        Pilot.read('Data/')
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        self.filePath = filePath
        
        self.classObj = User
        self.classObj.read(self.filePath)
       
        # Set root title
        self.root.title('REGISTER')
        self.root.iconbitmap("Images/plane_takeoff_13263.ico")
        
        #root geometry
        self.app_width=1300
        self.app_height=730
    
        #Find width and height screen's
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
        
        #place root in the middle of the screen
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))        
        self.root.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        #buttons
        self.center=self.app_width/2
        self.button_submit = Button(self.root,text="SUBMIT",  command=lambda:self.msg(status) ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=500,y=650)
        self.button_cancel = Button(self.root,text="CANCEL",  command= lambda: self.button_cancel_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=730,y=650)
        
        
        #title
        self.title=Label(self.root, text="C R E A T   A C C O U N T", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=300,y=30)
        
        
        #labels and entries
        self.namelb=Label(self.root, text="N A M E", fg="white",bg="#464646", font=("AMGDT",10))
        self.namelb.place(x=50,y=170)
        self.nameIB=Entry(self.root, width=40)
        self.nameIB.place(x=90,y=220)
        
        
        #gender combobox
        self.genderlb=Label(self.root, text="G E N D E R", fg="white",bg="#464646", font=("AMGDT",10))
        self.genderlb.place(x=50,y=480)
        self.genderlst=["male","female","other"]
        self.combobox_gender=ttk.Combobox(self.root,values=self.genderlst)
        self.combobox_gender.place(x=90,y=520)
       
        
        
        #Date of birth
        self.dob=Label(self.root, text="D A T E  O F  B I R T H", fg="white",bg="#464646", font=("AMGDT",10))
        self.dob.place(x=50,y=380)
        self.dob=DateEntry(self.root,width=40,bg=" ", fg="", date_pattern='YY/mm/dd')
        self.dob.place(x=90,y=420)
        
        
        #username
        self.unamelb=Label(self.root, text="U S E R N A M E", fg="white",bg="#464646", font=("AMGDT",10))
        self.unamelb.place(x=50,y=280)
        self.unameIB=Entry(self.root, width=40)
        self.unameIB.place(x=90,y=320)
        
        
        #phone number
        self.phonelb=Label(self.root, text="P H O N E  N U M B E R", fg="white",bg="#464646", font=("AMGDT",10))
        self.phonelb.place(x=480,y=170)
        self.phoneIB=Entry(self.root, width=40)
        self.phoneIB.place(x=520,y=220)
        
        #email address
        self.emaillb=Label(self.root, text="E M A I L  A D D R E S S", fg="white",bg="#464646", font=("AMGDT",10))
        self.emaillb.place(x=480,y=280)
        self.emailIB=Entry(self.root, width=40)
        self.emailIB.place(x=520,y=320)
        
        
        #NIF
        self.niflb=Label(self.root, text="N I F", fg="white",bg="#464646", font=("AMGDT",10))
        self.niflb.place(x=480,y=380)
        self.nifIB=Entry(self.root, width=40)
        self.nifIB.place(x=520,y=420)
        
        #city
        self.citylb=Label(self.root, text="C I T Y", fg="white",bg="#464646", font=("AMGDT",10))
        self.citylb.place(x=480,y=480)
        self.cityIB=Entry(self.root, width=40)
        self.cityIB.place(x=520,y=520)
        
        
        #password
        self.pwlb=Label(self.root, text="P A S S W O R D", fg="white",bg="#464646", font=("AMGDT",10))
        self.pwlb.place(x=880,y=170)
        self.pwIB=Entry(self.root, width=40)
        self.pwIB.place(x=920,y=220)
        self.pwIB.insert(0,"Minimum of 8 characters")
        
        
        #button password sugestion
        self.sugIB=Button(self.root,text="S U G E S T I O N",  command=self.choose_pw,bg='#b6b6b6',padx=15,pady=7,fg="black")
        self.sugIB.place(x=1100,y=170)
        
        
        #confirm password
        self.pwagainlb=Label(self.root, text="C O N F I R M  P A S S W O R D", fg="white",bg="#464646", font=("AMGDT",10))
        self.pwagainlb.place(x=880,y=280)
        self.pwagainIB=Entry(self.root, width=40)
        self.pwagainIB.place(x=920,y=320)
        
        
        
        
        if status=="Client":
            
            #payment card
            self.paymentlb=Label(self.root, text="P A Y M E N T  C A R D", fg="white",bg="#464646", font=("AMGDT",10))
            self.paymentlb.place(x=880,y=380)
            self.paymentIB=Entry(self.root, width=40)
            self.paymentIB.place(x=920,y=420)
            
        
        else:
            #employee
            
             #role
             self.rolelb=Label(self.root, text="R O L E", fg="white",bg="#464646", font=("AMGDT",10))
             self.rolelb.place(x=880,y=380)
             self.combobox=ttk.Combobox(self.root,values=["pilot","flight attendand","administrator","security","cleaner"])
             self.combobox.place(x=920,y=420)
             
             #photo path
             self.imagelb=Label(self.root, text="I M A G E", fg="white",bg="#464646", font=("AMGDT",10))
             self.imagelb.place(x=880,y=480)
             self.imageIB=Entry(self.root, width=40)
             self.imageIB.place(x=920,y=520)
             
             
             #button to save photo 
             self.openBt=Button(self.root,text="S E L E C T ",  command=self.add_path,bg='#b6b6b6',padx=15,pady=7,fg="black")
             self.openBt.place(x=1100,y=480)
        
             
            
        
        #self.registration_Status = "Not Registed"
        
        # Let the root wait for any events
        self.root.mainloop()

   
 
  
    
    #destroy root 
    def button_cancel_click(self):
       self.login_Status = "cancel"
       self.root.destroy()
       
     
    #generate password    
    def generate_password(self):
        self.my_password=""
    
        for i in range (8):
            self.char=chr(randint(33,126))
            self.my_password=self.my_password+self.char
            print( self.my_password)
        return self.my_password
    
    
    
    #insert password entry
    def choose_pw(self):
        self.pwIB.delete(0,END)
        self.pw=self.generate_password()
        self.pwIB.insert(0,self.pw)
        
        
        
        
    #pathimage and save photo    
    def open_image(self):

        self.pathimage= filedialog.asksaveasfilename()
        
        return self.pathimage
    
    
    
    
    #add path to entry    
    def add_path(self):
        self.imageIB.delete(0,END)
        self.pathimage=self.open_image()
        self.imageIB.insert(0,self.pathimage)
        
        
        
        
    #verify entrys
    def msg(self,status):
       
        self.all=True      #to check if any camp is empty
        
       
        self.set_background(self.nameIB)
        self.set_background(self.unameIB)
        self.set_background(self.phoneIB)
        self.set_background(self.emailIB)
        self.set_background(self.nifIB)
        self.set_background(self.cityIB)
        self.set_background(self.pwIB)
        
        
        # if self.combobox_gender=="":
        #     self.combobox_gender.config({"highlightbackground": "red"},highlightthickness=2)
        #     self.all=False
        
        # password=self.pwIB.get()
        # if Customer.password_check(password)==False:
        #     self.pwIB.config({"highlightbackground": "red"},highlightthickness=2)
        #     MessageBox.showinfo("Password",message=("Phone number should only have numbers"))
        #     self.all=False
            
       
        if self.pwagainIB.get()!=self.pwIB.get():
            #self.warninglb=Label(self.root, text="", fg="white",bg="#464646", font=("AMGDT",10)).place(x=12,y=13)
            self.pwagainIB.config({"highlightbackground": "red"},highlightthickness=2)
            self.all=False
            
            
        phone=self.phoneIB.get()
        #check if phone number is only numbers
        if User.phone_check(phone)==False:
            self.phoneIB.config({"highlightbackground": "red"},highlightthickness=2)
            MessageBox.showinfo("Phone number",message=("Phone number should only have numbers"))
            self.all=False
            
            
        if  self.all==True:
            self.save(status)
            
            
           
    #creats object and writes to csv      
    def save(self,status):
        
        self.db=self.dob.get_date()
        self.d=self.db.strftime('%Y/%m/%d')
        
        
        #defines user code
        if User.lst==[]:
            self.code=0
        else:
            self.code=int(User.lst[-1])+1
            
            
        #creat object and add to csv
        #creat user and write
        self.new_user= User(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender.get())
        self.new_user.write(self.filePath)
        
        
        #creat client and write
        if status=="Client":
            self.new_client=Client(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender.get(),self.paymentIB.get())
            self.new_client.write(self.filePath)
            
            MessageBox.showinfo("regist successfully")
            self.root.destroy()
            
        #creat employee and write
        if status=="Employee":
            
            self.classemp = Employee
            self.classemp.read(self.filePath)
            
            self.new_employee=Employee(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender.get(),0,self.imageIB.get())
            self.new_employee.write(self.filePath)
            
            
            
            if self.combobox.get()=="pilot":
                
               
                
                self.att=(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender.get(),self.nifIB.get())
                self.pilot_airplanes(self.att)
                
                
            #creat staff and write    
            else:
                self.new_staff=Staff(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender.get(),0,self.imageIB.get(),self.combobox.get())
                self.new_staff.write(self.filePath)
               
        
                MessageBox.showinfo("regist successfully")
                self.root.destroy()
        
       
            
    def set_background(self,button_name):
        data = button_name.get()
        if len(data) == 0:
            button_name.config({"highlightbackground": "red"},highlightthickness=2)
            self.all=False
        else:
            button_name.configure(highlightthickness=0)
            
            
            
    #listbox to choose pilot plane licenses        
    def pilot_airplanes(self,atti):
        
        Model.read('Data/')
        
        self.wi = Tk()
        self.wi.configure(bg='#464646')
        self.wi.title('PILOT LICENSES')
        self.wi.iconbitmap("Images/plane_takeoff_13263.ico")
        
        #root geometry
        self.app_width=500
        self.app_height=500
    
        #Find width and height screen's
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
    
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))        
        self.wi.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        #Labels
        self.title=Label(self.wi, text="L I C E N S E S", fg="white",bg="#464646", font=("AMGDT",20))
        self.title.place(x=100,y=20)
        
        #Label
        self.info=Label(self.wi, text="Please select the licenses",fg="white",bg="#464646")
        self.info.place(x=100,y=100)
        
        #variable list
        self.lista_models=Model.lst.copy()
        l=len(self.lista_models)
        
        #listbox
        self.listbox=Listbox(self.wi,selectmode=MULTIPLE) 
        
        for i in range(l):
            self.listbox.insert(END,self.lista_models[i])
            
        self.listbox.place(x=180,y=130)
       
        
        #button submit licenses
        self.button_submit=Button(self.wi,text="S U B M I T ",  command=self.get_licenses,bg='#b6b6b6',padx=15,pady=7,fg="black")
        self.button_submit.place(x=200,y=400)
        self.wi.mainloop()
        
        
        
    # return self.lista and creat Pilot
    def get_licenses(self):
        self.selected_airp=[]
        self.selected_indices = self.listbox.curselection()
        
        #get selected licenses
        for i in self.selected_indices:
            self.selected_airp.append(self.listbox.get(i))
  
        #creat and write Pilot
        self.new_pilot=Pilot(self.code,self.nameIB.get(),self.cityIB.get(),self.phoneIB.get(),self.nifIB.get(), self.db, self.emailIB.get(),self.pwIB.get(),self.unameIB.get(),self.combobox_gender,0,self.imageIB.get(),self.selected_airp,0)
        self.new_pilot.write(self.filePath)
        
        #destroy window with listbox
        self.wi.destroy()
        MessageBox.showinfo("regist successfully","Successfully Registered")
        
        #destroy resgister window
        self.root.destroy()
       
    
    
    
        
        

            
   
        
        
        
            
                   
                   
       