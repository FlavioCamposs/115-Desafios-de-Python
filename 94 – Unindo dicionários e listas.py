pessoas = list()
somaIdade = 0
mulheres = list()
acimaMedia = dict()

while True:
    pessoa = {}
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
    if sexo == 'F':
        mulheres.append(nome)

    idade = int(input('Idade: '))
    somaIdade += idade

    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = idade

    pessoas.append(pessoa)

    pc = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while pc not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        pc = str(input('Quer continuar? [S/N]: ')).upper()[0]

    if pc == 'N':
        break

print('-=' * 30)

quant = len(pessoas)
media = somaIdade / quant

print(f'Nós temos {quant} pessoas cadastradas')
print(f'A média de idade é de {int(media)} anos')

print('As mulheres cadastradas foram: ', end='')
for c in mulheres:
    print(c, end=' ')

print()

print('Listas das pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] >= media: #verificar se a idade da pessoa "p" é maior ou igual à média de idade.
        print('    ', end='')
        for k, v in p.items(): #outro loop que percorre os itens do dicionário que representa uma pessoa
            print(f'{k} = {v}; ', end='')
        print()