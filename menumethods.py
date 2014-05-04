# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:29:59 2014

@author: sgubba
"""
import Tkinter as tk

aboutprogopen = False
aboutcreatopen = False

def aboutprog():
    global aboutprogopen
    if not aboutprogopen:
        aboutprogopen = True
        
        popup = tk.Toplevel()
        popup.title("About this program")
        about_messageprog = "AN INTERACTIVE CIRCUIT DESIGN STUDIO SUITE FOR CREATION OF BREADBOARD AND SCHEMATIC PROTOTYPES."
    
        msg = tk.Message(popup,text=about_messageprog)
        msg.pack()
        
        button = tk.Button(popup,text="Close", command = lambda: aboutkill(popup,"p"))
        button.pack()

def aboutcreat():
    global aboutcreatopen
    if not aboutcreatopen:
        aboutcreatopen = True
        
        popup = tk.Toplevel()
        popup.title("About the creators")
        about_messagecreat = "CREATED BY DENIZ CELIK, SUBHASH GUBBA, CHRIS WALLACE, AND RADMER VAN DER HEYDE. ALL STUDENTS ARE FRESHMAN AT THE FRANKLIN W. OLIN COLLEGE OF ENGINEERING IN NEEDHAM, MA."        

        msg = tk.Message(popup,text=about_messagecreat)
        msg.pack()
        
        button = tk.Button(popup,text="Close", command = lambda: aboutkill(popup,"c"))
        button.pack()
        
def aboutkill(pp,ident):
    if ident=="p":   
        global aboutprogopen
        aboutprogopen = False
    elif ident=="c":
        global aboutcreatopen
        aboutcreatopen = False
    pp.destroy()    
        
about_messageSaveCheck = "Do you want to save your current project first?"
res_go=False
cap_go=False
dip_go=False
wire_go=False
add = False
res_coords=[]
res_coordssc=[]
cap_coords=[]
cap_coordssc=[]
dip_coords=[]
dip_coordssc=[]
wire_coords=[]
wire_coordssc=[]

def addcomps():
    global add
    add = not add
    
def insertResistor():
    global res_go
    temp = res_go
    clearall()
    res_go= not temp
    
def insertCapacitor():
    global cap_go
    temp = cap_go
    clearall()
    cap_go= not temp
    
def insertDip():
    global dip_go
    temp = dip_go
    clearall()
    dip_go= not temp
    
def insertWire():
    global wire_go
    temp = wire_go
    clearall()
    wire_go= not temp
    
def clearall():
    boolsfalse()
    coordsempty()
    
def boolsfalse():
    global res_go
    res_go=False
    global cap_go
    cap_go=False
    global dip_go
    dip_go=False
    global wire_go
    wire_go=False
    
def coordsempty():
    global res_coords
    res_coords=[]
    global res_coordssc
    res_coordssc=[]
    global cap_coords
    cap_coords=[]
    global cap_coordssc
    cap_coordssc=[]
    global dip_coords
    dip_coords=[]
    global dip_coordssc
    dip_coordssc=[]
    global wire_coords
    wire_coords=[]
    global wire_coordssc
    wire_coordssc=[]

def createNew():
    pass#if fileStatus == 'unsaved':
    #    msg = tk.Message(popup,text=self.about_messageSaveCheck)
    #    msg.pack()