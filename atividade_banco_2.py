saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
usuarios = []
agencia = 0000
conta = []


def cadastrar_usuario():
    cpf = int(input("Insira o CPF "))
    if cpf not in usuarios:
        nome = input("Insira o nome completo ")
        nascimento = input("Insira a data de nascimento ")
        endereco = input("Insira o endereço ").split()
        usuarios.extend([nome, cpf, nascimento, endereco])

    else:
        print("Usuario já cadastrado")


def cadastrar_conta():
    global agencia
    cpf = int(input("Insira o CPF para ser cadastrado: "))
    if cpf in usuarios:
        agencia += 1
        conta.extend(["0001", agencia, cpf])
    else:
        print("Usuário não encontrado")


def depositar():
    global saldo
    global extrato
    quantia = float(input("Insira o valor para ser depositado: "))
    if quantia > 0:
        saldo += quantia
        extrato += f"Deposito de {quantia:.2f}\n"
        print("Valor depositado com sucesso!")
    else:
        print("Insira uma quantia valida")


def sacar():
    global saldo
    global extrato
    global limite
    global LIMITE_SAQUES

    if saldo > 0:
        quantia = float(input("Insira o valor para ser sacado: "))

        if quantia > limite:
            print("Você não pode fazer um saque maior que o seu limite")
        elif quantia > saldo:
            print("Você não possui saldo na conta")
        elif LIMITE_SAQUES <= 0:
            print("Você não pode mais fazer saques hoje")
        elif saldo > quantia <= limite and LIMITE_SAQUES > 0:
            saldo -= quantia
            extrato += f"Saque de {quantia} feito\n"
            LIMITE_SAQUES -= 1
        else:
            print("Insira um valor valido")
    else:
        print("Você não possui saldo na conta")


def extrato_f():
    global saldo
    global extrato
    global limite
    global LIMITE_SAQUES
    print("Extrato da conta corrente")
    print(f"O saldo atual da conta é de R${saldo}")
    print(f"Você ainda pode fazer {LIMITE_SAQUES} saques hoje, e seu limite é de R${limite}")
    print(extrato)


menu = """
[1] Cadastro de Usúario
[2] Cadastro de Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair
"""

while True:
    print(menu)
    option = input("Insira a opção desejada: ")

    if option == "1":
        cadastrar_usuario()

    elif option == "2":
        cadastrar_conta()

    elif option == "3":
        depositar()

    elif option == "4":
        sacar()

    elif option == "5":
        extrato_f()

    elif option == "6":
        break

    elif option == "7":
        print(usuarios)
        print(conta)

    else:
        print("Opção invalida, tente novamente")
