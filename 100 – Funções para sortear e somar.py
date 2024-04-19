from random import randint

numeros = list()
def sorteia(nums):
    numeros.clear()
    for c in range(nums):
        n = randint(1, 9)
        numeros.append(n)
    print('-=' * 20)
    print(f'Os {nums} valores sorteados foram: ', end='')
    for c in numeros:
        print(c, end=' ')
    print(f'\nSomando os valores pares de {numeros}, temos: ', end='')

def somaPar():
    cont = 0
    for c in numeros:
        if c % 2 == 0:
            cont += c
    print(cont)


sorteia(5)
somaPar()
while True:
    print('-=' * 20)
    print('SUA VEZ!')
    sorteia(int(input('Quantos numeros você deseja sortear?: ')))
    somaPar()

    pc = str(input('Deseja continuar? [S/N]: '))[0].upper()
    if pc == 'N':
        break