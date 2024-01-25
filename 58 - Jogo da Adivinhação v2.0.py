import random

numPc = random.randint(0, 10)
print(numPc)
chute = int(input('Chute um numero: '))
cont = 0

while chute != numPc:
    print('Numero Errado, tente novamente!')
    chute = int(input('Chute um numero: '))
    cont += 1
print(f'Você Acertou! O numero era: {numPc}, e você tentou {cont}x')