def ordena(word):
    # Ordenação por inserção
    word = list(word)
    for i in range(1, len(word)):
        aux = word[i]
        j = i - 1
        while ((j >= 0) and (aux < word[j])):
            word[j+1] = word[j]
            j -= 1
        word[j+1] = aux
    return "".join(word)

hw = "helloworld"
print(ordena(hw))