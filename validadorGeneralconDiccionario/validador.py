items = []
transiciones = []
diccionario = []

    

def capturarTransiciones():
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneralconDiccionario/transiciones2.txt", "r") as archivo:
        for linea in archivo:
            transiciones.append(str(linea))

def obtenerDiccionario():
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneralconDiccionario/diccionario2.txt", "r") as archivo:
        for linea in archivo:
            palabra=linea.split("-")
            diccionario.append(str(palabra[1]))

def comparar(item):
    for dicc in diccionario:
        if str(item) == str(dicc):
            return True
    return False

def obtenerSentencia(dato):
    obtenerDiccionario()
    sentencia = input("Ingresa tu sentencia \n")
    palabras = sentencia.split()
    for i in palabras:
        if comparar(i):
            items.append(i)
        else:
            for caracter in i:
                items.append(caracter)
    validarSentencia()

def obtenerParametros():
    parametros = []
    with open("D:/7mo Cuatri/Lenguajes y Automatas/Automata/validadorGeneralconDiccionario/parametros.txt", "r") as archivo:
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
                print("Sentencia valida")
                break
        else:
            print("Sentencia invalida")
    else:
        print("Hubo un error, lo ingresado no es valido en el autómata (no encontró la ruta adecuada)")
                    
        


        

if __name__ == "__main__":
    obtenerSentencia("Hola")
    pass