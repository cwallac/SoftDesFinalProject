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
res_coords=[]
cap_coords=[]
dip_coords=[]
wire_coords=[]

def insertResistor():
    clearall()
    global res_go
    res_go= True
    
def insertCapacitor():
    clearall()
    global cap_go
    cap_go= True
    
def insertDip():
    clearall()    
    global dip_go
    dip_go= True
    
def insertWire():
    clearall()    
    global wire_go
    wire_go= True
    
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
    global cap_coords
    cap_coords=[]
    global dip_coords
    dip_coords=[]
    global wire_coords
    wire_coords=[]
    
def createNew():
    pass#if fileStatus == 'unsaved':
    #    msg = tk.Message(popup,text=self.about_messageSaveCheck)
    #    msg.pack()