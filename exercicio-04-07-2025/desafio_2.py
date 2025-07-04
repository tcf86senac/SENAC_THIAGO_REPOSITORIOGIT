import random

def lancar_dados(faces):
    resultado = random.randint(1,faces)
    return resultado


while True:
    faces = int(input("Quer rolar dados de quantos lados?\n"))
    resultado = lancar_dados(faces)
    print(resultado)