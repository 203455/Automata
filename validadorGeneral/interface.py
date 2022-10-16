from ast import Str
from cProfile import label
from cgitb import text
from re import T
from tkinter import *
from tkinter import filedialog

from validador import particionarSentencia

automatasDatos = []

sentencias = []
bloquesIf = []

root = Tk()
root.title('IF VALIDATOR')
root.resizable(0,0)
root.geometry("500x400")



def dividirBloques():
    for n in range(len(sentencias)):
        auxiliar = []
        if sentencias[n].startswith('if'):
            auxiliar.append(sentencias[n])
            i=1
            print("FALTAN POR RECORRER. "+str(len(sentencias)-n))
            while i < (len(sentencias)-n):
                if sentencias[n+i].startswith('if'):
                    i=len(sentencias)
                    break
                else:
                    auxiliar.append(sentencias[n+i])
                    i=i+1
            print(auxiliar)  
            bloquesIf.append(auxiliar)
    print(bloquesIf)
    evaluar()
        
def imprimirResultado(valor, bloque):
    texto = ""
    for linea in bloque:
        texto=texto+linea
    labelResultado = Label(root)
    frame = Frame(root)
    labelBloque = Label(frame, anchor="e", justify=LEFT )
    if valor == True:
        labelResultado.config(text="APROBADO", fg="green")
        labelResultado.pack()
        frame.pack()
        labelBloque.config(text=texto)
        labelBloque.pack()


def evaluar():
    for bloque in bloquesIf:
        valor = particionarSentencia(bloque)
        imprimirResultado(valor, bloque)

def leerArchivo(archivo):
    encontrado=False 
    with open(archivo, "r") as arch:
        for linea in arch:
            if linea.startswith('if'):
                sentencias.append(linea)
                encontrado=True
            elif encontrado==True:
                if linea.startswith('    '):
                    sentencias.append(linea)
                elif linea.startswith('elif') or linea.startswith('else'):
                    sentencias.append(linea)
                else:
                    encontrado=False  
    print(sentencias)             
    dividirBloques()  
                

def subirArchivo():
    botonSubir.config(state="disabled")
    archivo = filedialog.askopenfilename(title="abrir", filetypes=(("Archivos Python","*.py"),("Todos los archivos", "*.*")))
    leerArchivo(archivo)

indicaciones = Label(root,text="Ingresa el archivo python con sentencias if", pady=10)
indicaciones.pack()
botonSubir = Button(root, text="Subir Archivo", command=subirArchivo)
botonSubir.pack()

root.mainloop()