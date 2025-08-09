import os

caminho = "Manipulação de Arquivos em Python/tarefas.txt"

def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            print(linha.strip())

def atualizar_arquivo(caminho):
    nova_linha = input("Digite a tarefa de casa a ser incluída:\n")
    with open(caminho, 'a', encoding='utf-8') as arquivo:
        arquivo.write(nova_linha+"\n")

def escrever_arquivo(caminho):
    texto = input("Digite o texto para adicionar:\n")
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)

def criar_arquivo(caminho):
    with open(caminho, 'x', encoding='utf-8') as arquivo:
        arquivo.write("Agora sim!")

def deletar_arquivo(caminho):
    os.remove(caminho)

###########################  teste ################################################
def deletar_tarefa(caminho):
    # Primeiro, ler todas as tarefas
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        tarefas = arquivo.readlines()
    
    if not tarefas:
        print("Não há tarefas para excluir!")
        return
    
    # Mostrar as tarefas numeradas
    print("\nTarefas disponíveis:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa.strip()}")
    
    # Pedir ao usuário para escolher qual tarefa excluir
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja excluir: "))
        if 1 <= escolha <= len(tarefas):
            # Remover a tarefa escolhida
            tarefa_removida = tarefas.pop(escolha - 1)
            
            # Reescrever o arquivo sem a tarefa removida
            with open(caminho, 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(tarefas)
            
            print(f"Tarefa '{tarefa_removida.strip()}' removida com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Por favor, digite um número válido!")