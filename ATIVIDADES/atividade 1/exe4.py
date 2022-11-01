alcool = 3,45
gasolina = 4,53

abastecido = float(input("Quantidade em litros do abastecimento: "))
tipo = input("Tipo de combustivel: ")

if(tipo == "A"):
    print(f"Total: { (abastecido - (abastecido*0.03)) if (abastecido < 20) else (abastecido - (abastecido*0.05)) }")

elif(tipo == "G"):
    print(f"Total: { (abastecido - (abastecido*0.04)) if (abastecido < 20) else (abastecido - (abastecido*0.06)) }")
