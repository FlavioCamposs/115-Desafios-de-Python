from time import sleep

alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    pc = str(input('Quer continuar? [S/N]: '))[0]
    if pc in 'Nn':
        break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    pc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pc <= len(alunos) -1:
        print(f'Notas de {alunos[pc][0]} são {alunos[pc][1]}')
    if pc == 999:
        print('FINALIZANDO...')
        sleep(2)
        print('<<< VOLTE SEMPRE! >>>')
        break