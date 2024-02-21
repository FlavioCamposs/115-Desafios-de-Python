pessoas = list()
dados = list()
maior = menor = 0
while True:
    n1 = dados.append(str(input('Nome: ')))
    n2 = dados.append(int(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    pc = str(input('Deseja continuar? [S/N]: '))[0]
    if pc in 'Nn':
        break

print(f'{len(pessoas)} pessoas foram cadastradas')

print(f'O maior peso foi de {maior}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
        
print()

print(f'O menor peso foi de {menor}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
