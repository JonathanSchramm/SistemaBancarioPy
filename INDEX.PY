import tkinter as tk
from tkinter import messagebox

saldo_valor = 500  # Define o valor inicial do saldo

arquivo_dados = "dados.txt"  # Banco de dados

def carregar_dados():  
    # Função para carregar os dados do arquivo
    global saldo_valor
    try:
        with open(arquivo_dados, "r") as arquivo:
            saldo_valor = float(arquivo.read())
    except FileNotFoundError:
        salvar_dados()

def salvar_dados():
    # Função para salvar os dados no arquivo
    global saldo_valor
    with open(arquivo_dados, "w") as arquivo:
        arquivo.write(str(saldo_valor))

def saldo():
    global saldo_valor
    print(f"Seu saldo é de: {saldo_valor}")

    voltar = input("Deseja voltar ao menu principal, sim ou não?\n")
    if voltar == "sim":
        print("Retornando...")
        menu_principal()
    else:
        saldo()

def sacar():
    # Função para realizar um saque
    global saldo_valor
    saque_valor = float(input("Digite o valor do saque: "))
    if saque_valor <= saldo_valor:
        saldo_valor -= saque_valor
        print(f"Saque no valor de: {saque_valor} realizado com sucesso!")
        opt = int(input("Digite [1] para ver seu novo saldo e [2] para voltar ao menu principal: "))
        if opt == 1:
            saldo()
        else:
            menu_principal()
    else:
        print("Saldo insuficiente, digite um valor válido!")
    salvar_dados()

def depositar():
    # Função para realizar um depósito
    global saldo_valor

    while True:
        deposito_valor = float(input("Favor inserir o valor do depósito: "))
        if deposito_valor < 0:
            print ("Valor de depósito inválido, digite um valor acima de zero.")
        else:
            saldo_valor += deposito_valor
            break

    print(f"Depósito no valor de: R${deposito_valor} reais realizado com sucesso!")

    while True:
        opt = input("Digite [1] para ver seu novo saldo e [2] para voltar ao menu principal: ")
        if opt == "1":
            saldo()
            break
        elif opt == "2":
            menu_principal()
            break
        else:
            print ("Opção inválida, selecione uma das opções acima.")

    salvar_dados()

def menu_principal():
    # Função que exibe o menu principal e lida com as opções do usuário
    print(
"""
        ======================BEM-VINDO======================

Seja muito bem-vindo ao nosso banco. Escolha uma das opções abaixo para continuar!

[1] Saldo
[2] Sacar
[3] Depositar
[4] Sair
""")
    while True:
        opcoes_menu = input("Digite aqui sua opção: ")

        if opcoes_menu == "1":
            saldo()
        elif opcoes_menu == "2":
            sacar()
        elif opcoes_menu == "3":
            depositar()
        elif opcoes_menu == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida escolha uma das opções acima.")

carregar_dados()
menu_principal()
