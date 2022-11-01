class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None

class Agenda:
    def __init__(self):
        self._pessoas = []
    
    @property
    def pessoas(self):
        return self._pessoas
    @pessoas.setter
    def pessoas(self, pessoa):
        if(len(self._pessoas) < 2):
            self._pessoas.append(pessoa)
        else:
            print("Agenda lotada!")
    def armazenaPessoa(self, pessoa):
        self.pessoas = (pessoa)
    
    def removePessoa(self, nome):
        for i in self.pessoas:
            if(i.nome == nome):
                self.pessoas.remove(i)
                print("Excluido!")
                return
        print("Pessoa não cadastrada!")
        
    def buscaPessoa(self, nome):
        for i in self.pessoas:
            if(i.nome == nome):
                print(i.nome.capitalize(), i.idade, i.altura)

    
    def imprimeAgenda(self):
        infos = ""
        for i in self.pessoas:
            infos += f"{i.nome.capitalize()} {i.idade} {i.altura}\n"
        return infos
    
    
if __name__ == "__main__":
    agenda = Agenda()
    while True:
        print("0 - Adicionar pessoa\n1 - Remover pessoa\n2 - Busca Pessoa\n3 - Imprimir agenda\n4 - Sair")
        escolha = input("Escolha: ")
        
        if(escolha == "0"):
            temp = Pessoa()
            temp.nome = input("Nome: ").upper()
            temp.idade = int(input("Idade: "))
            temp.altura = float(input("Altura: "))
            agenda.armazenaPessoa(temp)
        elif(escolha == "1"):
            agenda.removePessoa(input("Nome: ").upper())
        elif(escolha == "2"):
            agenda.buscaPessoa(input("Nome: ").upper())
        elif(escolha == "3"):
            out = agenda.imprimeAgenda()
            print(out if out != "" else "Ninguem na agenda!")
        elif(escolha == "4"):
            break
        else:
            pass
