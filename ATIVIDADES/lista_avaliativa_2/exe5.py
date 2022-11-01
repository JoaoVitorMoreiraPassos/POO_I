from random import randint as rd

while True: 
    numero_magico = rd(0,100)
    print("O numero já foi sorteado!")
    for i in range(10):
        tentativa = int(input("Insira um numero: "))
        if(tentativa != numero_magico):
            if(tentativa > numero_magico): print(tentativa, "é maior")
            if(tentativa < numero_magico): print(tentativa, "é Menor")
            if(i == 9): 
                print("voce perdeu!")
                quit()
        if(tentativa == numero_magico):
            print("você acertou!")
            if input("Deseja continuar?1 p/sim: ") == '1':
                break
            else: quit()
