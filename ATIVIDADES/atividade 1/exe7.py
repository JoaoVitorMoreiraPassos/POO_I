def fatorial(n: int):
    if (n > 1):
        n *= fatorial(n-1)
    return n

while True:
    n = int(input("Insira um número: "))
    if(n < 0): break
    if(n > 16):
        print("Número Invalido!")
        continue
    print(f"fatorial de {n} é {fatorial(n)}")
    