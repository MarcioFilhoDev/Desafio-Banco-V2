from datetime import datetime

import random as rd
import os
import platform


# Função para limpar o console
def limparConsole():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Declaração das variaveis
opcaoA = 0
contas = []
usuarios = {}


# Funcao criar usuario
def criarUsuario():
    # Dados: cpf, nome, idade
    print("Preencha com os dados do usuário: \n")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    conta = gerarConta()
    saldo = 0
    saque = 0
    limiteDiario = 0
    lista_transacoes = ""

    if cpf in usuarios:
        print("Usuário possui conta registrada!")
    else:
        usuarios[cpf] = [
            conta,
            nome,
            idade,
            saldo,
            limiteDiario,
            lista_transacoes,
            saque,
        ]
    limparConsole()
    return usuarios


# Apresenta lista de usuarios cadastrados
def listaUsuarios(usuarios):
    for cpf, dados in usuarios.items():
        (
            conta,
            nome,
            idade,
            saldo,
            limiteDiario,
            lista_transacoes,
            saque,
        ) = dados
        # print("Usuários cadastrados: \n")
        print(f"CPF: {cpf} | Nome: {nome} | Saldo: R$ {saldo} \n")


# Funcao criar conta corrente
def gerarConta():
    if len(contas) == 0:
        numeroGerado = rd.randint(100000, 999999)
        contas.append(numeroGerado)
    else:
        numeroGerado = rd.randint(100000, 999999)
        if numeroGerado in contas:
            return False
        else:
            contas.append(numeroGerado)
    return numeroGerado


# Funcao acessar conta do usuario
def acessarContaUsuario():
    cpf = input("Digite seu CPF: ")
    if cpf in usuarios:
        (
            conta,
            nome,
            idade,
            saldo,
            limiteDiario,
            lista_transacoes,
            saque,
        ) = usuarios[cpf]
        print("Acessando: \n")
        print(
            f"Nome: {nome} | Idade: {idade} | Número da conta: {conta} | Saldo disponível: R$ {saldo}"
        )
        return cpf, saldo, lista_transacoes, limiteDiario, saque
    else:
        print("Usuario não existe")
        return False


# Funcao deposito
def deposito(saldo, lista_transacoes):
    valor_deposito = float(input("Depositando: R$ "))
    if valor_deposito <= 0:
        print("Valor inválido para depositar!")
    else:
        lista_transacoes += f"Deposito de R$ {valor_deposito:,.2f} reais \n\b Data da operação: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} \n"
        saldo += valor_deposito  # Incremento do saldo referente ao valor depositado
    return saldo, lista_transacoes


# Funcao saque
def sacar(saldo, lista_transacoes, limiteDiario, saque):
    valor = float(input("Retirando: R$ "))
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor < 500:
        limiteDiario += 1
        saldo -= valor
        lista_transacoes += f"Saque de R$ {valor:,.2f} reais \n\b Data da operação: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} \n"
    elif valor >= 500:
        if limiteDiario >= 3:
            print("Limite de saques atingido!")
        else:
            limiteDiario += 1
            saldo -= valor
            lista_transacoes += f"Saque de R$ {valor:,.2f} reais - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} \n"
    return saldo, lista_transacoes, limiteDiario, saque


# Funcao extrato
def extrato(saldo, lista_transacoes):
    print(
        f"""
>> Transações:
{lista_transacoes}
            
>> Extrato Bancário:
Saldo da conta: R$ {saldo:,.2f}
"""
    )


limparConsole()
while opcaoA != 4:
    print(
        """ 
1 - Cadastrar Usuário
2 - Lista de Usuários
3 - Acessar Conta Bancária do Usuário
4 - Sair"""
    )
    opcaoA = int(input("\n>> Escolha uma opção: "))
    if opcaoA == 1:
        limparConsole()
        criarUsuario()
    elif opcaoA == 2:
        limparConsole()
        if len(usuarios) == 0:
            print("Não existem usuários cadastrados. \n")
        else:
            listaUsuarios(usuarios)
    elif opcaoA == 3:
        limparConsole()
        if len(usuarios) == 0:
            print("Não existem usuários cadastrados. \n")
        else:
            opcaoB = 0
            cpf, saldo, lista_transacoes, limiteDiario, saque = acessarContaUsuario()
            while opcaoB != 4:
                print(
                    """
1 -> Depósito
2 -> Saque
3 -> Histórico
4 -> Sair
"""
                )
                opcaoB = int(input("\n>> Escolha uma opção: "))
                if opcaoB == 1:
                    saldo, lista_transacoes = deposito(saldo, lista_transacoes)
                    usuarios[cpf] = [
                        usuarios[cpf][0],
                        usuarios[cpf][1],
                        usuarios[cpf][2],
                        saldo,
                        limiteDiario,
                        lista_transacoes,
                        saque,
                    ]
                    limparConsole()
                elif opcaoB == 2:
                    saldo, lista_transacoes, limiteDiario, saque = sacar(
                        saldo, lista_transacoes, limiteDiario, saque
                    )
                    usuarios[cpf] = [
                        usuarios[cpf][0],
                        usuarios[cpf][1],
                        usuarios[cpf][2],
                        saldo,
                        limiteDiario,
                        lista_transacoes,
                        saque,
                    ]
                    limparConsole()
                elif opcaoB == 3:
                    # limparConsole()
                    extrato(saldo, lista_transacoes)
                elif opcaoB == 4:
                    limparConsole()
                    print("Saindo")
                    break
                else:
                    limparConsole()
                    print("Opcao Invalida")

    elif opcaoA == 4:
        limparConsole()
        print("Volte Sempre!")
        break
    else:
        print("Opção Inválida.")
