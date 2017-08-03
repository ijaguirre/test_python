def quedan_movimientos (tablero, x1,y1):#X es fila y es columna
    #Queda algun espacio libre en algun sitio
    #La pregunta es por lo que estan vacios, retona true si ambas piezas estan vacias y false si no estan vacias
    if 10 >x1 > 1 and 10 >y1 >1: #Bien para las situaciones donde aplica
        #Arriba
        arriba = check_pieza(tablero, x1-1, y1)
        abajo =  check_pieza(tablero, x1+1, y1)
        derecha = check_pieza(tablero, x1, y1+1)
        izquierda = check_pieza(tablero, x1, y1-1)
        arriba_derecha = check_pieza(tablero, x1-1, y1+1)
        arriba_izquierda = check_pieza(tablero, x1-1, y1-1)
        abajo_derecha = check_pieza(tablero, x1+1, y1+1)
        abajo_izquierda =  check_pieza(tablero, x1+1, y1-1)
        if arriba == True or abajo ==True or derecha == True or izquierda == True or arriba_derecha == True or arriba_izquierda == True or abajo_derecha == True or abajo_izquierda== True:
            return True
        else:
            return False

    elif x1==1 and 10 >y1 >1:#Caso de las b
        abajo = check_pieza(tablero, x1 + 1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        abajo_derecha = check_pieza(tablero, x1 + 1, y1 + 1)
        abajo_izquierda = check_pieza(tablero, x1 + 1, y1 - 1)
        if abajo ==True or derecha == True or izquierda == True or  abajo_derecha == True or abajo_izquierda== True:
            return True
        else:
            return False
    elif x1 == 10 and 10 >y1 >1:
        arriba = check_pieza(tablero, x1-1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        arriba_derecha = check_pieza(tablero, x1 - 1, y1 + 1)
        arriba_izquierda = check_pieza(tablero, x1 - 1, y1 - 1)
        if arriba == True or derecha == True or izquierda == True or arriba_derecha == True or arriba_izquierda == True:
            return True
        else:
            return False
    elif 10 >x1 > 1 and y1==1:
        arriba = check_pieza(tablero, x1 - 1, y1)
        abajo = check_pieza(tablero, x1 + 1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        arriba_derecha = check_pieza(tablero, x1 - 1, y1 + 1)
        abajo_derecha = check_pieza(tablero, x1 + 1, y1 + 1)
        if arriba == True or abajo ==True or derecha == True  or arriba_derecha == True or  abajo_derecha == True:
            return True
        else:
            return False
    elif 10 > x1 > 1 and y1 == 10:
        arriba = check_pieza(tablero, x1 - 1, y1)
        abajo = check_pieza(tablero, x1 + 1, y1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        arriba_izquierda = check_pieza(tablero, x1 - 1, y1 - 1)
        abajo_izquierda = check_pieza(tablero, x1 + 1, y1 - 1)
        if arriba == True or abajo == True or izquierda == True or  arriba_izquierda == True or abajo_izquierda == True:
            return True
        else:
            return False
    elif x1==1 and y1==1:#E
        abajo = check_pieza(tablero, x1 + 1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        abajo_derecha = check_pieza(tablero, x1 + 1, y1 + 1)
        if abajo == True or derecha == True or  abajo_derecha == True:
            return True
        else:
            return False
    elif x1==1 and y1==10: #F
        abajo = check_pieza(tablero, x1 + 1, y1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        abajo_izquierda = check_pieza(tablero, x1 + 1, y1 - 1)
        if abajo == True or  izquierda == True or abajo_izquierda == True:
            return True
        else:
            return False
    elif x1==10 and y1==1:#G
        arriba = check_pieza(tablero, x1 - 1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        arriba_derecha = check_pieza(tablero, x1 - 1, y1 + 1)
        if arriba == True or derecha == True or  arriba_derecha == True:
            return True
        else:
            return False
    elif x1==10 and y1 ==10:
        arriba = check_pieza(tablero, x1 - 1, y1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        arriba_izquierda = check_pieza(tablero, x1 - 1, y1 - 1)

        if arriba == True or izquierda == True or arriba_izquierda == True:
            return True
        else:
            return False




"""
tablero = [
    ["  ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ["10", 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'F'],
    ["9 ", 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'D'],
    ["8 ", 'C', 'A', '-', '-', '-', '-', '-', '-', 'A', 'D'],
    ["7 ", 'C', 'A', '-', '-', '-', '-', '-', '-', 'A', 'D'],
    ["6 ", 'C', 'A', '-', '-', '-', '-', '-', '-', 'A', 'D'],
    ["5 ", 'C', 'A', '-', 'A', '-', '-', '-', '-', 'A', 'D'],
    ["4 ", 'C', 'A', '-', '-', 'B', '-', '-', '-', 'A', 'D'],
    ["3 ", 'C', 'A', '-', '-', '-', '-', '-', '-', 'A', 'D'],
    ["2 ", 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'D'],
    ["1 ", 'G', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '-']
def quedan_movimientos(tablero, x1, y1):
    x2 = x1+1
    y2 = y1+ 1
    s = y1 + 1 #g1, g8
    mm = check_pieza(tablero, x2, y2)
"""