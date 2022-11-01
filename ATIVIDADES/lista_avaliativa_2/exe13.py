class Pessoa():
    def __init__(self, nome="", telefone=[]):
        self.nome = nome
        self.telefone = telefone
        
class Agenda():
    def __init__(self, pessoa=[]):
        self.pessoa = pessoa
    
    def incluirNovoNome(self, nome, telefone=[]):
        self.pessoa.append(Pessoa(nome,telefone))
        
    def incluirTelefone(self, nome, tel):
        for i in self.pessoa:
            if(i.nome.upper() == nome.upper()):
                i.telefone.append(tel)
                return
        cancel = input("Essa pessoa não está cadastrada!\nDeseja Continuar? y/n")
        if cancel in "Yy":
            novo_nome = input("Insira o novo nome: ")
            self.incluirNovoNome(novo_nome, [tel])
        else: print("Processo cancelado!")
    def excluirNome(self, name):
        for i in self.pessoa:
            if i.nome.upper() == name.upper():
                self.pessoa.remove(i)
                print("Perfil excluido com sucesso!")
                return
        print("Perfil não encontrado!")
        
    def excluirTelefone(self, telefone):
        for i in self.pessoa:
            for j in i.telefone:
                if(j == telefone):
                    if(len(i.telefone) == 1):
                        self.excluirNome(i.nome)
                        print("{i.nome.captalize()} foi removido da agenda!")
                        return
                    else:
                        i.telefone.remove(telefone)
                        print("Telefone Removido!")
                        return
        print("Telefone não encontrado!")
           
    def consultarTelefone(self, name):
        achou = False
        for i in self.pessoa:
            if(i.nome.upper() == name.upper()):
                print(f"Telefones de {i.nome} abaixo:")
                for i, v in enumerate(i.telefone):
                    print(f"Telefone {i+1}: {v}")
                achou = True
                print("-"*30)
        if(not(achou)): print("Usuário não registrado!")
        
print("-----BEM VINDOS PESSOAL-----")
agenda = Agenda()
while True:
    print("Adicionar novo nome[1]\nIncluir Telefone[2]\nExcluir Telefone[3]\nExcluirNome[4]\nConsultar Telefone[5]\nEncerra[nº negativo]")
    print("-"*40)
    escolha = int(input("O que voçê deseja fazer: "))
    try:
        if escolha == 1:
            nome = input("Nome: ")
            fones = [fone for fone in input("Insira os telefones separados por espaço: ").split()]
            agenda.incluirNovoNome(nome,fones)
        elif escolha == 2:
            nome = input("Nome da pessoa: ")
            fone = input("Telefone: ")
            agenda.incluirTelefone(nome, fone)
        elif escolha == 3:
            telefone = input("Telefone: ")
            agenda.excluirTelefone(telefone)
        elif escolha == 4:
            nome = input("Nome da pessoa: ")
            agenda.excluirNome(nome)
        elif escolha == 5:
            nome = input("Nome: ")
            agenda.consultarTelefone(nome)
        elif escolha < 1:
            break
    except:
        isinstance(escolha, int)
        print("Valor inválido!")
    print("-"*40)
    
    dic = {"joao":"vitor",2:5}
    dic.pop("joao")
    print(dic)