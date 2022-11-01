def media(dic):
    return (dic["nota1"] + dic["nota2"]) / 2

alunos = {}
print("Para encerrar a inserção de alunos digite -1 no lugar do nome.")
# Não podem ter duas pessoas com o mesmo nome
while True:
    nome = input("Digite o nome: ").upper()
    if(nome == "-1"):
        break
    alunos[nome] = {"nota1":float(input("Primeira nota: ")),"nota2":float(input("Segunda nota: "))}
     
escolhido = input("Digite o nome do aluno a consultar: ").upper()
try:
    print(f"Média de {escolhido.capitalize()} é {media(alunos[escolhido])}")
except:    
    print("Nome não encontrado")