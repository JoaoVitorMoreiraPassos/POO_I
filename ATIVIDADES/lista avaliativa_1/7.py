n = int(input("Digite um número: "))
binario = []
if(n not in [0,1]):
    while n >= 2: 
        binario.append(str(int(n % 2)))
        if(n <= 3):
            binario.append(str(int(n//2)))
        n = n // 2
else: binario.append(str(n))

for i in range(len(binario)//2):
    binario[i], binario[(i+1)*-1] = binario[(i+1)*-1], binario[i]
binario = "".join(binario)
print(binario)
   