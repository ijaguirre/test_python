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
    print ("Piezaas : X: ", j1, "Piezaas : Y: ", j2, "Flechas: * " )

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

#Variables

#Contadores

#Main

#saludo() #SAludo del juego
j1 = input("Diga nombre del jugador 1: ")
j2 = input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = int(input("Que quiere hacer: "))
if inicio ==1:
    print ("Eligio 1")
    print("Este es el tablero inicial")
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
    leyenda()
    for i in tablero_inicial:
        i = list(i)
        b= " ".join(i)
        print(b)
elif inicio ==2:
    print("Eligio 2")
    print(cargar_tablero())


"""
Falta una funcion para guardar el tablero y convertirlo antes
un ciclo para agarrar cada una de la vieja e irlo reemplazando en la función
"""