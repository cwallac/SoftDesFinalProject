# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 03:25:57 2014

@author: dcelik
"""
import Tkinter as tk

class bbnode(tk.Button):
    def __init__(self,frame,x,y):
        self.xloc = x/30#self.xpixtoloc(x)
        self.yloc = (y+22)/30
        tk.Button.__init__(self,frame)
        self.parent = frame
        self.height = 16
        self.width = 17
        self.xpix = x
        self.ypix = y
        self.place(x=self.xpix,y=self.ypix,height=self.height,width=self.width)
        
    def getloc(self):
        return (self.xloc,self.yloc)
class scnode(bbnode):
    def __init__(self,frame,x,y):
        bbnode.__init__(self,frame,x,y)
        self.height = 7
        self.width = 8
        self.xloc = x/30
        self.yloc = y/30
        self.place(x=self.xpix,y=self.ypix,height=self.height,width=self.width)
    def getloc(self):
        return (self.xloc,self.yloc) 
#    def xpixtoloc(self,val):
#        v = val/30
#        if v>=3:
#            v-=1
#        if v>=8:
#            v-=1
#        if v>=13:
#            v-=1
#        return v    
        
        