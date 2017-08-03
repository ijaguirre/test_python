# Se recomienda ejecutar el juego en IDLES como PyCharm, www.replit.com, Python Command Line o Python IDLE por Linux
import os


def saludo():
    print(
        "Se recomienda ejecutar el juego en IDLES como PyCharm, www.replit.com, Python Command Line o Python IDLE por Linux\n")
    print("\n== == == AMAZONAS - T2 IIC1103 == == ==")
    print("Bienvenido a Amazonas!")


def opciones_inicio():
    print("\nLas opciones de inicio son:")
    print("1 Empezar nuevo tablero")
    print("2 Cargar partida guardada")


def despedida(ganador):
    print("\n== == == AMAZONAS - T2 IIC1103 == == ==")
    print("Se ha cerrado el juego")  # Aquí después viene el ganador y/o el perdedor
    print("El ganador es", ganador)


def cambiar_columna(ingreso):
    letra = ingreso[0]
    letra = letra.lower()
    columna = 0
    if letra == "a":
        columna = 1
    elif letra == "b":
        columna = 2
    elif letra == "c":
        columna = 3
    elif letra == "d":
        columna = 4
    elif letra == "e":
        columna = 5
    elif letra == "f":
        columna = 6
    elif letra == "g":
        columna = 7
    elif letra == "h":
        columna = 8
    elif letra == "i":
        columna = 9
    elif letra == "j":
        columna = 10
    return columna


def cambiar_fila(ingreso):
    fila = 0
    if len(ingreso) == 2:
        num = ingreso[1]
        if num == "1":
            fila = 10
        elif num == "2":
            fila = 9
        elif num == "3":
            fila = 8
        elif num == "4":
            fila = 7
        elif num == "5":
            fila = 6
        elif num == "6":
            fila = 5
        elif num == "7":
            fila = 4
        elif num == "8":
            fila = 3
        elif num == "9":
            fila = 2
    elif len(ingreso) == 3:
        if ingreso[1] == "1" and ingreso[2] == "0":
            fila = 1
    return fila

def leyenda():
    print("Piezas X --> ", j1, "Piezas Y -->", j2, "Flechas: * ")

def tablero_to_string(tablero):
    for i in tablero:
        i = list(i)
        b = " ".join(i)
        print(b)
    print("")
    leyenda()
    print("")

def cargar_tablero():
    turno = 0
    piezas_1 = []
    piezas_2 = []
    flechas_inicio = []

    lista_listas = []
    anterior = open("tablero.txt")
    temp0 = anterior.readlines()
    anterior.seek(0)
    temp1 = (anterior.readline())
    temp2 = temp1.strip("\n")
    piezas_1 = temp2.split(",")  # Ready
    lista_listas.append(piezas_1)
    temp3 = (anterior.readline())
    temp4 = temp3.strip("\n")
    piezas_2 = temp4.split(",")
    lista_listas.append(piezas_2)
    temp5 = (anterior.readline())
    temp6 = temp5.strip("\n")
    flechas_inicio = temp6.split(",")
    lista_listas.append(flechas_inicio)
    turno = int((anterior.readline()))
    lista_listas.append(turno)
    anterior.close()
    return lista_listas

