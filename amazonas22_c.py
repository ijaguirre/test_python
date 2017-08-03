def quedan_movimientos (tablero,x1,y1):
    pass
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
        return False
    else:
        return True





tablero = [
        ["  ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        ["10", '-', '-', '-', 'Y', '-', '-', 'Y', '-', '-', '-'],
        ["9 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["8 ", '*', '-', '-', '-', 'X', '-', '-', 'Y', '-', '-'],
        ["7 ", 'Y', '-', '-', '-', '-', '-', '-', '-', '-', 'Y'],
        ["6 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["5 ", '-', '-', '-', '-', 'X', '-', '-', '-', '-', '-'],
        ["4 ", 'X', '-', '-', '-', '-', '-', '-', '-', '-', 'X'],
        ["3 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["2 ", '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ["1 ", '-', '-', '-', 'X', '-', '-', 'X', '-', '-', '-']
            ]
turno = 2
print(perdedor(tablero))



