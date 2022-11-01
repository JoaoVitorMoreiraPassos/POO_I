def triangulo():
    b = float(input("Valor da base: "))
    h = float(input("Valor da altura: "))
    print(f"Area é: {(b*h)/2}")

def quadrado():
    lmin = float(input("Valor do lado menor: "))
    lmax = float(input("Valor do lado maior: "))
    print(f"Area é: {lmin * lmax}")
    
def circulo():
    r = float(input("Valor do raio: "))
    print(f"Area é: {3.13149 * (r**2)}")

while input("Quer sair?[y/n]: ") not in "yY":
    direcionador = {"TRIANGULO": triangulo, "QUADRADO": quadrado, "CIRCULO": circulo}
    forma = input("Forma: ")
    direcionador[forma.upper()]() if forma.upper() in direcionador.keys() else print("Nome Inválido")