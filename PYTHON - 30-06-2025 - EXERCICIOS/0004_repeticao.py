posicao=int(input("Digite a posição inicial: "))


for i in range(posicao, 101, 1):
    if i % 2 == 0:  
        print(i)


print("\n")
print("\n")
print("\n")
print("-----FIM----------FIM-------FIM----FIM-------FIM-------FIM-----FIM---------------")
print("\n")
print("\n")
print("\n")

                                                            # IMPRIMIR FIBONACCI #

a, b = 0, 1  # Inicializa os dois primeiros termos

print("Sequência de Fibonacci até 2000:")
print(a)  # Imprime o primeiro termo (0)

while b <= 2000:
    print(b)  # Imprime o próximo termo
    a, b = b, a + b  # Atualiza os termos para o próximo passo