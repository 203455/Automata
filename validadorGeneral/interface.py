from tkinter import *
from tkinter import filedialog

sentencias = []
bloquesIf = []

root = Tk()
root.title('IF VALIDATOR')
root.resizable(0,0)
root.geometry("500x400")

def dividirBloques():
    auxiliar = []
    for sentencia in range(len(sentencias)):
        if sentencias[sentencia].startswith('if'):
            auxiliar.append(sentencias[sentencia])
            parar = False
            i=1
            while parar == False:
                if sentencias[sentencia].startswith('if'):
                    parar = True
                else:
                    auxiliar.append(sentencias[sentencia+i])
                    i=i+1
            bloquesIf.append(auxiliar)
            auxiliar.clear()
    print(bloquesIf)
        


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
    archivo = filedialog.askopenfilename(title="abrir", filetypes=(("Archivos Python","*.py"),("Todos los archivos", "*.*")))
    leerArchivo(archivo)

indicaciones = Label(root,text="Ingresa el archivo python con sentencias if")
indicaciones.pack()
botonSubir = Button(root, text="Subir Archivo", command=subirArchivo)
botonSubir.pack()

root.mainloop()