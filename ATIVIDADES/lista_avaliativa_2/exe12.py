from random import randint

corridas = {
            "João": {"1": randint(25,70), "2": randint(25,70), "3": randint(25,70)},
            "Vitor": {"1": randint(25,70), "2": randint(25,70), "3": randint(25,70)},
            "Moreira":{"1": randint(25,70), "2": randint(25,70), "3": randint(25,70)},
            "Passos":{"1": randint(25,70), "2": randint(25,70), "3": randint(25,70)},
            "Random":{"1": randint(25,70), "2": randint(25, 70), "3": randint(25,70)}
            }

melhor_volta = [list(corridas.keys())[0],list(list(corridas.values())[0].keys())[0],list(list(corridas.values())[0].values())[0]]#pega as informações do primeiro piloto
menor_media = [list(corridas.keys())[0], sum(list(corridas.values())[0].values())/3]
for k, v in corridas.items():
    if (sum(list(v.values()))/3 < menor_media[1]):
        menor_media[0] = k
        menor_media[1] = sum(list(v.values()))/3
    for m, v1 in v.items():
        if(v1 < melhor_volta[2]): 
            melhor_volta[0] = k
            melhor_volta[1] = m
            melhor_volta[2] = v1

for k,v in corridas.items():
    print(f"{k:8}: {v['1']:<3}-{v['2']:>3} -{v['3']:>3} | media: {sum(list(v.values()))/3:.2f}")

print("-"*60)
print(f"Melhor volta foi de {melhor_volta[0]} na volta {melhor_volta[1]} com o tempo de {melhor_volta[2]}s")
print(f"O campeão foi {menor_media[0]} com a media de {menor_media[1]:.2f}s")
print("-"*60)
lista = []