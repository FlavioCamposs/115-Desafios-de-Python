valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-=' * 20)
print(f'Você digitou os valores: {valores}')
print('-=' * 20)

print(f'O maior numero foi: {maior}, na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor numero foi: {menor}, na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')