# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:12:29 2023

@author: César
"""

class DatosUsu:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def getNombre (self):
        return self.__nombre
     
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def guardarCifradoU(self):    
        archivo=open("Nombre.txt","a")
        archivo.write("\n")
        archivo.write(self.nombre)
        archivo.write("\n")
        archivo.close()
        

class DatosContra:
    def __init__(self, contra):
        self.contra=contra
        
    def getContra(self):
        return self.__contra
     
        
    def setContra(self,contra):
        self.__contra=contra
    

    def guardarCifradoC(self):    
        archivo=open("Contraseñas.txt","a")
        archivo.write("\n")
        archivo.write(self.contra)
        archivo.write("\n")
        archivo.close()