numeros = []
pares = []
impares = []
while True:
    n = numeros.append(int(input('Digite um numero: ')))

    pc = str(input('Deseja continuar? [S/N]: '))[0]
    if pc in 'Nn':
        break

for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'A lista criada é: {numeros}')
print(f'Os numeros pares desta lista são: {pares}')
print(f'E os numeros ímpares são: {impares}')