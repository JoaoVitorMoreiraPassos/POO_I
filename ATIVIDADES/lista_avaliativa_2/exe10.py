import random

lista = []
for i in range(1,100): lista.append(i)
lista.sort()
print(lista)
#Media
media = sum(lista)/100
#Mediana
mediana = (lista[49]+lista[50])/2 if len(lista) % 2 == 0 else lista[len(lista)//2]
#Variancia
variancia = 0
for i in lista: variancia += ((i - media)**2)
variancia /= len(lista)-1
#Desvio padrao
desv_padrao = variancia ** (1/2)

#Saidas
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Variancia: {variancia:.2f}")
print(f"Desvio padrão: {desv_padrao:.2f}")
