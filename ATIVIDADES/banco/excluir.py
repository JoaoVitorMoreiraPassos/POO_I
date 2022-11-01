from tkinter import *
from tkinter import ttk
from functools import partial

        
class Senha():
    def __init__(self,banco, cod):
        # interface para confirmar a senha do usuário
        self.main = Tk()
        self.main.geometry("400x200+500+160")
        self.main.title("Excluir Conta")  
        self.lbl_senha = Label(self.main, text="Senha:")
        self.ent_senha = Entry(self.main)   
        self.lbl_senha.place(x=400/2-87.5, y = 60, width=75, height=25)
        self.ent_senha.place(x=400/2-12.5, y = 60, width=100, height=25)
        self.btncan = Button(self.main, text="Cancelar", anchor="center", command=self.main.destroy)
        self.btncon = Button(self.main, text="Confirmar",anchor="center", command=partial(self.exclui, banco, cod))   
        self.btncon.place(x=400/2+10, y = 100, width=100, height=25)
        self.btncan.place(x=400/2-110, y = 100, width=100, height=25)
        self.aviso = Label(self.main, anchor="center")
        
    def close(self):
        self.main.destroy()
        
    def exclui(self, banco, cod):
        # Método que irá excluir a conta do usuário
        senha = self.ent_senha.get()
        # Tenta excluir a conta
        resultado, mensagem = banco.excluirConta(cod, senha)
        if(resultado): # Se der tudo certo
            #Limpa e redimensiona a janela
            # Informa ao usuário que a exclusão ocorreu com sucesso
            self.lbl_senha.destroy()
            self.ent_senha.destroy()
            self.btncan.destroy()
            self.btncon.destroy()
            self.main.geometry("350x120")
            self.aviso['text'] = mensagem
            self.aviso.place(x=0, y = 10, width=350, height=25)
            sair = Button(self.main, text="Sair",command=self.close)
            sair.place(x=350/2-50, y = 45, width=100, height=25)
        else: #Se a exlusão der errado
            #informa ao usuário o erro
            self.aviso['text'] = mensagem
            self.aviso['anchor'] = "center"
            self.aviso.place(width=400,height=35,x=0,y=165)        
        
class Excluir():
    def __init__(self, banco):
        # Interface inicial
        self.main = Tk()
        self.main.title("Contas")
        self.main.geometry("600x200+500+160")
        self.main.title("Excluir")
        
        # Busca os dados dos clientes para gerar o menu de seleção
        resultado, dados = banco.listaContas()
        if(resultado):# Se a busca ocorrer bem
            # Cria uma tela com scroll
            
            self.main_frame = Frame(self.main)
            self.main_frame.pack(fill=BOTH, expand=1)
            self.my_canvas = Canvas(self.main_frame)
            self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            
            self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
            self.my_scrollbar.pack(side=RIGHT, fill=Y)
            
            self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
            self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

            self.second_frame = Frame(self.my_canvas)
            self.second_frame.place(x=0,y=0,width=600,height=200)

            # Trata os dados extraídos
            dados = dados.split("|")
            while '\n-------------------------------------------------------\n' in dados:
                dados.remove('\n-------------------------------------------------------\n')
            # Gera o menu de seleção com os dados extraídos
            lbls = []
            btns = []
            cont_btn = 0
            posy = 2
            posx = 15
            for i in range(0, len(dados)-2, 3):
                lbls.append(Label(self.second_frame, text=f"{dados[i]}", bd=1, relief="solid", anchor="center"))
                lbls.append(Label(self.second_frame, text=f"{dados[i+1]}", bd=1, relief="solid",padx=10, anchor="center"if i == 0 else "w"))
                lbls.append(Label(self.second_frame, text=f"{dados[i+2]}", bd=1, relief="solid", anchor="center"))
                lbls[i].place(x=posx,y=posy, width=45, height= 25)
                lbls[i+1].place(x=posx+45,y=posy, width=350, height= 25)
                lbls[i+2].place(x=posx+350,y=posy, width=100, height= 25)
                # Botões para selecionar o usuário desejado,
                # chamam o método excluir que irá gerar outra janela para confirmar a senha do usuário
                if(i>0):
                    btns.append(Button(self.second_frame,bg="#70aa87", cursor="hand2", anchor="center", text="Excluir", command=partial(self.excluir, banco,dados[i].strip())))
                    btns[cont_btn].place(x=posx+450, y=posy, width=100, height=25)
                    cont_btn += 1
                posy += 25
            self.aviso = Label(self.main, anchor="center")

                
        else:
            self.main.geometry("350x100")
            self.lbl = Label(self.main, text="NENHUM USUÁRIO CADASTRADO!", anchor="center")
            self.lbl.place(width=350, height=50, x=0, y = 100/2-25)
        self.main.mainloop()
    
    def close(self):
        self.main.destroy()
        
    def excluir(self, banco, codigo):
        Senha(banco, codigo)
        self.close()
        

if __name__ == "__main__":
    from Contas import Banco
    b = Banco()
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    Excluir(b)