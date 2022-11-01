def fatorialRecursiva(n):
    if(n > 1):
        n *= fatorialRecursiva(n-1)
    return n

def fatorialIterativa(n):
    fatorial = 1
    while n > 0:
        fatorial *= n
        n -= 1
    return fatorial

print(fatorialIterativa(5))
print(fatorialRecursiva(6))