from random import randint

cont = 0

while True:
    lista = []
    for i in range(9):
        lista.append(chr(randint(97, 122)))
    cont += 1
    if("".join(lista) == "joaovitor"):
        print("achei")
        break
print("cont: ", cont)
        