def nuevo_tablero():
    tablero = [
        ["  ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        ["10", '-', '-', '-', 'Y', '-', '-', 'Y', '-', '-', '-'],
        ["9 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["8 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["7 ", 'Y', '-', '-', '-', '-', '-', '-', '-', '-', 'Y'],
        ["6 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["5 ", '-', '-', '-', '-', 'X', '-', '-', '-', '-', '-'],
        ["4 ", 'X', '-', '-', '-', '-', '-', '-', '-', '-', 'X'],
        ["3 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["2 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["1 ", '-', '-', '-', 'X', '-', '-', 'X', '-', '-', '-']
    ]
    return tablero

def inverso_columna(num):
    colu = ""
    if num == 1:
        colu = "a"
    elif num == 2:
        colu = "b"
    elif num == 3:
        colu = "c"
    elif num == 4:
        colu = "d"
    elif num == 5:
        colu = "e"
    elif num == 6:
        colu = "f"
    elif num == 7:
        colu = "g"
    elif num == 8:
        colu = "h"
    elif num == 9:
        colu = "i"
    elif num == 10:
        colu = "j"
    return colu

def inverso_fila(num):
    fill = ""
    if num == 1:
        fill = "10"
    elif num == 2:
        fill = "9"
    elif num == 3:
        fill = "8"
    elif num == 4:
        fill = "7"
    elif num == 5:
        fill = "6"
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


def revisar_orden(cadena):
    letra = False
    num = False
    total = False
    la = cadena[0]
    l = la.lower()
    if l == "a" or l == "b" or l == "c" or l == "d" or l == "e" or l == "f" or l == "g" or l == "h" or l == "i" or l == "j":
        letra = True
    else:
        letra = False
    if len(cadena) == 2:
        n = cadena[1]

        if n == "1" or n == "2"  or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
            num = True
        else:
            num = False
    elif len(cadena) == 3:
        u = cadena[1]
        n = cadena[2]
        uno = u + n

        if uno == "10":
            num = True
        else:
            num = False
    else:
        num = False
    if letra == True and num == True:
        total = True
    else:
        total = False
    return total


def guardar_tablero(tablero):
    lista_piezas_a = []  # Solo para las piezas con X
    fu = 1
    while fu < 11:  # Fu es fila y cu columna
        cu = 1
        while cu < 11:
            if tablero[fu][cu] == "X":
                FILA = inverso_fila(fu)
                COLUMNA = inverso_columna(cu)
                # print(fu, cu, FILA + COLUMNA)
                fila_mas_columna = FILA + COLUMNA
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
                fila_mas_columna = COLUMNA + FILA
                lista_piezas_b.append(fila_mas_columna)
            # print(tab[fu][cu], fu, cu)
            co += 1
        fo += 1

    lista_piezas_c = []  # Flechas
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


def menu():
    print("Que deseas hacer:  ")
    print("1. Ingresar un movimiento ")
    print("2. Guardar el juego")
    print("3. Terminar el juego (Gana el otro)\n")


def old_tablero(viejo):
    piezas_a = viejo[0]
    largo_a = len(piezas_a)

    for w in range(largo_a):
        c = int(cambiar_columna(piezas_a[w]))
        f = int(cambiar_fila(piezas_a[w]))
        # print(c,f)
        # print(tablero_blanco[f][c])#ok
        tablero_blanco[f][c] = "X"  # Piezasa jugador 1
        tablero_to_2 = tablero_blanco  # Interesante
        # tablero_to_string(tablero_to_2)
    piezas_b = viejo[1]
    largo_b = len(piezas_b)
    # print(piezas_b, largo_b)
    for e in range(largo_b):
        c = int(cambiar_columna(piezas_b[e]))
        f = int(cambiar_fila(piezas_b[e]))
        # print(c,f)
        # print(tablero_blanco[f][c])#ok
        tablero_to_2[f][c] = "Y"  # Piezasa jugador 1
        tablero_to_3 = tablero_to_2

    piezas_c = viejo[2]
    largo_c = len(piezas_c)

    for r in range(largo_c):
        c = int(cambiar_columna(piezas_c[r]))
        f = int(cambiar_fila(piezas_c[r]))
        tablero_to_3[f][c] = "*"

        tablero_juego = tablero_to_3

    return tablero_juego

def check_pieza(tablero, x, y):
    if tablero[x][y] == "-":
        return True
    else:
        return False
    pass
    # return True o False si hay pieza en x, y


def movimiento_valido(tablero, x1, y1, x2, y2):
    s = y1 + 1 #g1, g8
    mm = check_pieza(tablero, x2, y2)
    if x1 == x2 and y2 > y1 and mm == True:  # La pieza nueva esta más a la derecha
        while s < y2 + 1:
            se_puede = check_pieza(tablero, x1, s)
            # print(se_puede, s)
            s += 1

            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 == x2 and y2 < y1 and mm == True:  # La pieza nueva estaria mas hacia la izquierda
        d = y1 -1
        while d > y2 :
            se_puede = check_pieza(tablero, x1, d)
            d -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True
    elif y1 == y2 and x2 > x1 and mm == True:  # Esta más abajo
        z = x1 + 1
        while z < x2 + 1:
            se_puede = check_pieza(tablero, z, y1)
            z += 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif y1 == y2 and x2 < x1 and mm == True:  # Esta mas arriba Mejorado
        v = x1 -1    #Decia x1
        print (v)
        while v >= x2 :
            se_puede = check_pieza(tablero, v, y1)
            v -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1<x2 and y1<y2 and ((x2-x1)== (y2-y1)) and mm == True:########### Ready!!!! Este movimiento es abajo a la derecha

        o = 1
        mm = check_pieza(tablero,x2,y2)
        while x1+o<x2 and y1+o<y2:
            se_puede= check_pieza(tablero,x1+o,y1+o)
            o+=1
            if se_puede == False:
                return False
            else:
                pass

        return True

    elif x1>x2 and y1>y2 and ((x1-x2)==(y1-y2)) and mm == True: #############De verdad esta lista, y es arriba a la izquierda
        p = x1-x2
        mm = check_pieza(tablero,x2,y2)
        while x1-p>x2 and x1-p>y2:
            se_puede = check_pieza(tablero,x1-p,y1-p)
            p-=1
            if se_puede ==False:
                return False
            else:
                pass
        return True


    elif x1>x2 and y1<y2 and ((x1-x2)==(y2-y1)) and mm == True:#Arriba a la derecha
        s = 1
        while x1-s>x2 and y1+s <y2: #como nunca entra retorna true igual
            se_puede = check_pieza(tablero,x1-s,y1+s)
            s+=1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1<x2 and y1>y2 and ((x2-x1)==(y1-y2))and mm == True:
        s = 1
        while x1+s < x2 and y1-s >y2:
            se_puede = check_pieza(tablero,x1+s,y1-s)
            s+=1
            if se_puede == False:
                return False
            else:
                pass
        return True



    else:
        return False

def lanzamiento_valido(tablero, x1, y1, x2, y2):
    s = y1 + 1
    mm = check_pieza(tablero, x2, y2)

    if x1 == x2 and y2 > y1 and mm == True:  # La pieza nueva esta más a la derecha

        print(x1, y1, x2, y2, s)
        while s < y2 + 1:
            se_puede = check_pieza(tablero, x1, s)
            # print(se_puede, s)
            s += 1

            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 == x2 and y2 < y1 and mm == True:  # La pieza nueva estaria mas hacia la izquierda
        d = y1 -1
        while d > y2 :
            se_puede = check_pieza(tablero, x1, d)
            d -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True
    elif y1 == y2 and x2 > x1 and mm == True:  # Esta más abajo
        z = x1 + 1
        while z < x2 + 1:
            se_puede = check_pieza(tablero, z, y1)
            z += 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif y1 == y2 and x2 < x1 and mm == True:  # Esta mas arriba Mejorado
        v = x1 - 1 
        print (v)
        while v > x2 + 1:
            se_puede = check_pieza(tablero, v, y1)
            v -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 < x2 and y1 < y2 and (
        (x2 - x1) == (y2 - y1)) and mm == True:  ########### Ready!!!! Este movimiento es abajo a la derecha

        o = 1
        mm = check_pieza(tablero, x2, y2)
        print("x1<x2 and y1<y2")
        while x1 + o < x2 and y1 + o < y2:
            se_puede = check_pieza(tablero, x1 + o, y1 + o)
            print(se_puede, x1 + o, y1 + o, "and o", o)
            o += 1
            if se_puede == False:
                return False
            else:
                pass

        return True

    elif x1 > x2 and y1 > y2 and (
        (x1 - x2) == (y1 - y2)) and mm == True:  #############De verdad esta lista, y es arriba a la izquierda
        print("entro")
        p = x1 - x2
        mm = check_pieza(tablero, x2, y2)
        print("x1>x2 and y1>y2")
        while x1 - p > x2 and x1 - p > y2:
            se_puede = check_pieza(tablero, x1 - p, y1 - p)
            print(se_puede, x1 - p, y1 - p, p)
            p -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True


    elif x1 > x2 and y1 < y2 and ((x1 - x2) == (y2 - y1)) and mm == True:  # Arriba a la derecha
        print("Arriba a la derecha")
        s = 1
        while x1 - s > x2 and y1 + s < y2:  # como nunca entra retorna true igual
            se_puede = check_pieza(tablero, x1 - s, y1 + s)
            s += 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 < x2 and y1 > y2 and ((x2 - x1) == (y1 - y2)) and mm == True:
        print("Abajo a la izquierda")
        s = 1
        while x1 + s < x2 and y1 - s > y2:
            se_puede = check_pieza(tablero, x1 + s, y1 - s)
            s += 1
            if se_puede == False:
                return False
            else:
                pass
        return True



    else:
        return False


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

def perdedor(tablero):
    if turno == 1:
        buscar = "X"
    else:
        buscar = "Y"
    lista_x = []
    lista_y = []
    f = 1
    while f < 11:  # Fu es fila y cu columna
        c = 1
        while c < 11:
            if tablero[f][c] == buscar:
                lista_x.append(f)
                lista_x.append(c)
            c += 1
        f += 1
    print(lista_x)


    x1 = quedan_movimientos (tablero, lista_x[0],lista_x[1])#True es que si puedo jugar con ella
    x2 = quedan_movimientos (tablero, lista_x[2],lista_x[3])#False es que no puedo jugar con esta pieza
    x3 = quedan_movimientos (tablero, lista_x[4],lista_x[5])
    x4 = quedan_movimientos (tablero, lista_x[6],lista_x[7])
    if x1 == False and x2 == False and x3 == False and x4 == False:
        return False #No tiene mas movimientos
    else:
        return True


# Variables
turno = 0
tablero_blanco = [
    ["  ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ["10", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["9 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["8 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["7 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["6 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["5 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["4 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["3 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["2 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ["1 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
]

# Main ---Esta parte antes de los turnos esta super


saludo()  # Saludo del juego
j1 = "Rocio"  # input("Diga nombre del jugador 1: ")
j2 = "Ignacio"  # input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = input("Que quiere hacer (elija el numero de la opcion): ")
# Este input ya permite ingresar cualquier cosa sin los errores que no te deja convertir a entero.
while inicio != "1" and inicio != "2":
    print("\nLas opciones solo son 1 y 2 ")
    inicio = input("Que quiere hacer (elija el numero de la opcion): ")

if inicio == "1":
    turno = 1
    print("\nEste es el tablero inicial: \n ")
    tablero_juego = nuevo_tablero()

elif inicio == "2":
    print("\nEste es el tablero anterior:\n")
    viejo = cargar_tablero()
    tablero_juego = old_tablero(viejo)
    turno = int(viejo[3])

tablero_to_string(tablero_juego)

while turno > 0:  # Falta condicion que ninguno este haya perdido, pero quedara pendiente. y debe ir con un if final
    if turno % 2 != 0:
        print("\nTurno del jugador:", j1, "\n")
        menu()
        que_hacer = input("Elija el numero de su opcion: ")
        while que_hacer != "1" and que_hacer != "2" and que_hacer != "3":
            print("Las opciones son 1, 2 y 3")
            que_hacer = input("Elija el numero de su opcion: ")

        if que_hacer == "1":#Dos ciclos, una para que lo ingreso correctamente y otro para que sea "X" o solo 1 con or
            print("\nEl formato correcto es letra y numero, sin espacios, por ejemplo a1 ")
            seleccion = input("Selecciona una pieza: ")
            seleccion = seleccion.lower()
            revisar_seleccion = revisar_orden(seleccion)  # Es un true o un false
            # Funcion para revisar, si es True hace lo demás sino vuelve a preguntar
            fila_seleccion = cambiar_fila(seleccion)
            columna_seleccion = cambiar_columna(seleccion)
            print ("Arriba y abajo, izq, derecha esta vacio", quedan_movimientos(tablero_juego,fila_seleccion,columna_seleccion))
            print("La respuesta de arriba es si aun puede jugar",perdedor(tablero_juego))
            while revisar_seleccion == False:
                print("")

                selecci = input("Selecciona una pieza(letranumero----): ")
                seleccion = selecci.lower()
                revisar_seleccion = revisar_orden(seleccion)  # Es un true o un false
                # Funcion para revisar, si es True hace lo demás si no vuelve a preguntar
                fila_seleccion = cambiar_fila(seleccion)
                columna_seleccion = cambiar_columna(seleccion)
            if revisar_seleccion == True:
                print(seleccion, fila_seleccion, columna_seleccion)
                print("")
                pieza_elegida = tablero_juego[fila_seleccion][columna_seleccion]
                print(pieza_elegida)
                print("")
                if pieza_elegida == "X":
                    print("Esa pieza es tuya y puedes moverla")
                    movimiento = True
                elif pieza_elegida == "Y":
                    print("Esa pieza no es tuya y por ende, no puedes moverla")
                    movimiento = False
                elif pieza_elegida == "-":
                    print("En ese lugar no hay nada aun ")
                    movimiento = False
                elif pieza_elegida == "*":
                    print("Esa pieza es una flecha y no puedes moverla")
                    movimiento = False
                else:
                    print("No puedes mover esa pieza o el ingreso es incorrecto")
                    movimiento = False
            else:
                print(
                    "Recuerda que el formato de entrada es letra y numero, sin espacios. Y que tanto la letra como el numero debe estar contenida en el tablero")
            tablero_to_string(tablero_juego)

            if movimiento == True:
                nueva_ubicacio = input("Ingresa la nueva ubicacion: ")
                nueva_ubicacion = nueva_ubicacio.lower()
                fila_nueva = cambiar_fila(nueva_ubicacion)
                columna_nueva = cambiar_columna(nueva_ubicacion)
                lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                rocio = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva, columna_nueva)
                chek = quedan_movimientos(tablero_juego,fila_nueva,columna_nueva)
                print ("Chek pieza nueva", chek )
                while rocio==False: ######Problema si la pieza no es movible
                    print("\nIngrese nuevamente la ubicacion final de la pieza seleccionada")
                    nueva_ubicacio = input("Ingresa la nueva ubicacion: ")
                    nueva_ubicacion = nueva_ubicacio.lower()
                    fila_nueva = cambiar_fila(nueva_ubicacion)
                    columna_nueva = cambiar_columna(nueva_ubicacion)
                    lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                    verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                    rocio = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva,
                                              columna_nueva)
                if rocio == True:
                    tablero_juego[fila_seleccion][columna_seleccion] = "-"
                    tablero_juego[fila_nueva][columna_nueva] = "X"
                    tablero_to_string(tablero_juego)
                    flecha = input("Ingrese donde quiere que vaya la flecha: ")
                    flecha = flecha.lower()
                    fila_flecha = cambiar_fila(flecha)
                    columna_flecha = cambiar_columna(flecha)
                    print("lugar nuevo --> ", nueva_ubicacion, fila_nueva, columna_nueva, lugar_nuevo, verificar)
                    print ("Flecha",fila_flecha, columna_flecha, tablero_juego[fila_flecha][columna_flecha])
                    nacho =lanzamiento_valido(tablero_juego,fila_nueva, columna_nueva, fila_flecha, columna_flecha)
                    print (nacho)

                    if nacho == True:
                        tablero_juego[fila_flecha] [columna_flecha]= "*"
                        tablero_to_string(tablero_juego)
                        turno = 2


            turno = 2



        elif que_hacer == "2":
            guardar_tablero(tablero_juego)
            print("\nSe ha guardado el juego. Hasta pronto!")
            turno = 0
        elif que_hacer == "3":
            despedida(j2)
            turno = 0
    else:
        print("Turno del jugador:", j2, "\n")
        menu()
        que_hacer = int(input("Elija el numero de su opcion: "))
        if que_hacer == 1:
            selecci = input("Selecciona una pieza(letranumero): ")
            seleccion = selecci.lower()
            revisar_seleccion = revisar_orden(seleccion)  # Es un true o un false
            # Funcion para revisar, si es True hace lo demás si no vuelve a preguntar
            fila_seleccion = cambiar_fila(seleccion)
            columna_seleccion = cambiar_columna(seleccion)
            if revisar_seleccion == True:
                print(seleccion, fila_seleccion, columna_seleccion)
                print("")
                pieza_elegida = tablero_juego[fila_seleccion][columna_seleccion]
                print(pieza_elegida)
                print("")
                if pieza_elegida == "Y":
                    print("Esa pieza es tuya y puedes moverla")
                    movimiento = True
                elif pieza_elegida == "X":
                    print("Esa pieza no es tuya y por ende, no puedes moverla")
                    movimiento = False
                elif pieza_elegida == "-":
                    print("En ese lugar no hay nada aun ")
                    movimiento = False
                elif pieza_elegida == "*":
                    print("Esa pieza es una flecha y no puedes moverla")
                    movimiento = False
                else:
                    print("No puedes mover esa pieza o el ingreso es incorrecto")
                    movimiento = False
            else:
                print(
                    "Recuerda que el formato de entrada es letra y numero, sin espacios. Y que tanto la letra como el numero debe estar contenida en el tablero")
            tablero_to_string(tablero_juego)

            if movimiento == True:
                nueva_ubicacio = input("Ingresa la nueva ubicacion")
                nueva_ubicacion = nueva_ubicacio.lower()
                fila_nueva = cambiar_fila(nueva_ubicacion)
                columna_nueva = cambiar_columna(nueva_ubicacion)
                print("La nueva ubicacion es:", nueva_ubicacion, fila_nueva, columna_nueva)
                lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                print("En ese lugar hay:", lugar_nuevo)
                print("Lugar viejo-->", seleccion, fila_seleccion, columna_seleccion, pieza_elegida)
                print("lugar nuevo --> ", nueva_ubicacion, fila_nueva, columna_nueva, lugar_nuevo)

            turno = 1
        elif que_hacer == 2:
            guardar_tablero(tablero_juego)
            print("\nSe ha guardado el juego. Hasta pronto!")
            turno = 0
        elif que_hacer == 3:
            despedida(j1)
            turno = 0

"""
La parte para partir el juego esta lista, falta normalizar la posición de la leyenda y mensajes,
pero cosas menores. El tablero, queda en tablero_juego ahi se ira jugando lo siguiente, aquello del ciclo while para los turnos.
Luego hay que modificar turno, para que solo sea un par o un impar, eso podria ser dentro de guardar

Falta una funcion para guardar el tablero y convertirlo antes
un ciclo para agarrar cada una de la vieja e irlo reemplazando en la función

Falta la funcion que obtenga los dos posiciones y compruebe si es posible moverlo y luego que lo mueva
Luego preguntar por la posicion de la flecha y comprobar si es posible
Bueno, eso dentro de un(os) ciclo(s)
Debo pedirlo hasta que sea cierto que es correcto while verificador es falso y luego el if si es cierto!

Falta mandar la flecha! y colocarla
Falta un ciclo para que la entrada sea correcta
Falta pensar lo diagonal
simplificar algo el codigo

Pero igual el algoritmo para mover las piezas en forma de cruz esta funcionando


Crear un ciclo para que no te el nombre del jugador para cada error

sistema de cambio listo


Se deberia definir un perdedor por pieza y por jugador

La funcion quedan_movimientos ya esta creada, aunque no esta usada correctamente. Pero esta bien definida

Falta
*Aplicar quedan_movimientos
*Repetir la estructura para j2, para que pueda jugar
*Crear la función quedan movimientos y que crea el perdedor
*Elegir un perdedor
"""
