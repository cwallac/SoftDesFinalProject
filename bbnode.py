# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 03:25:57 2014

@author: dcelik
"""
import Tkinter as tk
import ttk
from PIL import Image, ImageTk

class bbnode(ttk.Button):
    def __init__(self,frame,x,y):
        ttk.Button.__init__(self,frame,style='TCheckbutton')
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
        
    def ypixtoloc(self,val):
        return (val+22)/30
        
    def processMouseEvent(self, event):
        coords= str(self.xloc) + ", " + str(self.yloc)
        print(coords)
        
        