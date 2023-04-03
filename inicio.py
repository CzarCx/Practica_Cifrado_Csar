# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:53:08 2023

@author: César
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from io import *

class Inicio:
    def abrirventana():

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
        miFrame.config(width="400",height="350") #tamaño del frame 
        miFrame.config(bd=39)
        miFrame.config(relief="groove") 
        miFrame.config(cursor="pirate")
        
        inicio=Label(miFrame, text="Iniciar Sesión", font=("Agency FB",24) )
        inicio.pack()
        inicio.place(x=94, y=20)
        inicio.config(bg="white", relief="flat")
        
        usuario=Label(miFrame, text="Usuario", fg="black", font=("Agency FB",13))
        usuario.pack()
        usuario.place(x=140, y=70)
        usuario.config(bg="white", relief="flat")
        
        cajaus=Entry(miFrame, highlightthickness=2)
        cajaus.pack()
        cajaus.place(x=100,y=100)
        cajaus.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        passw=Label(miFrame, text="Contraseña", fg="black", font=("Agency FB",13))
        passw.pack()
        passw.place(x=128, y=150)
        passw.config(bg="white", relief="flat")
        
        
        cajapass=Entry(miFrame, highlightthickness=2, show="*")
        cajapass.pack()
        cajapass.place(x=95,y=180)
        cajapass.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        def buscar():
            if cajaus.get() != "" and cajapass.get()!="":
                textbuscar=cajaus.get()
                clavecon=694
                text_cifrado=''
                for letra in textbuscar:
                    if letra.isupper():
                        suma=ABC.find(letra)+clavecon
                        modulo=int(suma)%len(ABC)
                        text_cifrado=text_cifrado+str(ABC[modulo])
                    elif letra.islower():
                        suma=abc.find(letra) + clavecon
                        modulo=int(suma)%len(abc)
                        text_cifrado=text_cifrado+str(abc[modulo])
                    elif letra.isdigit():
                        suma=num.find(letra) + clavecon
                        modulo=int(suma)%len(num)
                        text_cifrado=text_cifrado+str(num[modulo])
                    elif letra.isascii():
                        suma=ascci.find(letra)+clavecon
                        modulo=int(suma)%len(ascci)
                        text_cifrado=text_cifrado+str(ascci[modulo])       
                print(textbuscar)
                with open("Nombre.txt", "r+") as archivog:
                    lineas = archivog.readlines()
                    for i, line in enumerate(lineas):
                        line = line.strip()
                        if line == text_cifrado:
                            break
                            
                    if line != text_cifrado:
                        tk.messagebox.showerror("Error","Usuario y/o Contraseña incorrectos")
                        caja1=cajaus.delete(0, tk.END)
                        caja2=cajapass.delete(0, tk.END)          
                            
                    archivog.seek(0)
                    archivog.writelines(lineas)
                    
                textbu=cajapass.get()
                clavecon=694
                contra_cifrada=''
                for letraa in textbu:
                    if letraa.isupper():
                        suma=ABC.find(letraa)+clavecon
                        modulo=int(suma)%len(ABC)
                        contra_cifrada=contra_cifrada+str(ABC[modulo])
                    elif letraa.islower():
                        suma=abc.find(letraa) + clavecon
                        modulo=int(suma)%len(abc)
                        contra_cifrada=contra_cifrada+str(abc[modulo])
                    elif letraa.isdigit():
                        suma=num.find(letraa) + clavecon
                        modulo=int(suma)%len(num)
                        contra_cifrada=contra_cifrada+str(num[modulo])
                    elif letraa.isascii():
                        suma=ascci.find(letraa)+clavecon
                        modulo=int(suma)%len(ascci)
                        contra_cifrada=contra_cifrada+str(ascci[modulo])       
                print(textbu)
                with open("Contraseñas.txt", "r+") as archivof:
                    lineas = archivof.readlines()
                    for i, linea in enumerate(lineas):
                        linea = linea.strip()
                        if linea == contra_cifrada and line == text_cifrado:
                            tk.messagebox.showinfo("Status","Haz iniciado sesión, bienvenid@")
                            acceso()
                            break
                    if linea != contra_cifrada:
                        tk.messagebox.showerror("Error","Los datos ingresados no coinciden con ningún registro")
                        caja1=cajaus.delete(0, tk.END)
                        caja2=cajapass.delete(0, tk.END)         
                        
                            
                    archivof.seek(0)
                    archivof.writelines(lineas)
            else:
                tk.messagebox.showerror("Error","Por favor llene todos los campos")
                

                
        def acceso():
                raiz.destroy()
                from ventanaRegitrarProduc import ventanaProducto
                ventanaProducto.abrirventana()
        
        def registro():
                raiz.destroy()
                from registro import Registrar
                Registrar.abrirventana()
            
        buton1=Button(text="Iniciar Sesión", command=buscar, font=("Agency FB",13))
        buton1.pack()
        buton1.place(x=110,y=255)
        
        butonuwu=Button(text="Registrarme", command=registro, font=("Agency FB",13))
        butonuwu.pack()
        butonuwu.place(x=210,y=255)
        
        
        
        
        
        
        
        
        
        
        raiz.mainloop() #Es como un </HTML>

