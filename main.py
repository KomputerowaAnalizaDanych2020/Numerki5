import math
import numpy as np
import matplotlib.pyplot as plt

def schemat_hornera(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def wartosci(x, choice):
    if choice == 1:
        return 10 * x - 2
    elif choice == 2:
        tab = [2, 1, 5, -4, -20]
        return schemat_hornera(tab, len(tab), x)
    elif choice == 3:
        return math.sin(2*x)
    elif choice == 4:
        return math.fabs(math.cos(x**2))

def przypisz_wezly(n, nodes, ak):
    if n==2:
        nodes.append(0.585786)
        nodes.append(3.414214)
        ak.append(0.853553)
        ak.append(0.146447)
    if n==3:
        nodes.append(0.415775)
        nodes.append(2.294280)
        nodes.append(6.289945)
        ak.append(0.711093)
        ak.append(0.278518)
        ak.append(0.010389)
    if n==4:
        nodes.append(0.322548)
        nodes.append(1.745761)
        nodes.append(4.536620)
        nodes.append(2.395071)
        ak.append(0.603154)
        ak.append(0.357419)
        ak.append(0.038888)
        ak.append(0.000539)
    if n==5:
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


def laguerre(stopien, x):
    if int(stopien) == 0:
        return 1
    elif int(stopien) == 1:
        return x-1
    else:
        L = []
        L.append(1)
        L.append(x-1)
        for i in range(1,int(stopien)):
            L.insert(i+1,((x-(2*i)-1) * L[i]) - ((i*i)*L[i-1]))
        return L[stopien]

def silnia(n):
    if int(n)>1:
        return n*silnia(n-1)    #wywolanie rekurencyjne funkcji
    elif int(n) in (0,1):
        return 1

def lambda1(choice, ilosc_wezlow, stopien_wielomianu, ak, wezly):
    wynik = 0
    for i in range(int(ilosc_wezlow)):
        wynik += (wartosci(wezly[i], choice)) * ak[i] * laguerre(stopien_wielomianu, wezly[i])
    return (wynik / (silnia(stopien_wielomianu) * silnia(stopien_wielomianu)))



def MSE(tab, tablica, number_of_points):
    output = 0
    for i in range(int(number_of_points)):
        output += (tab[i] - tablica[i]) ** 2
    output = output / int(number_of_points)
    return output


# nodes.append(0.263560)
# nodes.append(1.413403)
# nodes.append(3.596426)
# nodes.append(7.085810)
# nodes.append(12.640801)
# ak.append(0.521756)
# ak.append(0.398667)
# ak.append(0.075942)
# ak.append(0.003612)
# ak.append(0.000032)

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



if np.double(lewy) < 0 or np.double(prawy)<=np.double(lewy):
    print("Bledne przedzialy")

wsp = []
for i in range(int(stopien)+1):
    wsp.append(lambda1(choice, ilosc_wezlow, i, ak, nodes))


tablicax = np.linspace(np.double(lewy), np.double(prawy), 50)  #wartosci prawdziwych funkcji
tablicay = np.array([], float)

for i in range(len(tablicax)):
    yy = wartosci(tablicax[i], choice)
    tablicay = np.append(tablicay, yy)

tablicay_a = []


for i in range(len(tablicax)):
    wynik = 0
    for j in range(int(stopien)+1):
        wynik += wsp[j] * laguerre(j, tablicax[i])
    # tablicay_a = np.append(tablicay_a, wynik)
    tablicay_a.append(wynik)

tablicay_a1 = np.array([],float)                                   #wartosci aproksymacji

for i in range(len(tablicax)):
    tablicay_a1 = np.append(tablicay_a1, tablicay_a[i])


error = MSE(tablicay, tablicay_a1, len(tablicax))
print(error)

plt.plot(tablicax, tablicay, 'g', tablicax, tablicay_a1, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



