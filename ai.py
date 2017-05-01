from random import randrange



def tah(pole, cislo_policka, symbol):
    "Vrátí pole s daným symbolem umístěným na danou pozici."
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def oo_(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == a and herni_pole[i + 1] == a and herni_pole[i + 2] == "-":
            return tah(herni_pole, i + 2, a)

def _oo(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == "-" and herni_pole[i + 1] == a and herni_pole[i + 2] == a:
            return tah(herni_pole, i, a)

def o_o(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == a and herni_pole[i + 1] == "-" and herni_pole[i + 2] == a:
            return tah(herni_pole, i + 1, a)

def x_x(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == b and herni_pole[i + 1] == "-" and herni_pole[i + 2] == b:
            return tah(herni_pole, i + 1, a)

def xx_(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == b and herni_pole[i + 1] == b and herni_pole[i + 2] == "-":
            return tah(herni_pole, i + 2, a)

def _xx(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"

    for i in range(0,20):
        if herni_pole[i] == "-" and herni_pole[i + 1] == b and herni_pole[i + 2] == b:
            return tah(herni_pole, i, a)

def o_(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == a and herni_pole[i + 1] == "-":
            return tah(herni_pole, i + 1, a)

def _o(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == "-" and herni_pole[i + 1] == a:
            return tah(herni_pole, i, a)
def _x_(herni_pole, a):
    if a == "x":
        b = "o"
    elif a =="o":
        b = "x"
    for i in range(0,20):
        if herni_pole[i] == "-" and herni_pole[i + 1] == b and herni_pole[i + 2] == "-":
            nahoda = randrange(2)
            if nahoda == 0:
                return tah(herni_pole, i, a)
            else:
                return tah(herni_pole, i + 2, a)

def tah_pocitace(herni_pole, a):
    "Vrátí herní pole s tahem počítače určeným pravidly, hraje za zvolený symbol."

    if a == "x":
        b = "o"
    else:
        b = "x"

    if len(herni_pole) <= 0:
        raise ValueError("Velikost pole neodpovídá pravidlům hry.")

    if "-" not in herni_pole:
        raise ValueError("Herní pole neobsahuje volné pozice.")


    while True:
        if a + a + "-" in herni_pole:
            return oo_(herni_pole, a)
        elif "-" + a + a in herni_pole:
            return _oo(herni_pole, a)
        elif a + "-" + a in herni_pole:
            return o_o(herni_pole, a)
        elif b + "-" + b in herni_pole:
            return x_x(herni_pole, a)
        elif b + b + "-" in herni_pole:
            return xx_(herni_pole, a)
        elif "-" + b + b in herni_pole:
            return _xx(herni_pole, a)
        elif "-" + b + "-" in herni_pole:
            return _x_(herni_pole, a)
        elif "-" + a in herni_pole:
            return _o(herni_pole, a)
        elif a + "-" in herni_pole:
            return o_(herni_pole, a)
        else:
            for i in range(0,20):
                if herni_pole[i] == "-":
                    return tah(herni_pole, i, a)
