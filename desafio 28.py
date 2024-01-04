import random

numAleatorio = random.randint(1, 5)
num = int(input('Pensei em um numero, tende adivinhar qual é: '))
if num == numAleatorio:
    print('Parabéns, você acertou! :), eu pensei no numero {}'.format(numAleatorio))
else:
    print('Sinto muito, você perdeu! :(, eu pensei no numero {}'.format(numAleatorio))
