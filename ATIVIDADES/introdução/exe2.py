i = 0
while i <= 40:
    print(i if (i % 4 != 0 and i % 10 != 0) else ("PIN" if i != 40 else "FIM"))
    i += 1
