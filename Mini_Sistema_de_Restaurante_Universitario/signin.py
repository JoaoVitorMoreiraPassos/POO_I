import os
import cliente
import entrada
from administrador import *


class Signin():
    def __init__(self, database):
        self._database = database
        self._mensagem = None
        self.menu()
    
    @property
    def mensagem(self):
        return self._mensagem
       
    def menu(self):
        print("-"*55)
        print("|"+"Sign In".center(53," ")+"|")
        print("-"*55)
        user = input("| --> Usuário: ")
        senha = input("| --> Senha: ")
        resultado = self._database.login(user, senha)
        if resultado[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*55)
            print(f"| --> {'Login autorizado.':<48}|")
            print("-"*55)
            if isinstance(resultado[1], Adm):
                entrada.Entrada(self._database)
            else:
                cliente.Cliente(resultado[1])
        else:
           self._mensagem = resultado[1]
