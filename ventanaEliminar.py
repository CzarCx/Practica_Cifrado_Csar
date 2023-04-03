# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:02:02 2023

@author: César
"""
from tkinter import *
import tkinter as tk
#from tkinter.ttk import *


class Ventanaelim:
    def abrirEliminar():
        
        ventanaelim=Tk()
        ventanaelim.resizable(False,False)
        ventanaelim.title("Eliminar profesor")
        ventanaelim.geometry("500x300")
        ventanaelim.config(bg="#E2F9F9")

        miFrame=Frame() 
        miFrame.pack(fill="both", expand="True") 
        #miFrame.config(bg="white")
        miFrame.config(width="400",height="350") #tamaño del frame 
        miFrame.config(relief="groove") 
        miFrame.config(cursor="pirate")
        miFrame.config(bg="white")
        

        buscarzzz = Label(ventanaelim, text="ID del producto a eliminar:")
        buscarzzz.pack()
        buscarzzz.place(x=100, y=60)
        buscarzzz.config(bg="white", relief="flat")
            
        
        nota=Label(ventanaelim,text="Si el producto no existe, no funcionará.")
        nota.pack()
        nota.place(x=10,y=270)
        
        
        ebuscar=Entry(miFrame, highlightthickness=2)
        ebuscar.pack()
        ebuscar.place(x=100,y=90)
        ebuscar.config(highlightbackground = "black", highlightcolor= "red", relief="flat")
        
        
        def elimPro():
            xd="ID: "
            textbuscar=xd+ebuscar.get()
            with open("archivoProductos.txt", "r+") as archivop:
                lineas = archivop.readlines()
                for i, linea in enumerate(lineas):
                    linea = linea.strip()
                    if linea == textbuscar:
                        del lineas[i:i+4]
                        break  
                archivop.seek(0)
                archivop.writelines(lineas)
                archivop.truncate()
        def elimFa():
            xd="ID: "
            textbuscar=xd+ebuscar.get()
            with open("archivoFactura.txt", "r+") as archivop:
               lineas = archivop.readlines()
               for i, linea in enumerate(lineas):
                   linea = linea.strip()
                   if linea == textbuscar:
                       del lineas[i:i+3]
                       break  
               archivop.seek(0)
               archivop.writelines(lineas)
               archivop.truncate()
        def elimStock():
            uwu="ID: "
            textbuscar=uwu+ebuscar.get()
            with open("archivoStock.txt", "r+") as archivop:
                lineas = archivop.readlines()
                for i, linea in enumerate(lineas):
                    linea = linea.strip()
                    if linea == textbuscar:
                        del lineas[i:i+3]
                        messagebox.showinfo("", "Se ha eliminado el producto")
                        ebuscar.delete(0,END)
                        break  
                archivop.seek(0)
                archivop.writelines(lineas)
                archivop.truncate()
        
        def retro():
            ventanaelim.destroy()
            from ventanaRegitrarProduc import ventanaProducto
            ventanaProducto.abrirventana()
        

        botonVolver=Button(ventanaelim, text="Volver", command=retro)
        botonVolver.pack()
        botonVolver.place(x=420,y=260)
        
        botoneliminar3=Button(ventanaelim,text="Eliminar",command=lambda: [elimPro(),elimFa(),elimStock()])
        botoneliminar3.pack()
        botoneliminar3.place(x=100, y=120)
        
        mainloop()
