slph = float(input("Quanto voce ganha por horas: "))
ht = int(input("Quantas horas voce trabalhou esse mês: "))

bruto = slph * ht
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print(f"""Bruto: R${bruto}
Imposto de Renda: R${ir}
INSS: R${inss}
Sindicato: R${sind}
Salario liquido: R${liquido}""")