matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma2 = maior = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

        if matriz[l][c] % 2 == 0: #SOMA DOS NUMEROS PARES
            soma += matriz[l][c]

        soma2 += matriz[l][- 1] #SOMA DOS ULTIMOS ELEMENTOS DE CADA LISTA INTERNA

        if l == 1: #O MAIOR VALOR DA 2° LISTA INTERNA (usando max())
            maior = max(matriz[l])

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()

print('-=' * 30)

print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma2}')
print(f'O maior valor da segunda linha é: {maior}')
