def fatorial(n: int):
    if (n > 1):
        n *= fatorial(n-1)
    return n

print(fatorial(int(input("Insira Um número: "))))
    