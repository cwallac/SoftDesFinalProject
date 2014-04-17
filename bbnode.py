# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 03:25:57 2014

@author: dcelik
"""
import gui
import ttk
import menumethods

class bbnode(ttk.Button):
    def __init__(self,frame,x,y):
        ttk.Button.__init__(self,frame,style='TCheckbutton')
        self.parent = frame
        self.height = 16
        self.width = 17
        self.xpix = x
        self.ypix = y
        self.xloc = self.xpixtoloc(x)
        self.yloc = self.ypixtoloc(y)
        self.place(x=self.xpix,y=self.ypix,height=self.height,width=self.width)
        self.bind("<Button-1>",self.processMouseEvent)
        
    def getloc(self):
        return (self.xloc,self.yloc)  

    def xpixtoloc(self,val):
        v = val/30
        if v>=3:
            v-=1
        if v>=8:
            v-=1
        if v>=13:
            v-=1
        return v
        
    def xloctopix(self,val):
        v = val
        if v>=3:
            v+=1
        if v>=8:
            v+=1
        if v>=13:
            v+=1
        v = v*30
        return v
        
    def yloctopix(self,val):
        return (val*30)-22
        
    def ypixtoloc(self,val):
        return (val+22)/30
        
    def processMouseEvent(self, event):
        coords= str(self.xloc) + ", " + str(self.yloc)
        print(coords)
        print menumethods.res_coords
        print menumethods.res_go
        if menumethods.res_go and len(menumethods.res_coords)<2:
            print "added!"
            menumethods.res_coords.append((self.xloc,self.yloc))
        if len(menumethods.res_coords)>=2:
            print "visual"
            origin = menumethods.res_coords[0]
            pixorigin=(self.xloctopix(origin[0]),self.yloctopix(origin[1]))
            end = menumethods.res_coords[1]
            pixend=(self.xloctopix(end[0]),self.yloctopix(end[1]))
            menumethods.res_coords=[]
            print origin
            print end
            print pixorigin
            print pixend
            self.parent.create_rectangle(pixorigin[0],pixorigin[1],pixorigin[0]+17,pixend[1]+16,fill="blue")
        
        