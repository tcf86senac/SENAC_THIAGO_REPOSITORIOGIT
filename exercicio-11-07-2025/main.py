#  11-07-2025 - Tarefa de Hoje:

# Criar um programa para gerenciar uma lista de tarefas do usuário usando manipulação de arquivos python para persistencia de dados. 
# Crie um menu de opções (Exibir tarefas adicionadas, adicionar nova tarefa, sair)
# Adicione a lógica de manipulação de arquivos para cade escolha do usuário. 

# Lembre de separar a sua lógica em funções e usar comentários na criação do programa.

import os
import main_funcoes

caminho = 'tarefa.txt'

while True:
    print('MENU - TAREFAS DE CASA')
    print("1. Adicionar nova tarefa")
    print("2. Ver as tarefas")
    print("3. Excluir tarefas")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")
    
    # Processa a escolha do usuário
    if escolha == "1":
        print("\nVocê escolheu a Opção 1")
        main_funcoes.atualizar_arquivo(caminho)
        print('\n\n')
    
    
    elif escolha == "2":
        print("\nVocê escolheu a Opção 2")
        main_funcoes.ler_arquivo(caminho)
        print('\n\n')

    elif escolha == "3":
        print("\nVocê escolheu a Opção 3")
        main_funcoes.deletar_tarefa(caminho)   

    elif escolha == "0":
        print("\nSaindo do programa...")
        break  # esse 'break' sai do 'loop while'

    
 
    else:
        print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 2.")