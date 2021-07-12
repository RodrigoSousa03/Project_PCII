# -*- coding: utf-8 -*-
"""
Created on Mon May 17 22:01:17 2021

@author: Asus-Pc
"""

from tkinter import *
import pandas as pd
from tkinter import ttk,filedialog


class exceldisplay:
    
    def __init__(self,typ,title,corx,cory):
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        
        # Set root title
        self.root.title(title)
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
        
        
        #creat frame
        # self.my_frame=Frame(self.root)
        # self.my_frame.pack(pady=20)
       
        
        #creat treeview
        self.my_tree=ttk.Treeview(self.root)
        
        if typ=="none":
            self.my_menu=Menu(self.root)
            self.root.config(menu=self.my_menu)
            
            self.file_menu=Menu(self.my_menu,tearoff=False)
            self.my_menu.add_cascade(label="Spreadsheets",menu=self.file_menu)
            self.file_menu.add_command(label="Open", command=self.file_open)
            self.my_label=Label(self.root,text='')
            self.my_label.place(x=500,y=200)
            
            
        else:
            self.df=pd.read_csv(typ,delimiter=";",encoding='latin-1')
            
        self.my_tree["column"]=list(self.df.columns)
        self.my_tree["show"]="headings"
        
        #loop thru column list
        
        for column in self.my_tree["column"]:
            self.my_tree.heading(column, text=column)
        
        self.df_rows=self.df.to_numpy().tolist()
        for row in self.df_rows:
            self.my_tree.insert("","end",values=row)
        
        self.my_tree.place(x=corx,y=cory)
        self.root.mainloop()
        
        
    def file_open(self):
        global df
        self.filename=filedialog.askopenfilename(
            initialdir="",
            title="Open a file",
            filetype=(("csv files","*.csv"),('All Files','*.*'))
            )
        if self.filename:
            try:
                self.filename=r"{}".format(self.filename)
                df=pd.read_csv(self.filename,delimiter=";",encoding='latin-1')
                return df
            except ValueError:
                self.my_label.config(text="File Couldn't be Opened...")
            
            except FileNotFoundError:
                self.my_label.config(text="File Couldn't be found...")
        self.clear_tree()
    
    def clear_tree(self):
        self.my_tree.delete(*self.my_tree.get_children())
            
#exceldisplay("Data/client.csv","Clients")

                
                    
            
            
        