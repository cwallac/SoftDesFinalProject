# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 03:21:32 2014

@author: dcelik
"""

import Tkinter as tk
import ttk
from PIL import Image, ImageTk

RHEIGHT = 800
RWIDTH  = 1540

class gui(tk.Tk):
    def __init__(self,parent): 
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.about_messageprog = "AN INTERACTIVE CIRCUIT DESIGN STUDIO SUITE FOR CREATION OF BREADBOARD AND SCHEMATIC PROTOTYPES."
        self.about_messagecreat = "CREATED BY DENIZ CELIK, SUBHASH GUBBA, CHRIS WALLACE, AND RADMER VAN DER HEYDE. ALL STUDENTS ARE FRESHMAN AT THE FRANKLIN W. OLIN COLLEGE OF ENGINEERING IN NEEDHAM, MA."        
        self.initialize()
        
    def aboutprog(self):
        popup = tk.Toplevel()
        popup.title("About this program")
        
        msg = tk.Message(popup,text=self.about_messageprog)
        msg.pack()
        
        button = ttk.Button(popup,text="Close", command = popup.destroy)
        button.pack()
        
    def aboutcreat(self):
        popup = tk.Toplevel()
        popup.title("About the creators")
        
        msg = tk.Message(popup,text=self.about_messagecreat)
        msg.pack()
        
        button = tk.Button(popup,text="Close", command = popup.destroy)
        button.pack()

    def makemenu(self):
        #creating submenus for each item        
        self.filesubMenu = tk.Menu(self.menuBar)
        self.editsubMenu = tk.Menu(self.menuBar)
        self.viewsubMenu = tk.Menu(self.menuBar)
        self.toolssubMenu = tk.Menu(self.menuBar)
        self.aboutsubMenu = tk.Menu(self.menuBar)
        
        #creating menubar items
        self.menuBar.add_cascade(label='File', menu=self.filesubMenu)
        self.menuBar.add_cascade(label='Edit', menu=self.editsubMenu)
        self.menuBar.add_cascade(label='View', menu=self.viewsubMenu)
        self.menuBar.add_cascade(label='Tools', menu=self.toolssubMenu)
        self.menuBar.add_cascade(label='About', menu=self.aboutsubMenu)
        
        #creating commands for each submenu option
        
        #file submenu commands
        self.filesubMenu.add_command(label='New', command=self.quit)
        self.filesubMenu.add_command(label='Open', command=self.quit)
        self.filesubMenu.add_command(label='Save', command=self.quit)
        self.filesubMenu.add_command(label='Quit', command=self.quit)
        
        #edit submenu commands
        self.editsubMenu.add_command(label='Cut', command=self.quit)
        self.editsubMenu.add_command(label='Copy', command=self.quit)
        self.editsubMenu.add_command(label='Paste', command=self.quit)
        self.editsubMenu.add_command(label='Insert', command=self.quit)
        
        #view submenu commands
        self.viewsubMenu.add_command(label='Resistors', command=self.quit)
        self.viewsubMenu.add_command(label='Capacitors', command=self.quit)
        self.viewsubMenu.add_command(label='Dips', command=self.quit)
        self.viewsubMenu.add_command(label='Wires', command=self.quit)
        
        #tools submenu commands
        self.toolssubMenu.add_command(label='Move', command=self.quit)
        self.toolssubMenu.add_command(label='Rotate', command=self.quit)
        self.toolssubMenu.add_command(label='Erase', command=self.quit)
        self.toolssubMenu.add_command(label='Text', command=self.quit)
        
        #about submenu commands
        self.aboutsubMenu.add_command(label='About the Program', command=self.aboutprog)
        self.aboutsubMenu.add_command(label='About the Creators',command=self.aboutcreat)
        
    def processMouseEvent(self, event):
        mouse_coordinates= str(event.x) + ", " + str(event.y)
        self.bbcanvas.create_text(event.x,event.y, text = mouse_coordinates)
    
    def initialize(self):
        #initialize grid
        self.grid()
        
        #set minimum size and prevent resizing
        self.minsize(RWIDTH,RHEIGHT)
        self.resizable(False,False)
        
        #create and place breadboard canvas in grid
        self.bbcanvas=tk.Canvas(self.parent,bg='white')
        self.bbcanvas.grid(column=1,row=0,sticky='NEWS')
        self.bbcanvas.configure(width=575,height=RHEIGHT)
        
        #create and place schematic canvas in grid
        self.scanvas=tk.Canvas(self.parent,bg='red')
        self.scanvas.grid(column=0,row=0,sticky='NEWS')     
        self.scanvas.configure(width=RWIDTH-575,height=RHEIGHT)
        
        #top level gui creation
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top['menu'] = self.menuBar
        
        self.makemenu()    
        
        #creating breadboard
        self.bbimage = Image.open("bb.bmp")
        self.bbimage = self.bbimage.resize((500,1600),Image.ANTIALIAS)
        self.bbphoto = ImageTk.PhotoImage(self.bbimage)
        self.bbcanvas.create_image(250,800,image=self.bbphoto)
            
        #column weight configuration
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=1)
        
        self.bbcanvas.bind("<Button-1>", self.processMouseEvent)
        self.bbcanvas.focus_set()

        self.bbcanvas.columnconfigure        
        
        #self.circbutt = ttk.Checkbutton(self.bbcanvas,style = 'TCheckbutton')
        #self.circbutt.grid(column=0,row=0)
        
        #update and geometry
        self.update()
        self.geometry(self.geometry())     
        
    
        
if __name__ == "__main__":
    app = gui(None)
    app.title('C.I.R.C.U.I.T')
    app.mainloop()
    