import abc

class Adm(abc.ABC):
    '''
    Verifica se a senha do usuario está correta.
    '''
    def verifica(self, senha):
        pass

class Administrador():
    def __init__(self, usuario, senha):
        self._usuario = usuario
        self._senha = senha
        Adm.register(Administrador)
        
    def verifica(self, senha):
        if(self._senha == senha):
            return True, "| << Acesso autorizado."
        return False, "| << Acesso negado."
        