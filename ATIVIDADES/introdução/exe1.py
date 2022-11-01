lados = [int(i) for i in input().split()]

if(lados[0] > lados[1]+lados[2] or lados[1]> lados[0]+lados[2] or lados[2] > lados[0]+lados[1]): 
    print("não forma triangulo")
else:
    if(len (set(lados)) == 1): print("Equilatero")
    if(len (set(lados)) == 2): print("Isóceles")
    if(len (set(lados)) == 3): print("Escaleno")