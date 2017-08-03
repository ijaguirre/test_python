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

print(cambiar_columna("10c"))