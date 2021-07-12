# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:08:56 2021

@author: Asus-Pc
"""
from FormLogin import FormLogin
from FormRegister import FormRegister
from tkinter import *
from PIL import Image, ImageTk


def call_login_form_Class():
    s1 = FormLogin(filePath='Data/')
        
def call_regist_form_Class():
    s2=FormRegister('Client', filePath = 'Data/')
              

root=Tk()
root.title("A V I L U X")
root.iconbitmap("Images/plane_takeoff_13263.ico")

#Designate Height and Width of my app
app_width=1300
app_height=730


#Find width and height screen's
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()


x=int((screen_width/2)-(app_width/2))
y=int((screen_height/2)-(app_height/2))


#places window in the middle of the sceen
root.geometry(f'{app_width}x{app_height}+{x}+{y}')


#define image
bg=Image.open("Images/resizedpic.jpg")
bg=ImageTk.PhotoImage(bg)


#creat a canvas
my_canvas=Canvas(root, width=1300, height=730, bd=0, highlightthickness=0)
my_canvas.pack(fill="both",expand=True)


#set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")


#add a label
my_canvas.create_text(app_height/2,250,text="A V I L U X",font=("AMGDT",50),fill="white")
my_canvas.create_text(app_height/2,310,text="PRIVATE JETS AND PLANES",font=("AMGDT",10),fill="white")


#creat buttons
button1=Button(root,text="SIGN IN", bg="white", fg="black",font=("AIGDT",13),command=call_login_form_Class)
button2=Button(root,text="REGISTER",bg="white", fg="black",font=("AIGDT",13),command=call_regist_form_Class)


#add buttons to canvas in windows
button1_window=my_canvas.create_window(app_height/2-160,380,anchor="nw", window=button1)
button2_window=my_canvas.create_window(app_height/2+40,380,anchor="nw", window=button2)


root.mainloop()



