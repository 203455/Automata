from ast import Str
from cProfile import label
from cgi import print_directory
from cgitb import text
from re import T
from tkinter import *
from tkinter import filedialog
import requests
from validador import particionarSentencia


#user = 'c:/users/leona/' //Este dato puede ser cambiando para el uso local del tester / desarrollador

automatasDatos = []

sentencias = []
bloquesIf = []

root = Tk()
root.title('IF VALIDATOR')
root.resizable(0,1)
root.geometry("750x200")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.config(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

second_frame = Frame(canvas)

canvas.create_window((0,0), window=second_frame, anchor='nw')



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
    return
        
def imprimirResultado(valor, bloque):
    frame_position.forget()
    texto = ""
    for linea in bloque:
        texto=texto+linea
    labelResultado = Label(second_frame)
    frame = Frame(second_frame)
    labelBloque = Text(frame, width=90, height=30)
    if valor == True:
        labelResultado.config(text="APROBADO", fg="green")
    if valor == False:
        labelResultado.config(text="RECHAZADO", fg="red")
    labelResultado.pack()
    frame.pack()
    labelBloque.insert(INSERT, texto)
    labelBloque.config(state="disabled")
    labelBloque.pack()
    return
        


def evaluar():
    for bloque in bloquesIf:
        print("EVALUAR")
        valor = particionarSentencia(bloque)
        imprimirResultado(valor, bloque)
        
    return

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
    return 
 

def subirArchivo():
    archivo = filedialog.askopenfilename(title="abrir", filetypes=(("Archivos Python","*.py"),("Todos los archivos", "*.*")))
    leerArchivo(archivo)
    
indicaciones = Label(second_frame,text="archivo python con sentencias if", pady=10)
indicaciones.pack(side=TOP)
botonSubir = Button(second_frame, text="Subir Archivo", command=subirArchivo)
botonSubir.pack(side=TOP)

txt = ""
label_position = Label(second_frame)
frame_position = Frame(second_frame)
text_bloque = Text(frame_position, width=90, height=1)
frame_position.pack()
text_bloque.insert(INSERT, txt)
text_bloque.config(state="disabled")
text_bloque.pack()
#def descargarArchivo():
    #url = 'https://drive.google.com/file/d/1-zEBsmO2ukoXJOpfn1CajZY69JlHzH1E/view?usp=sharing'
    #myfile = requests.get(url, allow_redirects=True)
    #open(user+'downloads/REGLAS.pdf', 'wb').write(myfile.content)
#botonDescarga = Button(root, text="Descargar reglas", command=descargarArchivo)
#botonDescarga.pack()

root.mainloop()