import os

def limpar_tela():
    os.system('cls')

def esperar_input():
    input("Aperte qualquer tecla para continuar...")
    limpar_tela()

while True:
    opcao = int(input("Menu de opções padrãozão.\n1- Opção 1\n2- Opção 2\n"))

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    else:
        limpar_tela()
        print("Opção inválida!")
        esperar_input()
