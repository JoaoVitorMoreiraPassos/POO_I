import	abc
class Conta(abc.ABC):
    def	__init__(self,	numero,	titular,	saldo=0,	limite=1000.0):
        self._numero	=	numero
        self._titular	=	titular
        self._saldo	=	saldo
        self._limite	=	limite
    
    @abc.abstractmethod
    def atualiza(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo, limite)
    
    def atualiza(self):
        return super().atualiza()

if __name__ == "__main__":
    # c = Conta()
    c = ContaCorrente(1, "joao vitor", 50, 100)