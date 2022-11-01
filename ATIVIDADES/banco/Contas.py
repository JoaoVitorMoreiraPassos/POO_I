#João Vitor Moreira Passos

from random import randint
from datetime import datetime

class Historico():
    
    def __init__(self):
        self.data = datetime.now()
        self.transacoes = []

    def addTransacao(self, tipo, valor):
        self.transacoes.append([self.data, tipo, valor])
        
    def mostraTransacoes(self):
        if(len(self.transacoes) > 0):
            tabela = ""
            tabela += f"{'data':<20}|{'Tipo':<20}|{'Valor':>11}|\n"
            tabela += "-"*55+"\n"
            for t in self.transacoes:
                saldo = f"R${t[2]:.2f}".replace(".",",")
                tabela += f"|{str(t[0]).split('.')[0]:<20}|{t[1]:<20}|{saldo:>11}|\n"
                tabela += f"{'-'*55}\n"
            return True, tabela
        return False, "Nenhuma transação registrada!"

        
class Cliente():
    def __init__(self):
        self.nome = ""
        self._senha = ""
        self.cod = ""
        self._saldo = 0
        self.historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,valor):
        self._saldo += valor
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    def atribuiNome(self, nome):
        self.nome = nome
    def atribuiSaldo(self,saldo):
        self.saldo = saldo
    def atribuiSenha(self, senha):
        self.senha = senha
    def mostraHistorico(self):
        return self.historico.mostraTransacoes()

class Banco:
    def __init__(self):
        self.contas = {}
    
    
    def criarConta(self, nome, senha):
        if(nome == ""):
            return False, "nome inválido!"
        if(len(senha) < 8):
            return False, "senha fraca"
        cliente = Cliente()
        cliente.atribuiNome(nome)
        cliente.atribuiSenha(senha)
        cod = None
        while True:
            cod = "".join([str(randint(0,9)),str(randint(0,9)),str(randint(0,9))])
            if not(cod in self.contas.keys()):
                break
        self.contas[cod] = cliente
        return True, f"Conta criada com sucesso!"

    def mostrarHistorico(self, cod, senha):
        resultado,_ = self.listaContas()
        if(resultado):
            if(cod in self.contas.keys()):
                if(senha != self.contas[cod].senha):
                    return False, "Senha incorreta!"
                resposta, msg = self.contas[cod].mostraHistorico()
                return resposta, msg
            
            return False, "Usuário não cadastrado"
        return False, "Nenhum usuário cadastrado"
        
        
        
    def listaContas(self):
        tabela = ""
        if(self.contas):
            tabela += f"{'Nº':<7}|{'Nome':<30}|{'Saldo':>14}|\n"
            tabela += "-"*55+"\n"
            for k, v in self.contas.items():
                saldo = f"R${v.saldo:.2f}".replace(".",",")
                tabela += f"|{k:<7}|{v.nome.capitalize():<30}|{saldo:>14}|\n"
                tabela += f"{'-'*55}\n"
            return True, tabela
        
        return False, "Nenhum usuário cadastrado!"
    
    
    def sacarValor(self, cod, valor, senha):
        if(cod not in self.contas.keys()):
            return False, "Conta inexistente!"
        if(self.contas[cod].senha != senha):
            return False, "Senha incorreta!"
        if(not(cod.isnumeric()) or len(cod)!= 3):
            return False, "Codigo Inválido!"
        if not(cod in list(self.contas.keys())):
            return False, "Código não encontrado!"
        if(not(valor.isnumeric())):
            return False, "Valor inválido!"
    
        valor = float(valor)
        if(valor > self.contas[cod].saldo):
            return False, "Saldo insuficiente!"
        elif(valor  <= 0):
            return False, "Valor inválido!"
        
        self.contas[cod].atribuiSaldo(valor * -1)
        self.contas[cod].historico.addTransacao("Saque", valor)
        return True, "Operação concluida com sucesso!" 
        
    
    def depositaValor(self, cod, valor, senha, transf=False):
        if(cod not in self.contas.keys() and transf):
            return False, "Destinatário invalido!"
        if(cod not in self.contas.keys() and not(transf)):
            return False, "Essa conta não existe!"
         
        if(not(cod.isnumeric()) or len(cod)!= 3):
            return False, "Codigo Inválido!"
        if(self.contas[cod].senha != senha and not(transf)):
            return False, "Senha incorreta!"
        if not(cod in list(self.contas.keys())):
            return False, "Código não encontrado!"
        if not(valor.isnumeric()):
            return False, "Valor inválido!"
        valor = float(valor)
        if(valor  <= 0):
            return False, "Valor inválido!"
        
        self.contas[cod].atribuiSaldo(valor)
        self.contas[cod].historico.addTransacao("Deposito", valor)
        return True, "Operação conluida com sucesso!"

                
    def excluirConta(self, cod, senha):
        if(self.contas[cod].senha != senha):
            return False, "Senha incorreta!"
        if(not(cod.isnumeric()) or len(cod)!= 3):
            return False, "Codigo Inválido!"
        if not(cod in list(self.contas.keys())):
            return False, "Código não encontrado!"
  
        self.contas.pop(cod)
        return True, "Operação concluida com sucesso!"

    
    def transferir(self, cod1, cod2, valor, senha):
        if(self.contas[cod1].senha != senha):
            return False, "Senha incorreta!"
        if(not(valor.isnumeric())):
            return False, "Valor inválido!"
        if( cod1 == cod2 ):
            return False, "Não foi possível realziar essa transferência!"
        
        temp = self.sacarValor(cod1, valor, senha)
        if(not(temp[0])):
            return False, temp[1]
    
        resposta, mensagem = self.depositaValor(cod2, valor, senha, transf=True)
        if (not(resposta)):
            self.depositaValor(cod1, valor, senha)
            mensagem += " Valor estornado"
            return False, mensagem
        return True, "Transferência realizada com sucesso!"
        
            
if __name__ == "__main__":
    banco = Banco()
    banco.criarConta()
    banco.depositaValor()
    banco.sacarValor()
    banco.excluirConta()