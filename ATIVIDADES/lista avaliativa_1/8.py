preco = 5.00
quantidade = 120
lucro = preco * quantidade - 200
maior_lucro = {"price": preco, "quant": quantidade, "lucro": lucro}
while preco > 1:
    print(f"preço ingresso = {preco}, quantidade = {quantidade}, lucro = {lucro}")
    quantidade += 26
    preco -= 0.5
    lucro = preco * quantidade - 200
    if(lucro > maior_lucro["lucro"]):
        maior_lucro["price"] = preco
        maior_lucro["quantidade"] = quantidade
        maior_lucro["lucro"] = lucro

print(f"""
Lucro máximo: {maior_lucro['lucro']}
Preço do ingresso = {maior_lucro['price']}
quantidade: {maior_lucro['quant']}
""")
    