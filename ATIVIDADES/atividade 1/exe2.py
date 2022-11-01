peso = float(input("Peso dos pescados: "))
excesso = peso - 50
if(excesso>=1):
    print(f"Voce deverá pagar {4*excesso} de multa por {excesso} quilos acima do permitido")
else:
    print(f"Parabens voce não precisa pagar nenhuma multa")