

items = []
transiciones = []



def capturarTransiciones():
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones2.txt", "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def obtenerSentencia():
    sentencia = input("Ingresa tu sentencia \n")
    for i in sentencia:
        items.append(i)
    print(items)
    #validarSentencia()

def obtenerParametros():
    parametros = []
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros.txt", "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            parametros.append(str(palabra[1]))
    return parametros

def validarSentencia():
    capturarTransiciones()
    parametros = obtenerParametros()
    inicial = str(parametros[0])
    finales = []
    inicio = 0
    for final in parametros:
        if inicio > 0:
            finales.append(str(final))
        inicio=inicio+1
    actual = inicial
    correcto=False
    finalizar = False
    contador = 0
    
    
    while finalizar == False:
        correcto = False
        print("Estado actual: "+actual+" Valor actual: "+items[contador])
        
        for transicion in transiciones:
            t=transicion.split("-")
            if actual == t[0]:
                if items[contador] == t[1]:
                    actual=t[2]
                    contador=contador+1
                    correcto=True
                    break
        
        if correcto == False:
            finalizar=True
        if contador >= len(items):
            finalizar=True
    
    if correcto == True:
        for fin in finales:
            if actual == fin:
                print("Sentencia if valida")
                break
        else:
            print("Sentencia if invalida")
    else:
        print("Hubo un error, lo ingresado no es valido en el autómata")
                    
        


        

if __name__ == "__main__":
    obtenerSentencia()