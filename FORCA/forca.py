import random
vidas = 6

def escolhas_jogo(vidas):
    escolha = int(input('Digite o número da opção desejada:\n1. chutar uma letra\n2. chutar a palavra\n>>>'))
    if escolha == 1:
        letra_chute = input('Digite uma letra:\n>>>')
        if not letra_chute in forca:
            vidas = vidas - 1
            print(f'Você errou... Agora você tem {vidas}')
            return(vidas)
        else:
            for i in range(len(tracinho_in_game)):
                if letra_chute == forca[i]:
                    tracinho



    elif escolha == 2:
        chute = input("Qual é a palavra?\n>>>")
        if chute == palavra:
            print(f'Você acertou! A palavra era {palavra}')
        else:
            print(f'Você errou... A palavra era {palavra}')


nome = input('Digite o seu nome!')

print(f'Bem-vindo, {nome}. Vamos jogar um jogo?\nEu escolho uma palavra e você tenta adivinhar.\nEscolha um tema:')
lista_de_temas = [['girafa', 'tartaruga', 'elefante', 'borboleta'], ['abacaxi', 'espaguete', 'panqueca', 'chocolate'], ['noruega', 'egito', 'argentina', 'madagascar']]
escolha_de_tema = (int(input('1. Animais\n2. Comidas\n3. Países')) - 1)

palavra = random.choice(lista_de_temas[escolha_de_tema])
forca = list(palavra)
print(f'>>>>>>>>>>>>>>>>>{forca}')
print(f'Escolhi minha palavra...ela tem {len(forca)} letras')

tracinho = ''

for i in forca:
    tracinho = tracinho + '-'

print(tracinho)
tracinho_in_game = list(tracinho)
print(tracinho_in_game)

while True:
    if vidas == 0:
        print("Você morreu...")
    else:
        vidas_restantes, tracinho = escolhas_jogo(vidas, str(tracinho))
        vidas = vidas_restantes
        # letra = input("Escolha uma letra.")
        # for i in range(len(forca)):
        #     if letra == forca[i]:
        #         pass



