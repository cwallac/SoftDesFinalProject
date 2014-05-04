# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 03:25:57 2014

@author: dcelik
"""
import Tkinter as tk

class bbnode(tk.Button):
    def __init__(self,frame,x,y,c):
        self.xloc = x/30#self.xpixtoloc(x)
        self.yloc = (y+22)/30
        tk.Button.__init__(self,frame,bg=c)
        self.parent = frame
        self.height = 16
        self.width = 17
        self.xpix = x
        self.ypix = y
        self.place(x=self.xpix,y=self.ypix,height=self.height,width=self.width)
        
    def getloc(self):
        return (self.xloc,self.yloc)
class scnode(bbnode):
    def __init__(self,frame,x,y,c):
        bbnode.__init__(self,frame,x,y,c)
        self.height = 12
        self.width = 13
        self.xloc = (x+61)/73
        self.yloc = (y+54)/65
        self.place(x=self.xpix,y=self.ypix,height=self.height,width=self.width)
    def getloc(self):
        return (self.xloc,self.yloc) 
        
        