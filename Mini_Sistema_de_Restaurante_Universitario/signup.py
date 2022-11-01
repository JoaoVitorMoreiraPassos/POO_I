import os    
 
class Signup():
    def __init__(self, database):
        self._database = database
        self.menu()
    
    @property
    def mensagem(self):
        return self._mensagem
        
    def menu(self):
        while True:
            print("-"*55)
            print("|"+"Sign Up".center(53," ")+"|")
            print("-"*55)
            acao = input(f"|{('1 - Aluno'):<53}|\n|{'2 - Funcionário':<53}|\n|{'3 - Cancelar':<53}|\n{'-'*55}\n| --> Selecionar tipo de conta: ")
            print("-"*55)
            resultado = None
            if ( acao == '1' ):
                nome = input("| --> Nome: ")
                user = input("| --> Usuário: ")
                cpf = input("| --> CPF(com pontos e hífen): ")
                curso = input("| --> Curso: ")
                matricula = input("| --> Matricula: ")
                senha = input("| --> Senha(Min. 6 digtos.): ")
                resultado = self._database.add_discente(nome, user, cpf, curso, matricula, senha)
            elif ( acao == '2' ):
                nome = input("| --> Nome: ")
                user = input("| --> Usuário: ")
                cpf = input("| --> CPF(com pontos e hífen): ")
                cargo = input("| --> cargo: ")
                senha = input("| --> Senha(Min. 6 digtos.): ")
                resultado = self._database.add_funcionario(nome, user, cpf, cargo, senha)
            elif ( acao == '3' ):
                self._mensagem = "| << Cadastro cancelado."
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-"*55)
                print("| << Opção inválida!")
                continue
            self._mensagem = resultado[1]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*55)
            break
