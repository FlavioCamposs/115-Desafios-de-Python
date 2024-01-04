import random
import string #para usar e manipular strings

#geração aleatoria de strings pré criadas
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
alunos = [a1, a2, a3, a4]
sorteio = random.choice(alunos)
print('O aluno(a) sorteado para apagar o quadro foi: {}'.format(sorteio))


#geração aleatoria de strings aleatorias
tamanho = 5 #quantidade de caracteres
stringAleatoria = ' '.join(random.choices(string.ascii_letters, k=tamanho))
print(stringAleatoria)