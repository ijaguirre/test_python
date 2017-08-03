def perdedor(tablero):
    lista_x = []
    lista_y = []
    f = 1
    while f < 11:  # Fu es fila y cu columna
        c = 1
        while c < 11:
            if tablero[f][c] == "X":
                lista_x.append(f)
                lista_x.append(c)
            c += 1
        f += 1
    print(lista_x)
    f = 1
    while f < 11:  # Fu es fila y cu columna
        c = 1
        while c < 11:
            if tablero[f][c] == "Y":
                lista_y.append(f)
                lista_y.append(c)
            c += 1
        f += 1
    print(lista_y)

    x1 = quedan_movimientos (tablero, lista_x[0],lista_x[1])
    x2 = quedan_movimientos (tablero, lista_x[2],lista_x[3])
    x3 = quedan_movimientos (tablero, lista_x[4],lista_x[5])
    x4 = quedan_movimientos (tablero, lista_x[6],lista_x[7])


    print(x1)


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
(perdedor(tablero))



