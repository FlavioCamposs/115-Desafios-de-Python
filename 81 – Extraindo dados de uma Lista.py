numeros = list()
cont = 0
f = ''
while True:
    n = numeros.append(int(input('Digite um numero: ')))
    cont += 1

    pc = str(input('Deseja continuar? [S/N]: '))[0]
    if pc in 'Nn':
        break

print(f'{cont} numeros foram digitados') #outra forma é usar len()
print(f'Os numeros em ordem de digitação foram: {numeros}')

numeros.sort(reverse=True)
print(f'Os numeros em ordem decressente são: {numeros}')

if 5 in numeros:
    print('O numero 5 foi digitado! ele está na lista!!')
else:
    print('O numero 5 não foi digitado! Portanto, ele também não está na lista!!')