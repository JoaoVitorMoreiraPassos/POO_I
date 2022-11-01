def fibonacci(n, p=0,s=1):
    if(n > 0):
        print(p, end= ", "if n > 1 else ".")
        s,p = p+s, s
        fibonacci(n-1, p, s)

fibonacci(int(input("Insira um numero: ")))