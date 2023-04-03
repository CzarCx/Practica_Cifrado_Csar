# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:36:46 2023

@author: César
"""

from tkinter import *
import tkinter as tk

abc = 'abcdefghijklmnñopqrstuvwxyz'
ABC='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
num='1234567890'
ascci='!"#$%&()*+,-./:;<>=?@[]\^_`{}|~'


raiz=Tk()   
raiz.title("Inicio") #Titulo de la ventana
raiz.resizable(False,False)
raiz.config(bg="#FFB4A4")



miFrame=Frame() 
miFrame.pack(fill="both", expand="True") 
miFrame.config(bg="white")
miFrame.config(width="400",height="400") 
miFrame.config(bd=39)
miFrame.config(relief="groove") 
miFrame.config(cursor="pirate")

regis=Label(miFrame, text="Registrarme", font=("Agency FB",24) )
regis.pack()
regis.place(x=98,y=20)
regis.config(bg="white", relief="flat")

usuario=Label(miFrame, text="Usuario", fg="black", font=("Agency FB",13))
usuario.pack()
usuario.place(x=140, y=70)
usuario.config(bg="white", relief="flat")

cajaus=Entry(miFrame, highlightthickness=2)
cajaus.pack()
cajaus.place(x=100,y=100)
cajaus.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
cadenaus=cajaus.get()

passw=Label(miFrame, text="Contraseña", fg="black", font=("Agency FB",13))
passw.pack()
passw.place(x=128, y=150)
passw.config(bg="white", relief="flat")


cajapass=Entry(miFrame, highlightthickness=2, show="*")
cajapass.pack()
cajapass.place(x=95,y=180)
cajapass.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
cadenacon=cajapass.get()

def cifrarUsuario():
    if cajaus.get() != "" and cajapass.get!="":
         cadenaus=cajaus.get()
         claveus=694
         abc = 'abcdefghijklmnñopqrstuvwxyz'
         ABC='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
         num='1234567890'
         ascci='!"#$%&()*+,-./:;<>=?@[]\^_`{}|~'
         usu_cifrado=''
         for letra in cadenaus:
             if letra.isupper():
                 suma=ABC.find(letra)+claveus
                 modulo=int(suma)%len(ABC)
                 usu_cifrado=usu_cifrado+str(ABC[modulo])
             elif letra.islower():
                 suma=abc.find(letra)+claveus
                 modulo=int(suma)%len(abc)
                 usu_cifrado=usu_cifrado+str(abc[modulo])
             elif letra.isdigit():
                 suma=num.find(letra)+claveus
                 modulo=int(suma)%len(num)
                 usu_cifrado=usu_cifrado+str(num[modulo])
             elif letra.isascii():
                 suma=ascci.find(letra)+claveus
                 modulo=int(suma)%len(ascci)
                 usu_cifrado=usu_cifrado+str(ascci[modulo])
         
         tk.messagebox.showinfo("Status","Se ha registrado\n"+"Usuarios: "+cajaus.get()+"\nContraseña: "+cajapass.get())
         from Usuario import DatosUsu
         nombre=usu_cifrado
         DatosUsu=DatosUsu(nombre)
         DatosUsu.guardarCifradoU() 
    
         cajaus.delete(0, tk.END)
         cajapass.delete(0, tk.END)
    else:
        tk.messagebox.showerror("Error","Por favor llene todos los campos")
        


def cifrarContra():
    if cajaus.get() != "" and cajapass.get()!="":
        cadenacon=cajapass.get()
        clavecon=694
        abc = 'abcdefghijklmnñopqrstuvwxyz'
        ABC='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        num='1234567890'
        ascci='!"#$%&()*+,-./:;<>=?@[]\^_`{}|~'
        contra_cifrada=''
        for letra in cadenacon:
            if letra.isupper():
                suma=ABC.find(letra)+clavecon
                modulo=int(suma)%len(ABC)
                contra_cifrada=contra_cifrada+str(ABC[modulo])
    
            elif letra.islower():
                suma=abc.find(letra)+clavecon
                modulo=int(suma)%len(abc)
                contra_cifrada=contra_cifrada+str(abc[modulo])
    
            elif letra.isdigit():
                suma=num.find(letra)+clavecon
                modulo=int(suma)%len(num)
                contra_cifrada=contra_cifrada+str(num[modulo])
                
            elif letra.isascii():
                suma=ascci.find(letra)+clavecon
                modulo=int(suma)%len(ascci)
                contra_cifrada=contra_cifrada+str(ascci[modulo])  
    
        
        contra=contra_cifrada
        from Usuario import DatosContra
        DatosContra=DatosContra(contra)
        DatosContra.guardarCifradoC() 



def acceso():
    raiz.destroy()
    from inicio import Inicio
    Inicio.abrirventana()

butun=Button(miFrame,text="Registrar Cuenta", command=lambda: [cifrarContra(),cifrarUsuario()], font=("Agency FB",13))
butun.pack()
butun.place(x=114,y=220)
butun.config(cursor="hand2")

butun2=Button(miFrame,text="Ya tengo cuenta, Iniciar Sesión", command=acceso, font=("Agency FB",13))
butun2.pack()
butun2.place(x=76,y=260)
butun2.config(cursor="hand2")
raiz.mainloop() 