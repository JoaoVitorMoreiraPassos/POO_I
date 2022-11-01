from planos import *
from tributavel import Tributavel
Tributavel.register(ContaCorrente)
class Cliente():
    def __init__(self, nome, cpf, nascimento, profissao):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
        self._profissao = profissao
        self._planos = {"corrente": "", "poupanca": ""}
        self._seguros = []
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento
        
    @property
    def profissao(self):
        return self._profissao
    @profissao.setter
    def profissao(self, profissao):
        self._profissao = profissao
        
    def add_conta(self, tipo, num):
        if tipo == 1:
            if(self._planos['corrente'] == ''):
                self._planos['corrente'] = ContaCorrente(num, 0)
                return True, "| << Conta corrente criada com sucesso!"
            return False, "| << Número máximo de contas correntes já atingido!"
        
        if tipo == 2:
            if(self._planos['poupanca'] == ''):
                self._planos['poupanca'] = ContaPoupanca(num, 0)
                return True, "| << Conta poupanca criada com sucesso!"
            return False, "| << Número máximo de contas poupancas já atingido!"
            
    def add_seguro(self, mensal, total):
        try:
            mensal = float(mensal)
            total = float(total)
        except:
            return False, "| << Insira valores numéricos!"
        self._seguros.append(SeguroDeVida(mensal, total))
        return True, "| << Seguro de vida criado com sucesso!"
        
    def informacoes(self):
        return self._cpf, self._nome, self._nascimento, self._profissao
    
    def deposito(self, num_conta, valor):
        if self._planos["corrente"] != "":
            if (num_conta == self._planos["corrente"]._numero):
                return self._planos["corrente"].receber(valor)
        if self._planos["poupanca"] != "":
            if(num_conta == self._planos["poupanca"]._numero):
                return self._planos["poupanca"].receber(valor)
        return False, "| << Conta não encontrada ou não criada"
        
    def saque(self, num_conta, valor):
        if self._planos["corrente"] != "":
            if (num_conta == self._planos["corrente"]._numero):
                return self._planos["corrente"].retirar(valor)
        if self._planos["poupanca"] != "":
            if(num_conta == self._planos["poupanca"]._numero):
                return self._planos["poupanca"].retirar(valor)
        return False, "| << Conta não encontrada ou não criada"
    def extrato(self, num_conta):
        if self._planos["corrente"] != "":
            if (num_conta == self._planos["corrente"]._numero):
                return self._planos["corrente"].extrato()
        if self._planos["poupanca"] != "":
            if(num_conta == self._planos["poupanca"]._numero):
                return self._planos["poupanca"].extrato()
        return False, "| << Conta não encontrada ou não criada"

    def tributacao(self):
        tributos = []
        if isinstance( self._planos["corrente"], Tributavel):
            desconto = self._planos["corrente"].tributo()
            tributos.append(desconto)
            self._planos["corrente"].retirar(desconto, True)
            self._planos["corrente"].retirar(10, True)
        for indice, seguro in enumerate(self._seguros):
            desconto = seguro.tributo()
            tributos.append(desconto)
            self._seguros[indice].retirar(desconto)
        total = 10 + sum(tributos)
        return  True, total
