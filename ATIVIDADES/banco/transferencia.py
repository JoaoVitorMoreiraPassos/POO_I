from tkinter import *
from tkinter import ttk
from functools import partial

class Valor():
    def __init__(self,banco, cod1, cod2):
        # Interface para o usuário informar sua senha e o valor da transferência
        self.main = Tk()
        self.main.geometry("400x200+500+160")
        self.main.title("")
        self.saldo_atual = banco.contas[cod1].saldo
        self.saldo = Label(self.main, text=f"Seu saldo é de: R${self.saldo_atual}")
        self.lbl = Label(self.main, text="Valor(R$):")
        self.ent = Entry(self.main)
        self.lbl_senha = Label(self.main, text="Senha:")
        self.ent_senha = Entry(self.main)  
        self.saldo.place(x=0, y = 10, width=400, height=50)
        self.lbl.place(x=400/2-75, y = 60, width=75, height=25)
        self.ent.place(x=400/2, y = 60, width=100, height=25)
        self.lbl_senha.place(x=400/2-75, y = 90, width=75, height=25)
        self.ent_senha.place(x=400/2, y = 90, width=100, height=25)
        self.btncan = Button(self.main, text="Cancelar", anchor="center", command=self.main.destroy) # sSe o usuário quiser cancelar a transferencia
        self.btncon = Button(self.main, text="Confirmar",anchor="center", command=partial(self.fazTranferencia, banco, cod1, cod2)) # Votão para confirmar a transferência
        self.btncon.place(x=400/2+10, y = 140, width=100, height=25)
        self.btncan.place(x=400/2-110, y = 140, width=100, height=25)
        self.aviso = Label(self.main, anchor="center")
        
    def close(self):
        self.main.destroy()
        
    def fazTranferencia(self, banco, cod1, cod2):
        # Método para que irá fazer a transferência
        # Extrái os dados do inputs, valor e senha
        valor = self.ent.get()
        senha = self.ent_senha.get()
        # Tenta fazer a transferência
        resultado, mensagem = banco.transferir(cod1, cod2, valor, senha)
        if(resultado):  # Se a transferência for realizada com sucesso
            #Limpa e redimensiona a janela
            #Confirma para o usuário que a transferência ocorreu bem
            self.saldo.destroy()
            self.lbl.destroy()
            self.ent.destroy()
            self.lbl_senha.destroy()
            self.ent_senha.destroy()
            self.btncan.destroy()
            self.btncon.destroy()
            self.aviso['text'] = mensagem
            self.main.geometry("350x120")
            self.aviso.place(x=0, y = 10, width=350, height=25)
            sair = Button(self.main, text="Sair",command=self.close)
            sair.place(x=350/2-50, y = 45, width=100, height=25)
        else: # Se a transferência não der certo
            self.aviso['text'] = mensagem
            self.aviso['anchor'] = "center"
            self.aviso.place(width=400,height=35,x=0,y=165)
        
class Transferencia():
    def __init__(self, banco):
        # Interface inicial
        self.main = Tk()
        self.main.title("Selecionar Origem")
        self.main.geometry("600x200+500+160")

        # Busca os dados dos clientes para gerar o menu de seleção
        resultado, dados = banco.listaContas()
        if(resultado): # Se a busca ocorrer bem
            # Trata os dados extraídos
            dados = dados.split("|")
            while '\n-------------------------------------------------------\n' in dados:
                dados.remove('\n-------------------------------------------------------\n')
            if(len(dados) > 6): # Verifica se existe mais de 1 cliente cadastrado
                # Pois não faz sentido um usuário fazer uma tranferência para ele mesmo
                print(len(dados))
                print(dados)
                #Cria uma tela com scroll
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
                    # chamam o método selecionaDestino que irá abir um menu para selecionar o destinátario da transferência
                    if(i>0):
                        btns.append(Button(self.second_frame,bd=1, relief="solid", text="Selecionar", command=partial(self.selecionaDestino, banco,dados[i].strip()), bg="#70aa87", cursor="hand2", anchor="center"))
                        btns[cont_btn].place(x=posx+450, y=posy, width=100, height=25)
                        cont_btn+=1
                    posy+=25
            else: # Se houver apenas 1 usuário cadastrado
                self.main.geometry("350x100")
                self.lbl = Label(self.main, text="APENAS 1 USUÁRIO CADASTRADO!", anchor="center")
                self.lbl.place(width=350, height=50, x=0, y = 100/2-25)
                
                
        else: #Se a busca por usuários de errado
            self.main.geometry("350x100")
            self.lbl = Label(self.main, text="NENHUM USUÁRIO CADASTRADO!", anchor="center")
            self.lbl.place(width=350, height=50, x=0, y = 100/2-25)
        self.main.mainloop()
        
    def selecionaDestino(self, banco, codigo):
        self.main.destroy()
        Destino(banco,codigo)
        
class Destino():
    def __init__(self, banco, cod1):
        # Interface para selecionar o destinatário
        self.main = Tk()
        self.main.title("Selecionar Destino")
        self.main.geometry("600x200+500+160")

        # Busca os dados dos clientes para gerar o menu de seleção
        resultado, dados = banco.listaContas()
        if(resultado): # Se a busca ocorrer bem
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
            linha = 0
            posy = 2
            posx = 15
            for i in range(0, len(dados)-2, 3):
                if(dados[i].strip() != cod1): # Verifica se o usuárid da iteração atual é diferente do usuário que está tranferindo o dinheiro
                    lbls.append(Label(self.second_frame, text=f"{dados[i]}", bd=1, relief="solid", anchor="center"))
                    lbls.append(Label(self.second_frame, text=f"{dados[i+1]}", bd=1, relief="solid",padx=10, anchor="center"if i == 0 else "w"))
                    lbls.append(Label(self.second_frame, text=f"{dados[i+2]}", bd=1, relief="solid", anchor="center"))
                    lbls[len(lbls)-3].place(x=posx,y=posy, width=45, height= 25)
                    lbls[len(lbls)-2].place(x=posx+45,y=posy, width=350, height= 25)
                    lbls[len(lbls)-1].place(x=posx+350,y=posy, width=100, height= 25)
                    
                    # Botões para selecionar o usuário desejado,
                    # chamam o método selecionaValor que irá abir uma janela para o usuário confirmar o valor e sua senha 
                    if(i>0):
                        btns.append(Button(self.second_frame,bg="#70aa87", cursor="hand2", anchor="center", text="Selecionar", command=partial(self.selecionaValor, banco,cod1,dados[i].strip())))
                        btns[cont_btn].place(x=posx+450, y=posy, width=100, height=25)
                        cont_btn+=1
                    posy +=25
                    linha += 1 
                
        else: # Se houver algo de errado com a busca
            self.main.geometry("350x100")
            self.lbl = Label(self.main, text="NENHUM USUÁRIO CADASTRADO!", anchor="center")
            self.lbl.place(width=350, height=50, x=0, y = 100/2-25)
        self.main.mainloop()
        
    def selecionaValor(self, banco, cod, cod2):
        self.main.destroy()
        Valor(banco,cod, cod2)
        
if __name__ == "__main__":
    from Contas import Banco
    b = Banco()
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    b.criarConta("Joao", "asdfasdf")
    Transferencia(b)