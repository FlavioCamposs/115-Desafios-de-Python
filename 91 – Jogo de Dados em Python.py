from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados:')

jogadores = {
    'Jogador1':randint(1, 10),#3
    'Jogador2':randint(1, 10),#9
    'Jogador3':randint(1, 10),#1
    'Jogador4':randint(1,10)#8
}

#sleep(1)
for k, v in jogadores.items():
    print(f'{k} tirou: {v}')
    sleep(1)


print('-=' * 30)
print('==', end=' ')
print('{:^10}'.format('RANKING DOS JOGADORES'),end=' ')
print('==')

ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
