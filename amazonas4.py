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
    print ("Piezaas : X --> ", j1, "Piezaas : Y -->", j2, "Flechas: * " )

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

#yu= [['c10', 'i10', 'e9', 'g3'], ['d10', 'j10', 'a2', 'g2'], ['a1', 'a3', 'a5', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c4', 'c7', 'c9', 'd2', 'd3', 'd4', 'd5', 'd8', 'd9', 'e3', 'e5', 'e6', 'e10', 'f1', 'f2', 'f3', 'f4', 'f5', 'f7', 'f8', 'g1', 'g5', 'g7', 'h1', 'h2', 'h3', 'h4', 'h5', 'h7', 'h9', 'h10', 'i1', 'i3', 'i6', 'i8', 'i9', 'j1', 'j2', 'j3', 'j4', 'j9'], 1]
"""
def tablero_antiguo(tablero):#Recibe el tablero anterior
    #Fichas Jugador 1
    fichas_1 = tablero[0]
    print("fichas1",fichas_1)
    print(fichas_1[0])
    for j in range(0,2):
        c = int(cambiar_columna(fichas_1[j]))
        f = int(cambiar_fila(fichas_1[j]))
        tablero[f][c] = "X"
    print(tablero)
"""

#Variables
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

tablero_inicial = [
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
#Contadores

#Main

#saludo() #Saludo del juego
j1 = "Rocio" #input("Diga nombre del jugador 1: ")
j2 = "Ignacio"#input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = int(input("Que quiere hacer: "))
if inicio ==1:
    print("Este es el tablero inicial")
    print("")
    tablero_to_string(tablero_inicial)


elif inicio ==2:
    print("Eligio 2")
    viejo = cargar_tablero()
    print(viejo)
    piezas_a= viejo[0]
    largo_a = len(piezas_a)
    print(piezas_a, largo_a)

    for w in range(largo_a):
        c=int(cambiar_columna(piezas_a[w]))
        f =int(cambiar_fila(piezas_a[w]))
        print(c,f)
        print(tablero_blanco[f][c])#ok
        tablero_blanco [f][c] = "X" #Piezasa jugador 1
        tablero_to_2= tablero_blanco #Interesante
        tablero_to_string(tablero_to_2)

    piezas_b = viejo[1]
    largo_b = len(piezas_b)
    print(piezas_b, largo_b)

    for e in range(largo_b):
        c=int(cambiar_columna(piezas_b[e]))
        f =int(cambiar_fila(piezas_b[e]))
        print(c,f)
        #print(tablero_blanco[f][c])#ok
        tablero_to_2 [f][c] = "Y" #Piezasa jugador 1
        tablero_to_3 = tablero_to_2

tablero_to_string(tablero_to_3)
"""
Falta una funcion para guardar el tablero y convertirlo antes
un ciclo para agarrar cada una de la vieja e irlo reemplazando en la función
"""