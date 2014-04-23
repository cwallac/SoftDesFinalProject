# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:29:59 2014

@author: sgubba
"""

about_messageSaveCheck = "Do you want to save your current project first?"
res_go=False
cap_go=False
dip_go=False
wire_go=False
res_coords=[]
cap_coords=[]
dip_coords=[]
wire_coords=[]

def insertResistor():
    global res_go
    res_go= not res_go
    global res_coords
    res_coords = []    
    print res_go
    
def insertCapacitor():
    global cap_go
    cap_go= not cap_go
    global cap_coords
    cap_coords = []
    print cap_coords
    
def insertDip():
    pass#if dip_go:
    global dip_go
    dip_go= not dip_go
    global dip_coords
    dip_coords = []
    print dip_coords
    
def inserWire():
    pass#if dip_go:
    global wire_go
    wire_go= not wire_go
    global wire_coords
    wire_coords = []
    print wire_coords
        
def createNew():
    pass#if fileStatus == 'unsaved':
    #    msg = tk.Message(popup,text=self.about_messageSaveCheck)
    #    msg.pack()