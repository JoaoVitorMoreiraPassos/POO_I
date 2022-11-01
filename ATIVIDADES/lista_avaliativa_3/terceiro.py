from tkinter.messagebox import RETRY


class Elevador:
    
    def __init__(self):
        self._andar = 0
        self._total_de_andares = 0
        self._capacidade = 0
        self._quantidade_de_pessoas = 0

    
    def menu(self):
        print("0 - Entrar\n1 - Sair\n2 - Subir\n3 - Descer\n4 - Sair\n")
        escolha = input("Escolha: ")
        
        if(escolha == "0"):
            return self.entra()
        elif(escolha == "1"):
            return self.sai()
        elif(escolha == "2"):
            return self.sobe()
        elif(escolha == "3"):
            return self.desce()
        elif(escolha == "4"):
            return -1
        else:
            return False, "Opçao inválida!"
    
    @property
    def capacidade(self):
        return self._capacidade
    @capacidade.setter
    def capacidade(self, capac):
        try:
            if(isinstance(capac, str)):
                capac = int(capac)
            self._capacidade = capac
            return True
        except:
            return False
        
    @property
    def tot_andares(self):
        return self._total_de_andares
    @tot_andares.setter
    def tot_andares(self, tot):
        try:
            if (isinstance(tot, str)):
                tot = int(tot)
            self._total_de_andares = tot
            return True
        except:
            return False, "Erro"
    def inicializa(self, capacidade, total_de_andares):
        self.capacidade = capacidade
        self.tot_andares = total_de_andares
        
    @property
    def quantidade(self):
        return self._quantidade_de_pessoas
    @quantidade.setter
    def quantidade(self, quant):
        self._quantidade_de_pessoas += quant

    def entra(self):
        print(self._quantidade_de_pessoas, self._capacidade, self._total_de_andares)
        if(self._quantidade_de_pessoas < self._capacidade):
            self.quantidade = 1
            return True,f"{self.quantidade} Pessoa(s)"
        else:
            return False, "O elevador já está cheio"

    def sai(self):
        if(self._quantidade_de_pessoas > 0):
            self.quantidade = -1
            return True, f"{self.quantidade} Pessoa(s)"
        else:
            return False, "Não tem ninguem no elevador"
        
    @property
    def andar(self):
        return self._andar
    @andar.setter
    def mudaAndar(self, variavel):
        self._andar += variavel
        
    def sobe(self):
        if(self._andar < self._total_de_andares):
            self.mudaAndar = 1
            return True, f"Andar {self.andar}"
        else:
            return False, "ultimo andar alcançado"
        
    def desce(self):
        if(self._andar > 0):
            self.mudaAndar = -1
            return True, f"Andar {self.andar}"
        else:
            return False, "Já estamos no térreo"
    
    
if __name__ == "__main__":
    import os
    elevador = Elevador()
    elevador.inicializa(capacidade=3, total_de_andares=5)
    while True:
        resultado = elevador.menu()
        if(resultado == -1):
            break
        os.system('cls' if os.name == 'nt' else 'clear')    
        print(resultado[1])
        print("-----------------")