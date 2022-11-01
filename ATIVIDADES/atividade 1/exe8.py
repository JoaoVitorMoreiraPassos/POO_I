n = int(input("Montar a tabuada de: "))
i = int(input("Começar por: "))
f = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {n} começando em {i} e terminando em {f}")

for j in range(i, f+1 if i < f else f-1, 1 if i < f else -1):
    print(f"{n:<3}{'x':<3}{j:<3}{'=':<3}{n*j:<4}")
print("------------")
