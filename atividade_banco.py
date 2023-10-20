saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""


while True:
    print(menu)
    option = input("Insira a opção ")

    if option == "d":
        deposito = float(input("Insira o valor para ser depositado: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito de {deposito:.2f} \n"
        else:
            print("Insira um valor válido")

    elif option == "s":
        if LIMITE_SAQUES > 0 and saldo > 0:
            sacar = float(input("Insira o valor para ser sacado: "))
            resto = saldo - sacar
            if sacar <= 0 or resto < 0 or sacar >= limite:
                print("Insira um valor válido")
            else:
                saldo -= sacar
                LIMITE_SAQUES -= 1
                extrato += f"Saque no valor de {sacar:.2f}\n"
        else:
            print("Você não pode sacar no momento")

    elif option == "e":
        print("Seu extrato atual:")
        print(f"O saldo atual na conta é de {saldo}")
        print(f"Você ainda pode fazer {LIMITE_SAQUES} saques hoje")
        print(extrato)
    elif option == "q":
        break
    else:
        print("Insira uma opção valida")
