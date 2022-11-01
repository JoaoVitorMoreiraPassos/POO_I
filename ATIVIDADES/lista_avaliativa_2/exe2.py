def imprimeLista(lista, last):
    for i in lista:
        if type(i) == list:
            imprimeLista(i,last)
            continue
        print(i, end="." if i is last else ",")
        

a = [0,1,[2,[3,4]],5]
imprimeLista(a,a[-1])