import lib.graph

def my_carrer(y1, y2, x1, x2, color):
    for i in range(y1, y2):
        for j in range(x1, x2):
            lib.graph.plot(i, j, couleur=color)

def nb_lignes(lstlst):
    return (len(lstlst))

def nb_colones(lstlst):
    return (len(lstlst[0]))

def check(x_min, y_min , taille):
    x_max = 0
    y_max = 0

    x_min = x_min * taille
    x_max = x_min + taille

    y_min = y_min * taille
    y_max = y_min + taille

    return (x_min, x_max, y_min, y_max)


def taille_image(lstlst, taille):
    return((nb_lignes(lstlst) * taille), (nb_colones(lstlst) * taille))


def dessiner_grille(lstlst, taille):
    x1 = 0
    x2 = taille
    y1 = 0
    y2 = taille

    for y in range(len(lstlst)):
        for x in range(len(lstlst[y])):
            if (lstlst[y][x] == 0):
                my_carrer(y1, y2, x1, x2, "black")
                x1 += taille
                x2 += taille
            elif (lstlst[y][x] == 2):
                my_carrer(y1, y2, x1, x2, "blue")
                x1 += taille
                x2 += taille
            elif (lstlst[y][x] == 3):
                my_carrer(y1, y2, x1, x2, "red")
                x1 += taille
                x2 += taille
            else:
                my_carrer(y1, y2, x1, x2, "white")
                x1 += taille
                x2 += taille
        x1 = 0
        x2 = taille
        y1 = taille + y1
        y2 = taille + y2
