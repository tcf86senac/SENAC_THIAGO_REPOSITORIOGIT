import random

nome = input('Digite o seu nome!')

print(f'Bem-vindo, {nome}. Vamos jogar um jogo?\nEu escolho uma palavra e você tenta adivinhar.\nEscolha um tema:')
lista_de_temas = [['Girafa', 'Tartaruga', 'Elefante', 'Borboleta'], ['Abacaxi', 'Espaguete', 'Panqueca', 'Chocolate'], ['Noruega', 'Egito', 'Argentina', 'Madagascar']]
escolha_de_tema = (int(input('1. Animais\n2. Comidas\n3. Países')) - 1)

palavra = random.choice(lista_de_temas[escolha_de_tema])
forca = list(palavra)
print(f'Escolhi minha palavra...ela tem {len(forca)} letras')

tracinho = ''

for i in forca:
    tracinho = tracinho + '-'

print(tracinho)
tracinho_in_game = list(tracinho)
print(tracinho_in_game)

while True:
    vidas = 6
    if vidas == 0:
        print("Você morreu...")
    else:
        letra = input("Escolha uma letra.")
        for i in range(len(forca)):
            if letra == forca[i]:
                pass
                
