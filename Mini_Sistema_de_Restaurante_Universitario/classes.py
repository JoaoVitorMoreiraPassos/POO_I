class Wallet:
    def __inti__(self, code, balance):
        self.code = code
        self.balance = balance
        
        
class User:
    def __init__(self, code,username,password, name, registration, cpf, course, wallet = Wallet()):
        self.code = code
        self.username = username
        self.password = password
        self.name = name
        self.registration = registration
        self.cpf = cpf
        self.course = course
        self.wallet = wallet
    
