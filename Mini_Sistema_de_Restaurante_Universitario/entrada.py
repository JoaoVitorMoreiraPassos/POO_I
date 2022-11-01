import os

class Entrada():
    def __init__(self, database):
        self._database = database
        self._database.add_refeicao()
        self.menu()
        
    def menu(self):
        while True:
            print("-"*55)
            print("|"+"Entrada".center(53," ")+"|")
            print("-"*55)
            acao = input(f"|{'1 - Entrar no RU':<53}|\n|{'2 - Mostrar historico de consumo':<53}|\n|{'3 - Sair':<53}|\n{'-'*55}\n| --> O que deseja fazer: ")
            print("-"*55)
            resultado = None
            if(acao == '1'): 
                resultado = self.entrar(input("| --> Usuário: "))
            elif(acao == '2'):
                resultado = self._database.mostrar_historico()
            elif (acao == '3'):
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("| << Volte sempre.")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("| << Opção inválida!")
                continue
            os.system('cls' if os.name == 'nt' else 'clear')
            print(resultado[1])
  
    def entrar(self, user):
        return self._database.entrar(user)
    