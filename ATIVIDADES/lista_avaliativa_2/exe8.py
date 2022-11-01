from random import randint as rd

class Cartao:
    def __init__(self, num, nums =[]):
        self.num = num
        self.nums = nums
    
    def checkCard(self, result):
        um = list(filter(lambda x: x == 1, self.nums))
        dois = list(filter(lambda x: x == 2, self.nums))
        tres = list(filter(lambda x: x == 3, self.nums))
        for i in result:
            if(i == 1 and um):um.pop()
            if(i == 2 and dois):dois.pop()
            if(i == 3 and tres):tres.pop()
        acertos = 13 - (len(um)+len(dois)+len(tres))
        if(acertos == 13):print("Ganhador |", end="")
        print(f"Nª do Bilhete: {self.num:<5}|  Acertos: {acertos:<5}|  Numeros: {self.nums:}")
        
def geraLista():
    lista = []
    for i in range(13):
        lista.append(rd(1,3))
    return lista
      
lista = geraLista()

print("bilhete premiado: ",lista)

cards = []
for i in range(3):
    cards.append(Cartao(i))
    cards[i].nums = geraLista()
for i in cards:
    i.checkCard(lista)
