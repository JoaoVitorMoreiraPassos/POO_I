def fatorial(n: int):
    if (n > 1):
        n *= fatorial(n-1)
    return n

n1, n2 = [int(i) for i in input("Insira dois numeros: ").split()]

arranjo = fatorial(n1)/fatorial(n1-n2)
combinacao = fatorial(n1)/ (fatorial(n2)*fatorial(n1-n2))

print(f"Arranjo: {arranjo}, Combinação: {combinacao}")