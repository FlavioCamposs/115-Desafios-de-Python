import random

aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem sorteada foi: {}'.format(lista))