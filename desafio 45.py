import random
from time import sleep

escolha = str(input('Escolha o que vai jogar: ')).upper()
p = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(p).upper()

print('JO!')
sleep(1)
print('KEN!!')
sleep(1)
print('PO!!!')
print('-=' * 20)

#PARA A PEDRA
if escolha == pc == p[0]:
    print('EMPATE!, você jogou {} e eu escolhi {}!'.format(escolha, pc))
elif escolha == p[0] and pc == p[1]:
    print('EU GANHEI! {} cobre a {}!'.format(pc, escolha))
elif escolha == p[0] and pc == p[2]:
    print('VOCÊ GANHOU! {} quebra a {}!'.format(escolha, pc))

#PARA O PAPEL
elif escolha == pc == p[1]:
    print('EMPATE!, você jogou {} e eu escolhi {}!'.format(escolha, pc))
elif escolha == p[1] and pc == p[0]:
    print('VOCÊ GANHOU! {} cobre a {}!'.format(escolha, pc))
elif escolha == p[1] and pc == p[2]:
    print('EU GANHEI! {} corta o {}!'.format(pc, escolha))

#PARA A TESOURA
elif escolha == pc == p[2]:
    print('EMPATE!, você jogou {} e eu escolhi {}!'.format(escolha, pc))
elif escolha == p[2] and pc == p[0]:
    print('EU GANHEI! {} quebra a {}!'.format(pc, escolha))
elif escolha == p[2] and pc == p[1]:
    print('VOCÊ GANHOU! {} corta o {}!'.format(escolha, pc))
else:
    print('JOGADA INVÁLIDA!')