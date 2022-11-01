from datetime import datetime

class Refeicao():
    def __init__(self):
        hora = int(str(datetime.now()).split()[1].split(":")[0])
        if 7 < hora < 10:
            self._refeicao = "merenda"
        elif 10 < hora < 14:
            self._refeicao = "almoço"
        elif 16 < hora < 19:
            self._refeicao = "janta"
        else:
            self._refeicao = "teste"
        self._entradas = 0
    
    def conta_entradas(self):
        self._entradas += 1

class Historico():
    def __init__(self):
        self.historico = {}
        self.add_refeicao()
        
    def add_refeicao(self):
        ref = Refeicao()
        data = str(datetime.now()).split()[0]
        
        if((len(self.historico) == 0)):
            self.historico[data] = {ref._refeicao: ref}
        elif(ref._refeicao not in self.historico[data].keys()):
            self.historico[data][ref._refeicao] = ref
       
    def contador(self):
        ref = Refeicao()
        data = str(datetime.now()).split()[0]
        if(data in self.historico.keys()):
            self.historico[data][ref._refeicao].conta_entradas()
    
    def mostra(self):
        tabela = "-"*55+"\n"
        tabela += f"|{'Historico'.center(53, ' ')}|\n"
        tabela += "-"*55+"\n"
        tabela += f"|{'Data':<20}|{'Refeição'.center(20, ' ')}|{'Qtd.'.center(11, ' ')}|\n"
        tabela += "-"*55+"\n"
        for k, v in self.historico.items():
            for k1, v1 in v.items():
                data = "/".join(list(reversed(k.split("-"))))
                tabela += f"|{data:<20}|{f'{v1._refeicao}'.capitalize().center(20, ' ')}|{f'{v1._entradas}'.center(11,' ')}|\n"
                tabela += "-"*55+"\n"
        return True, tabela
    