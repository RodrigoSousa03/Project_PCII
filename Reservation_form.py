# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:31:52 2021

@author: Asus-Pc
"""

from tkinter import *
from Classes.reservation import Reservation
from tkinter import ttk,filedialog
import tkinter.messagebox as MessageBox
from Classes.airplane import Airplane
import pandas as pd
import datetime

from tkcalendar import DateEntry
class form_reservation():
    def __init__(self,filePath='./'):
        
        Reservation.read('Data/')
        Airplane.read('Data/')
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        self.filePath = filePath
        
        self.classObj = Reservation
        self.classObj.read(self.filePath)
        
        self.list_airplanes=Airplane.lst
        
        
        
        # Set attribute names and labels
        obja = self.classObj.first()
        
        
        # Set root title
        self.root.title('Reservation')
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
        
           
        
        
        #buttons
        self.center=self.app_width/2
        # self.button_submit = Button(self.root,text="SIMULATE",  command=self.msg ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=500,y=400)
        self.button_cancel = Button(self.root,text="CANCEL",  command= lambda: self.button_cancel_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=730,y=400)
        
        
        #title
        self.title=Label(self.root, text="N E W  R E S E R V A T I O N", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=300,y=30)
        
        #labels and entries
        
        #Client
        self.clientlb=Label(self.root, text="C L I E N T  C O D E", fg="white",bg="#464646", font=("AMGDT",10))
        self.clientlb.place(x=50,y=170)
        self.clientIB=Entry(self.root, width=40)
        self.clientIB.place(x=90,y=220)
        
        
        #Initial date
        self.idate=Label(self.root, text="I N I T I A L  D A T E", fg="white",bg="#464646", font=("AMGDT",10))
        self.idate.place(x=480,y=170)
        self.idate=DateEntry(self.root,width=40,bg=" ", fg="", date_pattern='YY/mm/dd')
        self.idate.place(x=520,y=220)
        
        
        #Final date
        self.fdate=Label(self.root, text="F I N A L  D A T E", fg="white",bg="#464646", font=("AMGDT",10))
        self.fdate.place(x=880,y=170)
        self.fdate=DateEntry(self.root,width=40,bg=" ", fg="", date_pattern='YY/mm/dd')
        self.fdate.place(x=920,y=220)
        
        
        #Button check Availability
        self.button_availability= Button(self.root,text="AVAILABILITY",  command=self.availability ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12))
        self.button_availability.place(x=500,y=400)
        
        
        # Let the root wait for any events
        self.root.mainloop()

                
  
    
    
    #close root
    def button_cancel_click(self):
       self.root.destroy()
       
       
    
    #check available planes
    def availability(self):
        
            self.di=self.idate.get_date()
            
            self.init_temp=self.di.strftime('%Y-%m-%d')
            self.datelist1 = list(map(int, self.init_temp.split('-')))
            self.date_init =datetime.date(self.datelist1[0], self.datelist1[1], self.datelist1[2])
            
            self.df=self.fdate.get_date()
            
            self.final_temp=self.df.strftime('%Y-%m-%d')
            
            self.datelist2 = list(map(int, self.final_temp.split('-')))
            self.date_final =datetime.date(self.datelist2[0], self.datelist2[1], self.datelist2[2])
            
                
            self.lista_airplanes=Reservation.available_planes(self.classObj,self.date_init,self.date_final)
            print(self.lista_airplanes)
            
            if self.lista_airplanes==[]:
                MessageBox.showinfo("Not available", "No planes available, please choose another dates")
            
            else:
                
                self.codelb=Label(self.root, text="A I R P L A N E", fg="white",bg="#464646", font=("AMGDT",10))
                self.codelb.place(x=50,y=280)
                
        
                #combobox 
                self.combobox=ttk.Combobox(self.root,values=self.lista_airplanes)
                self.combobox.place(x=90,y=320)
                self.model=self.combobox.get()
                
                #destroys date entry and set label
                self.idate.destroy()
                self.fdate.destroy()
                self.button_availability.destroy()
                
                self.idate_L=Label(self.root,text=self.init_temp,width=40)
                self.idate_L.place(x=520,y=220)
                
                self.fdate_L=Label(self.root,text=self.final_temp,width=40)
                self.fdate_L.place(x=920,y=220)
                
                        
                
                #cargo
                self.cargolb=Label(self.root, text="C A R G O", fg="white",bg="#464646", font=("AMGDT",10))
                self.cargolb.place(x=480,y=280)
                self.cargoIB=Entry(self.root, width=40)
                self.cargoIB.place(x=520,y=320)
                
                
                #buttons
                self.button_submit = Button(self.root,text="SIMULATE",  command=self.msg ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=500,y=400)
                self.button_cancel = Button(self.root,text="CANCEL",  command= lambda: self.button_cancel_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=730,y=400)
                
                
                self.display_treeview()
                
       
    
       
       
        
   
       
    def msg(self):
       
        self.all=True
        
        self.set_background(self.clientIB)
        self.set_background(self.cargoIB)
           
            
        if  self.all==True:
            self.Show_window_info()
           
            
   
        
       
    #set border red        
    def set_background(self,button_name):
        data = button_name.get()
        if len(data) == 0:
            button_name.config({"highlightbackground": "red"},highlightthickness=2)
            self.all=False
        else:
            button_name.configure(highlightthickness=0)
            
    #treeview with airplanes csv       
    def display_treeview(self):
         self.my_frame=Frame(self.root)
         self.my_frame.pack(side=BOTTOM,pady=15,padx=15)
         
         self.tree_scrolly=Scrollbar(self.my_frame)
         self.tree_scrolly.pack(side=RIGHT,fill=Y)
         
         self.tree_scrollx=Scrollbar(self.my_frame,orient=HORIZONTAL)
         self.tree_scrollx.pack(side=BOTTOM,fill=X)
        
         self.my_tree=ttk.Treeview(self.my_frame,yscrollcommand=self.tree_scrolly.set)
         self.my_tree=ttk.Treeview(self.my_frame,xscrollcommand=self.tree_scrollx.set)
         
         self.df=pd.read_csv('Data/Airplane.csv',delimiter=";")
            
         self.my_tree["column"]=list(self.df.columns)
         self.my_tree["show"]="headings"
        
        #loop thru column list
        
         for column in self.my_tree["column"]:
             self.my_tree.heading(column, text=column)
        
         self.df_rows=self.df.to_numpy().tolist()
         for row in self.df_rows:
             self.my_tree.insert("","end",values=row)
        
         self.my_tree.pack()
         
         self.tree_scrolly.config(command=self.my_tree.yview)
         self.tree_scrollx.config(command=self.my_tree.xview)
         
         
    #window with reservation details    
    def Show_window_info(self):
        self.window = Toplevel()
        self.window.configure(bg='#464646')
        
        self.window.title('Reservation')
        self.window.iconbitmap("Images/plane_takeoff_13263.ico")
        
        #root geometry
        self.app_width=730
        self.app_height=730
    
        #Find width and height screen's
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()
    
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))        
        self.window.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        self.classObj = Airplane
        self.classObj.read(self.filePath)
        
        #creat code
        if Reservation.lst==[]:
            self.code=0
        else:
            self.code=int(Reservation.lst[-1])+1
            
        #calculate price    
        self.price=self.price_calc()
        
       
        self.title=Label(self.window, text="R E S E R V A T I O N", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=60,y=30)
        
        #creat reservation
        self.new_reservation= Reservation(self.code,self.init_temp,self.final_temp,self.clientIB.get(), self.cargoIB.get(),self.combobox.get(),self.price)
        
        
        #labels showing details
        self.coder=Label(self.window,text="RESERVATION CODE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=1,column=0,pady=(150,0))
        self.coder=Label(self.window,text=self.new_reservation.code,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=1,column=1,pady=(150,0))
        
        self.date_init=Label(self.window,text="INITIAL DATE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=2,column=0)
        self.date_init=Label(self.window,text=self.new_reservation.date_init,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=2,column=1)
        
        self.date_fin=Label(self.window,text="FINAL DATE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=3,column=0)
        self.date_fin=Label(self.window,text=self.new_reservation.date_final,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=3,column=1)
        
        self.client=Label(self.window,text="CODE CLIENT:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=4,column=0)
        self.client=Label(self.window,text=self.new_reservation.client,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=4,column=1)
        
        self.cargo=Label(self.window,text="CARGO:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=5,column=0)
        self.cargo=Label(self.window,text=self.new_reservation.cargo,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=5,column=1)
        
        self.airpl=Label(self.window,text="AIRPLANE CODE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=6,column=0)
        self.airp=Label(self.window,text=self.new_reservation.airplane,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=6,column=1)
        
        self.price=Label(self.window,text="PRICE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=7,column=0)
        self.price=Label(self.window,text=str(self.new_reservation.price)+ ' €',font=('AMGDT', 10),fg="white",bg="#464646").grid(row=7,column=1)
        
        self.staff=Label(self.window,text="STAFF:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=8,column=0)
        self.staff=Label(self.window,text=self.classObj.obj[self.new_reservation.airplane].staff,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=8,column=1)
        
        self.dof=Label(self.window,text="PLANE'S FABRICATION DATE:",font=('AMGDT', 10),fg="white",bg="#464646").grid(row=9,column=0)
        self.dof=Label(self.window,text=self.classObj.obj[self.new_reservation.airplane].dof,font=('AMGDT', 10),fg="white",bg="#464646").grid(row=9,column=1)
        
        
        #buttons
        self.confirmbt=Button(self.window,text="CONFIRM",  command=self.reservation_confirmation ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=200,y=450)
        self.cancelbt=Button(self.window,text="CANCEL",  command=lambda: self.button_cancel_click_window() ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=450,y=450)
        
        
        #price description
        self.info1lb = Label(self.window, text='THE PRICE IS CALCULATED IN THE FOLLOWING WAY:', fg = 'white', bg= '#464646', font=('AMGDT', 10))
        self.info1lb.place(x=50, y = 650)
        
        self.info2lb = Label(self.window, text='BASE PRICE * DAYS + CARGO SUPLEMENT (IF CARGO BIGGER THAN MAX CARGO *0.9)', fg = 'white', bg= '#464646', font=('AMGDT', 10))
        self.info2lb.place(x =50, y = 680)
        
        
        self.window.mainloop()
        
        
    def reservation_confirmation(self):
        
        #write reservation to csv
        self.new_reservation.write('Data/')
        MessageBox.showinfo("Successful reservation","Contact us in any case.")
        self.window.destroy()
        self.root.destroy()
        
    def price_calc(self):
        self.plane_code = self.combobox.get()
        self.plane = Airplane.obj[self.plane_code]
        self.base_price = int(self.plane.price)
        self.delta = self.date_final - self.date_init
        print(self.date_init)
        print(self.date_final)
        self.days = int(self.delta.days)
        self.price = self.base_price * self.days
        print(self.days)
        #standard price
        if self.days > 3 and self.days <= 7:        
            self.price += 400                       #number os days modifier
        if self.days > 7:
            self.price += 1000
        
        self.cargo = int(self.cargoIB.get())
        self.max_cargo = int(self.plane.cargo)
        if self.cargo > self.max_cargo * 0.9:
            self.price += 100                       #cargo price modifier
            
        print(self.price)
        return self.price
    
    def button_cancel_click_window(self):
       self.window.destroy()
        

#form_reservation(filePath='Data/')           
