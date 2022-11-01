from random import randint as rd

lista1 = []
lista2 = []
for i in range(10):
    lista1.append(rd(0,10))
    lista2.append(rd(0,10))
    
lista3 = list(map(lambda x,y: x * y, lista1,lista2))

print(lista1)
print(lista2)
print(lista3)