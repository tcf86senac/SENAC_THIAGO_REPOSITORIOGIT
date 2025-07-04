import random


print("JO-KEN-PO")
escolha_do_jogador = input("Escolha seu movimento: Pedra, Papel ou Tesoura:  ")
escolha_do_jogador = escolha_do_jogador.lower()

possiveis_escolhas = ["Pedra", "Papel", "Tesoura"]

escolha_do_computador = random.choice(possiveis_escolhas)
escolha_do_computador = escolha_do_computador.lower()

if escolha_do_jogador == escolha_do_computador:
    print("Empate!")
elif escolha_do_jogador == "pedra":
    if escolha_do_computador == "tesoura":
        print("Você ganhou.")
    elif escolha_do_computador == "papel":
        print("Você perdeu.")
elif escolha_do_jogador == "papel":
    if escolha_do_computador == "tesoura":
        print("Você perdeu.")
    elif escolha_do_computador == "pedra":
        print("Você ganhou.")
elif escolha_do_jogador == "tesoura":
    if escolha_do_computador == "papel":
        print("Você ganhou.")
    elif escolha_do_computador == "pedra":
        print("Você perdeu.")