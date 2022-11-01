from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)
    
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor
        
    def extrato(self):
        return self.historico(self.saldo)
    
    def tributo(self):
        desconto = self.saldo * 0.01 if self.saldo > 0 else 0
        return desconto
    
    def receber(self, valor):
        try:
            valor = float(valor)
        except:
            return False, "| << Valor inválido!"
        if(valor <= 0):
            return False, "| << Valor inválido!"
        self.saldo = valor
        self.add_historico("Entrada", valor)
        return True, "| << Déposito realizado com sucesso!"
    
    def retirar(self, valor, ehtributo = False):
        try:
            valor = float(valor)
        except:
            return False, "| << Valor inválido!"
        if((valor) > self.saldo and not(ehtributo)):
            return False, "| << Saldo insuficiente!"
        if(valor < 0):
            return False, "| << Valor inválido!"
        valor = (valor) * -1
        self.saldo = valor
        if(valor != 0):
            self.add_historico("Saída", valor * -1)
        return True, "| << Saque Realizado com sucesso!"
    
class ContaPoupanca(Conta):
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)
        
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor

    def extrato(self):
        return self.historico(self.saldo)
    
    def receber(self, valor):
        try:
            valor = float(valor)
        except:
            return False, "| << Valor inválido!"
        if(valor <= 0):
            return False, "| << Valor inválido!"
        self.saldo = (valor)
        self.add_historico("Entrada", valor)
        return True, "| << Depósito realizado com sucesso!"
    
    def retirar(self, valor):
        try:
            valor = float(valor)
        except:
            return False, "| << Valor inválido!"
        if(valor > self.saldo):
            return False, "| << Saldo insuficiente!"
        if(valor <= 0):
            return False, "| << Valor inválido!"
        valor = valor * -1
        self.saldo = valor
        self.add_historico("Saída", valor)
        return True, "| << Saque Realizado com sucesso"
        
class SeguroDeVida():
    
    def __init__(self, mensal, total):
        self._mensal = mensal
        self._total = total
      
    @property
    def total(self):
        return self._total  
    
    @property
    def mensal(self):
        return self._mensal
    
    def tributo(self):
        desconto = self._mensal * 0.02
        return desconto
    
    def retirar(self, valor):
        self._total -= valor
        return True
    