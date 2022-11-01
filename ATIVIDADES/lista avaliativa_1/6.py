def ehPrimo(n):
    divisores = 0
    for i in range(1, n//2 + 1):
        if(n%i == 0):
            divisores += 1
    return True if divisores <= 1 else False

n1, n2 = [int(i) for i in input("Digite dois numeros: ").split()]
results = []
for i in range(n1, n2+1):
    temp = ehPrimo(i)
    if(temp):
        print(f"{i} É primo")
    results.append(temp)
    
if(not(any(results))):
    print("Não existe nenhum número primo dentro desse intervalo")
    