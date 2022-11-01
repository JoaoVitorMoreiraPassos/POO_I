import os
from bd import *
from signin import *
from signup import *
from cliente import *
from entrada import *
from administrador import *


def main(bd):
    while True:
        print("-"*55)
        print("|"+"Restaurante Universitário".center(53," ")+"|")
        print("-"*55)
        acao = input(f"|{('1 - Entre na sua conta'):<53}|\n|{'2 - Criar conta':<53}|\n|{'3 - Sair':<53}|\n{'-'*55}\n| --> O que deseja fazer: ")
        print("-"*55)
        os.system('cls' if os.name == 'nt' else 'clear')  
        if(acao == '1'):
            login = Signin(bd)
            if not login.mensagem is None:
                os.system('cls' if os.name == 'nt' else 'clear')  
                print("-"*55)
                print(login.mensagem)
        elif acao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastro = Signup(bd)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*55)
            print(cadastro.mensagem)
        elif acao == '3':
            print("| << Até mais autarquia.")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("| << Opção inválida!")
        
        
if __name__ == "__main__":
    bd = Database()
    inicio = main(bd)
