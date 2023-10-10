menu = "\n[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair\n"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido, tente novamente")
        
    elif opcao == "s":
        valor = float(input("Insira o valor para saque "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sem saldo na conta, tente novamente")
        elif excedeu_limite:
            print("Excedeu o Limite de saque, tente novamente ")
        elif excedeu_saques:
            print("Numero maximo de saques atingido, aguarde até amanha")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor invalido, tente novamente")

    elif opcao == "e":
        print("\n Extrato da conta")
        print("A conta não foi movimentada" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Opção invalida, tente novamente")
