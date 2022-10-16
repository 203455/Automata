
from curses import flash


items = []
transiciones = []

ifChecker = False
elseChecker = False
cuerpo = False
passChecker = False

validar = True


def capturarTransiciones(indicador):
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones"+str(indicador)+".txt", "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def particionarSentencia(bloque):
    for sentencia in bloque:
        items.clear()
        for i in sentencia:
            items.append(i)
        if validar == True:
            if ifChecker == False:
                ifChecker = True
                validar = validarSentencia(1)
            elif cuerpo == False:
                validar = validarSentencia(2)
            elif elseChecker == False:
                cuerpo = False
                if sentencia.starswith('els'):
                    elseChecker = True
                    validar = validarSentencia(3)
                else:
                    validar = validarSentencia(4)
                
    return validar

def obtenerParametros(indicador):
    parametros = []
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros"+str(indicador)+".txt", "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            parametros.append(str(palabra[1]))
    return parametros

def validarSentencia(indicador):
    resultado = False
    capturarTransiciones(indicador)
    parametros = obtenerParametros(indicador)
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
                resultado = True
                break
        else:
            print("Sentencia if invalida")
    else:
        print("Hubo un error, lo ingresado no es valido en el autómata")
    
    if indicador == 1:
        if actual == 'q100' or actual == 'q101':
                elseChecker = True
    elif indicador == 2:
        if actual == 'q7' or actual == 'q58':
            cuerpo = True
            
    return resultado
        
        