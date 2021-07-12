# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:01:46 2021

@author: julia
"""

from tkinter import * 
from Classes.user import User
from Classes.employee import Employee
from Classes.client import Client
from Classes.pilot import Pilot
from Classes.staff import Staff
from Classes.model import Model
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import filedialog



class profile_form():
    
    def __init__(self,code,filePath='./'):
        self.filePath = filePath
        
        User.read('Data/')
        Client.read('Data/')
        Employee.read('Data/')
        Staff.read('Data/')
        Pilot.read('Data/')
        
        self.status=self.get_status(code)
        
        print(self.status)
        
        self.root = Toplevel()
        self.root.configure(bg='#464646')
        
        #button
        self.button_edit = Button(self.root,text="EDIT",  command= self.edit,bg='white',padx=10,pady=8,fg="black",font=("AIGDT",10))
        self.button_edit.place(x=1100,y=370)
        
        # Set root title
        self.root.title('Profile')
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


        #title
        self.title=Label(self.root, text="P R O F I L E", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=300,y=30)
        
        
        #labels and entries
        self.namelb=Label(self.root, text="N A M E", fg="white",bg="#464646", font=("AMGDT",10))
        self.namelb.place(x=50,y=150)
        self.namelb2=Label(self.root,text= User.obj[code].name,bg="#464646",fg="white")
        self.namelb2.place(x=50,y=200)
        # self.nameIB=Entry(self.root, width=40)
        # self.nameIB.insert (0, User.obj[code].name)
        # self.nameIB.place(x=90,y=220)
        
        
        #Date of birth
        self.dob=Label(self.root, text="D A T E  O F  B I R T H", fg="white",bg="#464646", font=("AMGDT",10))
        self.dob.place(x=50,y=250)
        self.dob=Label(self.root,bg="#464646", fg="white",text=User.obj[code].dob)
        self.dob.place(x=50,y=300)
        
        
        #username
        self.usernamelb=Label(self.root, text="U S E R N A M E", fg="white",bg="#464646", font=("AMGDT",10))
        self.usernamelb.place(x=50,y=350)
        self.usernamelb2=Label(self.root,text= User.obj[code].username,bg="#464646",fg="white")
        self.usernamelb2.place(x=50,y=400)
        # sel
        
          #phone number
        self.phonelb=Label(self.root, text="P H O N E  N U M B E R", fg="white",bg="#464646", font=("AMGDT",10))
        self.phonelb.place(x=50,y=450)
        self.phonelb2=Label(self.root,text= User.obj[code].phone,bg="#464646",fg="white")
        self.phonelb2.place(x=50,y=500)
       
        
        
        #email city
        self.maillb=Label(self.root, text="E M A I L  A D D R E S S", fg="white",bg="#464646", font=("AMGDT",10))
        self.maillb.place(x=500,y=150)
        self.maillb2=Label(self.root,text= User.obj[code].mail,bg="#464646",fg="white")
        self.maillb2.place(x=500,y=200)
       
        
          #NIF
        self.niflb=Label(self.root, text="N I F", fg="white",bg="#464646", font=("AMGDT",10))
        self.niflb.place(x=500,y=250)
        self.niflb1=Label(self.root, text= User.obj[code].NIF, fg="white",bg="#464646")
        self.niflb1.place(x=500,y=300)
        
          #city
        self.citylb=Label(self.root, text="A D D R E S S", fg="white",bg="#464646", font=("AMGDT",10))
        self.citylb.place(x=500,y=350)
        self.citylb2=Label(self.root,text= User.obj[code].city,bg="#464646",fg="white")
        self.citylb2.place(x=500,y=400)
       
        
        self.imagemlb= Label(self.root, text="I M A G E", fg="white",bg="#464646", font=("AMGDT",10))
        self.imagemlb.place(x=1000,y=30)
        
        
        try:
            self.bg=Image.open(Employee.obj[code].photo)
            self.bg = self.bg.resize((1000, 90), Image.ANTIALIAS)
            self.bg=ImageTk.PhotoImage(self.bg)
            self.profpic=Label(self.root,image=self.bg,bd=0)
            self.profpic.place(x=1000,y=90)
        except:
            self.bg=Image.open("Images/profile.jpg")
            self.bg=ImageTk.PhotoImage(self.bg)
            self.profpic=Label(self.root,image=self.bg,bd=0)
            self.profpic.place(x=1000,y=70)
            
        
        if self.status=="Client":
              self.paymentlb=Label(self.root, text="P A Y M E N T  C A R D", fg="white",bg="#464646", font=("AMGDT",10))
              self.paymentlb.place(x=500,y=450)
              self.paymentlb2=Label(self.root,text= Client.obj[code].payment_card,bg="#464646",fg="white")
              self.paymentlb2.place(x=500,y=500)
             
              
            
        else: 
            
              self.salarylb=Label(self.root, text="S A L A R Y", fg="white",bg="#464646", font=("AMGDT",10))
              self.salarylb.place(x=500,y=450)
              self.salarylb2=Label(self.root, text= Employee.obj[code].salary, fg="white",bg="#464646", font=("AMGDT",10))
              self.salarylb2.place(x=500,y=500)
              
        
        
              if self.status=="Pilot":
             
                  self.airplaneslb =Label(self.root, text="A I R  P L A N E S", fg="white",bg="#464646", font=("AMGDT",10))
                  self.airplaneslb.place(x=500,y=550)
                  self.airplanelb2=Label(self.root,text= Pilot.obj[code].airplanes,bg="#464646",fg="white")
                  self.airplanelb2.place(x=500, y=600)
                  
                
                #flight_hours
                  self.flight_hourslb =Label(self.root, text="F L I G H T  H O U R S", fg="white",bg="#464646", font=("AMGDT",10))
                  self.flight_hourslb.place(x=500,y=650)
                  self.fight_hourslb2=Label(self.root,text= Pilot.obj[code].flight_hours,bg="#464646",fg="white") 
                  self.fight_hourslb2.place(x=500,y=700)
                  
                
              else :
                  self.rolelb =Label(self.root, text="R O L E", fg="white",bg="#464646", font=("AMGDT",10))
                  self.rolelb.place(x=500,y=550)
                  self.rolelb2=Label(self.root,text= Staff.obj[code].role,bg="#464646",fg="white")
                  self.rolelb2.place(x=500,y=600)
                  
        self.root.mainloop()
        
    def get_status(self,code):
        self.classClients = Client
        self.classClients.read('Data/')
        self.classtaff =Staff 
        self.classtaff.read('Data/')
        self.classPilot=Pilot
        self.classPilot.read('Data/')
        
        for pilot in self.classPilot.lst:
            if pilot==code:
                self.status="Pilot"
        
        for client in self.classClients.lst:
            if client==code:
                self.status="Client"
            
        for staff in self.classtaff.lst:
            if staff==code:
                self.status="Staff"
                
        return self.status
               
    def open_image(self):

        self.pathimage= filedialog.asksaveasfilename()
        
        
        return self.pathimage
    
    def add_path(self):
        #self.imageIB.delete(0,END)
        self.pathimage=self.open_image()
        self.entry_image =Entry(self.root, width=40)
        self.entry_image.place(x=850,y=50)
        self.entry_image.insert(0,self.pathimage)
        
    def edit(self):
        
        self.button_edit.destroy()
        self.button_confirm=self.button_edit = Button(self.root,text="SAVE",  command="",bg='white',padx=10,pady=8,fg="black",font=("AIGDT",10)).place(x=1100,y=470)
        self.namelb2.destroy()
        self.nameIB=Entry(self.root, width=40)
        self.nameIB.place(x=50,y=200)
        
        self.usernamelb2.destroy()
        self.usernameIB=Entry(self.root, width=40)
        self.usernameIB.place(x=50,y=400)
        
        self.phonelb2.destroy()
        self.phoneIB=Entry(self.root, width=40)
        self.phoneIB.place(x=50,y=500)
        
        self.maillb2.destroy()
        self.mailIB=Entry(self.root, width=40)
        self.mailIB.place(x=500,y=200)
        
        self.citylb2.destroy()
        self.cityIB=Entry(self.root, width=40)
        self.cityIB.place(x=500,y=400)
        
        if self.status=="Client":
            self.paymentlb2.delete()
            self.paymentIB=Entry(self.root, width=40)
            self.paymentIB.place(x=500,y=500)
            
        else:
            self.button_select = Button(self.root,text="SELECT IMAGE",  command= self.add_path,bg='white',padx=10,pady=8,fg="black",font=("AIGDT",10)).place(x=1000,y=300)
            self.profpic.destroy()
            
            if self.status=="Pilot":
                self.airplanelb2.destroy()
                self.airbutton=Button(self.root,text="LICENCES",  command= self.pilot_airplanes,bg='white',padx=10,pady=8,fg="black",font=("AIGDT",10)).place(x=900
                                                                                                                                                              ,y=470)
                self.airplanesIB =Entry(self.root, width=40)
                self.airplanesIB.place(x=500, y=600)
                
                # self.flight_hourslb2.destroy()
                # self.flight_hoursIB =Entry(self.root, width=40)
                # self.flight_hoursIB.place(x=500, y=650)
            else:
                self.rolelb2.destroy()
                self.roleIB =Entry(self.root, width=40)
                self.roleIB.place(x=500, y=600)
            
            
    def pilot_airplanes(self):
        
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
        self.title.place(relx=0.5, rely=0.05, anchor=CENTER)
        
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
            
        self.listbox.place(x=120,y=120)
        
        self.button_submit=Button(self.wi,text="S U B M I T ",  command=self.get_licenses,bg='#b6b6b6',padx=15,pady=7,fg="black")
        self.button_submit.place(x=130,y=300)
        self.wi.mainloop()
        
        
    # def save (self)
    
    
    def get_licenses(self):
        self.selected_airp=[]
        self.selected_indices = self.listbox.curselection()
        print(self.selected_indices)
        # get selected items
        for i in self.selected_indices:
            self.selected_airp.append(self.listbox.get(i))
        print(self.selected_airp)
        
        self.airplanesIB =Label(self.root, width=40,text=self.selected_airp)
        self.airplanesIB.place(x=150, y=550)
        
        # l=len(self.selected_airp)
        # for licence in range(l):
            
        
        self.wi.destroy()
        
#profile_form("14",filePath = "Data/")