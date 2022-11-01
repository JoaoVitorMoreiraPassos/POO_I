def tamString(word):
    tam = 0
    for i in word:
        tam += 1
    return tam

word = "helloworld!"
print(tamString(word))
