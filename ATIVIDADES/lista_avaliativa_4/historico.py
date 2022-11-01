from datetime import datetime

class Transacao():
    def __init__(self, tipo, valor):
        self._horario = datetime.now()
        self._tipo = tipo
        self._valor = valor

    
    def informacoes(self):
        return self._horario, self._tipo, self._valor

class Historico():
    def __init__(self):
        self._historico = []
        
    def add_historico(self, tipo, valor):
        self._historico.append(Transacao(tipo,valor))
        
    def historico(self, atual):
        tabela = ""
        if(self._historico):
            tabela += "-"*48+"\n"
            tabela += f"|{'Horario':<20}|{'Tipo':<10}|{'Valor':>14}|\n"
            tabela += "-"*48+"\n"
            for transacao in self._historico:
                infos = transacao.informacoes()
                data = str(infos[0]).split(".")[0]
                valor = f"R${infos[2]:.2f}".replace(".",",")
                tabela += f"|{data:<20}|{infos[1]:<10}|{valor:>14}|\n"
                tabela += f"{'-'*48}\n"
            atual = f"R${atual:.2f}".replace(".",",")
            tabela += f"|{'Saldo atual':<31}|{atual:>14}|\n"
            tabela += "-"*48+"\n"
            return True, tabela
        return False, "Nenhuma transacao registrada"
            