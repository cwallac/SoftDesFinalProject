# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 03:21:32 2014

@author: dcelik
"""

import Tkinter as tk

class gui(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        #initialize grid
        self.grid()
        
        #set minimum size and prevent resizing
        self.minsize(1280,800)
        self.resizable(False,False)
        
        #create and place breadboard canvas in grid
        self.bbcanvas=tk.Canvas(self.parent,bg='black')
        self.bbcanvas.grid(column=0,row=1,sticky='NEWS')  
        
        #create and place schematic canvas in grid
        self.scanvas=tk.Canvas(self.parent,bg='red')
        self.scanvas.grid(column=1,row=1,sticky='NEWS')     
        
        #top level gui creation
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top['menu'] = self.menuBar
        self.subMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Help', menu=self.subMenu)
        self.subMenu.add_command(label='About', command=self.quit)        
        
        #menu button creation testing
        self.mb=tk.Menubutton(self.parent,text='File',bg='grey',activebackground='white',height=2,relief=tk.RAISED)
        self.mb.grid(column=0,row=0,columnspan=2,sticky='NEWS')
        self.mb.menu = tk.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu
        self.mb.menu.add_command(label='quit',command=self.quit)
        
        #column weight configuration
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=1)
        
        #update and geometry
        self.update()
        self.geometry(self.geometry())     
        
if __name__ == "__main__":
    app = gui(None)
    app.title('C.I.R.C.U.I.T')
    app.mainloop()
    
    
    
    
    self.mb.grid()

    self.mb.menu = tk.Menu(self.mb, tearoff=0)
    self.mb['menu'] = self.mb.menu

    self.mayoVar  = tk.IntVar()
    self.ketchVar = tk.IntVar()
    self.mb.menu.add_checkbutton(label='mayo',
        variable=self.mayoVar)
    self.mb.menu.add_checkbutton(label='ketchup',
        variable=self.ketchVar)
    