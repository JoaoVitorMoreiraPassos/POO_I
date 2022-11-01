from tkinter import *
from tkinter import ttk

class Tabela():
    def __init__(self, banco):
        #Interface inicial
        self.main = Tk()
        self.main.title("Contas")
        self.main.geometry("500x200+500+160")
        self.main_frame = Frame(self.main)
        self.main_frame.pack(fill=BOTH, expand=1)
        
        # Busca os dados dos clientes
        resultado, dados = banco.listaContas()
        # Se tudo ocorrer bem na busca
        if(resultado):
            # Preparando uma tela com scroll
            self.my_canvas = Canvas(self.main_frame)
            self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            
            self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
            self.my_scrollbar.pack(side=RIGHT, fill=Y)
            
            self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
            self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

            self.second_frame = Frame(self.my_canvas)
            
            self.second_frame.place(x=0,y=0,width=600,height=200)

            # Trata os dados extraidos
            dados = dados.split("|")
            while '\n-------------------------------------------------------\n' in dados:
                dados.remove('\n-------------------------------------------------------\n')
            # Cria uma tabela com os dados dos usuários utilizando os dados extraídos
            lbls = []
            posy = 2
            posx = 15
            for i in range(0, len(dados)-2, 3):
                lbls.append(Label(self.second_frame, text=f"{dados[i]}", bd=1, relief="solid", anchor="center"))
                lbls.append(Label(self.second_frame, text=f"{dados[i+1]}", bd=1, relief="solid",padx=10, anchor="center"if i == 0 else "w"))
                lbls.append(Label(self.second_frame, text=f"{dados[i+2]}", bd=1, relief="solid", anchor="center"))
                lbls[i].place(x=posx,y=posy, width=45, height= 25)
                lbls[i+1].place(x=posx+45,y=posy, width=350, height= 25)
                lbls[i+2].place(x=posx+350,y=posy, width=100, height= 25)
                posy += 25
        else: # Se houver algo de errado com a busca dos dados
              # Mostra o erro ao usuário
            self.main.geometry("350x100")
            self.lbl = Label(self.main, text="NENHUM USUÁRIO CADASTRADO!", anchor="center")
            self.lbl.place(width=350, height=50, x=0, y = 100/2-25)
        self.main.mainloop()
        
    
