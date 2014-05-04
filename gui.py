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
RWIDTH  = 980
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
        self.viewsubMenu.add_checkbutton(label='Add Components', command = menumethods.addcomps)
        self.viewsubMenu.add_separator()
        self.viewsubMenu.add_radiobutton(label='Resistors', command=menumethods.insertResistor)
        self.viewsubMenu.add_radiobutton(label='Capacitors', command=menumethods.insertCapacitor)
        self.viewsubMenu.add_radiobutton(label='Dips', command=menumethods.insertDip)
        self.viewsubMenu.add_radiobutton(label='Wires', command=menumethods.insertWire)
        
        #tools submenu commands
        self.toolssubMenu.add_command(label='Move', command=self.quit)
        self.toolssubMenu.add_command(label='Rotate', command=self.quit)
        self.toolssubMenu.add_command(label='Erase', command=self.quit)
        self.toolssubMenu.add_command(label='Text', command=self.quit)
        
        #about submenu commands
        self.aboutsubMenu.add_command(label='About the Program', command=menumethods.aboutprog)
        self.aboutsubMenu.add_command(label='About the Creators',command=menumethods.aboutcreat)
        
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
        self.bbcanvas=tk.Canvas(self.parent,bg='white')
        self.bbcanvas.grid(column=1,row=0,sticky='NEWS')
        self.bbcanvas.configure(width=self.bbimagewidth+3,height=RHEIGHT)
        
        #create and place schematic canvas in grid
        self.scanvas=tk.Canvas(self.parent,bg='black')
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
        xrag = [i for i in range(120,450,30) if i!=270]
        for i in xrag:
            for j in range(8,800,30):
                n = nodes.bbnode(self.bbcanvas,i,j)
                n.bind("<Button-1>",self.processbbMouseEvent)
                self.buttonlist.append(n)
    
        yrag = [i for i in range(68,818,30) if i!=218 and i!=398 and i!=578 and i!=758]
        for i in [30,60,480,510]:
            for j in yrag:
                n=nodes.bbnode(self.bbcanvas,i,j)  
                n.bind("<Button-1>",self.processbbMouseEvent)
                self.buttonlist.append(n)
        self.DFTCLR = self.buttonlist[0].cget('bg')
        
        #adding buttons to scanvas
        xrag = [i for i in range(12,980,73)]
        yrag = [i for i in range(11,810,65)]
        for i in xrag:
            for j in yrag:
                n = nodes.scnode(self.scanvas,i,j)
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
                menumethods.res_coords=[]
                
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
                    self.drawres(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawres(org,end,w,"h","blue")
                menumethods.cap_coords=[]  
                
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
                org = menumethods.wire_coords[0]
                end = menumethods.wire_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawres(org,end,w,"v","yellow")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawres(org,end,w,"h","yellow")
                menumethods.wire_coords=[] 
                
            if menumethods.dip_go and len(menumethods.dip_coords)<2:
                if len(menumethods.dip_coords)==1:
                    org = menumethods.dip_coords[0]
                    if org[0]==8:
                        opt = [i for i in self.buttonlist if i.xloc==10]
                    if org[0]==10:
                        opt = [i for i in self.buttonlist if i.xloc==8]
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
                    opt = [i for i in self.buttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.dip_coords)>=2:
                org = menumethods.dip_coords[0]
                end = menumethods.dip_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawdip(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawdip(org,end,w,"h","blue")
                menumethods.dip_coords=[]
        else:
            print "not adding!"
            
    def processscMouseEvent(self,event):
        w=event.widget
        if menumethods.add:
            if menumethods.res_go and len(menumethods.res_coords)<2:
                if len(menumethods.res_coords)==1:
                    org = menumethods.res_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.res_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.res_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.res_coords)==1:
                    org = menumethods.res_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-1,org[1])) or (i.getloc()==(org[0]+1,org[1])) or (i.getloc()==(org[0],org[1]+1)) or (i.getloc()==(org[0],org[1]-1))]
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
                    self.drawressc(org,end,w,"v","red")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"h","red")
                menumethods.res_coords=[]
                
            if menumethods.cap_go and len(menumethods.cap_coords)<2:
                if len(menumethods.cap_coords)==1:
                    org = menumethods.cap_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.cap_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.cap_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.cap_coords)==1:
                    org = menumethods.cap_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.getloc()==(org[0]-2,org[1])) or (i.getloc()==(org[0]+2,org[1])) or (i.getloc()==(org[0],org[1]+2)) or (i.getloc()==(org[0],org[1]-2))]
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
                    self.drawressc(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"h","blue")
                menumethods.cap_coords=[]  
                
            if menumethods.wire_go and len(menumethods.wire_coords)<2:
                if len(menumethods.wire_coords)==1:
                    org = menumethods.wire_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    locs = [i.getloc() for i in opt]                
                    if (w.xloc,w.yloc) in locs:
                        for i in opt:
                            i.configure(bg=self.DFTCLR)
                        menumethods.wire_coords.append((w.xloc,w.yloc))
                else:
                    menumethods.wire_coords.append((w.xloc,w.yloc))
                
                if len(menumethods.wire_coords)==1:
                    org = menumethods.wire_coords[0]
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    for i in opt:
                        i.configure(bg="green")  
                        
            if len(menumethods.wire_coords)>=2:
                org = menumethods.wire_coords[0]
                end = menumethods.wire_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"v","yellow")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawressc(org,end,w,"h","yellow")
                menumethods.wire_coords=[] 
                
            if menumethods.dip_go and len(menumethods.dip_coords)<2:
                if len(menumethods.dip_coords)==1:
                    org = menumethods.dip_coords[0]
                    if org[0]==8:
                        opt = [i for i in self.scbuttonlist if i.xloc==10]
                    if org[0]==10:
                        opt = [i for i in self.scbuttonlist if i.xloc==8]
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
                    opt = [i for i in self.scbuttonlist if (i.xloc==org[0] or i.yloc==org[1]) and not i.getloc() == org]
                    for i in opt:
                        i.configure(bg="green")
                        
            if len(menumethods.dip_coords)>=2:
                org = menumethods.dip_coords[0]
                end = menumethods.dip_coords[1]
                if org[0]==end[0]:
                    if end[1]<org[1]:
                        temp = org
                        org = end
                        end = temp
                    self.drawdipsc(org,end,w,"v","blue")
                if org[1]==end[1]:
                    if end[0]<org[0]:
                        temp = org
                        org = end
                        end = temp
                    self.drawdipsc(org,end,w,"h","blue")
                menumethods.dip_coords=[]
        else:
            print "not adding!"
        
    def xpixtoloc(self,val):
