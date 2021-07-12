# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:13:40 2021

@author: Asus-Pc
"""

from tkinter import *
from Classes.user import User
from Mainwindow import MainWindow

import tkinter.messagebox as MessageBox

class FormLogin:
    def __init__(self, filePath = './'):
        
        User.read('Data/')
        
        self.root = Tk()
        self.root.configure(bg='#464646')
        
        self.filePath = filePath
        
        self.classObj = User
        self.classObj.read(self.filePath)
        
        # Set attribute names and labels
        obj = self.classObj.first()
        self.att = list(obj.__dict__.keys())
        
        
        # Set root title
        self.root.title('SIGN IN')
        self.root.iconbitmap("Images/plane_takeoff_13263.ico")
        
        #root geometry
        self.app_width=500
        self.app_height=730
    
        #Find width and height screen's
        self.screen_width=self.root.winfo_screenwidth()
        self.screen_height=self.root.winfo_screenheight()
    
        self.x=int((self.screen_width/2)-(self.app_width/2))
        self.y=int((self.screen_height/2)-(self.app_height/2))        
        self.root.geometry(f'{self.app_width}x{self.app_height}+{self.x}+{self.y}')
        
        #buttons
        self.center=self.app_width/2
        self.button_login = Button(self.root,text="LOGIN",  command= lambda: self.button_login_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=50,y=400)
        self.button_cancel = Button(self.root,text="CANCEL",  command= lambda: self.button_cancel_click(),bg='white',padx=20,pady=8,fg="black",font=("AIGDT",12)).place(x=300,y=400)
        
        
        #title
        self.title=Label(self.root, text="L O G I N", fg="white",bg="#464646", font=("AMGDT",30))
        self.title.place(x=100,y=30)
        
        #labels and entries
        #username
        self.unamelb=Label(self.root, text="U S E R N A M E", fg="white",bg="#464646", font=("AMGDT",10))
        self.unamelb.place(x=40,y=170)
        self.unameIB=Entry(self.root, width=40)
        self.unameIB.place(x=90,y=220)
        
        #password
        self.pwlb=Label(self.root, text="P A S S W O R D", fg="white",bg="#464646", font=("AMGDT",10))
        self.pwlb.place(x=40,y=270)
        self.pwIB=Entry(self.root,width=40)
        self.pwIB.place(x=90,y=320)
        
        
        self.login_Status = "Not Login"
        
        # Let the root wait for any events
        self.root.mainloop()

   
 
    #verify login
    def button_login_click(self):
        
        loginIn = self.unameIB.get()
        passwordIn = self.pwIB.get()
        
        for customer in self.classObj.lst:
            
            if self.classObj.obj[customer].username == loginIn:
                
                if self.classObj.obj[customer].password == passwordIn:
                    
                    self.code=customer           #user code
                    print(self.code)
                    self.login_Status = "Login"
                    break
                
                else:
                    print("Password errada para login fornecido")
            
        if  self.login_Status == "Login":
            
            MessageBox.showinfo(loginIn,"logged successfully")
            
            self.root.destroy()
            
            MainWindow(self.code, filePath = 'Data/')
            
           
        else:
            print("login errado")
            MessageBox.showinfo(loginIn,"Username or password are not correct")
            
            
    #destroy window
    def button_cancel_click(self):
       self.login_Status = "cancel"
       self.root.destroy()
       
   
       
    