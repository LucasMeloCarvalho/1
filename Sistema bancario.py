menu = """

[d] Depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0.00:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação invalida! Valor informado é invalido")


    elif opcao == "s":
        valor = float(input("informe o valor do Saque: "))

        excedeu_limite = valor > limite
        
        excedeu_saldo = valor > saldo
        
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação invalida! Você não possui saldo sulficiente.")

        elif excedeu_limite:
            print("Operação invalida! Valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação invalida! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1


        else:
            print("Operação invalida! Valor informado é invalido")

    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram ralizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")           
        print("=====================================") 

    elif opcao == "q":
        break

    else:
        print("Operação invalida!")