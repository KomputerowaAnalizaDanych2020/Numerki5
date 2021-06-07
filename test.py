import math
import numpy as np
import matplotlib.pyplot as plt


def schemat_hornera(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result


def wartosci(x, choose):
    if choose == '1':
        return 10 * x - 2
    elif choose == '2':
        tab = [2, 1, 5, -4, -20]
        return schemat_hornera(tab, len(tab), x)
    elif choose == '3':
        return math.sin(2*x)
    elif choose == '4':
        return math.fabs(math.cos(x**2))


def przypisz_wezly(n, nodes, ak):
    if n == 2:
        nodes.append(0.585786)
        nodes.append(3.414214)
        ak.append(0.853553)
        ak.append(0.146447)
    if n == 3:
        nodes.append(0.415775)
        nodes.append(2.294280)
        nodes.append(6.289945)
        ak.append(0.711093)
        ak.append(0.278518)
        ak.append(0.010389)
    if n == 4:
        nodes.append(0.322548)
        nodes.append(1.745761)
        nodes.append(4.536620)
        nodes.append(2.395071)
        ak.append(0.603154)
        ak.append(0.357419)
        ak.append(0.038888)
        ak.append(0.000539)
    if n == 5:
        nodes.append(0.263560)
        nodes.append(1.413403)
        nodes.append(3.596426)
        nodes.append(7.085810)
        nodes.append(12.640801)
        ak.append(0.521756)
        ak.append(0.398667)
        ak.append(0.075942)
        ak.append(0.003612)
        ak.append(0.000032)
    return nodes, ak

print("Wybierz jedna z funkcji:")
print("1. 10x - 2 ")
print("2. 2x^4 + x^3 + 5x^2 - 4x - 20 ")
print("3. sin(2*x) ")
print("4. |cos(x^2)| ")
choice = int(input("Podaj wariant wybranej funkcji: "))
stopien = int(input("Podaj stopien wielomianu: "))
ilosc_wezlow = int(input("Podaj ilosc wezlow: "))
print("Podaj krance przedzialow: od 0 do nieskonczonosci")
lewy = np.double(input("lewy kraniec: "))
prawy = np.double(input("prawy kraniec: "))

nodes = []
ak = []
nodes, ak = przypisz_wezly(ilosc_wezlow, nodes, ak)

