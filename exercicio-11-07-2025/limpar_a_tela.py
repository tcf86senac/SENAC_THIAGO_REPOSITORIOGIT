import os

def limpar_tela():
    os.system('cls')

opcao = input("Menu de opções padrãozão.\n1- Opção 1\n2- Opção 2\n")
limpar_tela()
print('Você escolheu:',opcao)