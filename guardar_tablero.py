import os
def inverso_columna(num):
    colu = ""
    if num==1:
        colu="a"
    elif num==2:
        colu="b"
    elif num==3:
        colu="c"
    elif num==4:
        colu="d"
    elif num==5:
        colu="e"
    elif num==6:
        colu="f"
    elif num==7:
        colu="g"
    elif num==8:
        colu="h"
    elif num==9:
        colu="i"
    elif num==10:
        colu="j"
    return colu

def inverso_fila(num):
    fill = ""
    if num==1:
        fill="10"
    elif num==2:
        fill="9"
    elif num==3:
        fill="8"
    elif num==4:
        fill="7"
    elif num==5:
        fill="6"
    elif num == 6:
        fill = "5"
    elif num == 7:
        fill = "4"
    elif num == 8:
        fill = "3"
    elif num == 9:
        fill = "2"
    elif num == 10:
        fill = "1"
    return fill

"""
   a b c d e f g h i j
10 - - X Y * - - * X Y
9  - - * * X - - * * *
8  * - - * - * - - * -
7  - - * - - * * * - -
6  - - - - * - - - * -
5  * * - * * * * * - -
4  - * * * - * - * - *
3  * * - * * * X * * *
2  Y * * * - * Y * - *
1  * * * - - * * * * *

"""

def guardar_tablero(tablero):
    lista_piezas_a = [] #Solo para las piezas con X
    fu = 1
    while fu < 11: #Fu es fila y cu columna
        cu = 1
        while cu < 11:
            if tablero[fu][cu] == "X":
                FILA = inverso_fila(fu)
                COLUMNA = inverso_columna(cu)
                #print(fu, cu, FILA + COLUMNA)
                fila_mas_columna= FILA+COLUMNA
                lista_piezas_a.append(fila_mas_columna)
            # print(tab[fu][cu], fu, cu)
            cu += 1
        fu += 1

    lista_piezas_b = []
    fo = 1
    while fo < 11:  # Fo es fila y co columna
        co = 1
        while co < 11:
            if tablero[fo][co] == "Y":
                FILA = inverso_fila(fo)
                COLUMNA = inverso_columna(co)
                # print(fu, cu, FILA + COLUMNA)
                fila_mas_columna =  COLUMNA + FILA
                lista_piezas_b.append(fila_mas_columna)
            # print(tab[fu][cu], fu, cu)
            co += 1
        fo += 1

    lista_piezas_c = []#Flechas
    fa = 1
    while fa < 11:  # Fa es fila y ca columna
        ca = 1
        while ca < 11:
            if tablero[fa][ca] == "*":
                FILA = inverso_fila(fa)
                COLUMNA = inverso_columna(ca)
                # print(fu, cu, FILA + COLUMNA)
                fila_mas_columna = COLUMNA + FILA
                lista_piezas_c.append(fila_mas_columna)
            # print(tab[fu][cu], fu, cu)
            ca += 1
        fa += 1

    new = open('nuevo_tablero.txt', 'w')
    a_join = ",".join(lista_piezas_a)
    new.write(a_join)
    b_join = ",".join(lista_piezas_b)
    new.write("\n")
    new.write(b_join)
    new.write("\n")
    c_join = ",".join(lista_piezas_c)
    new.write(c_join)
    new.write("\n")
    turno_jugador = str(turno)
    new.write(turno_jugador)

    new.close()

    pass

turno = 1
tab = [['  ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
       ['10', 'X', '-', 'X', 'Y', '*', '-', '-', '*', 'X', 'Y'],
       ['9 ', '-', '-', '*', '*', 'X', '-', '-', '*', '*', '*'],
       ['8 ', '*', '-', '-', '*', '-', '*', '-', '-', '*', '-'],
       ['7 ', '-', '-', '*', '-', '-', '*', '*', '*', '-', '-'],
       ['6 ', '-', '-', '-', '-', '*', '-', '-', '-', '*', 'X'],
       ['5 ', '*', '*', '-', '*', '*', '*', '*', '*', '-', '-'],
       ['4 ', '-', '*', '*', '*', '-', '*', '-', '*', '-', '*'],
       ['3 ', '*', '*', '-', '*', '*', '*', 'X', '*', '*', '*'],
       ['2 ', 'Y', '*', '*', '*', '-', '*', 'Y', '*', '-', '*'],
       ['1 ', '*', '*', '*', '-', '-', '*', '*', '*', '*', '*']]

#Hay que guardar cada pieza por separado, o sea, pieza 1, pieza2, flecha

(guardar_tablero(tab))

