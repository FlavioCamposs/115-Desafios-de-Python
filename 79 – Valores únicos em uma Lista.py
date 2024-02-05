valores = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in valores:
        print('Valor Adcionado!')
        valores.append(n)
    else:
        print('Valor repetido, não irei adcionar!')

    pc = str(input('Deseja continuar? [S/N]: '))[0]
    if pc in 'Nn':
        break

valores.sort()
print(f'Os valores únicos digitados, em ordem crescente são: {valores}')