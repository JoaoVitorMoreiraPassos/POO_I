from banco import Banco


if __name__ == '__main__':
    def menu():
        print("-"*55)
        print("|"+"MENU".center(53," ")+"|")
        print("-"*55)
        acao = input(f"|{'1  - Cadastrar Funcionario':<53}|\n|{'2  - Cadastrar  Cliente':<53}|\n|{'3  - Criar Conta Corrente':<53}|\n|{'4  - Criar Conta Poupança':<53}|\n|{'5  - Criar Seguro de Vida':<53}|\n|{'6  - Calcular Tributação':<53}|\n|{'7  - Saque':<53}|\n|{'8  - Depósito':<53}|\n|{'9  - Transferir':<53}|\n|{'10 - Historico de transaçoes':<53}|\n|{'11 - Mostrar tudo':<53}|\n|{'12 - Sair':<53}|\n{'-'*55}\n| --> O que deseja fazer: ")
        print("-"*55)
        return acao
       
        
    banco = Banco()
    while True:
        acao = menu()
        resultado = None
        if ( acao == '1' ):   # Cadastrar Funcionario
            nome = input("| --> Insira um nome: ").upper()
            cpf = input("| --> CPF: ")
            nascimento = input("| --> Nascimento: ")
            salario = float(input("| --> Salário: "))
            resultado = banco.cadastrar_funcionario(nome, cpf, nascimento, salario)
        elif ( acao == '2' ):  # Cadastrar Clientes
            nome  = input("| --> Insira um nome: ").upper()
            cpf   = input("| --> CPF: ")
            nascimento = input("| --> Nascimento: ")
            profissao = input("| --> Profissão: ")
            resultado = banco.cadastrar_cliente(nome, cpf, nascimento, profissao)
        elif ( acao == '3' ):  # Criar conta corrente
            cpf   = input("| --> CPF: ")
            num   = input("| --> Numero da conta: ")
            resultado = banco.criar_conta_corrente(cpf, num)
        elif ( acao == '4' ):  # Criar conta poupança
            cpf   = input("| --> CPF: ")
            num   = input("| --> Numero da conta: ")
            resultado = banco.criar_conta_poupanca(cpf, num)
        elif ( acao == '5' ):  # Criar seguro
            cpf   = input("| --> CPF: ")
            mensal= input("| --> Valor mensal: ")
            total = input("| --> Total: ")
            resultado = banco.criar_seguro(cpf, mensal, total)
        elif ( acao == '6' ): # Calcular tributação
            resultado = banco.calc_tributos()
        elif ( acao == '7' ): # Saque
            cpf   = input("| --> CPF: ")
            num   = input("| --> Numero da conta: ")
            valor = input("| --> Valor: R$ ")
            resultado = banco.saque(cpf, num, valor)
        elif ( acao == '8' ): # Deposito
            cpf   = input("| --> CPF: ")
            num   = input("| --> Numero da conta: ")
            valor = input("| --> Valor: R$ ")
            resultado = banco.deposito(cpf, num, valor)
        elif ( acao == '9' ): # transferencia
            cpf1  = input("| --> CPF da conta de origem: ")
            contas = banco.consulta_contas(cpf1)
            if(contas[0]):
                if isinstance(contas[0], int):
                    if(contas[0] > 1):
                        for i in contas[1]:
                            print(f"| << {i}")
                num1  = input("| --> Numero da conta de origem: ")
            else: 
                print(contas[1])
                continue
            cpf2  = input("| --> CPF da conta de destino: ")
            contas = banco.consulta_contas(cpf2)
            if(contas[0]):
                if isinstance(contas[0], int):
                    if(contas[0] > 1):
                        for i in contas[1]:
                            print(f"| << {i}")
                num2  = input("| --> Numero da conta de destino: ")
            else:
                print(contas[1])
                continue
            valor = input("| --> Valor: R$ ")
            resultado = banco.transferir(cpf1, num1, cpf2, num2, valor)
        elif ( acao == '10' ): # Consultar historico de uma conta em específico
            cpf = input("| --> CPF: ")
            num = input("| --> Numero da conta: ")
            resultado = banco.extrato(cpf, num)
        elif ( acao == '11' ): # Mostrar todos os clientes cadastrados no banco
            resultado = banco.mostrar_tudo()
        elif ( acao == '12' ): # Sair
            break
        elif ( acao == '13'): # Listar clientes
            resultado = banco.lista_clientes()
        else: # Previni contra teclas que não estão nas condições acima
            resultado = False, "Opção Inválida!"
        print(resultado[1])
        