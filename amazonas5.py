#Importacion
import os

#POO y Funciones
def saludo():
    print ("== == == AMAZONAS - T2 IIC1103 == == ==")
    print ("Bienvenido a Amazonas!")
def opciones_inicio():
    print("")
    print("Las opciones de inicio son:")
    print("1 Empezar nuevo tablero")
    print("2 Cargar partida guardada")

def cambiar_columna(ingreso):
    letra=ingreso[0]
    letra = letra.lower()
    columna=0
    if letra=="a":
        columna=1
    elif letra=="b":
        columna=2
    elif letra=="c":
        columna=3
    elif letra=="d":
        columna=4
    elif letra=="e":
        columna=5
    elif letra=="f":
        columna=6
    elif letra=="g":
        columna=7
    elif letra=="h":
        columna=8
    elif letra=="i":
        columna=9
    elif letra=="j":
        columna=10
    return columna

def cambiar_fila(ingreso):
    fila = 0
    if len(ingreso)==2:
        num = ingreso[1]

        if num=="1":
            fila = 10
        elif num=="2":
            fila = 9
        elif num=="3":
            fila = 8
        elif num=="4":
            fila = 7
        elif num=="5":
            fila = 6
        elif num=="6":
            fila = 5
        elif num=="7":
            fila = 4
        elif num=="8":
            fila = 3
        elif num=="9":
            fila = 2
    elif len(ingreso)==3:
        if ingreso[1]=="1" and ingreso[2]=="0":
            fila = 1
    return fila

def leyenda():
    print ("Piezas:X --> ", j1, "Piezaas: Y -->", j2, "Flechas: * " )

def tablero_to_string(tablero):
    for i in tablero:
        i = list(i)
        b= " ".join(i)
        print(b)
    print("")
    leyenda()

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
        ["5 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["4 ", 'X', '-', '-', '-', '-', '-', '-', '-', '-', 'X'],
        ["3 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["2 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["1 ", '-', '-', '-', 'X', '-', '-', 'X', '-', '-', '-']
    ]
    return tablero

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

#Variables
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


#Contadores

#Main

#saludo() #Saludo del juego
j1 = "Rocio" #input("Diga nombre del jugador 1: ")
j2 = "Ignacio"#input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = int(input("Que quiere hacer: "))

if inicio ==1:
    turno = 1
    print("Este es el tablero inicial")
    print("")
    #tablero_to_string(tablero_inicial)

    tablero_juego = nuevo_tablero()
    print("turno", turno)


elif inicio ==2:
    print("Eligio 2")
    viejo = cargar_tablero()
    #print(viejo)
    piezas_a= viejo[0]
    largo_a = len(piezas_a)

    turno = int(viejo[3])
    print("turno", turno)

    #print(piezas_a, largo_a)

    for w in range(largo_a):
        c=int(cambiar_columna(piezas_a[w]))
        f =int(cambiar_fila(piezas_a[w]))
        #print(c,f)
        #print(tablero_blanco[f][c])#ok
        tablero_blanco [f][c] = "X" #Piezasa jugador 1
        tablero_to_2= tablero_blanco #Interesante
        #tablero_to_string(tablero_to_2)

    piezas_b = viejo[1]
    largo_b = len(piezas_b)
    #print(piezas_b, largo_b)

    for e in range(largo_b):
        c=int(cambiar_columna(piezas_b[e]))
        f =int(cambiar_fila(piezas_b[e]))
        #print(c,f)
        #print(tablero_blanco[f][c])#ok
        tablero_to_2 [f][c] = "Y" #Piezasa jugador 1
        tablero_to_3 = tablero_to_2

    piezas_c = viejo[2]
    largo_c = len(piezas_c)

    for r in range ( largo_c):
        c = int(cambiar_columna(piezas_c[r]))
        f = int(cambiar_fila(piezas_c[r]))
        tablero_to_3 [f][c] = "*"

        tablero_juego = tablero_to_3

#print(tablero_juego)
tablero_to_string(tablero_juego)

#guardar_tablero(tablero_juego)

"""
La parte para partir el juego esta lista, falta normalizar la posición de la leyenda y mensajes,
pero cosas menores. El tablero, queda en tablero_juego ahi se ira jugando lo siguiente, aquello del ciclo while para los turnos.
Luego hay que modificar turno, para que solo sea un par o un impar, eso podria ser dentro de guardar

Falta una funcion para guardar el tablero y convertirlo antes
un ciclo para agarrar cada una de la vieja e irlo reemplazando en la función
"""
