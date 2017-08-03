# Se recomienda ejecutar el juego en IDLES como PyCharm, www.replit.com, etc. Excepto IDLE Python 3.5.2.

import os

def saludo():#Saludo
    print("\n== == == AMAZONAS - T2 IIC1103 == == ==")
    print("Bienvenido a Amazonas!")

def opciones_inicio():#Muestra las opciones de inicio
    print("\nLas opciones de inicio son:")
    print("1 Empezar nuevo tablero")
    print("2 Cargar partida guardada")

def despedida(ganador):#Para cuando se acaba el juego
    print("\n== == == AMAZONAS - T2 IIC1103 == == ==")
    print("Se ha acabado el juego")
    print("El ganador es", ganador)

def cambiar_columna(ingreso):#Para convertir desde el archivo de texto
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


def cambiar_fila(ingreso): #Para convertir desde el archivo de texto
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
    print("Piezas X --> ", j1 +", "+"Piezas Y -->", j2+", "+ "Flechas --> * ")


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
    piezas_1 = temp2.split(",")
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
        ["5 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
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


def revisar_orden(cadena): #Para ver si el input es correcto
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
                fila_mas_columna =  COLUMNA + FILA
                lista_piezas_a.append(fila_mas_columna)

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
                fila_mas_columna = COLUMNA + FILA
                lista_piezas_b.append(fila_mas_columna)
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
                fila_mas_columna = COLUMNA + FILA
                lista_piezas_c.append(fila_mas_columna)
            ca += 1
        fa += 1

    new = open('tablero.txt', 'w')
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


def old_tablero(viejo):#Para pasar del tablero guardado a uno de la forma correcta
    piezas_a = viejo[0]
    largo_a = len(piezas_a)

    for w in range(largo_a):
        c = (cambiar_columna(piezas_a[w]))
        f = (cambiar_fila(piezas_a[w]))
        tablero_blanco[f][c] = "X"
        tablero_to_2 = tablero_blanco
    piezas_b = viejo[1]
    largo_b = len(piezas_b)
    for e in range(largo_b):
        c = int(cambiar_columna(piezas_b[e]))
        f = int(cambiar_fila(piezas_b[e]))
        tablero_to_2[f][c] = "Y"
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
    s = y1 + 1
    mm = check_pieza(tablero, x2, y2)
    if x1 == x2 and y2 > y1 and mm == True:
        while s < y2 + 1:
            se_puede = check_pieza(tablero, x1, s)
            s += 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 == x2 and y2 < y1 and mm == True:
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

    elif y1 == y2 and x2 < x1 and mm == True:  # Esta mas arriba
        v = x1 -1
        while v >= x2 :
            se_puede = check_pieza(tablero, v, y1)
            v -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1<x2 and y1<y2 and ((x2-x1)== (y2-y1)) and mm == True:# abajo a la derecha

        o = 1
        while x1+o<x2 and y1+o<y2:
            se_puede= check_pieza(tablero,x1+o,y1+o)
            o+=1
            if se_puede == False:
                return False
            else:
                pass

        return True

    elif x1>x2 and y1>y2 and ((x1-x2)==(y1-y2)) and mm == True: #arriba a la izquierda
        p = x1-x2
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
        while x1-s>x2 and y1+s <y2:
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
        while s < y2 + 1:
            se_puede = check_pieza(tablero, x1, s)

            s += 1

            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 == x2 and y2 < y1 and mm == True:  #izquierda
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

    elif y1 == y2 and x2 < x1 and mm == True:  # Esta mas arriba
        v = x1 -1
        while v >= x2 :
            se_puede = check_pieza(tablero, v, y1)
            v -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1<x2 and y1<y2 and ((x2-x1)== (y2-y1)) and mm == True:#abajo a la derecha

        o = 1
        while x1+o<x2 and y1+o<y2:
            se_puede= check_pieza(tablero,x1+o,y1+o)
            o+=1
            if se_puede == False:
                return False
            else:
                pass

        return True

    elif x1>x2 and y1>y2 and ((x1-x2)==(y1-y2)) and mm == True: #arriba a la izquierda
        p = x1-x2
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
        while x1-s>x2 and y1+s <y2:
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

def quedan_movimientos (tablero, x1,y1):#X es fila y es columna
    if 10 >x1 > 1 and 10 >y1 >1:
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

    elif x1==1 and 10 >y1 >1:
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
    elif x1==1 and y1==1:
        abajo = check_pieza(tablero, x1 + 1, y1)
        derecha = check_pieza(tablero, x1, y1 + 1)
        abajo_derecha = check_pieza(tablero, x1 + 1, y1 + 1)
        if abajo == True or derecha == True or  abajo_derecha == True:
            return True
        else:
            return False

    elif x1==1 and y1==10:
        abajo = check_pieza(tablero, x1 + 1, y1)
        izquierda = check_pieza(tablero, x1, y1 - 1)
        abajo_izquierda = check_pieza(tablero, x1 + 1, y1 - 1)
        if abajo == True or  izquierda == True or abajo_izquierda == True:
            return True
        else:
            return False
    elif x1==10 and y1==1:
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
    elif turno ==2:
        buscar = "Y"
    lista_x = []
    f = 1
    while f < 11:
        c = 1
        while c < 11:
            if tablero[f][c] == buscar:
                lista_x.append(f)
                lista_x.append(c)

            c += 1
        f += 1
    x1 = quedan_movimientos (tablero, lista_x[0],lista_x[1])#True es que si puedo jugar con ella
    x2 = quedan_movimientos (tablero, lista_x[2],lista_x[3])#False es que no puedo jugar con esta pieza
    x3 = quedan_movimientos (tablero, lista_x[4],lista_x[5])
    x4 = quedan_movimientos (tablero, lista_x[6],lista_x[7])
    if x1 == False and x2 == False and x3 == False and x4 == False:
        return True #True(es perdedor)
    else:
        return False #No es perdedor

def perdedor_inicio(tablero,turno):
    if turno == 1:
        buscar = "X"
    elif turno ==2:
        buscar = "Y"
    lista_x = []
    f = 1
    while f < 11:
        c = 1
        while c < 11:
            if tablero[f][c] == buscar:
                lista_x.append(f)
                lista_x.append(c)

            c += 1
        f += 1
    x1 = quedan_movimientos (tablero, lista_x[0],lista_x[1])#True es que si puedo jugar con ella
    x2 = quedan_movimientos (tablero, lista_x[2],lista_x[3])#False es que no puedo jugar con esta pieza
    x3 = quedan_movimientos (tablero, lista_x[4],lista_x[5])
    x4 = quedan_movimientos (tablero, lista_x[6],lista_x[7])
    if x1 == False and x2 == False and x3 == False and x4 == False:
        return True #True(es perdedor)
    else:
        return False #No es perdedor

def es_x(tablero, x1, y1):  #Para ver si la pieza la puede mover el jugador 1
    pieza_elegida = tablero[x1][y1]
    if pieza_elegida == "X":
        return True
    else:
        return False

def es_y(tablero, x1, y1):  #Para ver si la pieza la puede mover el jugador 2
    pieza_elegida = tablero[x1][y1]
    if pieza_elegida == "Y":
        return True
    else:
        return False

#Main!
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


saludo()  # Saludo del juego
print("")
j1 = input("Diga nombre del jugador 1: ")
j2 = input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = input("Que quiere hacer (elija el numero de la opcion): ")
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

puede_iniciar_1 = perdedor_inicio(tablero_juego,1)
puede_iniciar_2 = perdedor_inicio(tablero_juego,2)
while turno > 0 and puede_iniciar_1 == False and puede_iniciar_2 == False:
    if turno % 2 != 0:
        es_perdedor = perdedor(tablero_juego)
        if es_perdedor == True:
            despedida(j2)
            turno = 0

        else:
            print("\nTurno del jugador:", j1, "\n")
            menu()
            que_hacer = input("Elija el numero de su opcion: ")
            while que_hacer != "1" and que_hacer != "2" and que_hacer != "3":
                print("Las opciones son 1, 2 y 3")
                que_hacer = input("Elija el numero de su opcion: ")

            if que_hacer == "1":
                print("\nEl formato correcto es letra y numero, sin espacios, por ejemplo a1 ")
                seleccion = input("Selecciona una pieza: ")
                seleccion = seleccion.lower()
                revisar_seleccion = revisar_orden(seleccion)
                fila_seleccion = cambiar_fila(seleccion)
                columna_seleccion = cambiar_columna(seleccion)
                corresponde = es_x(tablero_juego,fila_seleccion,columna_seleccion)
                se_puede_mover = quedan_movimientos(tablero_juego,fila_seleccion, columna_seleccion)

                while revisar_seleccion == False or corresponde == False or se_puede_mover == False:
                    print("")
                    if revisar_seleccion ==False:
                        print ("Entrada incorrecta por formato. ")
                    elif corresponde ==False:
                        print("No puedes mover lo que hay en esa posicion")
                    elif se_puede_mover == False:
                        print("No te quedan movimientos con esa pieza. ")

                    selecci = input("Selecciona una pieza nuevamente(letranumero): ")
                    seleccion = selecci.lower()
                    revisar_seleccion = revisar_orden(seleccion)
                    fila_seleccion = cambiar_fila(seleccion)
                    columna_seleccion = cambiar_columna(seleccion)
                    corresponde = es_x(tablero_juego, fila_seleccion, columna_seleccion)
                    se_puede_mover = quedan_movimientos(tablero_juego, fila_seleccion, columna_seleccion)

                print("\nTablero de juego: \n")
                tablero_to_string(tablero_juego)

                if corresponde == True and revisar_seleccion ==True and se_puede_mover == True:
                    nueva_ubicacion = input("Ingresa la nueva ubicacion: ")
                    nueva_ubicacion = nueva_ubicacion.lower()
                    bien_escrita = revisar_orden(nueva_ubicacion)
                    fila_nueva = cambiar_fila(nueva_ubicacion)
                    columna_nueva = cambiar_columna(nueva_ubicacion)
                    lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                    verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                    mov_licito = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva, columna_nueva)

                    while mov_licito==False or bien_escrita ==False :
                        print("\nIngrese nuevamente la ubicacion final de la pieza seleccionada")
                        if mov_licito ==False:
                            print("Ese movimiento no esta permitido")
                        elif bien_escrita ==False:
                            print("La entrada esta incorrecta según formato")



                        nueva_ubicacion = input("\nIngrese la nueva ubicacion: ")
                        nueva_ubicacion = nueva_ubicacion.lower()
                        fila_nueva = cambiar_fila(nueva_ubicacion)
                        columna_nueva = cambiar_columna(nueva_ubicacion)
                        lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                        verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                        mov_licito = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva,columna_nueva)
                        bien_escrita = revisar_orden(nueva_ubicacion)

                    if mov_licito == True and bien_escrita ==True:
                        print("\nMovimiento valido\n")
                        tablero_juego[fila_seleccion][columna_seleccion] = "-"
                        tablero_juego[fila_nueva][columna_nueva] = "X"
                        tablero_to_string(tablero_juego)

                        flecha = input("Ingrese donde quiere que vaya la flecha: ")
                        flecha = flecha.lower()
                        fila_flecha = cambiar_fila(flecha)
                        columna_flecha = cambiar_columna(flecha)
                        bien_escrita_flecha = revisar_orden(flecha)
                        flecha_valida = lanzamiento_valido(tablero_juego,fila_nueva, columna_nueva, fila_flecha, columna_flecha)

                        while bien_escrita_flecha==False or flecha_valida == False:
                            if bien_escrita_flecha == False:
                                print("La entrada esta mal escrita")
                            elif flecha_valida == False:
                                print("El lanzamiento no es valido")
                            flecha = input("\nIngrese nuevamente donde quiere que vaya la flecha: ")


                            flecha = flecha.lower()
                            fila_flecha = cambiar_fila(flecha)
                            columna_flecha = cambiar_columna(flecha)
                            bien_escrita_flecha = revisar_orden(flecha)
                            flecha_valida = lanzamiento_valido(tablero_juego, fila_nueva, columna_nueva, fila_flecha,
                                                               columna_flecha)

                        if bien_escrita_flecha ==True and flecha_valida ==True:
                            print("\nLanzamiento valido\n")
                            tablero_juego[fila_flecha] [columna_flecha]= "*"
                            tablero_to_string(tablero_juego)

                            perdimos_ya = perdedor(tablero_juego)
                            if perdimos_ya ==True:
                                despedida(j2)
                                turno = 0
                            else:
                                turno = 2



            elif que_hacer == "2":
                guardar_tablero(tablero_juego)
                print("\nSe ha guardado el juego. Hasta pronto!")
                turno = 0
            elif que_hacer == "3":
                despedida(j2)
                turno = 0
    else:
        es_perdedor = perdedor(tablero_juego)
        if es_perdedor == True:
            despedida(j1)
            turno = 0
        else:
            print("\nTurno del jugador:", j2, "\n")
            menu()
            que_hacer = input("Elija el numero de su opcion: ")
            while que_hacer != "1" and que_hacer != "2" and que_hacer != "3":
                print("Las opciones son 1, 2 y 3")
                que_hacer = input("Elija el numero de su opcion: ")

            if que_hacer == "1":
                print("\nEl formato correcto es letra y numero, sin espacios, por ejemplo a1 ")
                seleccion = input("Selecciona una pieza: ")
                seleccion = seleccion.lower()
                revisar_seleccion = revisar_orden(seleccion)
                fila_seleccion = cambiar_fila(seleccion)
                columna_seleccion = cambiar_columna(seleccion)
                corresponde = es_y(tablero_juego, fila_seleccion, columna_seleccion)
                se_puede_mover = quedan_movimientos(tablero_juego, fila_seleccion,
                                                    columna_seleccion)

                while revisar_seleccion == False or corresponde == False or se_puede_mover == False:
                    print("")
                    if revisar_seleccion ==False:
                        print ("Entrada incorrecta por formato. ")
                    elif corresponde ==False:
                        print("No puedes mover lo que hay en esa posicion")
                    elif se_puede_mover == False:
                        print("No te quedan movimientos con esa pieza. ")

                    seleccion = input("Selecciona una pieza nuevamente(letranumero): ")
                    seleccion = seleccion.lower()
                    revisar_seleccion = revisar_orden(seleccion)
                    fila_seleccion = cambiar_fila(seleccion)
                    columna_seleccion = cambiar_columna(seleccion)
                    corresponde = es_y(tablero_juego, fila_seleccion, columna_seleccion)
                    se_puede_mover = quedan_movimientos(tablero_juego, fila_seleccion, columna_seleccion)

                print("\nTablero de juego: \n")
                tablero_to_string(tablero_juego)

                if corresponde == True and se_puede_mover == True and revisar_seleccion ==True :
                    nueva_ubicacion = input("Ingresa la nueva ubicacion: ")
                    nueva_ubicacion = nueva_ubicacion.lower()
                    bien_escrita = revisar_orden(nueva_ubicacion)
                    fila_nueva = cambiar_fila(nueva_ubicacion)
                    columna_nueva = cambiar_columna(nueva_ubicacion)
                    lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                    verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                    mov_licito = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva,
                                                   columna_nueva)

                    while mov_licito == False or bien_escrita == False:

                        if mov_licito == False:
                            print("Ese movimiento no esta permitido")
                        elif bien_escrita == False:
                            print("La entrada esta incorrecta según formato")
                        print("\nIngrese nuevamente la ubicacion final de la pieza seleccionada")

                        nueva_ubicacion = input("Ingrese la nueva ubicacion: ")
                        nueva_ubicacion = nueva_ubicacion.lower()
                        fila_nueva = cambiar_fila(nueva_ubicacion)
                        columna_nueva = cambiar_columna(nueva_ubicacion)
                        lugar_nuevo = tablero_juego[fila_nueva][columna_nueva]
                        verificar = check_pieza(tablero_juego, fila_nueva, columna_nueva)
                        mov_licito = movimiento_valido(tablero_juego, fila_seleccion, columna_seleccion, fila_nueva,
                                                       columna_nueva)
                        bien_escrita = revisar_orden(nueva_ubicacion)  # True si esta bien escrita

                    if mov_licito == True and bien_escrita ==True:
                        print("\nMovimiento valido\n")
                        tablero_juego[fila_seleccion][columna_seleccion] = "-"
                        tablero_juego[fila_nueva][columna_nueva] = "Y"
                        tablero_to_string(tablero_juego)

                        # Parte flecha
                        flecha = input(
                            "Ingrese donde quiere que vaya la flecha: ")
                        flecha = flecha.lower()
                        fila_flecha = cambiar_fila(flecha)
                        columna_flecha = cambiar_columna(flecha)
                        bien_escrita_flecha = revisar_orden(flecha)
                        flecha_valida = lanzamiento_valido(tablero_juego, fila_nueva, columna_nueva, fila_flecha,
                                                           columna_flecha)

                        while bien_escrita_flecha == False or flecha_valida == False:
                            if bien_escrita_flecha == False:
                                print("La entrada esta mal escrita")
                            elif flecha_valida == False:
                                print("El lanzamiento no es valido")

                            flecha = input("\nIngrese nuevamente donde quiere que vaya la flecha: ")

                            flecha = flecha.lower()
                            fila_flecha = cambiar_fila(flecha)
                            columna_flecha = cambiar_columna(flecha)
                            bien_escrita_flecha = revisar_orden(flecha)
                            flecha_valida = lanzamiento_valido(tablero_juego, fila_nueva, columna_nueva, fila_flecha,
                                                               columna_flecha)

                        if bien_escrita_flecha == True and flecha_valida == True:
                            print("\nLanzamiento valido\n")
                            tablero_juego[fila_flecha][columna_flecha] = "*"
                            tablero_to_string(tablero_juego)

                            perdimos_ya = perdedor(tablero_juego)
                            if perdimos_ya == True:
                                despedida(j1)
                                turno = 0
                            else:
                                turno = 1



            elif que_hacer == "2":
                guardar_tablero(tablero_juego)
                print("\nSe ha guardado el juego. Hasta pronto!")
                turno = 0
            elif que_hacer == "3":
                despedida(j1)
                turno = 0
if puede_iniciar_1 == True:
    despedida(j2)
    turno = 0
elif puede_iniciar_2 == True:
    despedida(j1)
    turno = 0
