from nltk import CFG
from nltk import ChartParser
from nltk.tree import ParentedTree


cadenaEntrada = []
cadenaSalida = []
cadenaAuxiliar = []
items = []
transiciones = []

#Las siguientes direcciones deben ser cambiadas según sea el caso de usabilidad de manera local

transicionesUrls = ["D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley1.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley2.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley3.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley4.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley5.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/ley6.txt"]

parametrossUrls = ["D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey1.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey2.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey3.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey4.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey5.txt",
                    "D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosLey6.txt"]


def capturarTransiciones(indicador):
    transiciones.clear()
    with open(transicionesUrls[indicador-1], "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def obtenerParametros(indicador):
    parametros = []
    with open(parametrossUrls[indicador-1], "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            parametros.append(str(palabra[1]))
    return parametros

def itemsToCadena():
    cadenaEntrada.clear()
    cadenaSalida.clear()
    cadenaAuxiliar.clear()
    num = 0
    for i in range(20):
        cadenaEntrada.append('0')
        cadenaSalida.append('0')
        cadenaAuxiliar.append('0')
    
    for item in items:
        cadenaEntrada[num] = item
        num = num +1   
        
    print(cadenaEntrada) 

def mt(indicador):
    posicion1 = 0
    posicion2 = 0
    posicion3 = 0
    itemsToCadena()
    capturarTransiciones(indicador)
    parametros = obtenerParametros(indicador)
    inicial = str(parametros[1])
    cintas = str(parametros[0])
    finales = []
    inicio = 0
    for final in parametros:
        if inicio > 1:
            finales.append(str(final))
        inicio=inicio+1
    actual = inicial
    correcto=False
    finalizar = False
    contador = 0
    
    
    while finalizar == False:
        correcto = False
        
        print("Estado inicial" + actual + " Posicion 1 " + str(posicion1) + " Posicion 2 " + str(posicion2) + " POsicion 3 " + str(posicion3) + " Valor 1 " + cadenaEntrada[posicion1] + " " + cadenaSalida[posicion2] + " " + cadenaAuxiliar[posicion3] )
        
        if cintas == '2':
            for transicion in transiciones:
                t=transicion.split("-")
                if actual == t[0]:
                    if cadenaEntrada[posicion1] == t[1]:
                        if cadenaSalida[posicion2] == t[2]:
                            actual=t[3]
                            cadenaEntrada[posicion1] = t[4]
                            cadenaSalida[posicion2] = t[5]
                            if t[6] == 'D':
                                posicion1 = posicion1+1
                            elif t[6] == 'I':
                                posicion1 = posicion1-1
                            elif t[6] == 'S':
                                posicion1 = posicion1
                            
                            if t[7] == 'D':
                                posicion2 = posicion2+1
                            elif t[7] == 'I':
                                posicion2 = posicion2-1
                            elif t[7] == 'S':
                                posicion2 = posicion2
                            correcto=True
                            for fin in finales:
                                if actual == fin:
                                    finalizar = True
                                    break
                            break 
        if cintas == '3':
            for transicion in transiciones:
                t=transicion.split("-")
                if actual == t[0]:
                    if cadenaEntrada[posicion1] == t[1]:
                        if cadenaSalida[posicion2] == t[2]:
                            if cadenaAuxiliar[posicion3] == t[3]:
                                actual=t[4]
                                cadenaEntrada[posicion1] = t[5]
                                cadenaSalida[posicion2] = t[6]
                                cadenaAuxiliar[posicion3]= t[7]
                                if t[8] == 'D':
                                    posicion1 = posicion1+1
                                elif t[8] == 'I':
                                    posicion1 = posicion1-1
                                elif t[9] == 'S':
                                    posicion1 = posicion1
                                
                                if t[9] == 'D':
                                    posicion2 = posicion2+1
                                elif t[9] == 'I':
                                    posicion2 = posicion2-1
                                elif t[9] == 'S':
                                    posicion2 = posicion2
                                
                                if t[10] == 'D':
                                    posicion3 = posicion3+1
                                elif t[10] == 'I':
                                    posicion3 = posicion3-1
                                elif t[10] == 'S':
                                    posicion3 = posicion3
                                
                                correcto=True
                                for fin in finales:
                                    if actual == fin:
                                        finalizar = True
                                        break
                                break 
                
        if correcto == False:
            finalizar=True
    
    if correcto == True:
        print(cadenaSalida)
    else:
        print('No es posible')


def obtenerSentencia(tipo, sentencia):
    for i in sentencia:
        if i != " ":
            items.append(i)
    print(items)
    validar(tipo)
    

grammar = CFG.fromstring("""
    E -> L
    L -> I | N I | N L | I O I | P I O I F | P I F | P L O L F O L | L O P L O L F 
    I -> 'A' | 'B' | 'C' | 'D' | 'Z' | 'E'
    N -> '!' 
    P -> '('
    F -> ')'
    O -> 'u' | 'n' | 
""")

def validar(tipo):
    valor = False
    parser = ChartParser(grammar)
    sentencia = []
    for tree in parser.parse(items): 
        valor = True
        sentencia.append(tree)
        print(tree)
    print(sentencia)
    if valor == True: 
        mt(tipo)
        



if __name__ == "__main__":
    obtenerSentencia(3, '((AnB)uC)nD')
    pass