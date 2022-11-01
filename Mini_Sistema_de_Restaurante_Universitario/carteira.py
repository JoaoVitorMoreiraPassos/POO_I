import abc
class Carteira(abc.ABC):
    def __init__(self, codigo):
        self._codigo = codigo
        self._fichas = 0
        self._saldo = 0.0
        
    @abc.abstractmethod
    def verifica(self):
        pass
    
    @abc.abstractmethod
    def deposito(self):
        pass
    
    @abc.abstractmethod
    def entrada(self):
        pass
    