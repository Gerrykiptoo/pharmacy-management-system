import random
import time
import  datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
def main():
    root = Tk()
    app = window1(root)
    root.mainloop()
    
    
class window1:
    def __init__(self,master):
        self.master = master 
        self.master.title("Pharmacy management system")
        self.master.geometry('1350*750+0+0')#x-axis, y-axis,0 ,0 are the location of the leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
        
        
        self.LabelTitle = Label(self.frame,text="  Pharmacy Management system ",font = ("arial",40,"bold"),
                 bd= 10, relief= "sunken")
        self.LabelTitle.grid(row = 0 , column = 0, columnspan = 2, pady=20 )
        




 
class window2:
    def __init__(self,master):
        self.master = master 
        self.master.title("Pharmacy management system")
        self.master.geometry('1350*750+0+0')#x-axis, y-axis,0 ,0 are the location of the leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
                




 
class window3:
    def __init__(self,master):
        self.master = master 
        self.master.title("Pharmacy management system")
        self.master.geometry('1350*750+0+0')#x-axis, y-axis,0 ,0 are the location of the leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
                
       




 
class window4:
    def __init__(self,master):
        self.master = master 
        self.master.title("Pharmacy management system")
        self.master.geometry('1350*750+0+0')#x-axis, y-axis,0 ,0 are the location of the leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
        
    



 
class window5:
    def __init__(self,master):
        self.master = master 
        self.master.title("Pharmacy management system")
        self.master.geometry('1350*750+0+0')#x-axis, y-axis,0 ,0 are the location of the leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
        





if __name__== "_main__":
    main()
        
    