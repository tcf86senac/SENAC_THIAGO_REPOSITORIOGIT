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


