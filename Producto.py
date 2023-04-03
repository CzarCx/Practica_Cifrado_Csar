# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:03:43 2023

@author: César
"""

class RegistrarProductos:
    def __init__(self,codigo,producto,pvp):
        self.codigo=codigo
        self.producto=producto
        self.pvp=pvp
        
    def getCodigo(self):
        return self.__codigo
        
    def getProducto (self):
        return self.__producto
        
    def getPvp (self):
        return self.__pvp

        
        
    def setCodigo(self,codigo):
        self.__codigo=codigo
        
    def setProducto (self,producto):
        self.__producto=producto
        
    def setPvp (self,pvp):
        self.__pvp=pvp
            
    def guardar(self): 
                
        archivo=open("archivoProductos.txt","a")
        archivo.write("\n")
        archivo.write("ID: " + self.codigo)
        archivo.write("\n")
        archivo.write("Nombre del Producto: " + self.producto)
        archivo.write("\n")
        archivo.write("Pvp: " + self.pvp)
        archivo.write("\n")

        archivo.close()
         
class ConsultarStock:
    def __init__(self,codigo,cantidad):
        self.codigo=codigo
        self.cantidad=cantidad
    
    def getCodigo(self):
         return self.__codigo
     
    def getCantidad (self):
         return self.__cantidad
    
    def setCodigo(self,codigo):
        self.__codigo=codigo
        
    def setCantidad(self,cantidad):
        self.__cantidad=cantidad
    
    
    def guardarStock(self): 
                 
        archivo=open("archivoStock.txt","a")
        archivo.write("\n")
        archivo.write("ID: " + self.codigo)
        archivo.write("\n")
        archivo.write("Cantidad: " + self.cantidad)
        archivo.write("\n")
        archivo.close()
    
class ConsultarFactura:
    def __init__(self,codigo,cantidad,pvp):
        self.codigo=codigo
        self.cantidad=cantidad
        self.pvp=pvp

        
    def getCodigo(self):
         return self.__codigo
     
    def getCantidad (self):
         return self.__cantidad
    
    def getPvp (self):
        return self.__pvp
        
    
    def setCodigo(self,codigo):
        self.__codigo=codigo
        
    def setCantidad(self,cantidad):
        self.__cantidad=cantidad

    def setPvp (self,pvp):
        self.__pvp=pvp
    
    
    def guardarFactura(self): 
            archivo=open("archivoFactura.txt","a")
            archivo.write("\n")
            archivo.write("ID: " + self.codigo)
            archivo.write("\n")
            archivo.write("Total: "  +str(float(self.pvp)*int(self.cantidad)))
            archivo.write("\n")
            archivo.close()