from datetime import datetime

pessoa = {
    'Nome':str(input('Nome: ')),
    'Idade':int(input('Ano de Nascimento: ')),
    'CTPS': int(input('Carteira de Trabalho (0 - não tem): '))
}

if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))

    idadeInicial = pessoa['Ano de Contratação'] - pessoa['Idade'] #o ano de nascimento
    pessoa['Irá aposentar com'] = idadeInicial + 35

idade = datetime.now().year - pessoa['Idade']
pessoa['Idade'] = idade

print('-' * 30)

for k, v in pessoa.items():
    print(f'{k}: {v}')
