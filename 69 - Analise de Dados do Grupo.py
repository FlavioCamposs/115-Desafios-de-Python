id = p = m = f = 0
while True:
    idade = int(input('Qual a sua idade?: '))

    while True:
        sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Dado inválido! Por favor, digite M ou S')

    while True:
        pc = str(input('Deseja continuar? [S/N]: ')).upper()
        if pc == 'S' or pc == 'N':
            break
        else:
            print('Dado inválido! Por favor, digite S ou N')

    print('-=' * 16)

    if idade >= 0:
        p += 1

    if sexo == 'M':
        m += 1

    if idade < 20 and sexo == 'F':
        f += 1

    if idade > 18:
        id += 1

    if pc == 'N':
        print('Você saiu do programa!')
        break

print('-=' * 28)

if p == 1:
    print(f'Você cadastrou {p} pessoa')
    print('-=' * 16)
else:
    print(f'Você cadastrou {p} pessoas')
    print('-=' * 16)

if id == 1:
    print(f'{id} pessoa tem mais de 18 anos')
    print('-=' * 16)
else:
    print(f'{id} pessoas tem mais de 18 anos')
    print('-=' * 16)

print(f'Apenas {m} dessas pessoas são homens')

print('-=' * 16)

print(f'Apenas {f} dessas pessoas são mulheres abaixo de 20 anos')