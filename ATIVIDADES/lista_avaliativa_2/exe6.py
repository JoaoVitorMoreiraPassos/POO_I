from random import randint as rd

lista = []
for i in range(10): lista.append(rd(0,10))
print(lista)
for i in range(5) : lista[i], lista[(i+1)*-1] = lista[(i+1)*-1],lista[i]
print(lista)