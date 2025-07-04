# Solicita as notas ao usuário
nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))
nota3 = float(input("Digite a terceira nota:\n"))
nota4 = float(input("Digite a quarta nota:\n"))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Encontra a maior nota
maior_nota = max(nota1, nota2, nota3, nota4)

# Verifica se a média é par ou ímpar
if media % 2 == 0:
    par_ou_impar = "par"
else:
    par_ou_impar = "ímpar"

if media > 5.9:
    print(f"Aluno aprovado")
else:    
    print(f"Aluno reprovado")

# Exibe os resultados
print(f"Sua média foi {media}")
print(f"A maior nota foi {maior_nota}")
print(f"A média é um número {par_ou_impar}.")

