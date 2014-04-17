# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:29:59 2014

@author: sgubba
"""

about_messageSaveCheck = "Do you want to save your current project first?"
res_go=False
res_coords=[]

def insertResistor():
    global res_go
    res_go= not res_go
    global res_coords
    res_coords = []    
    print res_go
    
def insertCapacitor():
    pass#if cap_go:
        
def insertDip():
    pass#if dip_go:
        
def inserWire():
    pass#if wire_go:
        
def createNew():
    pass#if fileStatus == 'unsaved':
    #    msg = tk.Message(popup,text=self.about_messageSaveCheck)
    #    msg.pack()