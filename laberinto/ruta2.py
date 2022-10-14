
def localizadorRuta(movimientos):
    rutaCorta = []
    for i in range(len(movimientos)):
        print(str(len(movimientos)))
        print(str(i))
        print(str(movimientos[i]))
        if movimientos[i]=="A":
            continuar = 1
            if movimientos[i-continuar]=="I" and movimientos[i+continuar]=="I":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="F"
            elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="D":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="F"
            elif movimientos[i-continuar]=="F" and movimientos[i+continuar]=="F":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="A"
            elif movimientos[i-continuar]=="I" and movimientos[i+continuar]=="D":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="A"
            elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="I":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="A"
            elif movimientos[i-continuar]=="F" and movimientos[i+continuar]=="I":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="D"
            elif movimientos[i-continuar]=="I" and movimientos[i+continuar]=="F":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="D"
            elif movimientos[i-continuar]=="D" and movimientos[i+continuar]=="F":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="I"
            elif movimientos[i-continuar]=="F" and movimientos[i+continuar]=="D":
                movimientos[i+continuar]="X"
                movimientos[i-continuar]="X"
                movimientos[continuar]="I"
            
            
    
    return movimientos
                

if __name__ == "__main__":
    movimientos = ["F", "I", "F","D", "F", "I","F", "F", "I","F", "A", "F","F", "F", "F","F", "F", "F","F", "F", "A", "F", "I", "F", "I", "A", "D", "F", "I", "F", "F", "I", "F", "I", "A", "D", "F", "I", "F", "F", "F", "I", "F" , "F", "I", "F", "I", "F", "I", "F", "F", "F", "I", "A", "I", "F", "F", "D", "F", "I", "F", "F", "F", "I", "F", "F", "F", "D", "F", "A", "F", "I", "F","F","F","F","F","F","F","I","F","F","I","F" ]
    movimientos = localizadorRuta(movimientos)
    print(movimientos)