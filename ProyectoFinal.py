# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:43:31 2019

@author: Jesús Villa y Herrera, Mauricio Lozada, Alejandro Rubio López          INTEGRANTES
"""

from tkinter import *
import serial, time
import matplotlib.pyplot as plt

def Validar (lecturaMuestras):
    while True:
        try:
            int(lecturaMuestras)
            return int(lecturaMuestras)
            break
        except ValueError:
            return 0
    
def Arduino(lectura):
    arduino = serial.Serial('COM3', 9600)
    time.sleep(4)
    muestras=lectura[1]
    arduino.write(str(muestras).encode())
    muestra=[]
    for i in range(muestras):
        muestra.append(arduino.readline())                  
    arduino.close()
    for i in range(len(muestra)):
        muestra[i]=str(muestra[i])
        muestra[i]=muestra[i].replace("\\r\\n","")
        muestra[i]=muestra[i].replace("b'","")
        muestra[i]=muestra[i].replace("'","")
    #print (muestra)
    return muestra



def Archivo (lecturaArchivo, lista):
    archivo = open(lecturaArchivo, "w")
    for i in range(len(lista)):
        if i < len(lista)-1:
            archivo.write(lista[i])
            archivo.write(" ")
        else:
            archivo.write(lista[i])
    archivo.close()
        
def Leer ():
        lectura=[]
        lecturaArchivo= nArchivo.get()
        lecturaMuestras= nMuestras.get()
        #print(lecturaMuestras)
        #nMuestras.delete(0, len(lecturaMuestras))
        if Validar(lecturaMuestras) == 0:
            nMuestras.delete(0, len(lecturaMuestras))
            messagebox.showinfo("Mensaje", "Formato de muestras no válido.\nDa un número correcto")
            
        else:
            #lectura=[lecturaArchivo, int(lecturaMuestras)]
            #lista = Arduino (lectura)
            #print (type(lista[2]))
            bGuardar.pack(side = RIGHT)
            messagebox.showinfo("Mensaje", "Datos leídos con éxito")
            
def Guardar():
    nombreArchivo= nArchivo.get()
    Muestras= nMuestras.get()
    lectura=[nombreArchivo, int(Muestras)]
    lista = Arduino (lectura)
    #print (lista)
    Archivo (nombreArchivo, lista)
    messagebox.showinfo("Mensaje", "Datos guardados con éxito")
    bGraficar.pack(side = BOTTOM)
    etiqueta.pack()
       
def Graficar ():
    archivo = open (nArchivo.get(),"r")
    numeros = archivo.readline()
    archivo.close
    graf = numeros.split(" ")
    for i in range(len(graf)):
        graf[i]=int(graf[i])
    plt.plot(graf)
    plt.xlabel("Número de datos")
    plt.ylabel("Valor")
    plt.show()
    
ventana = Tk()

frame = Frame(ventana)
frame.pack(padx=20, pady=20)

label1 = Label(frame, text = "Nombre Archivo:")
label1.pack(side=TOP)

nArchivo = Entry (frame)
nArchivo.pack()

label2 = Label(frame, text = "Número de muestras:")
label2.pack()

nMuestras = Entry (frame)
nMuestras.pack()

bLeer = Button(frame, text = "Leer", command = Leer)
bLeer.pack(side = LEFT)

bGuardar = Button(frame, text = "Guardar", command = Guardar)

bGraficar = Button(frame, text = "Graficar", command = Graficar)

etiqueta = Label(frame, text = "\n\n")

ventana.mainloop()  


