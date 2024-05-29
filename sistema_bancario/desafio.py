menu = '''
**************************MENU***************************
[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair
************obrigado por usar nosso sistema**************
'''

saldo = 0
limite = 500
extrato = ""

numero_saque = 0
LIMITE_SAQUE = 3
while True:
    opcao = input(menu)
    if opcao == "d":
        print("Deposito")
        valor = float(input("informa o valor a depositar \n"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f} \n"
            print("foi depositado R$ {} \n Saldo actual {}".format(valor,saldo))
        else:
            print("Valor inválido, por favor, volte a tentar")
    elif opcao == "s":
        print("Saque")
        valor = float(input("informa o valor a sacar \n"))
        if saldo > valor and valor >= 0:
            numero_saque += 1 
            if numero_saque > LIMITE_SAQUE:
                print("Excedeu limite de saque diario")
                continue
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            print("foi sacado R$ {} \n Saldo actual {}".format(valor,saldo))
        elif valor < 0:
            print("O valor não pode ser negativo \n porfavor, volte a operar")
        elif valor > 500:
            print("R$ 500 é o valor máximo de saque")
        elif valor > saldo:
            print("Saldo insuficiente")

    elif opcao == "e":
        print("Extrato")
        print("\t\t\t=============MENU==========")
        print("não foram encontrados movimentações "if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operaçao inválida, por favor selecione novamente a operação desejada")
