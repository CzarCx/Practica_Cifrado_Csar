# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:18:53 2023

@author: César
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Producto import RegistrarProductos
from Producto import ConsultarStock
from io import *

class ventanaProducto:
    def abrirventana():
        raiz=Tk()  
        raiz.title("Registrar y/o Modificar :D") 
        raiz.config(bg="#FFB4A4")
        raiz.resizable(False,False)
        raiz.geometry("700x400")
                 
        miFrame=Frame() 
        miFrame.pack(fill="both", expand="True")
        miFrame.config(bg="white")
        miFrame.config(width="500",height="400") 
        miFrame.config(bd=39) 
        miFrame.config(relief="groove") 
        miFrame.config(cursor="hand2")
         
        validate_entry = lambda text: text.isdecimal()
        validate_entry2 = lambda text: text.isalpha()
         
         #Etiquetaas
         
        title=Label(miFrame, text="Registrar y/o Modificar Productos", fg="black")
        title.pack()
        title.config(bg="white", relief="flat")
         
        ingresa=Label(miFrame, text="REGISTRAR", fg="black")
        ingresa.pack()
        ingresa.place(x=73, y=30)
        ingresa.config(bg="white", relief="flat")
         
        codeproducto=Label(miFrame, text="Codigo de Producto:", fg="black")
        codeproducto.pack()
        codeproducto.place(x=50, y=60)
        codeproducto.config(bg="white", relief="flat")
         
        cantiproduct=Label(miFrame, text="Cantidad:", fg="black")
        cantiproduct.pack()
        cantiproduct.place(x=50, y=120)
        cantiproduct.config(bg="white", relief="flat")
         
         
        nombreproduct=Label(miFrame, text="Nombre del producto:", fg="black")
        nombreproduct.pack()
        nombreproduct.place(x=50, y=180)
        nombreproduct.config(bg="white", relief="flat")
         
        pevpeproduct=Label(miFrame, text="Pvp:", fg="black")
        pevpeproduct.pack()
        pevpeproduct.place(x=50, y=240)
        pevpeproduct.config(bg="white", relief="flat")
        
        #Etiquetaas
        
        ingresa_m=Label(miFrame, text="MODIFICAR", fg="black")
        ingresa_m.pack()
        ingresa_m.place(x=483, y=30)
        ingresa_m.config(bg="white", relief="flat")
        
        codeproducto_m=Label(miFrame, text="Codigo de Producto:", fg="black")
        codeproducto_m.pack()
        codeproducto_m.place(x=460, y=60)
        codeproducto_m.config(bg="white", relief="flat")
        
        cantiproduct_m=Label(miFrame, text="Cantidad:", fg="black")
        cantiproduct_m.pack()
        cantiproduct_m.place(x=460, y=120)
        cantiproduct_m.config(bg="white", relief="flat")
       
        nameproduct_m=Label(miFrame, text="Producto:", fg="black")
        nameproduct_m.pack()
        nameproduct_m.place(x=460, y=180)
        nameproduct_m.config(bg="white", relief="flat")
        
        pevpeproduct_m=Label(miFrame, text="Pvp:", fg="black")
        pevpeproduct_m.pack()
        pevpeproduct_m.place(x=460, y=240)
        pevpeproduct_m.config(bg="white", relief="flat")
         
         #Cajas de texto 
         
        
        code=Entry(miFrame, highlightthickness=2, validate="key", validatecommand=(raiz.register(validate_entry), "%S") )
        code.pack()
        code.place(x=50,y=90)
        code.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
         
         
        produ=Entry(miFrame, highlightthickness=2)
        produ.pack()
        produ.place(x=50,y=210)
        produ.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
         
        pevpe=Entry(miFrame, highlightthickness=2, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        pevpe.pack()
        pevpe.place(x=50,y=270)
        pevpe.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
         
        canti=Entry(miFrame, highlightthickness=2, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        canti.pack()
        canti.place(x=50, y=150)
        canti.config(highlightbackground = "black", highlightcolor= "green", relief="flat", justify="center")
        
        code_m=Entry(miFrame, highlightthickness=2, )
        code_m.pack()
        code_m.place(x=460,y=90)
        code_m.config(highlightbackground = "black", highlightcolor= "yellow", relief="flat", justify="center", validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
         
        produ_m=Entry(miFrame, highlightthickness=2)
        produ_m.pack()
        produ_m.place(x=460,y=210)
        produ_m.config(highlightbackground = "black", highlightcolor= "yellow", relief="flat", justify="center")
        
        pevpe_m=Entry(miFrame, highlightthickness=2, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        pevpe_m.pack()
        pevpe_m.place(x=460,y=270)
        pevpe_m.config(highlightbackground = "black", highlightcolor= "yellow", relief="flat", justify="center")
         
        canti_m=Entry(miFrame, highlightthickness=2, validate="key", validatecommand=(raiz.register(validate_entry), "%S"))
        canti_m.pack()
        canti_m.place(x=460, y=150)
        canti_m.config(highlightbackground = "black", highlightcolor= "yellow", relief="flat", justify="center")
         
        
        
        def registrarProducto():
            
        
            codigo=code.get()
            producto=produ.get()
            pvp=pevpe.get()
            cantidad=canti.get()
            
            
            producto=producto.replace(" ", "")
        
            if codigo!="" and producto!="" and pvp!="" and cantidad!="":
                if len(codigo) <=3 and len(producto) < 20 and len(pvp) <= 4 and len(cantidad) <=4 and producto.isalpha() == True:
                    uwu="ID: "
                    textbuscar=uwu+code.get()
                    xd="Nombre del Producto: "
                    textbu=xd+produ.get()
                    with open("archivoProductos.txt", "r+") as archivof:
                        lineas = archivof.readlines()
                        for i, lineaa in enumerate(lineas):
                            lineaa = lineaa.strip()
                            if lineaa == textbuscar:
                                break
                    with open("archivoProductos.txt", "r+") as archivop:
                        lineas = archivop.readlines()
                        for i, linea in enumerate(lineas):
                            linea = linea.strip()
                            if linea == textbu:
                                break
                            
                        if lineaa == textbuscar:
                            tk.messagebox.showerror("Error","Ya existe un producto con ese codigo")
                        elif linea == textbu:
                            tk.messagebox.showerror("Error","Ya existe un producto con ese nombre")
                        elif linea != textbuscar and linea != textbu:
                            codigo=code.get()
                            produto=produ.get()
                            pvp=str(pevpe.get())
                            cantidad=str(canti.get())  
                            from Producto import RegistrarProductos
                            from Producto import ConsultarStock
                            from Producto import ConsultarFactura
                                
                            RegistrarProductos=RegistrarProductos(codigo,producto.title(),pvp)
                            RegistrarProductos.guardar()
                            ConsultarStock=ConsultarStock(codigo,cantidad)
                            ConsultarStock.guardarStock()
                            ConsultarFactura=ConsultarFactura(codigo,cantidad,pvp)
                            ConsultarFactura.guardarFactura()
                                
                            tk.messagebox.showinfo("Status","Se ha registrado el producto")
                                
                            codigo=code.delete(0, tk.END)
                            producto=produ.delete(0, tk.END)
                            pvp=pevpe.delete(0, tk.END)
                            cantidad=canti.delete(0, tk.END)
                                
                            from Producto import RegistrarProductos
                            from Producto import ConsultarStock
                            from Producto import ConsultarFactura
                    
                elif len(codigo) > 3:
                     tk.messagebox.showerror("Error","El codigo del producto solo puede tener 3 digitos")
                elif producto.isalpha() == False:
                     tk.messagebox.showerror("Error","No puede incluir numeros en el nombre del producto")
                elif len(cantidad) > 4:
                     tk.messagebox.showerror("Error","Verifique que la cantidad de productos agregados sea el correcto correcto")
                elif len(pvp) > 4:
                     tk.messagebox.showerror("Error","Verifique que el precio del producto sea correcto")

            else:
                tk.messagebox.showerror("Error","Verifique que todos los campos estén llenos")
               
        
        def consultar():
            archivo=open("archivoProductos.txt","r")
            registros=archivo.read()
            archivo.close()
            tk.messagebox.showinfo("Registros: ", registros)
        
        def consultarS():
            archivo=open("archivoStock.txt","r")
            registros=archivo.read()
            archivo.close()
            tk.messagebox.showinfo("Stock: ", registros)
            
        def consultarFactura():
            archivo=open("archivoFactura.txt","r")
            registros=archivo.read()
            archivo.close()
            tk.messagebox.showinfo("Factura: ", registros)
        
        def modificarPro():
            
            codigo=code_m.get()
            producto=produ_m.get()
            pvp=pevpe_m.get()
            cantidad=canti_m.get()
            
            
            producto=producto.replace(" ", "")
        
            
            if codigo!="" and producto!="" and pvp!="" and cantidad!="":
                if len(codigo) <=3 and len(producto) < 20 and len(pvp) <= 4 and len(cantidad) <=4 and producto.isalpha() == True:
                    uwu="ID: "
                    textbuscar=uwu+code_m.get()
                    with open("archivoProductos.txt", "r+") as archivop:
                        lineas = archivop.readlines()
                        for i, linea in enumerate(lineas):
                            linea = linea.strip()
                            if linea == textbuscar:
                                del lineas[i:i+4]
                                archivop.truncate()
                                break  
                        archivop.seek(0)
                        archivop.writelines(lineas)
                        archivop.truncate()
                        if linea == textbuscar:
                            codigo=code_m.get()
                            producto=produ_m.get()
                            pvp=str(pevpe_m.get())
                            from Producto import RegistrarProductos
                            RegistrarProductos=RegistrarProductos(codigo,producto.title(),pvp)
                            RegistrarProductos.guardar()
                            
                            codigo=code_m.delete(0, tk.END)
                            producto=produ_m.delete(0, tk.END)
                            pvp=pevpe_m.delete(0, tk.END)
                            cantidad=canti_m.delete(0, tk.END)
                        else:
                            tk.messagebox.showerror("Error","No se pudo encontrar el producto")
                elif len(codigo) > 3:
                    tk.messagebox.showerror("Error","El codigo del producto solo puede tener 3 digitos")
                elif producto.isalpha() == False:
                    tk.messagebox.showerror("Error","No puede incluir numeros en el nombre del producto")
                elif len(cantidad) > 4:
                    tk.messagebox.showerror("Error","Verifique que la cantidad de productos agregados sea el correcto correcto")
                elif len(pvp) > 4:
                    tk.messagebox.showerror("Error","Verifique que el precio del producto sea correcto")

            else:
                tk.messagebox.showerror("Error","Verifique que todos los campos estén llenos")
                

        def modificarStock():
            codigo=code_m.get()
            producto=produ_m.get()
            pvp=pevpe_m.get()
            cantidad=canti_m.get()
            
            
            producto=producto.replace(" ", "")
            if codigo!="" and producto!="" and pvp!="" and cantidad!="":
                if len(codigo) <=3 and len(producto) < 20 and len(pvp) <= 4 and len(cantidad) <=4 and producto.isalpha() == True:
                    uwu="ID: "
                    textbuscar=uwu+code_m.get()
                    with open("archivoStock.txt", "r+") as archivop:
                        lineas = archivop.readlines()
                        for i, linea in enumerate(lineas):
                            linea = linea.strip()
                            if linea == textbuscar:
                                del lineas[i:i+3]
                                tk.messagebox.showinfo("", "Se ha actualizado el producto")
                                archivop.truncate()
                                break  
                        archivop.seek(0)
                        archivop.writelines(lineas)
                        archivop.truncate()
                        if linea == textbuscar:
                            codigo=code_m.get()
                            cantidad=str(canti_m.get())  
                            from Producto import ConsultarStock
                            ConsultarStock=ConsultarStock(codigo,cantidad)
                            ConsultarStock.guardarStock()
                
    
        def modificarFactura():
            codigo=code_m.get()
            producto=produ_m.get()
            pvp=pevpe_m.get()
            cantidad=canti_m.get()
            
            
            producto=producto.replace(" ", "")
            
            if codigo!="" and producto!="" and pvp!="" and cantidad!="":
                if len(codigo) <=3 and len(producto) < 20 and len(pvp) <= 4 and len(cantidad) <=4 and producto.isalpha() == True:
                    codigo=code_m.get()
                    producto=produ_m.get()
                    pvp=pevpe_m.get()
                    cantidad=canti_m.get()
                    producto=producto.replace(" ", "")
                    
                    uwu="ID: "
                    textbuscar=uwu+code_m.get()
                    with open("archivoFactura.txt", "r+") as archivop:
                        lineas = archivop.readlines()
                        for i, linea in enumerate(lineas):
                            linea = linea.strip()
                            if linea == textbuscar:
                                del lineas[i:i+3]
                                archivop.truncate()
                                break  
                        archivop.seek(0)
                        archivop.writelines(lineas)
                        archivop.truncate()
                        if linea == textbuscar:
                            codigo=code_m.get()
                            cantidad=str(canti_m.get())
                            pvp=str(pevpe_m.get())
                            from Producto import ConsultarFactura
                            ConsultarFactura=ConsultarFactura(codigo,cantidad,pvp)
                            ConsultarFactura.guardarFactura()
        
        def acceso():
            raiz.destroy()
            from ventanaEliminar import Ventanaelim
            Ventanaelim.abrirEliminar()
            
            
        buton1=Button(miFrame, text="Registrar", command=registrarProducto, bg="green", fg="white")
        buton1.pack()
        buton1.place(x=250, y=130)
        
        buton2=Button(miFrame, text="Mostrar Registros", command=consultar)
        buton2.pack()
        buton2.place(x=260, y=180)
        
        buton3=Button(miFrame, text="Mostrar Stock", command=consultarS)
        buton3.pack()
        buton3.place(x=270, y=210)
        
        buton4=Button(miFrame, text="Consultar Factura", command=consultarFactura)
        buton4.pack()
        buton4.place(x=259, y=240)
        
        buton1=Button(miFrame, text="Modificar", command=lambda: [modificarStock(),modificarFactura(),modificarPro()], bg="yellow")
        buton1.pack()
        buton1.place(x=310, y=130)
        
        butonele=Button(miFrame, text="Eliminar", command=acceso, bg="red",  fg="white")
        butonele.pack()
        butonele.place(x=280, y=270)
         
        
        raiz.mainloop()

