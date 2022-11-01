import os

class Cliente():
    def __init__(self, conta):
        self._conta = conta
        self.menu()
        
    def menu(self):
        while True:
            print("-"*55)
            print("|"+f"Oi {f'{self._conta._nome}'.capitalize()}".center(53," ")+"|")
            print("-"*55)
            acao = input(f"|{'1 - Comprar fichas':<53}|\n|{'2 - Consultar saldo':<53}|\n|{'3 - Sair':<53}|\n{'-'*55}\n| --> O que deseja fazer: ")
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("-"*55)
            resultado = None
            if ( acao == '1' ):
                resultado = self._conta.deposito(input("| --> Valor: R$ "))
            elif ( acao == '2' ):
                resultado = self._conta.consulta()
            elif ( acao == '3' ):
                print("| << Volte sempre.")
                break
            else:
                print("| << Opção inválida!")
                continue
            print(resultado[1])