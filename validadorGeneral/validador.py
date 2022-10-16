from cgitb import reset


items = []
transiciones = []

transicionesUrls = ["D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones1.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones2.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones3.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/transiciones4.txt"]

parametrossUrls = ["D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros1.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros2.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros3.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneral/parametros4.txt"]

class validaciones:
    def __init__(self):
        self.ifChecker = False
        self.elseChecker = False
        self.cuerpo = False
        self.passChecker = False
        self.validar = True

validador = validaciones()


def capturarTransiciones(indicador):
    transiciones.clear()
    with open(transicionesUrls[indicador-1], "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def resetValidador():
    validador.ifChecker = False
    validador.elseChecker = False
    validador.cuerpo = False
    validador.passChecker = False
    validador.validar = True

def particionarSentencia(bloque):
    resetValidador()
    for sentencia in bloque:
        items.clear()
        for i in sentencia:
            items.append(i)
        print(items)
        if validador.validar == True:
            if validador.ifChecker == False:
                validador.ifChecker = True
                validador.validar = validarSentencia(1)
            elif validador.cuerpo == False:
                validador.validar = validarSentencia(2)
            elif validador.elseChecker == False:
                validador.cuerpo = False
                if sentencia.starswith('els'):
                    validador.elseChecker = True
                    validador.validar = validarSentencia(3)
                else:
                    validador.validar = validarSentencia(4)
                
    return validador.validar

def obtenerParametros(indicador):
    parametros = []
    with open(parametrossUrls[indicador-1], "r") as archivo:
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
        print("Estado actual: " + actual + " Valor actual: "+ str(items[contador]))
        
        
        for transicion in transiciones:
            t=transicion.split("-")
            if actual == t[0]:
                print(t[0]+t[1]+t[2])
                if str(items[contador]) == '\n':
                    items[contador] = 'tab'
                if str(items[contador]) == str(t[1]):
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
                validador.elseChecker = True
    elif indicador == 2:
        if actual == 'q7' or actual == 'q58':
            validador.cuerpo = True
    return resultado
        
        