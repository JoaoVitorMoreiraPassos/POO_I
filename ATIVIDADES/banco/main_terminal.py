# João Vitor Moreira Passos

from Contas import Banco

def menu(obj):
        print("-"*55)
        print("|"+"MENU".center(53," ")+"|")
        print("-"*55)
        acao = input(f"|{'1 - Criar conta':<53}|\n|{'2 - Listar contas':<53}|\n|{'3 - Saque':<53}|\n|{'4 - Deposito':<53}|\n|{'5 - Excluir conta':<53}|\n|{'6 - Transferencia':<53}|\n|{'7 - Ver historico':<53}|\n|{'8 - Sair':<53}|\n{'-'*55}\n| << O que deseja fazer: ")
        print("-"*55)
        if(acao == '1'):   
            nome = input("| << Insira um nome: ").upper()
            senha = input("| << Senha: ")
            return obj.criarConta(nome, senha)
        elif(acao == '2'): 
            return obj.listaContas()
        elif(acao == '3'): 
            resultado, mensagem = obj.listaContas()
            if(resultado):
                print(f"|{mensagem}")
                cod = input("| << Digite o codigo da sua conta: ")
                senha = input("| << Senha: ")
                valor = input("| << Valor a ser sacado: R$")
                return obj.sacarValor(cod, valor, senha)
            else:
                return resultado, mensagem
        elif(acao == '4'): 
            resultado, mensagem = obj.listaContas()
            if(resultado):
                print(f"|{mensagem}")
                cod = input("| << Digite o codigo da sua conta: ")
                senha = input("| << Senha: ")
                valor = input("| << Valor do depósito: R$")
                return obj.depositaValor(cod, valor, senha)
            else:
                return resultado, mensagem
        elif(acao == '5'): 
            resultado, mensagem = obj.listaContas()
            if(resultado):
                print(f"|{mensagem}")
                cod = input("| << Digite o código da sua conta: ")
                senha = input("| << Senha: ")
                return obj.excluirConta(cod, senha)
            else:
                return resultado, mensagem
        elif(acao == '6'):
            resultado, mensagem = obj.listaContas()
            if(resultado):
                print(f"|{mensagem}")
                cod1 = input("| << Conta de origem: ")
                cod2 = input("| << Conta de destino: ")
                senha = input("| << Senha: ")
                valor = input("| << Valor: R$")
                return obj.transferir(cod1, cod2, valor, senha)
            else:
                return resultado, mensagem
        elif(acao == "7"):
            resultado, mensagem = obj.listaContas()
            if(resultado):
                print(f"|{mensagem}")
                cod = input("Codigo: ")
                senha = input("Senha: ")
                return obj.mostrarHistorico(cod, senha)
            return resultado, mensagem
        elif(acao == '8'): 
            return "0", "Volte sempre!"
        
        else: 
            return False, "Opção Inválida!"
        

banco = Banco()
while True:
    acao = menu(banco)
    print(f"|{acao[1]}")
    print("\n")
    if(acao[0] == "0"):break
    