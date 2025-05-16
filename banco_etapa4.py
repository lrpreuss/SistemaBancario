saldo = 1000.0  #Saldo inicial (você pode alterar este valor)

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo  # Indica que estamos modificando a variável global saldo
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break #sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    global saldo 
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break #sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    saldo += valor_deposito
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo: .2f}")

#Código principal com loop while:
while True:
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1 <= opcao <= 4:
                break #sai do loop se a opção for válida
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")
 
    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        print("Obrigado por utilizar o banco virtual!")
        break #Sai do laço while, encerrando o programa