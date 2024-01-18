maior = 0
menor = 0

for i in range(1, 6):
    pesos = float(input(f'Qual o peso da {i}º pessoa: '))

    if i == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print(f'O maior peso é "{maior}"\nE o menor é {menor}')