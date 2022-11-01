def acheC(word, c):
    for i, v in enumerate(word):
        if(v == c):
            return i
    return -1

hw = "helloworld!"
print(acheC(hw, "l"))