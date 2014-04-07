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
        self.grid()
        
        self.bbcanvas=tk.Canvas(self.parent,bg='black')
        self.scanvas=tk.Canvas(self.parent,bg='red')
        self.menu=tk.Menubutton(self.parent,bg='blue')
        
        self.bbcanvas.grid(column=0,row=1,sticky='NEWS')  
        self.scanvas.grid(column=1,row=1,sticky='NEWS')              
        self.menu.grid(column=0,row=0,columnspan=2,sticky='NEWS')        
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())     
        
if __name__ == "__main__":
    app = gui(None)
    app.title('C.I.R.C.U.I.T')
    app.mainloop()
    
    
    