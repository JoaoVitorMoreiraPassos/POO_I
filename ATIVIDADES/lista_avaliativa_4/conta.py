import abc
from historico import Historico


class Conta(abc.ABC, Historico):
    
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        super().__init__()
    
    @abc.abstractmethod
    def extrato(self):
        pass
    