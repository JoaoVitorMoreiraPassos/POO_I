import re
from refeicoes import * 
from discente import Discente
from funcionario import Funcionario
from administrador import Administrador

class Database():
    def __init__(self):
        self._usuarios = {}
        self._historico = Historico()
        self.add_admin("admin","admin")
        
    @property
    def usuarios(self):
        return self._usuarios   

    def validate(self, cpf):
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True
        
    def login(self, user, senha):
        if user in self._usuarios.keys():
            resultado = self._usuarios[user].verifica(senha)
            if resultado[0]:
                return True, self.usuarios[user]
            return False, resultado[1]
        return False, "|<< Usuário não castrado."
    
    def add_refeicao(self):
        self._historico.add_refeicao()
        
    def add_admin(self, usuario, senha):
        self._usuarios[usuario] = Administrador(usuario, senha)
    
    def add_discente(self, nome, user, cpf, curso, matricula, senha):
        if not self.validate(cpf):
            return False, "| << CPF inválido."
        if len(nome) == 0:
            return False, "| << Nome inválido."
        if len(user) == 0:
            return False, "| << Usuario inválido."
        if len(curso) == 0:
            return False, "| << Curso inválido."
        if len(senha) < 6:
            return False, "| << Senha inválida."
        if len(matricula) == 0:
            return False, "| << Matricula inválida."
        for usuario in self.usuarios.values():
            if isinstance(usuario, Administrador):
                continue
            if usuario.cpf == cpf:
                return False, "| << Esse CPF já está cadastrado em outro usuario."
            if usuario.matricula == matricula:
                return False, "| << Esta Matrícula já está cadastrada em outro usuario."
        if ( user not in self._usuarios.keys()):
            self._usuarios[user] = Discente(nome, cpf, curso, matricula, senha)
            return True, "| << Conta criada."
        return False, "| << Esse nome de usuario não está disponível."
    
    def add_funcionario(self, nome, user, cpf, cargo, senha):
        if not self.validate(cpf):
            return False, "| << CPF inválido."
        if len(nome) == 0:
            return False, "| << Nome inválido."
        if len(user) == 0:
            return False, "| << Usuario inválido."
        if len(cargo) == 0:
            return False, "| << Cargo inválido."
        if len(senha) < 6:
            return False, "| << Senha inválida."
        for usuario in self.usuarios.values():
            if isinstance(usuario, Administrador):
                continue
            if usuario.cpf == cpf:
                return False, "| << Esse CPF já está cadastrado."
        if ( user not in self._usuarios.keys() ):
            self._usuarios[user] = Funcionario(nome, cpf, cargo, senha)
            return True, "| << Conta criada."
        return False, "| << Esse nome de usuario não está disponível."
        
    def remove_usuarios(self, user, senha):
        if user in self.usuarios.keys():
            if(self.usuarios[user].verifica(senha))[0]:
                self._usuarios.pop(user)
                return True, "| << Conta excluida com sucesso."
            return False, "| << Senha incorreta."
        return False, "| << Esse usuário não está cadastrado."
        
    def criar_carteira(self, user, senha):      
        return self._usuarios[user].add_carteira(senha)
        
    def mostrar_usuarios(self):
        for user in self._usuarios.values():
            print(user._nome, user._cpf)

    def entrar(self, user):
        if(user in self._usuarios.keys()):
            if not isinstance(self._usuarios[user], Administrador):    
                result =  self._usuarios[user].entrada()
                if(result[0]):
                    self._historico.contador()
                return result
        return False, "| << Usuário não cadastrado."
        
    def deposito(self, user, valor): 
        if(user in self._usuarios.keys()):
            return self._usuarios[user].deposito(valor)
        return False, "| << Usuário não cadastrado."
    
    def mostrar_historico(self):
        return self._historico.mostra()
        
    