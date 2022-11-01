from Contas import Banco
# from ast import main
# from os import RWF_NOWAIT
from tkinter import *
from tkinter.tix import COLUMN
from cadastro import Cadastro
from functools import partial
from tkinter import ttk
from clientes import Tabela
from saque import Saque
from deposito import Deposito
from excluir import Excluir
from transferencia import Transferencia


if __name__ == "__main__":
    banco = Banco()
    main = Tk()

    main.geometry("500x500+500+130")
    main.resizable(width=False, height=False)
    main.title("Banco do Estudante")
    main['bg'] = "white"

    titulo = Label(main, text="BEM-VINDO(A)", anchor="center",font=24,bd=1,relief="solid", bg="#70aa87")
    titulo.place(x=0, y = 10, width=500, height=50)

    novaconta = Button(main, text="Criar Conta", command=partial(Cadastro,banco), bg="#70aa87", cursor="hand2")
    novaconta.place(width=200, x=25, y= 150, height=50)

    listar = Button(main, text="Mostrar Contas", command=partial(Tabela, banco), bg="#70aa87", cursor="hand2")
    listar.place(width=200, x=275, y= 150, height=50)

    sacar = Button(main, text="Saque", command=partial(Saque, banco), bg="#70aa87", cursor="hand2")
    sacar.place(width=200, x=25, y= 225, height=50)

    depositar = Button(main, text="Deposito", command=partial(Deposito, banco), bg="#70aa87", cursor="hand2")
    depositar.place(width=200, x=275, y= 225, height=50)

    transferir = Button(main, text="Transferencia", command=partial(Transferencia, banco), bg="#70aa87", cursor="hand2")
    transferir.place(width=200, x=25, y= 300, height=50)

    excluir = Button(main, text="Excluir conta", command=partial(Excluir, banco), bg="#70aa87", cursor="hand2")
    excluir.place(width=200, x=275, y= 300, height=50)

    sair = Button(main, text="Sair", command=main.destroy, bg="#70aa87", cursor="hand2")
    sair.place(width=200, x=500/2-100, y= 375, height=50)

    main.mainloop()

