# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:51:43 2021

@author: User
"""

from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#thinguys to graph stuff
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from tkinter import ttk,filedialog

from Classes.airplane import Airplane
from Classes.client import Client
from Classes.employee import Employee
from Classes.model import Model
from Classes.pilot import Pilot
from Classes.reservation import Reservation
from Classes.staff import Staff 
from Classes.user import User


class Statistics:
    def __init__(self, filePath = './'):
        
        #read data files
        User.read('Data/')           
        Model.read('Data/')
        Airplane.read('Data/')
        Employee.read('Data/')
        Reservation.read('Data/')
        Pilot.read('Data/')
        Staff.read('Data/')
        Client.read('Data/')
        
        #standard beggining
        self.root = Toplevel()
        self.root.configure(bg='#464646')
        self.filePath = filePath
        
        
        # Set root title
        self.root.title('STATS')
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
        
        # self.data_png = PhotoImage(file='Images/data_bg.jpg')
        # self.img_lb = Label(self.root, image=self.data_png)
        # self.img_lb.place(x = 700, y = 300)
        
        #buttons
        self.center=self.app_width/2
        self.button_plot = Button(self.root,text="PLOT",  command=self.button_plot_click ,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=500,y=650)
        self.button_cancel = Button(self.root,text="CANCEL",  command= self.button_cancel_click,bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=730,y=650)
        
        #title
        self.title=Label(self.root, text="L E T ' S    P L O T", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=300,y=30)
        
        self.graphlb = Label(self.root, text="CHOOSE YOUR TYPE OF GRAPH WISELY", fg="white",bg="#464646", font=("AMGDT",14))
        self.graphlb.place(x = 698, y = 220)
        
        self.clicked = StringVar(self.root)
        self.clicked.set('Select one graph!')
        self.graph_types = ['SCATTER', 'BAR', 'HISTOGRAM']
        self.drop = OptionMenu(self.root, self.clicked, *self.graph_types, command = self.callback1)
        self.drop.place(x=750, y= 290)
 
        
        #scrapped
        #type of graph radiobuttons
        # self.rvar1=IntVar()
        # self.rbplot1=Radiobutton(self.root,variable=self.rvar1,value=1, text="H I S T O G R A M", fg="white",bg="#464646", font=("AMGDT",10))
        # self.rbplot1.place(x=170,y=300)
        # self.rbplot2=Radiobutton(self.root,variable=self.rvar1,value=2, text="B A R", fg="white",bg="#464646", font=("AMGDT",10))
        # self.rbplot2.place(x=170,y=400)
        # self.rbplot3=Radiobutton(self.root,variable=self.rvar1,value=3, text="L I N E", fg="white",bg="#464646", font=("AMGDT",10))
        # self.rbplot3.place(x=170,y=500)

        self.combo_classlb = Label(self.root, text="CHOOSE ONE CLASS", fg="white",bg="#464646", font=("AMGDT",14))
        self.combo_classlb.place(x = 198, y = 180)
        self.options_classes=["Client","User","Employee","Pilot","Staff","Airplane","Model","Reservation"]
        self.combobox_classes=ttk.Combobox(self.root,values=self.options_classes)
        self.combobox_classes.place(x=200,y=230)
        self.combobox_classes.bind("<<ComboboxSelected>>", self.attributes)
        self.class_plot = self.combobox_classes.get()
           
    
    def callback1(self,selection):
        self.graph_type = selection
        print(self.graph_type)
        return self.graph_type
        
        
    def attributes(self,event):
        self.combo_attlb = Label(self.root, text="CHOOSE ONE ATTRIBUTE TO PLOT", fg="white",bg="#464646", font=("AMGDT",14))
        self.combo_attlb.place(x = 198, y = 440)
        self.classObj = globals()[self.combobox_classes.get()]
        print(self.combobox_classes.get())
        print(self.classObj)
        self.classObj.read(self.filePath)
        # Set attribute names and labels
        obj = self.classObj.first()
        print(obj)
        self.att = list(obj.__dict__.keys())
        self.att = list(map(lambda x : x[1:], self.att))
        self.combobox_att=ttk.Combobox(self.root,values=self.att)
        self.combobox_att.place(x=200,y=490)
        self.att_plot = self.combobox_att.get()
        
    
    def button_plot_click(self):
        
        #creation of the new window
        self.window = Toplevel()
        self.window.configure(bg='#464646')
        
        self.window.wm_title('PLOTS!')
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
        
        self.bool1 = True
        
        try:
            self.combo_class_test = str(self.combobox_classes.get())
            self.combo_att_test = str(self.combobox_att.get() + 'welelele')
            print(self.combo_att_test)
            if self.combo_class_test == None or self.combo_att_test == None or self.combo_att_test == '' :
                raise ValueError
            # self.file_name = self.filePath + str(self.combobox_classes.get()) + '.csv'
            # self.file_test = pd.read_csv(self.file_name,sep=";") 
        except:
            self.errorlb = Label(self.window, text="PLEASE SELECT EVERITHING NEEDED", fg="white",bg="#464646", font=("AMGDT",15))
            self.errorlb.pack(pady = 20)
            self.bool1 = False
            print('erro!!!')
        
        if self.bool1:
            
            #create figure and read csv
            self.fig = Figure(figsize=(8,6), dpi=100)
            self.file_name = self.filePath + str(self.combobox_classes.get()) + '.csv'
            self.df = pd.read_csv(self.file_name,sep=";",encoding='latin-1')   
            self.a=self.df.head()
            print(self.a)
            
            self.x_plot = str(self.combobox_att.get())
    
            self.ax1 = self.fig.add_subplot(111)
            
            #code for scatter plot
            if self.graph_type == 'SCATTER':
                #model is the only class with no code, since models are unique
                if str(self.combobox_classes.get()) == "Model":
                    self.df1 = self.df[[self.x_plot,'model']].groupby(self.x_plot).count()
                else:
                    self.ax1.scatter(self.df[self.x_plot],self.df['code'], color = 'g')
                self.scatter = FigureCanvasTkAgg(self.fig, self.window) 
                self.scatter.get_tk_widget().pack(side=LEFT, fill=BOTH)
                self.ax1.legend(["User's code"]) 
                self.ax1.set_xlabel(self.x_plot)
                self.ax1.set_title(self.x_plot + " per each "+ str(self.combobox_classes.get()))
                pass
            
            elif self.graph_type == 'BAR':
                
                
                self.bar1 = FigureCanvasTkAgg(self.fig, self.window)
                self.bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
                if str(self.combobox_classes.get()) == "Model":
                    self.df1 = self.df[['model',self.x_plot]]
                    self.df1.plot(kind='bar', legend = False, ax=self.ax1)
                    self.ax1.set_xlabel(self.x_plot)
                    self.ax1.set_title('Count of ' + str(self.combobox_classes.get()) + "'s " + self.x_plot)
                else:
                    self.df1 = self.df[[self.x_plot,'code']].groupby(self.x_plot).count()
                    self.df1.plot(kind='bar', legend = False, ax=self.ax1)
                    self.ax1.set_xlabel(self.x_plot)
                    self.ax1.set_title('Count of ' + str(self.combobox_classes.get()) + "'s " + self.x_plot)
                
            elif self.graph_type == 'HISTOGRAM':
          
                self.hist1 = FigureCanvasTkAgg(self.fig, self.window)
                self.hist1.get_tk_widget().pack(side=LEFT, fill=BOTH)
                if str(self.combobox_classes.get()) == "Model":
                    self.df1 = self.df[[self.x_plot,'model']].groupby(self.x_plot).count()
                else:
                    self.df1 = self.df[[self.x_plot,'code']].groupby(self.x_plot).count()
                self.df1.plot(kind='hist', legend = False, ax=self.ax1, color = 'r')
                self.ax1.set_xlabel(self.x_plot)
                self.ax1.set_title('Count of ' + str(self.combobox_classes.get()) + "'s " + self.x_plot)
             
    def button_cancel_click(self):
       self.login_Status = "cancel"
       self.root.destroy()
       
             

# Statistics(filePath='Data/')
           
            
