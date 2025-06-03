import os
from time import sleep
os.system("clear || cls")

ARQUIVO_CONTAS = "arquivo_contas.txt"

def menu():
    while True:
        print("""
              
🏦   SISTEMA BANCÁRIO PYTHON   

[1]   Criar conta
[2]   Listar contas
[3]   Depositar
[4]   Sacar
[5]   Sair
""")
        print("═" * 30) 
              
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("\nDigite o nome do titular: ")
                cpf = input("Digite o CPF (apenas números): ")
                saldo = float(input("Digite o saldo inicial: "))
                criar_conta(nome, cpf, saldo)
            except ValueError:
                print("\n Valor inválido. Tente novamente.")

        elif opcao == "2":
            listar_contas()

        elif opcao == "3":
            cpf = input("\nDigite o CPF da conta para depósito: ")
            contas = carregar_contas()
            conta = next((c for c in contas if c["cpf"] == cpf), None)
            if not conta:
                print("\n Conta não encontrada.")
            else:
                try:
                    valor = float(input("Valor do depósito: "))
                    depositar(cpf, valor)
                except ValueError:
                    print("\ Valor inválido. Tente novamente.")

        elif opcao == "4":
            cpf = input("\nDigite o CPF da conta para saque: ")
            contas = carregar_contas()
            conta = next((c for c in contas if c["cpf"] == cpf), None)
            if not conta:
                print("\ Conta não encontrada.")
            else:
                try:
                    valor = float(input("Valor do saque: "))
                    sacar(cpf, valor)
                except ValueError:
                    print("\ Valor inválido. Tente novamente.")

        elif opcao == "5":
            print("\nEncerrando o sistema... Até logo!")
            sleep(1.5)
            break

        else:
            print("\ Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_contas():
    contas = []
    try:
        with open(ARQUIVO_CONTAS, "r") as arquivo:
            for linha in arquivo:
                nome, cpf, saldo = linha.strip().split(",")
                contas.append({"nome": nome, "cpf": cpf, "saldo": float(saldo)})
    except FileNotFoundError:
        pass
    return contas

def salvar_contas(contas):
    with open(ARQUIVO_CONTAS, "w") as arquivo:
        for conta in contas:
            arquivo.write(f"{conta['nome']},{conta['cpf']},{conta['saldo']}\n")

def criar_conta(nome, cpf, saldo_inicial):
    contas = carregar_contas()
    for conta in contas:
        if conta["cpf"] == cpf:
            print("\ Já existe uma conta com esse CPF.")
            return
    contas.append({"nome": nome, "cpf": cpf, "saldo": saldo_inicial})
    salvar_contas(contas)
    print(f"\nConta criada com sucesso para {nome} (CPF: {cpf})!")

def listar_contas():
    contas = carregar_contas()
    if not contas:
        print("\nNenhuma conta encontrada.")
    else:
        print("\n --- Contas Cadastradas ---")
        for conta in contas:
            print(f" Titular: {conta['nome']} | CPF: {conta['cpf']} | Saldo: R${conta['saldo']:.2f}")

def depositar(cpf, valor):
    contas = carregar_contas()
    for conta in contas:
        if conta["cpf"] == cpf:
            conta["saldo"] += valor
            salvar_contas(contas)
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso para {conta['nome']} (CPF: {cpf}).")
            return
    print("\ Conta não encontrada.")

def sacar(cpf, valor):
    contas = carregar_contas()
    for conta in contas:
        if conta["cpf"] == cpf:
            if conta["saldo"] >= valor:
                conta["saldo"] -= valor
                salvar_contas(contas)
                print(f"\nSaque de R${valor:.2f} realizado com sucesso para {conta['nome']} (CPF: {cpf}).")
            else:
                print("\ Saldo insuficiente.")
            return
    print("\ Conta não encontrada.")
    
menu()
    