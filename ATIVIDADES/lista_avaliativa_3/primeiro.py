
from datetime import datetime


class Pessoa:
    def __init__(self):
        self._nome = None
        self._nasc = None
        self._altura = None
        
    # Manipular o nome
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def atribuiNome(self, nome):
        self._nome = nome
    #Manipular o nascimento
    @property
    def nasc(self):
        return self._nasc
    
    @nasc.setter
    def atribuiNasc(self, nasc):
        try: 
            datetime.strptime(nasc, '%d-%m-%Y')
            self._nasc = nasc
        except: 
            try: 
                datetime.strptime(nasc, '%d/%m/%Y')
                self._nasc = nasc
            except: 
                try: 
                    datetime.strptime(nasc, '%d %m %Y')
                    self._nasc = nasc
                except: print("data invalida")
        
    #Manipular a altura
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def atribuiAltura(self, altura):
        self._altura = altura
    
    #Calcular a idade 
    @property
    def idade(self):
        confirma = True
        try: 
            datetime.strptime(self._nasc, '%d-%m-%Y')
        except: 
            try: 
                datetime.strptime(self._nasc, '%d/%m/%Y')
            except: 
                try: 
                    datetime.strptime(self._nasc, '%d %m %Y')
                except: 
                    confirma = False
        if(confirma):
            separador = self.nasc[2]
            dia, mes, ano = list(map(lambda x: int(x),self._nasc.split(separador)))            
            ano_a, mes_a, dia_a = list(map(lambda x: int(x),str(datetime.now()).split(" ")[0].split("-")))

            idade = int(ano_a) - int(ano)
            if(mes_a < mes): idade -= 1
            elif mes_a == mes:
                if(dia_a < dia): idade -= 1
                
            return True, idade
        return False, "Formato de data inválido!"

    def cadastro(self, nome, nasc, altura):
        self.atribuiNome = nome
        self.atribuiNasc = nasc
        self.atribuiAltura = altura
    def imprime(self):
        print(self._nome, self._altura, self.idade[1])
                
            
        
if __name__ == "__main__":
    a = Pessoa()
    a.cadastro("Joao Vitor", "08/04/2001", 1.74)
    a.imprime()