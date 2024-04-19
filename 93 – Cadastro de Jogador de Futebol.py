jogador = {
    'Nome':str(input('Nome do jogador? '))
}

partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
quantGols = list()
tot = 0

if partidas != 0:
    for c in range(1, partidas+1):
        gols = int(input(f'    Quantos gols na {c}° partida? '))
        quantGols.append(gols)
        tot += gols

jogador['Gols'] = quantGols
jogador['Total'] = tot

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'{k} tem o valor: {v}')

print('-=' * 30)

print(f'O jogador {jogador['Nome']} jogou {partidas} partidas')

for i, c in enumerate(quantGols):
    print(f'    => Na {i+1}° partida, {jogador['Nome']} fez {c} gols')

print(f'Foi um total de {tot} gols!')