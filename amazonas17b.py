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
print (cambiar_fila("g1"),cambiar_columna("g1"))
print (cambiar_fila("i3"),cambiar_columna("i3"))