#        v = val/30
#        if v>=3:
#            v-=1
#        if v>=8:
#            v-=1
#        if v>=13:
#            v-=1
        return val/30#v
        
    def xloctopix(self,val):
#        v = val
#        if v>=3:
#            v+=1
#        if v>=9:
#            v+=1
#        if v>=15:
#            v+=1
#        v = v*30
        return val*30#v
        
    def yloctopix(self,val):
        return (val*30)-22
        
    def ypixtoloc(self,val):
        return (val+22)/30

    def xpixtolocsc(self,val):
        return val/73

    def xloctopixsc(self,val):
        return val*73

    def ypixtolocsc(self,val):
        return (val+11)/65
    
    def yloctopixsc(self,val):
        return (val*65)-11

    def drawres(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopix(origin[0]),self.yloctopix(origin[1]))
        pixend=(self.xloctopix(end[0]),self.yloctopix(end[1]))
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
    def drawdip(self,origin,end,w,orent,c):
        self.drawres(self,origin,end,w,orent,c)
#draw functions for the schematic
    def drawressc(self,origin,end,w,orent,c):
        pixorigin=(self.xloctopixsc(origin[0]),self.yloctopixsc(origin[1]))
        pixend=(self.xloctopixsc(end[0]),self.yloctopixsc(end[1]))
        #w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill="red")     
        if orent=="v":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixorigin[0]+17+5,pixend[1]+16+5,fill=c)
#            resbut = [i for i in self.buttonlist if i.yloc>=origin[1] and i.yloc<=end[1] and i.xloc==origin[0]]
        elif orent=="h":
            w.parent.create_rectangle(pixorigin[0]-5,pixorigin[1]-5,pixend[0]+17+5,pixorigin[1]+16+5,fill=c)
#            resbut = [i for i in self.buttonlist if i.xloc>=origin[0] and i.xloc<=end[0] and i.yloc==origin[1]]
#        self.buttonlist = [i for i in self.buttonlist if i not in resbut]
#        for i in resbut:
#            i.destroy()   

    def drawdipsc(self,origin,end,w,orent,c):
        self.drawressc(self,origin,end,w,orent,c)
        
if __name__ == "__main__":
    app = gui(None)
    app.title('C.I.R.C.U.I.T')
    app.mainloop()