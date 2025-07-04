import random

numero_escolhido = int(input("Vou escolher um número aleatório de 1 a 10.  Tente adivinhar! Qual o número você acha que é?"))

numero = random.randint(1,10)

# if numero_escolhido == numero:
#     print(f"Eu escolhi {numero}. E você {numero_escolhido}. Parabéns, você acertou!!!!")
# else:
#     print(f"Eu escolhi {numero}. E você {numero_escolhido}. Tente de novo, você ERROU!!!!")

while numero_escolhido != numero = true:
    print(f"Eu escolhi {numero}. E você {numero_escolhido}. Tente de novo, você ERROU!!!!")
else:
    print(f"Eu escolhi {numero}. E você {numero_escolhido}. Parabéns, você acertou!!!!")
    