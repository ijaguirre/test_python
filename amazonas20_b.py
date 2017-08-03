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


def quedan_movimientos(tablero, x1, y1):
    x2 = x1+1
    y2 = y1+ 1
    s = y1 + 1 #g1, g8
    mm = check_pieza(tablero, x2, y2)
    

    elif x1 == x2 and y2 > y1 and mm == True:  # La pieza nueva esta más a la derecha
        while s < y2 + 1:
            se_puede = check_pieza(tablero, x1, s)
            # print(se_puede, s)
            s += 1

            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1 == x2 and y2 < y1 and mm == True:  # La pieza nueva estaria mas hacia la izquierda
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

    elif y1 == y2 and x2 < x1 and mm == True:  # Esta mas arriba Mejorado
        v = x1 -1    #Decia x1
        print (v)
        while v >= x2 :
            se_puede = check_pieza(tablero, v, y1)
            v -= 1
            if se_puede == False:
                return False
            else:
                pass
        return True

    elif x1<x2 and y1<y2 and ((x2-x1)== (y2-y1)) and mm == True:########### Ready!!!! Este movimiento es abajo a la derecha

        o = 1
        mm = check_pieza(tablero,x2,y2)
        while x1+o<x2 and y1+o<y2:
            se_puede= check_pieza(tablero,x1+o,y1+o)
            o+=1
            if se_puede == False:
                return False
            else:
                pass

        return True

    elif x1>x2 and y1>y2 and ((x1-x2)==(y1-y2)) and mm == True: #############De verdad esta lista, y es arriba a la izquierda
        p = x1-x2
        mm = check_pieza(tablero,x2,y2)
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
        while x1-s>x2 and y1+s <y2: #como nunca entra retorna true igual
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