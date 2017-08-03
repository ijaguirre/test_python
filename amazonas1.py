#POO y Funciones
def saludo():
    print ("== == == AMAZONAS - T2 IIC1103 == == == \n Bienvenido a Amazonas!")
    
def opciones_inicio():
    print("")
    print("Las opciones de inicio son:")
    print("1 Empezar nuevo tablero")
    print("2 Cargar partida guardada")

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
#j1 = input("Diga nombre del jugador 1: ")
#j2 = input("Diga nombre del jugador 2: ")
opciones_inicio()
inicio = int(input("Que quiere hacer: "))
if inicio ==1:
    print ("Eligio 1")
    nueva = [
["  ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
["10",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["9 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["8 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["7 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["6 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["5 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["4 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["3 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["2 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
["1 ",'-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    ]
    for i in nueva:
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
