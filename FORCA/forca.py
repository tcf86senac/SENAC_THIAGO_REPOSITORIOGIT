import random

nome = input('Digite o seu nome!')

print(f'Bem-vindo, {nome}. Vamos jogar um jogo?\nEu escolho uma palavra e você tenta adivinhar.')
lista_de_temas = [['Girafa', 'Tartaruga', 'Elefante', 'Borboleta'], ['Abacaxi', 'Espaguete', 'Panqueca', 'Chocolate'], ['Noruega', 'Egito', 'Argentina', 'Madagascar']]
escolha_de_tema = (int(input('1. Animais\n2. Comidas\n3. Países')) - 1)

palavra = random.choice(lista_de_temas[escolha_de_tema])
print(palavra)

forca = list(palavra)

tracinho = ''

for i in forca:
    tracinho = tracinho + '-'

print(tracinho)