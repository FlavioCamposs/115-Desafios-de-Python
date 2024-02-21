aluno = {
    'nome': str(input('Nome: ')),
    'media': float(input('Média: ')),
    'situação': ''
}

print(f'O nome do aluno é {aluno['nome']}')
print(f'A média dele(a) é: {aluno['media']}')

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO!'
    print(f'Ele(a) está: {aluno['situação']}')
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
    print(f'Ele(a) está de: {aluno['situação']}')
else:
    aluno['situação'] = 'REPROVADO'
    print(f'Ele(a) está: {aluno['situação']}')