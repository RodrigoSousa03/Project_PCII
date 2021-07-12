# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:50:44 2021

@author: Asus-Pc
"""
from tkinter import *
from Classes.airplane import Airplane
from Classes.model import Model
from tkinter import ttk,filedialog
import tkinter.messagebox as MessageBox

from tkcalendar import DateEntry

class FormNewAirplane:
    def __init__(self,filePath = './'):
        
        Airplane.read('Data/')
        Model.read('Data/')
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        self.filePath = filePath
        
        self.classObj = Airplane
        self.classObj.read(self.filePath)
        self.list=Model.lst
        
        
        self.classmodel = Model
        self.classmodel.read(self.filePath)
        # self.classmodel.remove('')
        # Set attribute names and labels
        obj = self.classmodel.first()
        print(self.classmodel.obj)
        #self.att = list(obj.__dict__.keys())
        # Set attribute names and labels
        obja = self.classObj.first()
        # self.att = list(obj.__dict__.keys())
        
        
        # Set root title
        self.root.title('Airplane')
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
        
        #options combobox
        # self.classObj.remove(".!entry7")
        self.options=self.list.copy()
        print(self.options)
        self.options.append("New")
        
        
        
       #buttons
        self.center=self.app_width/2
        self.button_submit = Button(self.root,text="SUBMIT",  command=self.msg ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=500,y=650)
        self.button_cancel = Button(self.root,text="CANCEL",  command= lambda: self.button_cancel_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=730,y=650)
        
        
        #title
        self.title=Label(self.root, text="N E W  A I R P L A N E", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=300,y=30)
        
        #labels and entries
        self.modellb=Label(self.root, text="M O D E L", fg="white",bg="#464646", font=("AMGDT",10))
        self.modellb.place(x=50,y=170)
        
        
        #combobox 
        self.combobox=ttk.Combobox(self.root,values=self.options)
        self.combobox.place(x=90,y=220)
        self.model=self.combobox.get()
        print(self.model, 'jhjh')
        self.combobox.bind("<<ComboboxSelected>>", self.fillcamps)
        
        
        
        
        #Date of Fabrication
        self.dof=Label(self.root, text="D A T E  O F  F A B R I C A T I O N", fg="white",bg="#464646", font=("AMGDT",10))
        self.dof.place(x=50,y=280)
        self.dof=DateEntry(self.root,width=40,bg=" ", fg="", date_pattern='dd/mm/YY')
        self.dof.place(x=90,y=320)
        
        
        # #Client code
        # self.clientlb=Label(self.root, text="C L I E N T  C O D E", fg="white",bg="#464646", font=("AMGDT",10))
        # self.clientlb.place(x=50,y=280)
        # self.clientIB=Entry(self.root, width=40)
        # self.clientIB.place(x=90,y=320)
        
        
        #Capacity
        self.caplb=Label(self.root, text="C A P A C I T Y ", fg="white",bg="#464646", font=("AMGDT",10))
        self.caplb.place(x=50,y=380)
        self.capIB=Entry(self.root, width=40)
        self.capIB.place(x=90,y=420)
        
        #Autonomy
        self.autlb=Label(self.root, text="A U T O N O M Y ", fg="white",bg="#464646", font=("AMGDT",10))
        self.autlb.place(x=480,y=170)
        self.autIB=Entry(self.root, width=40)
        self.autIB.place(x=520,y=220)
        
        #cargo
        self.cargolb=Label(self.root, text="C A R G O", fg="white",bg="#464646", font=("AMGDT",10))
        self.cargolb.place(x=480,y=280)
        self.cargoIB=Entry(self.root, width=40)
        self.cargoIB.place(x=520,y=320)
        
        
        #Price
        self.pricelb=Label(self.root, text="P R I C E", fg="white",bg="#464646", font=("AMGDT",10))
        self.pricelb.place(x=480,y=380)
        self.priceIB=Entry(self.root, width=40)
        self.priceIB.place(x=520,y=420)
        
        #Image path
        self.imagelb=Label(self.root, text="I M A G E", fg="white",bg="#464646", font=("AMGDT",10))
        self.imagelb.place(x=880,y=170)
        self.imageIB=Entry(self.root, width=40)
        self.imageIB.place(x=920,y=220)
        
        self.openBt=Button(self.root,text="S E L E C T ",  command=self.add_path,bg='#b6b6b6',padx=15,pady=7,fg="black")
        self.openBt.place(x=1100,y=170)
        
        
        #staff
        self.stafflb=Label(self.root, text="STAFF", fg="white",bg="#464646", font=("AMGDT",10))
        self.stafflb.place(x=880,y=280)
        self.staffIB=Entry(self.root, width=40)
        self.staffIB.place(x=920,y=320)
        
         
       
       
        
    
        
        self.registration_Status = "Not Registed"
        
        # Let the root wait for any events
        self.root.mainloop()

    def fillcamps(self,event):
        print(self.combobox.get(), "jskd",self.list)
        if self.combobox.get()in self.list:
            self.model=self.combobox.get()
            
        
           
            self.capIB.delete(0,END)
            self.capIB.insert(0, self.classmodel.obj[self.model].capacity)
            
            self.autIB.delete(0,END)
            self.autIB.insert(0, self.classmodel.obj[self.model].autonomy)
            
            self.cargoIB.delete(0,END)
            self.cargoIB.insert(0,self.classmodel.obj[self.model].cargo)
            
            self.priceIB.delete(0,END)
            self.priceIB.insert(0,self.classmodel.obj[self.model].price)
            
            self.imageIB.delete(0,END)
            self.imageIB.insert(0,self.classmodel.obj[self.model].image_path)
            
            self.staffIB.delete(0,END)
            self.staffIB.insert(0, self.classmodel.obj[self.model].staff)
        
        else:
            self.modelIB=Entry(self.root, width=40)
            self.modelIB.place(x=90,y=240)
            
  
    
    
    def button_cancel_click(self):
       self.login_Status = "cancel"
       self.root.destroy()
       
    def open_image(self):

        self.pathimage= filedialog.asksaveasfilename()
        
        return self.pathimage
        
    def add_path(self):
        self.imageIB.delete(0,END)
        self.pathimage=self.open_image()
        self.imageIB.insert(0,self.pathimage)
    
        
   
       
    def msg(self):
       
        self.all=True
        
        try:
            self.set_background(self.modelIB)
            self.set_background(self.capIB)
            self.set_background(self.cargoIB)
            self.set_background(self.priceIB)
            self.set_background(self.imageIB)
            self.set_background(self.staffIB)
        except:
            self.set_background(self.capIB)
            self.set_background(self.cargoIB)
            self.set_background(self.priceIB)
            self.set_background(self.imageIB)
            self.set_background(self.staffIB)
            
        
            
            
        if  self.all==True:
            self.save()
           
            
    def save(self):
        self.db=self.dof.get_date()
        self.d=self.db.strftime('%Y-%m-%d')
        if Airplane.lst==[]:
            self.code=0
        else:
            self.code=int(Airplane.lst[-1])+1
            
            
        #creat object and add to csv
        # Airplane.read('Data/')
        if self.combobox.get()in self.list:
            self.new_airplane= Airplane(self.combobox.get(),self.capIB.get(),self.autIB.get(),self.staffIB.get(), self.cargoIB.get(), self.priceIB.get(),self.imageIB.get(), self.code,self.d)
            self.new_airplane.write(self.filePath)
        else:
            self.new_airplane= Airplane(self.modelIB.get(),self.capIB.get(),self.autIB.get(),self.staffIB.get(), self.cargoIB.get(), self.priceIB.get(),self.imageIB.get(), self.code,self.d)
            self.new_airplane.write(self.filePath)
            self.new_model= Model(self.modelIB.get(),self.capIB.get(),self.autIB.get(),self.staffIB.get(), self.cargoIB.get(), self.priceIB.get(),self.imageIB.get())
            self.new_model.write(self.filePath)
            
        
        MessageBox.showinfo("regist successfully")
        self.root.destroy()
        
       
            
    def set_background(self,button_name):
        data = button_name.get()
        if len(data) == 0:
            button_name.config({"highlightbackground": "red"},highlightthickness=2)
            self.all=False
        else:
            button_name.configure(highlightthickness=0)
            
#FormNewAirplane('Data/')           

