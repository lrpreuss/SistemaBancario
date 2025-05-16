import datetime
import json
import os #importa o módulo para verificar a existência do arquivo

nome_arquivo = "banco_dados.json" #nome do arquivo para salvar os dados

#Tenta carregar os dados do arquivo, se existir:
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            saldo = dados.get("saldo", 1000.0) #carrega o saldo, usa 1000.0 como padrão se não encontrar
            extrato = dados.get("extrato", [])#Carrega o extrato, usa [] como padrão
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados padrão.")
        saldo = 1000.0  #Saldo inicial
        extrato = [] #lista para armazenar as transações
else:
    saldo = 1000.0 #saldo inicial
    extrato = [] #lista para armazenar as transações

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
    
def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo, extrato  
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break 
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    
    if valor_saque <= saldo:
        saldo -= valor_saque
        agora = datetime.datetime.now()
        extrato.append({"data_hora": str(agora.strftime("%d/%m/%y %H:%M:%S")), "tipo": "Saque", "valor": valor_saque})
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")
        
def depositar():
    """Realiza a operação de depósito."""
    global saldo, extrato
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break 
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    saldo += valor_deposito
    agora = datetime.datetime.now()
    extrato.append({"data_hora": str(agora.strftime("%d/%m/%y %H:%M:%S")), "tipo": "Deposito", "valor": valor_deposito})
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo: .2f}")

def exibir_extrato():
    """Exibe extrato bancário"""
    global extrato
    if not extrato:
        print("Não foram realizadas transações.")
    else:
        print("\n--- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"] #.strftime("%d/%m/%Y %H:%M:%S")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        
#nova opção do menu - transferência bancária
def realizar_transferencia():
    global saldo, extrato
    while True:
        try:
            conta_destinatario = int(input("Digite o número da conta do destinatário:"))
            valor_transferencia = float(input("Digite o valor a ser transferido: R$ "))
            break
        except ValueError:
           print("Valores inválidos. Digite apenas números.")
      
    if valor_transferencia <= saldo:
        saldo -= valor_transferencia
        agora = datetime.datetime.now()
        extrato.append({"data_hora": str(agora.strftime("%d/%m/%y %H:%M:%S")), "tipo": "Transferencia", "valor": valor_transferencia})
        print(f"Transferência de R$ {valor_transferencia:.2f} realizado com sucesso para a conta {conta_destinatario}.")
        print(f"Seu novo saldo é: R$ {saldo: .2f}")
    else:
        print("Saldo insuficiente.")       
    
while True:
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato")
    print("5 - Realizar transferência")
    print("6 - Sair")

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1 <= opcao <= 6: #atualizado para a nova opção
                break 
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 6.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")
 
    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        exibir_extrato()
    elif opcao == 5: #nova opção
        realizar_transferencia()
    elif opcao == 6: #opção para sair
        print("Obrigado por utilizar o banco virtual!")
        break #Sai do laço while, encerrando o programa
    
# Salva o saldo e o extrato no arquivo antes de sair
try:
    with open(nome_arquivo, "w") as arquivo:
        json.dump({"saldo": saldo, "extrato": extrato}, arquivo, indent=4) #identação para melhor legibilidade
        print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}.")