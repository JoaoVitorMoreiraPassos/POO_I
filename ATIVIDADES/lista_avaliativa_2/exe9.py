from random import randint as rd

class Pessoa:
    def __init__(self, nome = "", endereco = "", cep="", bairro="", telefone=""):
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.bairro = bairro
        self.telefone = telefone
        
agenda = []
for i in range(10):
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    cep = input("Digite o cep: ")
    bairro = input("Digite o bairro: ")
    telefone = input("Digite o telefone: ")
    agenda.append(Pessoa(nome, endereco, cep, bairro, telefone))
print("------------")

titulo = f"{'Nome':<25}|{'Endereco':<30}|{'CEP':<10}|{'Bairro':<25}|{'Telefone':<15}"
print(titulo)
print("-"*len(titulo))
for i in reversed(agenda):
    print(f"{i.nome:<25}|{i.endereco:<30}|{i.cep:<10}|{i.bairro:<25}|{i.telefone:<15}")
    print("-"*len(titulo)+5)