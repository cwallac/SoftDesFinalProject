# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 03:21:32 2014

@author: dcelik
"""

import Tkinter as tk
#import ttk
from PIL import Image, ImageTk
import nodes
import menumethods

RHEIGHT = 810
RWIDTH  = 985
dipopen = False
resopen = False
capopen = False
wireopen = False
class gui(tk.Tk):
    def __init__(self,parent): 
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.buttonlist = []  
        self.scbuttonlist = []
        self.DFTCLR = ""
        self.initialize()

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
        self.filesubMenu.add_separator()
        self.filesubMenu.add_command(label='Quit', command=self.quit)
        
        #edit submenu commands
        self.editsubMenu.add_command(label='Cut', command=self.quit)
        self.editsubMenu.add_command(label='Copy', command=self.quit)
        self.editsubMenu.add_command(label='Paste', command=self.quit)
        self.editsubMenu.add_command(label='Insert', command=self.quit)
        
        #view submenu commands
        self.viewsubMenu.add_checkbutton(label='Add Components', command = lambda: self.insert("A"))
        self.viewsubMenu.add_separator()
        self.viewsubMenu.add_radiobutton(label='Resistors', command=lambda: self.insert("R"))
        self.viewsubMenu.add_radiobutton(label='Capacitors', command=lambda: self.insert("C"))
        self.viewsubMenu.add_radiobutton(label='Dips', command=lambda: self.insert("D"))
        self.viewsubMenu.add_radiobutton(label='Wires', command=lambda: self.insert("W"))
        
        #tools submenu commands
        self.toolssubMenu.add_command(label='Move', command=self.quit)
        self.toolssubMenu.add_command(label='Rotate', command=self.quit)
        self.toolssubMenu.add_command(label='Erase', command=self.quit)
        self.toolssubMenu.add_command(label='Text', command=self.quit)
        
        #about submenu commands
        self.aboutsubMenu.add_command(label='About the Program', command=menumethods.aboutprog)
        self.aboutsubMenu.add_command(label='About the Creators',command=menumethods.aboutcreat)
        
    def insert(self,ident):
        for i in self.buttonlist:
            i.configure(bg=self.DFTCLR)
        for i in self.scbuttonlist:
            i.configure(bg="black")            
        if ident=="A":
            menumethods.addcomps()
        if ident=="R":
            self.insertResistor()
        if ident=="C":
            self.insertCapacitor()
        if ident=="D":
            self.insertDip()
        if ident=="W":
            self.insertWire()
        if ident=="K":
            menumethods.clearall()
            
    def insertDip(self):
        global dipopen
        if menumethods.add and not dipopen:
            dipopen=True
            popup = tk.Toplevel()
            popup.title("Dip Size")
            popup.resizable(False,False)
            msg = tk.Message(popup,text="Enter the number of Dip Pins:")
            msg.grid(row=0,column=0,sticky='NEWS')
            size = tk.Listbox(popup,selectmode = tk.SINGLE,height = 5)
            for item in ["8", "10", "12", "14","16"]:
                size.insert(tk.END, item)
            size.grid(row=0,column=1,sticky='NEWS')
            size.bind("<Double-Button-1>", lambda notused : self.dipenter(popup,int(size.get(tk.ACTIVE))))
            
            enter = tk.Button(popup,text="Enter", command = lambda: self.dipenter(popup,int(size.get(tk.ACTIVE))))
            enter.grid(row=1,column=0,sticky='NEWS')
            
            cancel = tk.Button(popup,text="Cancel", command = lambda: self.kill(popup,"d"))
            cancel.grid(row=1,column=1,sticky='NEWS')
            
    def insertWire(self):
        global wireopen
        if menumethods.add and not wireopen:
            wireopen=True
            popup = tk.Toplevel()
            popup.title("Wire Color")
            popup.resizable(False,False)
            msg = tk.Message(popup,text="Select Desired Color of Wire")
            msg.grid(row=0,column=0,sticky='NEWS')
            size = tk.Listbox(popup,selectmode = tk.SINGLE,height = 6)
            for item in ["Black", "White", "Red", "Yellow", "Blue","Green"]:
                size.insert(tk.END, item)
            size.grid(row=0,column=1,sticky='NEWS')
            size.bind("<Double-Button-1>", lambda notused : self.wireenter(popup,size.get(tk.ACTIVE)))
            
            enter = tk.Button(popup,text="Enter", command = lambda: self.wireenter(popup,size.get(tk.ACTIVE)))
            enter.grid(row=1,column=0,sticky='NEWS')
            
            cancel = tk.Button(popup,text="Cancel", command = lambda: self.kill(popup,"w"))
            cancel.grid(row=1,column=1,sticky='NEWS')
            
    def insertCapacitor(self):
        global capopen
        if menumethods.add and not capopen:
            capopen=True
            popup = tk.Toplevel()
            popup.title("Cap Value")
            popup.resizable(False,False)
            msg = tk.Message(popup,text="Enter the capacitance value:")
            msg.grid(row=0,column=0,sticky='NEWS')
            
            vcmd = (popup.register(self.validnums),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            size = tk.Entry(popup,validate = 'key', validatecommand = vcmd)
            size.insert(0,"0")
            size.grid(row=0,column=1,sticky = 'EW')
            
            units = tk.Listbox(popup,selectmode = tk.SINGLE,height = 7)
            for item in ["pF", "nF",u"\u03bcF", "mF", "cF","dF","F"]:
                units.insert(tk.END, item)
            units.activate(0)
            units.grid(row=0,column=2,sticky='NEWS')
            
            enter = tk.Button(popup,text="Enter", command = lambda: self.capenter(popup,int(size.get()),units.get(tk.ACTIVE)))
            enter.grid(row=1,column=0,sticky='NEWS')
            
            cancel = tk.Button(popup,text="Cancel", command = lambda: self.kill(popup,"c"))
            cancel.grid(row=1,column=1,sticky='NEWS')
            
    def insertResistor(self):
        global resopen
        if menumethods.add and not resopen:
            resopen=True
            popup = tk.Toplevel()
            popup.title("Resistor Value")
            popup.resizable(False,False)
            msg = tk.Message(popup,text="Enter the resistance value:")
            msg.grid(row=0,column=0,sticky='NEWS')
            
            vcmd = (popup.register(self.validnums),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            size = tk.Entry(popup,validate = 'key', validatecommand = vcmd)
            size.insert(0,"0")
            size.grid(row=0,column=1,sticky = 'EW')
            
            units = tk.Listbox(popup,selectmode = tk.SINGLE,height = 4)
            for item in [u"\u03a9", u"K\u03a9", u"M\u03a9",u"G\u03a9"]:
                units.insert(tk.END, item)
            units.activate(0)
            units.grid(row=0,column=2,sticky='NEWS')
            
            enter = tk.Button(popup,text="Enter", command = lambda: self.resenter(popup,int(size.get()),units.get(tk.ACTIVE)))
            enter.grid(row=1,column=0,sticky='NEWS')
            
            cancel = tk.Button(popup,text="Cancel", command = lambda: self.kill(popup,"c"))
            cancel.grid(row=1,column=1,sticky='NEWS')
            
    def validnums(self, action, index, value_if_allowed,prior_value, text, validation_type, trigger_type, widget_name):
        return len(value_if_allowed)<=3 and text in '0123456789'
        
    def dipenter(self,pp,val):
        global dipopen
        dipopen = False
        self.dipsize = val
        menumethods.insertDip()
        pp.destroy()
        
    def capenter(self,pp,val,units):
        global capopen
        capopen = False
        self.capval = val
        self.capunits = units
        menumethods.insertCapacitor()
        pp.destroy()
    
    def wireenter(self,pp,col):
        global wireopen
        wireopen = False
        self.wirecolor = col
        menumethods.insertWire()
        pp.destroy()
        
    def resenter(self,pp,val,units):
        global resopen
        resopen = False
        self.resval = val
        self.resunits = units
        menumethods.insertResistor()
        pp.destroy()

    def kill(self,pp,ident):
        if ident == "d":
            global dipopen
            dipopen = False
        if ident == "c":
            global capopen
            capopen = False
        if ident == "w":
            global wireopen
            wireopen = False
        if ident == "r":
            global resopen
            resopen = False
        pp.destroy()   
        
    def forgetbuttons(self,i,j):
        return self.buttonlist
        
    def initialize(self):
        #initialize grid
        self.grid()
        
        #set minimum size and prevent resizing
        self.minsize(RWIDTH,RHEIGHT)
        self.resizable(False,False)
        
        #create and place breadboard canvas in grid
        self.bbimageheight = 1110
        self.bbimagewidth = 557
        self.bbcanvas=tk.Canvas(self.parent,bg='black')
        self.bbcanvas.grid(column=1,row=0,sticky='NEWS')
        self.bbcanvas.configure(width=self.bbimagewidth,height=RHEIGHT)
        
        #create and place schematic canvas in grid
        self.scanvas=tk.Canvas(self.parent,bg='white')
        self.scanvas.grid(column=0,row=0,sticky='NEWS')     
        self.scanvas.configure(width=RWIDTH,height=RHEIGHT)
        
        #top level gui creation
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top['menu'] = self.menuBar
        
        self.makemenu()    
        
        #creating breadboard
        self.bbimage = Image.open("bb1.bmp")
        
        self.bbphoto = ImageTk.PhotoImage(self.bbimage)
        self.bbcanvas.create_image(self.bbimagewidth/2,self.bbimageheight/2,image=self.bbphoto)
          
        #column weight configuration
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=1)
        
        self.bbcanvas.columnconfigure
        self.scanvas.columnconfigure        
        
        #adding buttons to bbcanvas
        self.DFTCLR = top.cget("bg")
        xrag = [i for i in range(120,450,30) if i!=270]
        for i in xrag:
            for j in range(8,800,30):
                n = nodes.bbnode(self.bbcanvas,i,j,self.DFTCLR)
                n.bind("<Button-1>",self.processbbMouseEvent)
                self.buttonlist.append(n)
    
        yrag = [i for i in range(68,818,30) if i!=218 and i!=398 and i!=578 and i!=758]
        for i in [30,60,480,510]:
            for j in yrag:
                n=nodes.bbnode(self.bbcanvas,i,j,self.DFTCLR)  
                n.bind("<Button-1>",self.processbbMouseEvent)
                self.buttonlist.append(n)
        
        #adding buttons to scanvas
        xrag = [i for i in range(12,980,73)]
        yrag = [i for i in range(11,810,65)]
        for i in xrag:
            for j in yrag:
                n = nodes.scnode(self.scanvas,i,j,"black")
                n.bind("<Button-1>",self.processscMouseEvent)
                self.scbuttonlist.append(n)
                
        #update and geometry
        self.update()
        self.geometry(self.geometry())     
        
    def processbbMouseEvent(self,event):
        w=event.widget
        if menumethods.add:
            if menumethods.res_go and len(menumethods.res_coords)<2:
                if len(menumethods.res_coords)==1:
                    org = menumethods.res_coords[0]
                    opt = [i for i in self.buttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.res_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.res_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.res_coords)==1:
                    org = menumethods.res_coords[0]
                    opt = [i for i in self.buttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.res_coords)>=2:
                org = menumethods.res_coords[0]
                end = menumethods.res_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawres(org,end,w,"v","red")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawres(org,end,w,"h","red")
                self.insert("K")
                
            if menumethods.cap_go and len(menumethods.cap_coords)<2:
                if len(menumethods.cap_coords)==1:
                    org = menumethods.cap_coords[0]
                    opt = [i for i in self.buttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.cap_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.cap_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.cap_coords)==1:
                    org = menumethods.cap_coords[0]
                    opt = [i for i in self.buttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.cap_coords)>=2:
                org = menumethods.cap_coords[0]
                end = menumethods.cap_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawcap(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawcap(org,end,w,"h","blue")
                self.insert("K")  
                
            if menumethods.wire_go and len(menumethods.wire_coords)<2:
                if len(menumethods.wire_coords)==1:
                    org = menumethods.wire_coords[0]
                    opt = [i for i in self.buttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.wire_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.wire_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.wire_coords)==1:
                    org = menumethods.wire_coords[0]
                    opt = [i for i in self.buttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    for i in opt:
                        i.configure(bg="green")  
                        
            if len(menumethods.wire_coords)>=2:
                col = self.wirecolor
                org = menumethods.wire_coords[0]
                end = menumethods.wire_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawwire(org,end,w,"v",col)
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawwire(org,end,w,"h",col)
                self.insert("K") 
                
            if menumethods.dip_go and len(menumethods.dip_coords)<2:
                if len(menumethods.dip_coords)==1:
                    org = menumethods.dip_coords[0]
                    if org[0]==8:
                        opt = [i for i in self.buttonlist if (i.xloc==10) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    if org[0]==10:
                        opt = [i for i in self.buttonlist if (i.xloc==10) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.dip_coords.append((w.xloc,w.yloc))
                elif w.xloc==8 or w.xloc==10:
                    menumethods.dip_coords.append((w.xloc,w.yloc))
                else:
                    print 'not appropriate location for a dip'
                
                if len(menumethods.dip_coords)==1:
                    org = menumethods.dip_coords[0]
                    if org[0]==8:                        
                        opt = [i for i in self.buttonlist if (i.xloc==10) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    elif org[0]==10:
                        opt = [i for i in self.buttonlist if (i.xloc==8) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.dip_coords)>=2:
                org = menumethods.dip_coords[0]
                end = menumethods.dip_coords[1]
                if org[0]==8:
                    if org[1]<end[1]:
                        self.drawdip(org,end,w,"d","black")
                    if org[1]>end[1]:
                        self.drawdip(org,end,w,"u","black")
                if org[0]==10:
                    temp = org
                    org = end
                    end = temp
                    if org[1]<end[1]:
                        self.drawdip(org,end,w,"d","black")
                    if org[1]>end[1]:
                        self.drawdip(org,end,w,"u","black") 
                self.insert("K")
        else:
            print "not adding at "+ "("+ str(w.xloc) + "," + str(w.yloc) + ")" + "!"
            
    def processscMouseEvent(self,event):
        w=event.widget
        if menumethods.add:
            if menumethods.res_go and len(menumethods.res_coordssc)<2:
                if len(menumethods.res_coordssc)==1:
                    org = menumethods.res_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-1,org[1])) or (i.getloc()==(org[0]+1,org[1])) or (i.getloc()==(org[0],org[1]+1)) or (i.getloc()==(org[0],org[1]-1))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg="black")
                        menumethods.res_coordssc.append((w.xloc,w.yloc))
                else:
                    menumethods.res_coordssc.append((w.xloc,w.yloc))
                
                if len(menumethods.res_coordssc)==1:
                    org = menumethods.res_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-1,org[1])) or (i.getloc()==(org[0]+1,org[1])) or (i.getloc()==(org[0],org[1]+1)) or (i.getloc()==(org[0],org[1]-1))]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.res_coordssc)>=2:
                org = menumethods.res_coordssc[0]
                end = menumethods.res_coordssc[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"v","red")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"h","red")
                self.insert("K")
                
            if menumethods.cap_go and len(menumethods.cap_coordssc)<2:
                if len(menumethods.cap_coordssc)==1:
                    org = menumethods.cap_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-1,org[1])) or (i.getloc()==(org[0]+1,org[1])) or (i.getloc()==(org[0],org[1]+1)) or (i.getloc()==(org[0],org[1]-1))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg="black")
                        menumethods.cap_coordssc.append((w.xloc,w.yloc))
                else:
                    menumethods.cap_coordssc.append((w.xloc,w.yloc))
                
                if len(menumethods.cap_coordssc)==1:
                    org = menumethods.cap_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-1,org[1])) or (i.getloc()==(org[0]+1,org[1])) or (i.getloc()==(org[0],org[1]+1)) or (i.getloc()==(org[0],org[1]-1))]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.cap_coordssc)>=2:
                org = menumethods.cap_coordssc[0]
                end = menumethods.cap_coordssc[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawcapsc(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawcapsc(org,end,w,"h","blue")
                self.insert("K") 
                
            if menumethods.wire_go and len(menumethods.wire_coordssc)<2:
                if len(menumethods.wire_coordssc)==1:
                    org = menumethods.wire_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg="black")
                        menumethods.wire_coordssc.append((w.xloc,w.yloc))
                else:
                    menumethods.wire_coordssc.append((w.xloc,w.yloc))
                
                if len(menumethods.wire_coordssc)==1:
                    org = menumethods.wire_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    for i in opt:
                        i.configure(bg="green")  
                        
            if len(menumethods.wire_coordssc)>=2:
                col = self.wirecolor
                org = menumethods.wire_coordssc[0]
                end = menumethods.wire_coordssc[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawwiresc(org,end,w,"v",col)
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawwiresc(org,end,w,"h",col)
                self.insert("K")
                
            if menumethods.dip_go and len(menumethods.dip_coordssc)<2:
                if len(menumethods.dip_coordssc)==1:
                    org = menumethods.dip_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0]+1 or i.xloc==org[0]-1) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg="black")
                        menumethods.dip_coordssc.append((w.xloc,w.yloc))
                else:
                    menumethods.dip_coordssc.append((w.xloc,w.yloc))
                
                if len(menumethods.dip_coordssc)==1:
                    org = menumethods.dip_coordssc[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0]+1 or i.xloc==org[0]-1) and (i.yloc==org[1]+(self.dipsize/2)-1 or i.yloc==org[1]-(self.dipsize/2)+1)]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.dip_coordssc)>=2:
                org = menumethods.dip_coordssc[0]
                end = menumethods.dip_coordssc[1]
                if org[0]<end[0]:
                    if org[1]<end[1]:
                        self.drawdipsc(org,end,w,"d","black")
                    if org[1]>end[1]:
                        self.drawdipsc(org,end,w,"u","black")
                if org[0]>end[0]:
                    temp = org
                    org = end
                    end = temp
                    if org[1]<end[1]:
                        self.drawdipsc(org,end,w,"d","black")
                    if org[1]>end[1]:
                        self.drawdipsc(org,end,w,"u","black") 
                self.insert("K")
        else:
            print "not adding at "+ "("+ str(w.xloc) + "," + str(w.yloc) + ")" + "!"
    
    def xpixtoloc(self,val,ident):
        if ident=="bb":
            return val/30
        elif ident=="sc":
            return (val+61)/73
        
    def xloctopix(self,val,ident):
        if ident=="bb":
            return val*30
        elif ident=="sc":
            return (val*73)-61
            
    def ypixtoloc(self,val,ident):
        if ident=="bb":
            return (val+22)/30
        elif ident=="sc":
            return (val+54)/65
        
    def yloctopix(self,val,ident):
        if ident=="bb":
            return (val*30)-22
        elif ident=="sc":
            return (val*65)-54

    def drawres(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"bb"),self.yloctopix(origin[1],"bb"))
        pixend=(self.xloctopix(end[0],"bb"),self.yloctopix(end[1],"bb"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill=c)
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)),text = str(self.resval),fill="white")
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)+16),text = self.resunits,fill="white")
            resbut = [i for i in self.buttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+17+5,pixorigin[1]+16+5,fill=c)
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,pixend[1]+8),text = str(self.resval)+" "+self.resunits,fill="white")
            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
        self.buttonlist = [i for i in self.buttonlist if i not in resbut]
        for i in resbut:
            i.destroy() 
            
    def drawcap(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"bb"),self.yloctopix(origin[1],"bb"))
        pixend=(self.xloctopix(end[0],"bb"),self.yloctopix(end[1],"bb"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill=c)
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)),text = str(self.capval),fill="white")
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)+16),text = self.capunits,fill="white")
            resbut = [i for i in self.buttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+17+5,pixorigin[1]+16+5,fill=c)
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,pixend[1]+8),text = str(self.capval)+" "+self.capunits,fill="white")
            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
        self.buttonlist = [i for i in self.buttonlist if i not in resbut]
        for i in resbut:
            i.destroy()
            
    def drawdip(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"bb"),self.yloctopix(origin[1],"bb"))
        pixend=(self.xloctopix(end[0],"bb"),self.yloctopix(end[1],"bb"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="u":
            w.parent.create_rectangle(pixorigin[0]-5,pixend[1]-5,pixend[0]+17+5,pixorigin[1]+16+5,fill=c)
            #w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[0]+pixend[0])/2)+8),text = str(self.resval)+" "+self.resunits,fill="white")
            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc<=origin[1] and i.yloc>=end[1]]
        elif orent=="d":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+17+5,pixend[1]+16+5,fill=c)
            #w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[0]+pixend[0])/2)+8),text = str(self.resval)+" "+self.resunits,fill="white")
            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc>=origin[1] and i.yloc<=end[1]]
        self.buttonlist = [i for i in self.buttonlist if i not in resbut]
        for i in resbut:
            i.destroy()
    
    def drawwire(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"bb"),self.yloctopix(origin[1],"bb"))
        pixend=(self.xloctopix(end[0],"bb"),self.yloctopix(end[1],"bb"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill=c)
            resbut = [i for i in self.buttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+17+5,pixorigin[1]+16+5,fill=c)
            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
        self.buttonlist = [i for i in self.buttonlist if i not in resbut]
        for i in resbut:
            i.destroy()
            
#draw functions for the schematic
    def drawressc(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"sc"),self.yloctopix(origin[1],"sc"))
        pixend=(self.xloctopix(end[0],"sc"),self.yloctopix(end[1],"sc"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixorigin[0]+13+7,pixend[1]+12+7,fill=c)
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)),text = str(self.resval),fill="white")
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)+16),text = self.resunits,fill="white")
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[0]+pixend[0])/2)+8),text = str(self.resval)+" "+self.resunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixend[0]+13+7,pixorigin[1]+12+7,fill=c)
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,pixend[1]+8),text = str(self.resval)+" "+self.resunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
#        self.scbuttonlist = [i for i in self.scbuttonlist if i not in resbut]
#        for i in resbut:
#            i.destroy()

    def drawcapsc(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"sc"),self.yloctopix(origin[1],"sc"))
        pixend=(self.xloctopix(end[0],"sc"),self.yloctopix(end[1],"sc"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixorigin[0]+13+7,pixend[1]+12+7,fill=c)
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)),text = str(self.capval),fill="white")
            w.parent.create_text((pixend[0]+8,((pixorigin[1]+pixend[1])/2)+16),text = self.capunits,fill="white")
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[0]+pixend[0])/2)+8),text = str(self.capval)+" "+self.capunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixend[0]+13+7,pixorigin[1]+12+7,fill=c)
            w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,pixend[1]+8),text = str(self.capval)+" "+self.capunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
#        self.scbuttonlist = [i for i in self.scbuttonlist if i not in resbut]
#        for i in resbut:
#            i.destroy()    

    def drawdipsc(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"sc"),self.yloctopix(origin[1],"sc"))
        pixend=(self.xloctopix(end[0],"sc"),self.yloctopix(end[1],"sc"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="u":
            w.parent.create_rectangle(pixorigin[0]-5,pixend[1]-5,pixend[0]+13+5,pixorigin[1]+12+5,fill=c)
            #w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[1]+pixend[1])/2)+8),text = str(self.resval)+" "+self.resunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc<=origin[1] and i.yloc>=end[1]]
        elif orent=="d":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+13+5,pixend[1]+12+5,fill=c)
            #w.parent.create_text((((pixorigin[0]+pixend[0])/2)+8,((pixorigin[1]+pixend[1])/2)+8),text = str(self.resval)+" "+self.resunits,fill="white")
#            resbut = [i for i in self.scbuttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc>=origin[1] and i.yloc<=end[1]]
#        self.scbuttonlist = [i for i in self.scbuttonlist if i not in resbut]
#        for i in resbut:
#            i.destroy()

    def drawwiresc(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0],"sc"),self.yloctopix(origin[1],"sc"))
        pixend=(self.xloctopix(end[0],"sc"),self.yloctopix(end[1],"sc"))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixorigin[0]+13+7,pixend[1]+12+7,fill=c)
#            resbut = [i for i in self.scbuttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-7,pixorigin[1]-7,pixend[0]+13+7,pixorigin[1]+12+7,fill=c)
#            resbut = [i for i in self.scbuttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
#        self.scbuttonlist = [i for i in self.buttonlist if i not in resbut]
#        for i in resbut:
#            i.destroy()
       
if __name__ == "__main__":
    app = gui(None)
    app.title('C.I.R.C.U.I.T')
    app.mainloop()