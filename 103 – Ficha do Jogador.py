def ficha(jogador='<Desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gols no campeonato!'

nome = str(input('Nome do jogador: '))
quantGols = str(input('Número de gol(s): '))
if quantGols.isnumeric():
    quantGols = int(quantGols)
else:
    quantGols = 0
if nome.strip() == '':
    print(ficha(gols=quantGols))
else:
    print(ficha(nome, quantGols))