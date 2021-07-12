# -*- coding: utf-8 -*-
"""
Created on Tue May 25 23:33:19 2021

@author: Asus-Pc
"""
from tkinter import * 
from tkinter import ttk
import pandas as pd
from Classes.user import User
from Classes.employee import Employee
from Classes.client import Client
from Classes.pilot import Pilot
from Classes.staff import Staff


class Tabs():
    def __init__(self):
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
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
        
        self.notebook=ttk.Notebook(self.root)
        self.notebook.pack()
        
        self.frame_user=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_clients=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_employees=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_staff=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_pilots=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_airplanes=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_model=Frame(self.notebook,width=1300,height=730,bg="#464646")
        self.frame_reservations=Frame(self.notebook,width=1300,height=730,bg="#464646")
        
        self.frame_user.pack(fill="both",expand=1)
        self.frame_clients.pack(fill="both",expand=1)
        
        self.notebook.add(self.frame_user,text="U S E R S",)
        self.notebook.add(self.frame_clients,text="C L I E N T S")
        self.notebook.add(self.frame_employees,text="E M P L O Y E E S")
        self.notebook.add(self.frame_staff,text="S T A F F")
        self.notebook.add(self.frame_pilots,text="P I L O T S")
        self.notebook.add(self.frame_airplanes,text="A I R P L A N E S")
        self.notebook.add(self.frame_model,text="M O D E L S")
        self.notebook.add(self.frame_reservations,text="R E S E R V A T I O N S")
        
        self.display_treeview(self.frame_user,'Data/user.csv')
        self.display_treeview(self.frame_clients,'Data/Client.csv')
        #self.display_treeview(self.frame_employees,'Data/Employee.csv')
        self.display_treeview(self.frame_staff,'Data/Staff.csv')
        self.display_treeview(self.frame_pilots,'Data/Pilot.csv')
        self.display_treeview(self.frame_airplanes,'Data/Airplane.csv')
        self.display_treeview(self.frame_model,'Data/Model.csv')
        self.display_treeview(self.frame_reservations,'Data/Reservation.csv')
        
        
        
        self.root.mainloop()
        
    def display_treeview(self,root_name,path):
             self.my_frame=Frame(root_name)
             self.my_frame.pack(side=TOP,pady=15,padx=15,fill="both", expand=1)
             
             self.tree_scrolly=Scrollbar(self.my_frame)
             self.tree_scrolly.pack(side=RIGHT,fill=Y)
             
             self.tree_scrollx=Scrollbar(self.my_frame,orient=HORIZONTAL)
             self.tree_scrollx.pack(side=BOTTOM,fill=X)
            
             self.my_tree=ttk.Treeview(self.my_frame,yscrollcommand=self.tree_scrolly.set)
             self.my_tree=ttk.Treeview(self.my_frame,xscrollcommand=self.tree_scrollx.set)
             
             self.df=pd.read_csv(path,delimiter=";",encoding='latin-1')
                
             self.my_tree["column"]=list(self.df.columns)
             self.my_tree["show"]="headings"
            
            #loop thru column list
            
             for column in self.my_tree["column"]:
                 self.my_tree.heading(column, text=column)
            
             self.df_rows=self.df.to_numpy().tolist()
             for row in self.df_rows:
                 self.my_tree.insert("","end",values=row)
            
             self.my_tree.pack(fill="both", expand=1)
             
             self.tree_scrolly.config(command=self.my_tree.yview)
             self.tree_scrollx.config(command=self.my_tree.xview)
             
        
# profile_form()
         
        