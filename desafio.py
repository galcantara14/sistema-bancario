LIMITE_SAQUE = 3
saques = 0
saldo = 0
limite = 500
extrato = ""

menu = """ 

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print('Operação falhou! valor inválido')
    elif opcao == '2':
        valor = float(input("Insira o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou! saldo insuficiente")
        elif excedeu_limite:
            print("Operação falhou! valor do saque excede o limite!")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif  valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: .2f}\n"
                saques += 1
        else:
            print("Operação falhou! Valor invalido!")
            
    elif opcao == '3':
        print("\n****************** EXTRATO ******************")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("**********************************************")

    elif opcao == '0':
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação invalida!")
