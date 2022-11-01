import	abc
class Conta(abc.ABC):
    def	__init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero	=	numero
        self._titular	=	titular
        self._saldo	    =	saldo
        self._limite	=	limite
    
    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo, limite)
        self._tipo  =   "Conta Corrente"
        
    def atualiza(self, taxa):
        self._saldo +=  self._saldo * taxa * 5
    def mostra(self):
        print(self._numero,self._titular, self._saldo, self._limite)

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo, limite)
        self._tipo  =   "Conta Poupança"
        
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
    def mostra(self):
        print(self._numero,self._titular, self._saldo, self._limite)

class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo, limite)
        self._tipo  =   "Conta Investimento"
    
    def deposita(self, valor):
        self._saldo = valor
    
    def atualiza(self, taxa):
        self._saldo	+=	self._saldo * taxa * 5
    
    
if __name__ == "__main__":
    # c = Conta() # Retorna um erro pois não é possíve instanciar uma classe abstrata
    cc	=	ContaCorrente('123-4',	'João',10,	1000.0)
    cp	=	ContaPoupanca('123-5',	'José',100,	1000.0)
    
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    
    print(cc._saldo)
    print(cp._saldo)
    
    
    ci	=   ContaInvestimento('123-6',	'Maria', 1000.0)
    ci.deposita(1000)
    ci.atualiza(0.01)
    print(ci._saldo)
    print(ci._tipo)
