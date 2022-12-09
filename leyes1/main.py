from nltk import CFG
from nltk import ChartParser
from nltk.parse.generate import generate
import random


cadenaEntrada = []
cadenaSalida = []
cadenaAuxiliar = []
cadenaEntradaRed = []
cadenaSalidaRed = []
cadenaA = [] 
cadenaB = []
cadenaC = []
items = []
transiciones = []

#Las siguientes direcciones deben ser cambiadas según sea el caso de usabilidad de manera local
transicionesReduccion = [
    'D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/reduccion2_6.txt'
]

parametrosreduccion = [
    'D:/7mo Cuatri/Lenguajes y Automatas/Automata/leyes1/parametrosReduccion2_6.txt'
]

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
            
def capturarTransicionesRed(indicador):
    transiciones.clear()
    with open(transicionesReduccion[indicador-1], "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def obtenerParametros(indicador):
    parametros = []
    with open(parametrossUrls[indicador-1], "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            parametros.append(str(palabra[1]))
    return parametros

def obtenerParametrosRed(indicador):
    parametros = []
    with open(parametrosreduccion[indicador-1], "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            parametros.append(str(palabra[1]))
    return parametros

def itemsToCadena():
    cadenaEntrada.clear()
    cadenaSalida.clear()
    cadenaAuxiliar.clear()
    cadenaEntradaRed.clear()
    cadenaSalidaRed.clear()
    cadenaA.clear()
    cadenaB.clear()
    cadenaC.clear()
    num = 0
    for i in range(50):
        cadenaEntrada.append('0')
        cadenaSalida.append('0')
        cadenaAuxiliar.append('0')
        cadenaEntradaRed.append('0')
        cadenaSalidaRed.append('0')
        cadenaA.append('0')
        cadenaB.append('0')
        cadenaC.append('0')
    
    for item in items:
        cadenaEntradaRed[num] = item
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
        resultado =  []
        result = ""
        for item in cadenaSalida:
            if item != "0":
                resultado.append(item)
            else:
                break
        result= ''.join(resultado)
        return result
    else:
        print('No es posible')
        return "No es posible hacer la operación"

def mtReduccion(indicador):
    posicion1 = 0
    posicion2 = 0
    posicion3 = 0
    posicion4 = 0
    posicion5 = 0
    itemsToCadena()
    capturarTransicionesRed(indicador)
    parametros = obtenerParametrosRed(indicador)
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
        print(actual)
        print(cintas)
        print(contador)
        print(cadenaEntradaRed)
        print(cadenaSalidaRed)
        print(cadenaA)
        print(cadenaB)
        if cintas == '3':
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
        if cintas == '4':
            for transicion in transiciones:
                t=transicion.split("-")
                if actual == t[0]:
                    if t[1] == 'contador':
                        if contador == 0:
                            actual=t[2]
                        else:
                            actual=t[3]
                        correcto=True
                        for fin in finales:
                            if actual == fin:
                                finalizar = True
                                break
                        break 
                        
                    else:
                        if cadenaEntradaRed[posicion1] == t[1]:
                            if cadenaSalidaRed[posicion2] == t[2]:
                                if cadenaA[posicion3] == t[3]:
                                    if cadenaB[posicion4] == t[4]:
                                        actual=t[5]
                                        cadenaEntradaRed[posicion1] = t[6]
                                        cadenaSalidaRed[posicion2] = t[7]
                                        cadenaA[posicion3]= t[8]
                                        cadenaB[posicion4] = t[9]
                                        if t[10] == 'D':
                                            posicion1 = posicion1+1
                                        elif t[10] == 'I':
                                            posicion1 = posicion1-1
                                        elif t[10] == 'S':
                                            posicion1 = posicion1
                                        
                                        if t[11] == 'D':
                                            posicion2 = posicion2+1
                                        elif t[11] == 'I':
                                            posicion2 = posicion2-1
                                        elif t[11] == 'S':
                                            posicion2 = posicion2
                                        
                                        if t[12] == 'D':
                                            posicion3 = posicion3+1
                                        elif t[12] == 'I':
                                            posicion3 = posicion3-1
                                        elif t[12] == 'S':
                                            posicion3 = posicion3
                                        
                                        if t[13] == 'D':
                                            posicion3 = posicion3+1
                                        elif t[13] == 'I':
                                            posicion3 = posicion3-1
                                        elif t[13] == 'S':
                                            posicion3 = posicion3
                                        
                                        if t[14] == 'M':
                                            contador = contador+1
                                        elif t[14] == 'm':
                                            contador = contador-1
                                        elif t[14] == 's':
                                            contador = contador
                                        
                                        correcto=True
                                        for fin in finales:
                                            if actual == fin:
                                                finalizar = True
                                                break
                                        break 
                
        if correcto == False:
            finalizar=True
    
    if correcto == True:
        resultado =  []
        result = ""
        for item in cadenaSalidaRed:
            if item != "0":
                resultado.append(item)
            else:
                break
        result= ''.join(resultado)
        print(result)
        return result
    else:
        print('No es posible')
        return "No es posible hacer la operación"


def obtenerSentencia(tipo, sentencia):
    items.clear()
    for i in sentencia:
        if i != " ":
            items.append(i)
    resultado = validar(tipo)
    return resultado
    

grammarOficial = CFG.fromstring("""
    E -> L
    L -> P I O I F O I | P I O I F  | P I F | P L O L F O L | L O P L O L F | I | I O I | N I | N L | P L O L F
    I -> 'A' | 'B' | 'C' | 'D' | 'Z' | 'E' | 'R' | 'S' | "T" | 'Q'
    N -> '!' 
    P -> '('
    F -> ')'
    O -> 'u' | 'n' | 
""")

grammarCorto = CFG.fromstring("""
    E -> L
    L -> I  | I O I | P I O I F O I | P I O I F  | P I F | P L O L F O L | L O P L O L F |  N I | N L | P L O L F 
    I -> 'A' | 'B' | 'C' | 'D' | 'Z' | 'E'
    N -> '!' 
    P -> '('
    F -> ')'
    O -> 'u' | 'n' | 
""")


def validar(tipo):
    num1 = random.randint(1,70)
    num2 = random.randint(71,100)
    iteracion = 0
    otros = []
    valor = False
    parser = ChartParser(grammarOficial)
    sentencia = []
    for tree in parser.parse(items): 
        valor = True
        sentencia.append(str(tree))
    if tipo > 3:
        for s in generate(grammarCorto, n=300):
            if iteracion == num1 or iteracion==num2:
                otros.append(s)
            iteracion = iteracion + 1
    else:
        for s in generate(grammarOficial, n=300):
            if iteracion == num1 or iteracion==num2:
                otros.append(s)
            iteracion = iteracion + 1
    if valor == True: 
        resultado = mtReduccion(tipo)
        return [[resultado, True], ["".join(otros[0]), False], ["".join(otros[1]), False]]
    
    return  [["No es posible obtener sentencia",True], ["".join(otros[0]), False],["".join(otros[0]), False]]
        



if __name__ == "__main__":
    resultados = obtenerSentencia(1, 'RuR')
    print(resultados)
    pass