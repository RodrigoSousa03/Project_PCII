# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:06:34 2021

@author:António Brito / Carlos Bragança

#objective: Class OpenForm to manage base classes info
"""

# import all components from the tkinter library
from tkinter import *

class OpenForm:
    def __init__(self, classObj, attnames, ncols = 2, filePath = './'):
        self.root = Tk()
        self.classObj = classObj
        
        # Set attribute names and labels
        obj = classObj.first()
        
        self.att = list(obj.__dict__.keys())
        self.filePath = filePath
        self.attnames =attnames
        
        # Set root title
        self.root.title('AVILUX')
        self.root.configure(bg='#464646')
        self.root.iconbitmap("Images/plane_takeoff_13263.ico")
                
        # Frame to navegate  buttons   
        self.frame_buttons = Frame(self.root, bg = '#464646')
        self.frame_buttons.grid(row=0,column=0)
        
        # Frame to Move buttons
        self.frame_move_button = Frame(self.frame_buttons)
        self.frame_move_button.grid(row=0,column=1, padx=10)
        # Move Buttons  
        self.button_first = Button(self.frame_move_button,text="<<", command= lambda: self.showObject('F'), font=("AIGDT",7))
        self.button_back = Button(self.frame_move_button,text="<", command= lambda: self.showObject('P'),font=("AIGDT",7))
        self.button_next = Button(self.frame_move_button,text=">", command= lambda: self.showObject('N'),font=("AIGDT",7))
        self.button_last = Button(self.frame_move_button,text=">>",command= lambda: self.showObject('L'),font=("AIGDT",7))
        # Move Buttons to Grid
        self.button_first.grid(row=0,column=0)
        self.button_back.grid(row=0,column=1)
        self.button_next.grid(row=0,column=3)
        self.button_last.grid(row=0,column=4)
        
         # Exit Button
        self.button_exit = Button(self.frame_buttons,text="EXIT",command=self.root.destroy,font=("AIGDT",7))#,bg='white',fg="black",font=("AIGDT",9))
        self.button_exit.grid(row=0,column=5,padx=10)
        
        # Frame to Edit buttons
        self.frame_edit_button = Frame(self.frame_buttons)
        self.frame_edit_button.grid(row=0,column=0, padx=10)
        # Edit Buttons  
        self.button_edit = Button(self.frame_edit_button,text="EDIT",  command= lambda: self.button_edit_click(),font=("AIGDT",7))
        self.button_delete = Button(self.frame_edit_button,text="DELETE",  command= lambda: self.button_delete_click(),font=("AIGDT",7))#bg='white',fg="black",font=("AIGDT",9))
        self.button_insert = Button(self.frame_edit_button,text="INSERT",command= lambda: self.button_insert_click(),font=("AIGDT",7))#bg='white',fg="black",font=("AIGDT",9))
        self.button_save = Button(self.frame_edit_button,text="SAVE",command= lambda: self.button_save_click(),font=("AIGDT",7))#bg='white',fg="black",font=("AIGDT",9))
        self.button_cancel = Button(self.frame_edit_button,text="CANCEL",command= lambda: self.button_cancel__click(),font=("AIGDT",7))#bg='white',fg="black",font=("AIGDT",9))
        # put Edit Buttons in frame Grid
        self.button_edit.grid(row=0,column=0)
        self.button_delete.grid(row=0,column=1)
        self.button_insert.grid(row=0,column=3)
        self.button_save.grid(row=0,column=4)
        self.button_cancel.grid(row=0,column=5)
        
        # Frame to class
        self.frame_class = LabelFrame(self.root,text = str(self.classObj.__name__).upper(),font=("AIGDT",9))
        self.frame_class.grid(row=2,column=0,padx=10,pady=10)
        
        # Creates the labels and field entries
        self.ent = list()
        r = 0
        c = 0
        for desc in attnames:
            lbl = Label(self.frame_class, text=str(desc).upper(),font=("AIGDT",7))
            lbl.grid(row=r, column=c, padx=10, pady=10)
            c = c + 1
            ent = Entry(self.frame_class)
            ent.grid(row=r, column=c, padx=10, pady=10)
            self.ent.append(ent)
            if c == 2 * ncols - 1:
                r = r + 1
                c = 0
            else:
                c = c + 1
        

        
                
        
        # # class variables
        # lb_code = Label(self.frame_class,text = 'Code :')
        # self.en_code = Entry(self.frame_class)
        
        # lb_name = Label(self.frame_class,text = 'name :')
        # self.en_name = Entry(self.frame_class)
        
        # lb_price = Label(self.frame_class,text = 'price :')
        # self.en_price = Entry(self.frame_class)
        
        # lb_stock = Label(self.frame_class,text = 'stock :')
        # self.en_stock = Entry(self.frame_class)
        
        # # put  in frame Grid
        # lb_code.grid(row=0, column=0, padx=10, pady=10)
        # self.en_code.grid(row=0, column=1, padx=10, pady=10)
     
        # lb_name.grid(row=0, column=2, padx=10, pady=10)
        # self.en_name.grid(row=0, column=3, padx=10, pady=10)
        
        # lb_price.grid(row=1, column=0, padx=10, pady=10)
        # self.en_price.grid(row=1, column=1, padx=10, pady=10)
        
        # lb_stock.grid(row=2, column=0, padx=10, pady=10)
        # self.en_stock.grid(row=2, column=1, padx=10, pady=10)
        
        #self.filePath = './'
        self.classObj.read(self.filePath)
        
        self.config_mode("Show")
        self.showObject("C")
        # Let the root wait for any events
        self.root.mainloop()

    # Create New Object
    def Creat_newobj_from_Entry(self):
        str_obj = ''
        sep = ''
        for ent in self.ent:
            str_obj = str_obj + sep + ent.get()
            sep = ';'
        return self.classObj.from_string(str_obj)

        # return self.classObj(self.en_code.get(),self.en_name.get(),self.en_price.get(),self.en_stock.get())
    
    # update  Object from form
    def update_my_object(self, objet):
        for idx, ent in enumerate(self.ent):
            setattr(objet, self.att[idx], ent.get())

        # objet.code = en_code.get()
        # objet.name = en_name.get()
        # objet.price = en_price.get()
        # objet.stock = self.en_stock.get()
    
    def cleanForm(self):
        # clean all entrys
        for ent in self.ent:
            ent.config(state='normal')
            ent.delete(0, 'end')

        # children_widgets = self.frame_class.winfo_children()
        # for child_widget in children_widgets:
        #     if child_widget.winfo_class() == 'Entry':
        #         child_widget.delete(0,END)
    
    def button_edit_click(self):
        self.config_mode("Edit")
    
    def button_delete_click(self):
        selobj = 'C'
        resp = messagebox.askyesno(title='delete record', message='Are you sure?')
        if resp:
            self.classObj.remove(self.visible_object.code)
            self.classObj.write(self.filePath)
            selobj = 'P'
        self.config_mode("Show")
        self.showObject(selobj)
    
    def button_insert_click(self):
        self.visible_object = None
        self.config_mode("Edit")
        self.cleanForm()
        
    def button_save_click(self):
        if self.visible_object == None:
            # Insert new
            self.visible_object = self.Creat_newobj_from_Entry()
            self.visible_object=self.classObj.last() 
        else:
            #Update
            self.update_my_object(self.visible_object)
        
        self.classObj.write(self.filePath)
        self.visible_object=self.classObj.current() 
        self.config_mode("Show")
     
    def button_cancel__click(self):
        self.visible_object=self.classObj.current() 
        self.config_mode("Show")
        self.showObject("C")

    #configure form according to the state
    def config_mode(self, mode):
        
        if mode == "Show":
            self.button_first['state'] = "normal"
            self.button_back['state'] = "normal"
            self.button_next['state'] = "normal"
            self.button_last['state'] = "normal"
            
            self.button_edit['state'] = "normal"
            self.button_delete['state'] = "normal"
            self.button_insert['state'] = "normal"
            self.button_save['state'] = "disabled"
            self.button_cancel['state'] = "disabled"
            
            self.button_exit['state'] = "normal"
            for ent in self.ent:
                ent.config(state='readonly')

            
        elif mode == "Edit":
            self.button_first['state'] = "disabled"
            self.button_back['state'] = "disabled"
            self.button_next['state'] = "disabled"
            self.button_last['state'] = "disabled"
            
            self.button_edit['state'] = "disabled"
            self.button_delete['state'] = "disabled"
            self.button_insert['state'] = "disabled"
            self.button_save['state'] = "normal"
            self.button_cancel['state'] = "normal"
            
            self.button_exit['state'] = "disabled"
            for ent in self.ent:
                ent.config(state='normal')

    
    # update fields
    def objectToEntrys(self):
        for idx, ent in enumerate(self.ent):
            ent.config(state='normal')
            ent.delete(0, 'end')
            ent.insert(0, getattr(self.visible_object, self.att[idx]))
            ent.config(state='readonly')

        # self.en_code.delete(0,END)
        # self.en_code.insert(0, self.visible_object.code)
        
        # self.en_name.delete(0,END)
        # self.en_name.insert(0, self.visible_object.name)
        
        # self.en_price.delete(0,END)
        # self.en_price.insert(0, self.visible_object.price)
        
        # self.en_stock.delete(0,END)
        # self.en_stock.insert(0, self.visible_object.stock)
        
    def showObject(self, option):
        # C - current
        # F - first
        # P - previous
        # N - next
        # L - last
        option = option.upper()
       
        if option == 'C':
            self.visible_object=self.classObj.current()
            
        elif  option == 'F':
            self.visible_object=self.classObj.first()
            
        elif  option == 'P':
            self.visible_object=self.classObj.previous()
            if self.visible_object == None:
                self.visible_object=self.classObj.first()
                
        elif  option == 'N':
            self.visible_object=self.classObj.next()
            if self.visible_object == None:
                self.visible_object=self.classObj.last()
                
        elif  option == 'L':
            self.visible_object=self.classObj.last()

        self.objectToEntrys()    
 

