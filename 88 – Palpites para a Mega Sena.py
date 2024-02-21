import random
from time import sleep

print('-' * 30)
print('{:^30}'.format('JOGAR NA MEGA SENA'))
print('-' * 30)

pc = int(input('Quantos jogos você quer sortear? '))

print('-=' * 3, end='')
print(f' SORTEANDO {pc} JOGOS ', end='')
print('-=' * 3)

for c in range(1, pc+1):
    lista = []
    for i in range(6):
        num = random.randint(1, 61)
        while num in lista: #Se o número já estiver na lista, significa que ele já foi sorteado e precisamos gerar um novo número
            num = random.randint(1, 61)
        lista.append(num)
    lista.sort()
    print(f'Jogo {c}: {lista}')
    sleep(0.50)

print('-=' * 5, end='')
print('{:^5}'.format(' < BOA SORTE! > '), end='')
print('-=' * 5)