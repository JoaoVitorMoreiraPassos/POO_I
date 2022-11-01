import random
from carteira import Carteira

class Funcionario(Carteira):
    def __init__(self, nome, cpf, cargo, senha):
        self._nome = nome
        self._cpf = cpf
        self._cargo = cargo
        self._senha = senha
        self._carteira = False
        self.add_carteira()
    
    @property
    def carteira(self):
        return self._carteira
    @carteira.setter
    def carteira(self, inicia):
        self._carteira = inicia
      
    @property
    def cpf(self):
        return self._cpf
      
    def consulta(self):
        if self.carteira:
            return True,f"| << Seu saldo é de R$ {self._saldo:.2f}".replace(".",",")+ f" e você possui {self._fichas} ficha(s)"
        else:
            return False, "| << Voce ainda não possui uma carteira."

    def add_carteira(self):    
        codigo = ""
        for i in range(9):
            codigo += chr(random.randint(33,122)) 
        if(self.carteira):
            return False, f"| << O usuario {self._cpf} já possui uma carteira"  
        super().__init__(codigo)
        self.carteira = True
        return True, "| << Cateria criada."
        
    def verifica(self, senha):
        if self._senha == senha:
            return True, "| << Acesso autorizado."
        return False, "| << Acesso negado."
    
    def deposito(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            return False, "| << Valor inválido."
        if not(self.carteira):
            return False, "| << Primeiro você precisa criar uma carteira."
        if valor <= 0:
            return False, "| << Valor inválido."
        
        self._saldo += valor
        self._saldo = round(self._saldo, 2)
        fichas = int(self._saldo / 7)
        self._saldo -= round(fichas * 7, 2)
        self._saldo = round(self._saldo, 2)
        self._fichas += fichas
        return True, f"| << Agora voce possui {self._fichas} ficha(s)."
    
    def entrada(self):
        if(self._fichas > 0):
            self._fichas -= 1
            return True, "| << Voce pode entrar."
        return False, "| << Voce não possui nenhuma ficha."
