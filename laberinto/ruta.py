
def localizadorRuta(movimientos):
    rutaCorta = []
    ciclo = True
    i = 0
    while ciclo == True:
        print(str(i))
        print(str(movimientos[i]))
        if movimientos[i]=="A":
            detener = False
            continuar = 1
            if movimientos[i-continuar]=="I" and movimientos[i+continuar]=="I":
                detener = True
            elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="D":
                detener = True
            else:
                movimientos[i]="X"
                while(detener==False):
                    if movimientos[i-continuar]=="F" and movimientos[i+continuar]=="F":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="X"
                        continuar = continuar +1
                    elif movimientos[i-continuar]=="A" and movimientos[i+continuar]=="A":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="X"
                        continuar = continuar +1
                    elif movimientos[i-continuar]=="I" and movimientos[i+continuar]=="D":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="X"
                        continuar = continuar +1
                    elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="I":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="X"
                        continuar = continuar +1
                    elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="D":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="F"
                        detener=True
                        break
                    elif movimientos[i-continuar]=="I" and movimientos[i+continuar]=="I":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="F"
                        detener=True
                        break
                    elif movimientos[i-continuar]=="F" and movimientos[i+continuar]=="I":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="D"
                        detener=True
                        break
                    elif movimientos[i-continuar]=="I" and movimientos[i+continuar]=="F":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="D"
                        detener=True
                        break
                    elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="F":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="I"
                        detener=True
                        break
                    elif movimientos[i-continuar]=="F" and movimientos[i+continuar]=="D":
                        movimientos[i+continuar]="X"
                        movimientos[i-continuar]="I"
                        detener=True
                        break
                for nuevo in range(len(movimientos)):
                    if str(movimientos[nuevo])!="X":
                        rutaCorta.append(movimientos[nuevo])
                ciclo = False
        if i >= (len(movimientos)-1):
            ciclo = False
        i=i+1
    if len(rutaCorta) > 0:
        movimientos = localizadorRuta(rutaCorta)
    
    return movimientos
                

if __name__ == "__main__":
    movimientos = ["F", "I", "F","D", "F", "I","F", "F", "I","F", "A", "F","D", "F", "F","D", "F", "I","F", "I", "F", "F", "F", "I", "A", "I", "F", "F", "D", "F", "I", "F", "F", "F", "I", "F", "F", "F", "D", "F", "A", "F", "I" , "F", "F", "F", "D", "F", "F", "F", "D", "F", "I", "F", "F", "D", "A", "D", "F", "F", "F", "I", "F", "I", "F", "F", "D", "F", "I", "F" ]
    movimientos = localizadorRuta(movimientos)
    print(movimientos)