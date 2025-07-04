import random
import time

locais = ["quarto", "sala", "cozinha", "banheiro", "varanda", "garagem"]

# -------------------------------------------------------------------------------------------------Garante que a escolha seja realmente aleatória
random.seed(time.time())

def escolher_local_do_crime():
    return random.choice(locais)

local_do_crime = escolher_local_do_crime()

# ----------------------------------------------------------------------------------------------print("(Para teste, o local do crime é:", local_do_crime + ")")  # Remova depois

while True:
    palpite = input(
        "\nOnde você acha que o crime aconteceu?\n"
        "Opções: quarto, sala, cozinha, banheiro, varanda ou garagem?\n"
    ).lower().strip()

    if palpite not in locais:
        print("Local inválido! Tente novamente.")
        continue

    if palpite == local_do_crime:
        print("Parabéns, você acertou!")
        break
    else:
        print(f"Você errou. O crime aconteceu no(a) {local_do_crime}.")
        jogar_novamente = input("Quer jogar de novo? (s/n) ").lower().strip()
        if jogar_novamente == 's':
            local_do_crime = escolher_local_do_crime()
# -----------------------------------------------------------------------------------------------------print("(Novo local do crime:", local_do_crime + ")")  # Remova depois
        else:
            print("Fim do jogo!")
            break