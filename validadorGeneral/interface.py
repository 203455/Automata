from ast import Str
from cProfile import label
from cgi import print_directory
from cgitb import text
from re import T
from tkinter import *
from tkinter import filedialog
import requests
from validador import particionarSentencia

automatasDatos = []

sentencias = []
bloquesIf = []

root = Tk()
root.title('IF VALIDATOR')
root.resizable(0,1)
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
    if valor == False:
        labelResultado.config(text="RECHAZADO", fg="red")
    labelResultado.pack()
    frame.pack()
    labelBloque.config(text=texto)
    labelBloque.pack()
        


def evaluar():
    for bloque in bloquesIf:
        print("EVALUAR")
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
    
def descargarArchivo():
    url = '7d/CONSIDERACIONES.pdf'
    myfile = requests.get(url)
    open('/d/7mo Cuatri/Lenguajes y Automatas/Automata/Reglas.pdf', 'wb').write(myfile.content)

indicaciones = Label(root,text="Ingresa el archivo python con sentencias if", pady=10)
indicaciones.pack()
botonSubir = Button(root, text="Subir Archivo", command=subirArchivo)
botonSubir.pack()
botonDescarga = Button(root, text="Descargar reglas", command=descargarArchivo)
botonDescarga.pack()

root.mainloop()