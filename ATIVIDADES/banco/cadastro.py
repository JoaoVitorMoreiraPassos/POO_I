from tkinter import Button
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from Contas import Banco
from functools import partial

class Cadastro():
    def __init__(self, banco):
        # Interface
        self.main = Tk()
        self.main.title("Cadastro")
        self.main.geometry("350x150+515+160")
        # Pega Nome
        self.lab_nome = Label(self.main, text="Nome:")
        self.lab_nome.place(x=15, y = 10, width=75, height=25)
        self.entr_nome = Entry(self.main, justify='center')
        self.entr_nome.place(x=85, y = 10, width=225, height=25)
        # Pega Senha
        self.lab_senha = Label(self.main, text="Senha:")
        self.lab_senha.place(x=15, y = 45, width = 75, height = 25)
        self.entr_senha = Entry(self.main, justify='center')
        self.entr_senha.place(x=85, y = 45, width=225, height=25)
        # Botão de Confirmação
        self.btn = Button(self.main, text="Confirmar", command=partial(self.getItems,banco))
        self.btn.place(x=350/2-50, y = 80, width=100, height=25)
        self.aviso = Label(self.main, anchor="center")
        self.main.mainloop()
        
    def close(self):
        self.main.destroy()
    def getItems(self, banco):
        # Extrai as informações dos inputs
        nome = self.entr_nome.get()
        senha = self.entr_senha.get()
        # Tenta Criar a Conta com as informações extraídas
        resposta, mensagem = banco.criarConta(nome, senha)
        # Se o cadastro o ocorrer bem
        if(resposta):
            # Limpa a janela e avisa que foi um sucesso
            self.lab_nome.destroy()
            self.entr_nome.destroy()
            self.lab_senha.destroy()
            self.entr_senha.destroy()
            self.btn.destroy()
            self.aviso['text'] = mensagem
            self.aviso.place(x=0, y = 10, width=350, height=25)
            self.sair = Button(self.main, text="Sair",command=self.close)
            self.sair.place(x=350/2-50, y = 45, width=100, height=25)
        else: # Se o houver algum erro no cadastro
            # Informa ao usuário o erro
            self.aviso['text'] = mensagem
            self.aviso.place(width=350, height=50, x=0, y = 110)
            

if __name__ == "__main__":
    from Contas import Banco
    b = Banco()
    Cadastro(b)