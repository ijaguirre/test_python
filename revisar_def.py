if revisar_seleccion == True:
    fila_seleccion = cambiar_fila(seleccion)
    columna_seleccion = cambiar_columna(seleccion)
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


def es_x (tablero,x1,y1):#Como numeros
    pieza_elegida = tablero[x1][y1]
    if pieza_elegida ==True:
        return True
    else:
        return False


