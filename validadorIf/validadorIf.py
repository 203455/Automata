
items = []

diccionario = ["if", "not", "or", "and", "True", "False"]

numerosCero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numerosUno = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
letrasMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letrasMay = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "I", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def comparar(item):
    for dicc in diccionario:
        if item == dicc:
            return True
    return False

def definirItems():
    sentencia = input("Ingresa tu sentencia If \n")
    palabras = sentencia.split()
    for i in palabras:
        if comparar(i):
            items.append(i)
        else:
            if i == "True:":
                items.append("True")
                items.append(":")
            else:
                if i == "False:":
                    items.append("False")
                    items.append(":")
                else:
                    for caracter in i:
                        items.append(caracter)
    
    print(items)
    validadorIf()
        
            
        
    

def validarNumUno(item):
    for numeroUno in numerosUno:
        if item == numeroUno:
            return True
    return False

def validarNumCero(item):
    for numeroCero in numerosCero:
        if item == numeroCero:
            return True
    return False

def validarLetraMin(item):
    for letraMin in letrasMin:
        if item == letraMin:
            return True
    return False

def validarLetraMay(item):
    for letraMay in letrasMay:
        if item == letraMay:
            return True
    return False

def validadorIf():
    correcto = True
    incio = "A"
    fin = "L"
    actual = incio 
    finalizar = False
    contador = 0
    
    while finalizar == False:
        print(actual)
        print(items[contador])
        
        if actual == "A" :
            if items[contador] == "if" :
                actual="B"
                contador=contador+1
            else:
                correcto = False
                break
        elif actual == "B" :
            if items[contador] == "not" :
                actual="B"
                contador=contador+1
            else:
                if items[contador] == "True" or items[contador] == "False" :
                    actual="C"
                    contador=contador+1
                else:
                    if validarNumUno(items[contador]) == True :
                        actual="F"
                        contador=contador+1
                    else:
                        if validarLetraMin(items[contador]) == True :
                            actual="D"
                            contador=contador+1
                        else:
                            correcto=False
                            break
        elif actual == "C":
            if items[contador] == ":" :
                actual="L"
                contador=contador+1
            else:
                correcto=False
                break
        elif actual == "D":
            if items[contador] == "!" or items[contador] == "=":
                actual="I"
                contador=contador+1
            else:
                if items[contador] == "<" or items[contador] == ">":
                    actual="J"
                    contador=contador+1
                else:
                    if validarLetraMay(items[contador]) == True :
                        actual="D"
                        contador=contador+1
                    else:
                        if validarLetraMin(items[contador]) == True :
                            actual="E"
                            contador=contador+1
                        else:
                            if items[contador] == ":":
                                actual="L"
                            else:
                                correcto=False
                                break
        elif actual == "E":
            if items == "!" or items == "=":
                actual="I"
                contador=contador+1
            else:
                if items == "<" or items == ">":
                    actual="J"
                    contador=contador+1
                else:
                    if validarLetraMay(items[contador]) == True :
                        actual="E"
                        contador=contador+1
                    else:
                        if validarLetraMin(items[contador]) == True :
                            actual="D"
                            contador=contador+1
                        else:
                            if items[contador] == ":":
                                actual="L"
                            else:
                                correcto=False
                                break
        elif actual == "F" :
            if items[contador] == "!" or items[contador] == "=":
                actual="G"
                contador=contador+1
            else:
                if items[contador] == "<" or items[contador] == ">":
                    actual="H"
                    contador=contador+1
                else:
                    if validarNumCero(items[contador]) == True :
                        actual="F"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "G":
            if items[contador] == "=":
                actual="H"
                contador=contador+1
            else:
                correcto=False
                break
        elif actual == "H" :
            if items[contador] == "=":
                actual="H"
                contador=contador+1
            else:
                if validarNumUno(items[contador]) == True :
                    actual="K"
                    contador=contador+1
                else:
                    correcto=False
                    break
        elif actual == "I":
            if items[contador] == "=":
                actual="N"
                contador=contador+1
            else:
                correcto=False
                break
        elif actual == "J":
            if items[contador] == "=":
                actual="J"
                contador=contador+1
            else:
                if validarNumUno(items[contador]) == True :
                    actual="O"
                    contador=contador+1
                else:
                    correcto=False
                    break
        elif actual == "K":
            if items[contador] == ":":
                actual="L"
                contador=contador+1
            else:
                if items[contador] == "or" or items[contador] == "and":
                    actual="M"
                    contador=contador+1
                else:
                    if validarNumCero(items[contador]) == True :
                        actual="K"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "L":
            correcto=False
            break
        elif actual == "M":
            if items[contador] == "not":
                actual="M"
                contador=contador+1
            else:
                if validarNumUno(items[contador]) == True :
                    actual="F"
                    contador=contador+1
                else:
                    if validarLetraMin(items[contador]) == True :
                        actual="D"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "N":
            if items[contador] == '"':
                actual="Q"
                contador=contador+1
            else:
                if items[contador] == "True" or items[contador] == "False":
                    actual="P"
                    contador=contador+1
                else:
                    if validarNumUno(items[contador]) == True :
                        actual="O"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "O":
            if items[contador] == ":":
                actual="L"
                contador=contador+1
            else:
                if items[contador] == "or" or items[contador] == "and":
                    actual="M"
                    contador=contador+1
                else:
                    if validarNumCero(items[contador]) == True :
                        actual="O"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "P":
            if items[contador] == ":":
                actual="L"
                contador=contador+1
            else:
                if items[contador] == "or" or items[contador] == "and":
                    actual="M"
                    contador=contador+1
                else:
                    correcto=False
                    break
        elif actual == "Q": 
            if items[contador] == '"':
                actual="R"
                contador=contador+1
            else:
                if validarLetraMay(items[contador]) == True:
                    actual="Q"
                    contador=contador+1
                else:
                    if validarLetraMin(items[contador]) == True:
                        actual="Q"
                        contador=contador+1
                    else:
                        correcto=False
                        break
        elif actual == "R":
            if items[contador] == ":":
                actual="L"
                contador=contador+1
            else:
                if items[contador] == "or" or items[contador] == "and":
                    actual="M"
                    contador=contador+1
                else:
                    correcto=False
                    break
        
        if correcto == False:
            finalizar=True
        if contador >= len(items):
            finalizar=True
    
    if correcto == True:
        if actual == fin : 
            print("La sentencia ingresada es valida")
        else:
            print("La sentencia ingresada es invalida")
    else:
        print("Hubo un error, lo ingresado no es valido en el autómata")

if __name__ == "__main__":
    definirItems()
            